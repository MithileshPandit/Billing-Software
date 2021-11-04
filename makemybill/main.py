from tkinter import *
from tkinter import ttk
from typing import Reversible
from PIL import Image, ImageTk
import sqlite3
from tkcalendar import *
from tkinter import messagebox
import smtplib
from email.message import EmailMessage
from twilio.rest import Client
from tkinter import messagebox

account_sid = 'ACfa2fc7f1d36dfed0e1701cfe55bfa1ff'
auth_token = '0da5c83cbf27d93062aad18efa91cd7d'
my_cell = '+91 97627 43580'
my_twilio = '+1 803 282 9026'


class BillItems:
        def __init__(self,quantity,discount,material,unit,price):
                self.billQuantity = quantity
                self.billdiscount = discount
                self.billmaterial = material
                self.billUnit = unit
                self.price = price
        def getQuantity(self):
                return self.billQuantity
        def getDiscount(self):
                return self.billdiscount
        def getMaterial(self):
                return self.billmaterial
        def getUnit(self):
                return self.billUnit
        def getPrice(self):
                return self.billPrice
        

class Bill_App:


        # global billString

        def __init__(self,root):
                self.totalBill = 5

                # print(totalBill)
                self.root = root
                self.root.geometry("1530x800+0+0")
                self.root.title("Billing System")
                



                def email_alert():
                        client = Client(account_sid,auth_token)
                        # my_msg = "Your message goes here......"
                        message = client.messages.create(to="+91"+self.sendMessageEntry.get(),from_=my_twilio,
                                        body=f"You have made a purchase of {self.totalBill}")
                # email_alert("This is the first Message","FIRST FIRST FIRST","mithileshpandit7577@gmail.com")
                sideFrame = Frame(self.root, bg="#F8F8F8",borderwidth=6,relief=SUNKEN)
                # sideFrame.pack(side=LEFT,fill="y") 
                sideFrame.place(x=0,y=0,width=225,height=120)

                sideFrame2 = Frame(self.root, bg="#F8F8F8", borderwidth=6,relief=SUNKEN)
                sideFrame2.place(x=0,y=126,width=225,height=680)

                # sideFrameImg = Image.open("Python projects/images/userProfile.png")
                # sideFrameImg = sideFrameImg.resize((75,75),Image.ANTIALIAS)
                # self.sideFrameTopImg=ImageTk.PhotoImage(sideFrameImg)

                # sideFrameTopImage = Label(sideFrame,image=self.sideFrameTopImg)
                # sideFrameTopImage.pack(side=TOP,anchor=NW,padx=15,pady=15)

                nameLabel = Label(sideFrame,text="Mithilesh\n Pandit")
                nameLabel.place(x=100,y=25)

                homeButtonLabel = Button(sideFrame2,text="HOME",bg="blue",command=lambda:showFrame(middleFrame))
                homeButtonLabel.place(x=0,y=15,width=215,height=30)

                homeButtonLabel2 = Button(sideFrame2,text="PURCHASE",bg="blue",command=lambda:showFrame(purchaseEntryFrame))
                homeButtonLabel2.place(x=0,y=60,width=215,height=30)

                homeButtonLabel3 = Button(sideFrame2,text="SALES",bg="blue",command=lambda:showFrame(salesFrame))
                homeButtonLabel3.place(x=0,y=150,width=215,height=30)

                homeButtonLabel3 = Button(sideFrame2,text="CLIENTS",bg="blue",command=lambda:showFrame(clientFrame))
                homeButtonLabel3.place(x=0,y=105,width=215,height=30)

                homeButtonLabel4 = Button(sideFrame2,text="REPORT",bg="blue",command=lambda:showFrame(reportFrame))
                homeButtonLabel4.place(x=0,y=195,width=215,height=30)

                topFrame = Frame(self.root, bg="#F8F8F8",borderwidth=6,relief=SUNKEN)
                # sideFrame.pack(side=LEFT,fill="y") 
                topFrame.place(x=225,y=0,width=1132,height=90)


        # Image 1
                # topImg = Image.open("Python projects/images/horizontalCow.jpg")
                # topImg = topImg.resize((1120,120),Image.ANTIALIAS)
                # self.topPicture=ImageTk.PhotoImage(topImg)

                # labelTopImage = Label(topFrame,image=self.topPicture)
                # labelTopImage.pack(side="top",anchor="w")

                # TO bring one fram eabove aniother on click
                def showFrame(frame):
                        frame.tkraise()
        #--------xxxxxxxSAhow Frame----xxxx-x-x-x-x-x-



                megaMiddleFrame = Frame(self.root,border=6,relief=SUNKEN)
                megaMiddleFrame.place(x=225,y=90,width=1132,height=610)
                # createBillFrameGoBackButton = Button(megaMiddleFrame, text="Go back").pack()
                megaMiddleFrame.rowconfigure(0,weight=1)
                megaMiddleFrame.columnconfigure(0,weight=1)
        
        #Middle Frame ---------------------------------------------------------------------
                middleFrame = Frame(megaMiddleFrame)
                createBillFrame = Frame(megaMiddleFrame)
                purchaseEntryFrame = Frame(megaMiddleFrame)
                paymentFrame = Frame(megaMiddleFrame)
                clientFrame = Frame(megaMiddleFrame)
                salesFrame = Frame(megaMiddleFrame)
                reportFrame = Frame(megaMiddleFrame)

                # sideFrame.pack(side=LEFT,fill="y") 
                # middleFrame.place(x=225,y=120,width=1132,height=580)
                # createBillButton = Button(middleFrame,text="CREATE BILL",bg="blue",command=lambda:showFrame(createBillFrame))
                # createBillButton.place(x=30,y=30,width=150,height=30)

                purchaseEntryButton = Button(middleFrame,text="PURCHASE ENTRY",bg="blue",command=lambda:showFrame(purchaseEntryFrame))
                purchaseEntryButton.place(x=30,y=80,width=150,height=30)

                receivedPaymentButton = Button(middleFrame,text="RECEIVED PAYMENT",bg="blue",command=lambda:showFrame(paymentFrame))
                receivedPaymentButton.place(x=30,y=130,width=150,height=30)

        #middleFrame---------x-x-x-x-x-x-x-x-x-x-x-x-x-xx-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-

        #Purchase Frame components--------------------------------------------------------------

        
                def materialDetailsWindow():
                        materialDetailsWindow = Tk()
                        materialDetailsWindow.title("Upload client")
                        materialDetailsWindow.geometry('600x230+250+250')

                        materialTextView  = Entry(materialDetailsWindow)
                        materialTextView.pack()
                        def printTheTextOnTheScreen():
                                conn = sqlite3.connect('makeMyBill.db')

                                c = conn.cursor()
                                c.execute("INSERT INTO materials2 VALUES (:materialName,:materialQuantity)",
                                {
                                        'materialName': materialTextView.get(),
                                        'materialQuantity': 0
                                })
                        
                                c.execute("SELECT materialName FROM materials2")
                                self.materials = [i[0] for i in c.fetchall()]

                                self.materialNamesOptionsMenu = OptionMenu(purchaseDataFrame,self.clickedMaterial, *self.materials)
                                self.materialNamesOptionsMenu.grid(row=0, column=1, padx=10, pady=10)

                                self.materialNamesOptionsMenuCreateBill = OptionMenu(createBillFrame,self.clickedMaterial, *self.materials)
                                self.materialNamesOptionsMenuCreateBill.place(x=430,y=105,height=30,width=150)


                                records = c.fetchall()

                                

                                print(records)
                        # Commit changes
                                conn.commit()
                                conn.close()

                                


                        saveButton = Button(materialDetailsWindow,text="Save",command=printTheTextOnTheScreen)
                        saveButton.place(x=230,y=175,height=30,width=150)


        #Create bill frame---------------------------------------------------------------------


















        #Purchase Entry Frame Start ---------------###################-----------------------------------
        








# Do some database stuff
# Create a database or connect to one that exists


                conn = sqlite3.connect('makeMyBill.db')

                c = conn.cursor()
                c.execute("SELECT clientName FROM clientDetails")
                
                self.suppliers = [i[0] for i in c.fetchall()]
                
                c.execute("SELECT materialName FROM materials2")
                self.materials = [i[0] for i in c.fetchall()]

                conn.commit()

                # Create a cursor instance
                c = conn.cursor()

                # Create Table
                c.execute("""CREATE TABLE if not exists purchaseEntry (
                        materialName text,
                        supplierName text,
                        dateOfPurchase integer,
                        invoiceNumber text,
                        quantity text,
                        remark text)
                """)
                c.execute("""CREATE TABLE if not exists materials2 (
                        materialName text, materialQuantity integer)
                """)
                def query_database():
                        # Create a database or connect to one that exists
                        conn = sqlite3.connect('makeMyBill.db')

                        # Create a cursor instance
                        c = conn.cursor()

                        c.execute("SELECT rowid, * FROM purchaseEntry")
                        records =[]
                        records = c.fetchall()


                        ################## MIDDLE PURCHASE RECORDS ###################################################

                        materialsConn = sqlite3.connect('makeMyBill.db')

                        # Create a cursor instance
                        materialCursor = conn.cursor()

                        materialCursor.execute("SELECT * FROM materials2")
                        materialsCount =[]
                        materialsCount = materialCursor.fetchall()
                        

                        ################## MIDDLE PURCHASE RECORDS ###################################################
                        
                        # Add our data to the screen
                        global count
                        count = 0

                        global materialsCountInc
                        materialsCountInc = 0
                        
                        #for record in records:
                                

                        # for record in records:

                        #         if count % 2 == 0:
                        #                 purchaseTree.insert(parent='', index='end',text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('evenrow',))
                        #         else:
                        #                 purchaseTree.insert(parent='', index='end', text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('oddrow',))
                                
                        #         count = count+1


                        for record in records:
                                if count % 2==0:
                                        purchaseTree.insert(parent='',index='end',text='',values=(record[0],record[1],record[2],record[3],record[4],record[5], record[6]), tags=('evenrow',))
                                #Solved
                                else:
                                        purchaseTree.insert(parent='',index='end',text='',values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]), tags=('oddrow',))
                                count +=1

                        for record2 in materialsCount:
                                if count % 2==0:
                                        middlePurchaseTree.insert(parent='',index='end',text='',values=(record2[0],record2[1]), tags=('evenrow',))
                                        #Solved
                                else:
                                        middlePurchaseTree.insert(parent='',index='end',text='',values=(record2[0],record2[1]), tags=('oddrow',))
                                materialsCountInc +=1
                        
                                # increment counter


                        # Commit changes
                        conn.commit()

                        conn.close()

                        materialsConn.commit()
                        # Close our connection
                        materialsConn.close()



        # Add Some Style
                style = ttk.Style()

                # Pick A Theme
                style.theme_use('default')

                # Configure the Treeview Colors
                style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3")

                
        # Change Selected Color
                style.map('Treeview',
                        background=[('selected', "#347083")])

                # Create a Treeview Frame
                purchaseTreeFrame = Frame(purchaseEntryFrame)
                purchaseTreeFrame.pack(pady=10)

                # Create a Treeview Scrollbar
                purchaseTreeScrollBar = Scrollbar(purchaseTreeFrame)
                purchaseTreeScrollBar.pack(side=RIGHT, fill=Y)

                # Create The Treeview
                purchaseTree = ttk.Treeview(purchaseTreeFrame, yscrollcommand=purchaseTreeScrollBar.set, 
                selectmode="extended")
                purchaseTree.pack()


                middlePurchaseTree = ttk.Treeview(middleFrame, yscrollcommand=purchaseTreeScrollBar.set, 
                selectmode="extended")
                middlePurchaseTree.place(x=15,y=300)
                #Minato namikaze

                purchaseTreeScrollBar.config(command=purchaseTree.yview)

                # Define Our Columns
                purchaseTree['columns'] = ("ID", "Material Name", "Supplier Name", "date of purchase",
                "invoice Number", "Quantity", "Remark")


                middlePurchaseTree['columns'] = ("Material Name", "Quantity Remaining")



                # Format Our Columns
                purchaseTree.column("#0", width=0, stretch=NO)
                purchaseTree.column("ID", anchor=W, width=140)
                purchaseTree.column("Material Name", anchor=W, width=140)
                purchaseTree.column("Supplier Name", anchor=CENTER, width=100)
                purchaseTree.column("date of purchase", anchor=CENTER, width=140)
                purchaseTree.column("invoice Number", anchor=CENTER, width=140)
                purchaseTree.column("Quantity", anchor=CENTER, width=140)
                purchaseTree.column("Remark", anchor=CENTER, width=140)


                middlePurchaseTree.column("#0", width=0, stretch=NO)
                middlePurchaseTree.column("Material Name", anchor=W, width=140)
                middlePurchaseTree.column("Quantity Remaining", anchor=CENTER, width=100)



                # Create Headings
                purchaseTree.heading("#0", text="", anchor=W)
                purchaseTree.heading("ID", text="ID", anchor=W)
                purchaseTree.heading("Material Name", text="Material Name", anchor=W)
                purchaseTree.heading("Supplier Name", text="Supplier Name", anchor=CENTER)
                purchaseTree.heading("date of purchase", text="date of Purchase", anchor=CENTER)
                purchaseTree.heading("invoice Number", text="Invoice Number", anchor=CENTER)
                purchaseTree.heading("Quantity", text="Quantity", anchor=CENTER)
                purchaseTree.heading("Remark", text="Remark", anchor=CENTER)

                middlePurchaseTree.heading("#0", text="", anchor=W)
                middlePurchaseTree.heading("Material Name", text="Material Name", anchor=W)
                middlePurchaseTree.heading("Quantity Remaining", text="Quantity Remaining", anchor=CENTER)




                # Create Striped Row Tags
                purchaseTree.tag_configure('oddrow', background="white")
                purchaseTree.tag_configure('evenrow', background="lightblue")


                middlePurchaseTree.tag_configure('oddrow', background="white")
                middlePurchaseTree.tag_configure('evenrow', background="lightblue")



                purchaseDataFrame = LabelFrame(purchaseEntryFrame, text="Record")
                purchaseDataFrame.pack(fill="x", expand="yes", padx=20)


                purchaseIdLabel = Label(purchaseDataFrame, text="ID")
                purchaseIdLabel.grid(row=1, column=6, padx=10, pady=10)
                purchaseIdEntry = Entry(purchaseDataFrame)
                purchaseIdEntry.grid(row=1, column=7, padx=10, pady=10)



                purchaseMaterialNameLabel = Label(purchaseDataFrame, text="Material Name")
                purchaseMaterialNameLabel.grid(row=0, column=0, padx=10, pady=10)
                # purchaseMaterialNameEntry = Entry(purchaseDataFrame)
                # purchaseMaterialNameEntry.grid(row=0, column=1, padx=10, pady=10)
                # self.materials = []
                self.clickedMaterial = StringVar()
                if len(self.materials)==0:
                        self.clickedMaterial.set("Default")
                        self.materials = ["Default"]
                else :
                        self.clickedMaterial.set(self.materials[0])

                self.materialNamesOptionsMenu = OptionMenu(purchaseDataFrame,self.clickedMaterial, *self.materials)
                self.materialNamesOptionsMenu.grid(row=0, column=1, padx=10, pady=10)


                purchaseSupplierNameLabel = Label(purchaseDataFrame, text="Supplier Name")
                purchaseSupplierNameLabel.grid(row=0, column=2, padx=10, pady=10)
                purchaseSupplierNameEntry = Entry(purchaseDataFrame)
                purchaseSupplierNameEntry.grid(row=0, column=3, padx=10, pady=10)

                dateOfPurchaseLabel = Label(purchaseDataFrame, text="Date")
                dateOfPurchaseLabel.grid(row=0, column=4, padx=10, pady=10)
                # dateOfPurchaseEntry = Entry(data_frame)
                # dateOfPurchaseEntry.grid(row=0, column=5, padx=10, pady=10)
                purchaseCal = Calendar(purchaseDataFrame, selectmode="day", year=2020,month=5,day=22)
                purchaseCal.grid(row=0, column=5, padx=10, pady=10)




                purchaseQuantityLabel = Label(purchaseDataFrame, text="Quantity")
                purchaseQuantityLabel.grid(row=1, column=0, padx=10, pady=10)
                purchaseQuantityEntry = Entry(purchaseDataFrame)
                purchaseQuantityEntry.grid(row=1, column=1, padx=10, pady=10)

                purchaseRemarkLabel = Label(purchaseDataFrame, text="Remark")
                purchaseRemarkLabel.grid(row=1, column=2, padx=10, pady=10)
                purchaseRemarkEntry = Entry(purchaseDataFrame)
                purchaseRemarkEntry.grid(row=1, column=3, padx=10, pady=10)


                purchaseInvoiceLabel = Label(purchaseDataFrame, text="Invoice")
                purchaseInvoiceLabel.grid(row=1, column=4, padx=10, pady=10)
                purchaseInvoiceEntry = Entry(purchaseDataFrame)
                purchaseInvoiceEntry.grid(row=1, column=5, padx=10, pady=10)


                backButton = Button(purchaseEntryFrame,text="Go back",command=lambda:showFrame(middleFrame))
                backButton.place(x=2,y=2)
                backButton = Button(purchaseEntryFrame,text="Add Material",command=lambda:materialDetailsWindow())
                backButton.place(x=2,y=30)
                # Move Row Up
                def up():
                        rows = purchaseTree.selection()
                        for row in rows:
                                purchaseTree.move(row, purchaseTree.parent(row), purchaseTree.index(row)-1)

                # Move Rown Down
                def down():
                        rows = purchaseTree.selection()
                        for row in reversed(rows):
                                purchaseTree.move(row, purchaseTree.parent(row), purchaseTree.index(row)+1)

        # Remove one record
                def remove_one():
                        x = purchaseTree.selection()[0]

                        curItem = purchaseTree.focus()
                        print(purchaseTree.item(curItem))
                        # midTreeValueDictionary = purchaseTree.item(curItem)

                        # midTreeValueList = midTreeValueDictionary['values']

                        # print(midTreeValueList)

                        # midTreeValueToBeDeletedIndex = midTreeValueList[0]

                        # middleMaterialTreeItemToBeDeleted = middlePurchaseTree.get_children()[midTreeValueToBeDeletedIndex]
                        

                        purchaseTree.delete(x)


                        # middlePurchaseTree.delete(middleMaterialTreeItemToBeDeleted)
                        # Create a database or connect to one that exists
                        conn = sqlite3.connect('makeMyBill.db')

                        # Create a cursor instance
                        c = conn.cursor()

                        # Delete From Database
                        c.execute("DELETE from purchaseEntry WHERE oid=" + purchaseIdEntry.get())

                        # Commit changes
                        conn.commit()

                        # Close our connection
                        conn.close()
                        clear_entries()

                # Add a little message box for fun



        # Remove Many records
                def remove_many():
                        # Add a little message box for fun
                        response = messagebox.askyesno("WOAH!!!!", "This Will Delete EVERYTHING SELECTED From The Table\nAre You Sure?!")

                        #Add logic for message box
                        if response == 1:
                                # Designate selections
                                x = purchaseTree.selection()

                                # Create List of ID's
                                ids_to_delete = []
                                
                                # Add selections to ids_to_delete list
                                for record in x:
                                        ids_to_delete.append(purchaseTree.item(record, 'values')[2])

                                # Delete From Treeview
                                for record in x:
                                        purchaseTree.delete(record)

                                # Create a database or connect to one that exists
                                conn = sqlite3.connect('makeMyBill.db')

                                # Create a cursor instance
                                c = conn.cursor()
                                

                                # Delete Everything From The Table
                                c.executemany("DELETE FROM purchaseEntry WHERE id = ?", [(a,) for a in ids_to_delete])

                                # Reset List
                                ids_to_delete = []


                                # Commit changes
                                conn.commit()

                                # Close our connection
                                conn.close()

                                # Clear entry boxes if filled
                                clear_entries()


        # Remove all records
                def remove_all():
                        # Add a little message box for fun
                        response = messagebox.askyesno("WOAH!!!!", "This Will Delete EVERYTHING From The Table\nAre You Sure?!")

                        #Add logic for message box
                        if response == 1:
                                # Clear the Treeview
                                for record in purchaseTree.get_children():
                                        purchaseTree.delete(record)

                                # Create a database or connect to one that exists
                                conn = sqlite3.connect('tree_crm.db')

                                # Create a cursor instance
                                c = conn.cursor()

                                # Delete Everything From The Table
                                c.execute("DROP TABLE purchaseEntry")
                                        


                                # Commit changes
                                conn.commit()

                                # Close our connection
                                conn.close()

                                # Clear entry boxes if filled
                                clear_entries()

                                # Recreate The Table
                                create_table_again()
                def clear_entries():
                        # Clear entry boxes
                        # purchaseMaterialNameEntry.delete(0, END)
                        
                        purchaseSupplierNameEntry.delete(0, END)
                        # d.delete(0, END)
                        purchaseInvoiceEntry.delete(0, END)
                        purchaseQuantityEntry.delete(0, END)
                        purchaseRemarkEntry.delete(0, END)
                        purchaseIdEntry.delete(0, END)

                def select_record(e):
                # Clear entry boxes
                        # purchaseMaterialNameEntry.delete(0, END)
                        purchaseSupplierNameEntry.delete(0, END)
                        # d.delete(0, END)
                        purchaseInvoiceEntry.delete(0, END)
                        purchaseQuantityEntry.delete(0, END)
                        purchaseRemarkEntry.delete(0, END)
                        purchaseIdEntry.delete(0, END)

                # Grab record Number
                        selected = purchaseTree.focus()
                        # Grab record values
                        values = purchaseTree.item(selected, 'values')

                        # outpus to entry boxes
                        # purchaseMaterialNameEntry.insert(0, values[1])
                        purchaseSupplierNameEntry.insert(0, values[2])
                        purchaseInvoiceEntry.insert(0, values[4])
                        purchaseQuantityEntry.insert(0, values[5])
                        purchaseRemarkEntry.insert(0, values[6])
                        purchaseIdEntry.insert(0, values[0])

                def update_record():
                        # Grab the record number
                        selected = purchaseTree.focus()
                        # Update record
                        purchaseTree.item(selected, text="", values=
                        (purchaseIdEntry.get(), self.clickedMaterial, purchaseSupplierNameEntry.get(),purchaseCal.get_date(),
                         purchaseInvoiceEntry.get(),purchaseQuantityEntry.get(),
                        purchaseRemarkEntry.get()))

                        # Update the database
                        # Create a database or connect to one that exists
                        conn = sqlite3.connect('makeMyBill.db')

                        # Create a cursor instance
                        c = conn.cursor()

                        c.execute("""UPDATE purchaseEntry SET
                                materialName = :material,
                                supplierName = :supplier,
                                dateOfPurchase = :date,
                                invoiceNumber = :invoice,
                                quantity = :quantity,
                                remark = :remark

                                WHERE oid = :oid""",
                                {
                                        'material': self.clickedMaterial,
                                        'supplier': purchaseSupplierNameEntry.get(),
                                        'date': purchaseCal.get_date()+'',
                                        'invoice': purchaseInvoiceEntry.get(),
                                        'quantity': purchaseQuantityEntry.get(),
                                        'remark': purchaseRemarkEntry.get(),
                                        'oid': purchaseIdEntry.get(),
                                })
                        


                        # Commit changes
                        conn.commit()

                        # Close our connection
                        conn.close()


                        # Clear entry boxes
                        # purchaseMaterialNameEntry.delete(0, END)
                        purchaseSupplierNameEntry.delete(0, END)
                        # d.delete(0, END)
                        purchaseInvoiceEntry.delete(0, END)
                        purchaseQuantityEntry.delete(0, END)
                        purchaseRemarkEntry.delete(0, END)
                        purchaseIdEntry.delete(0, END)
                def add_record():
                        # Update the database
                        # Create a database or connect to one that exists
                        conn = sqlite3.connect('makeMyBill.db')

                        # Create a cursor instance
                        c = conn.cursor()

                        # Add New Record
                        c.execute("INSERT INTO purchaseEntry VALUES (:materialName, :supplierName, :dateOfPurchase, :invoiceNumber, :quantity, :remark)",
                                {
                                        'materialName': self.clickedMaterial.get(),
                                        'supplierName': purchaseSupplierNameEntry.get(),
                                        'dateOfPurchase': purchaseCal.get_date()+'',
                                        'invoiceNumber': purchaseInvoiceEntry.get(),
                                        'quantity': purchaseQuantityEntry.get(),
                                        'remark': purchaseRemarkEntry.get(),
                                })


                        # Commit changes
                        conn.commit()

                        # Close our connection
                        conn.close()

                        # Clear entry boxes
                        # purchaseMaterialNameEntry.delete(0, END)
                        purchaseSupplierNameEntry.delete(0, END)
                        # d.delete(0, END)
                        purchaseInvoiceEntry.delete(0, END)
                        purchaseRemarkEntry.delete(0, END)
                        purchaseIdEntry.delete(0, END)

                        # Run to pull data from database on start
                        middlePurchaseTree.delete(*middlePurchaseTree.get_children())

                        purchaseTree.delete(*purchaseTree.get_children())

                        query_database()



                        ##############################################
                        ##############################################
                        
                        conn = sqlite3.connect('makeMyBill.db')

                        c = conn.cursor()
                
                        c.execute(f"SELECT materialQuantity FROM materials2 where materialName = '{self.clickedMaterial.get()}'")
                        currentQuantity = [i[0] for i in c.fetchall()]
                        # print(str(currentQuantity)+"  updated")


                        currentQuantity[0] = currentQuantity[0]+int(purchaseQuantityEntry.get())
                        purchaseQuantityEntry.delete(0, END)

                        c.execute(f"UPDATE materials2 SET materialQuantity = {currentQuantity[0]} WHERE materialName = '{self.clickedMaterial.get()}'")

                        c.execute(f"SELECT materialQuantity FROM materials2 where materialName = '{self.clickedMaterial.get()}'")
                        currentQuantity2 = [i[0] for i in c.fetchall()]

                        # print(str(currentQuantity2)+"  updated")

                        # Commit changes
                        conn.commit()

                        # Close our connection
                        conn.close()

                        # print(str(currentQuantity2)+"  updated")

                        ##############################################
                        ###############################################
                        



                def create_table_again():
                        # Create a database or connect to one that exists
                        conn = sqlite3.connect('makeMyBill.db')

                        # Create a cursor instance
                        c = conn.cursor()

                        # Create Table
                        c.execute("""CREATE TABLE if not exists purchaseEntry (
                                materialName text,
                                supplierName text,
                                dateOfPurchase integer,
                                invoiceNumber text,
                                quantity text,
                                remark text,
                                """)
                        # c.execute("""CREATE TABLE if not exists purchaseEntryStocks (
                        #         materialName text,
                        #         supplierName text,
                        #         dateOfPurchase integer,
                        #         invoiceNumber text,
                        #         quantity integer,
                        #         remark text,
                        #         """)
                        


                        # Commit changes
                        conn.commit()

                        # Close our connection
                        conn.close()

                purchaseButtonFrame = LabelFrame(purchaseEntryFrame, text="Commands")
                purchaseButtonFrame.pack(fill="x", expand="yes", padx=20)

                purchaseUpdateButton = Button(purchaseButtonFrame, text="Update Record", command=update_record)
                purchaseUpdateButton.grid(row=0, column=0, padx=10, pady=10)

                purchaseAddButton = Button(purchaseButtonFrame, text="Add Record", command=add_record)
                purchaseAddButton.grid(row=0, column=1, padx=10, pady=10)


                purchaseRemoveOneButton = Button(purchaseButtonFrame, text="Remove One Selected", command=remove_one)
                purchaseRemoveOneButton.grid(row=0, column=3, padx=10, pady=10)


                purchaseMoveUpButton = Button(purchaseButtonFrame, text="Move Up", command=up)
                purchaseMoveUpButton.grid(row=0, column=5, padx=10, pady=10)

                purchaseMoveDownButton = Button(purchaseButtonFrame, text="Move Down", command=down)
                purchaseMoveDownButton.grid(row=0, column=6, padx=10, pady=10)

                purchaseSelectRecordButton = Button(purchaseButtonFrame, text="Clear Entry Boxes", command=clear_entries)
                purchaseSelectRecordButton.grid(row=0, column=7, padx=10, pady=10)

                # Bind the treeview
                purchaseTree.bind("<ButtonRelease-1>", select_record)

                query_database()










        # Purchase Entry Frame End ---------------###################-----------------------------------
                


        # Payment Frame starts here-----------------###############################____________----------------------




# Do some database stuff
# Create a database or connect to one that exists
                conn = sqlite3.connect('makeMyBill.db')

                # Create a cursor instance
                c = conn.cursor()

                # Create Table
                c.execute("""CREATE TABLE if not exists paymentDetails (
                                id text,
                                clientName text,
                                amount integer,
                                date text,
                                modeOfPayment text,
                                remark text)
                """)

                def paymentQueryDatabase():
                        # Create a database or connect to one that exists
                        conn = sqlite3.connect('makeMyBill.db')

                        # Create a cursor instance
                        c = conn.cursor()

                        c.execute("SELECT rowid, * FROM paymentDetails")
                        paymentRecords =[]
                        paymentRecords = c.fetchall()
                        
                        # c.execute("SELECT rowid,totalPayment = amount - modeOfPayment * FROM paymentDetails ORDER BY totalPayment DESC")
                        # paymentRecords2 =[]
                        # paymentRecords2 = c.fetchall()
                    
                        # Add our data to the screen
                        global count2
                        count2 = 0
                        
                        #for record in records:
                                

                        for record in paymentRecords:

                                if count2 % 2 == 0:
                                        amountRemaining = int(record[3]) - int(record[5])
                                        paymentTree.insert(parent='', index='end',text='', values=(record[0], record[2], record[3], record[4], record[5], record[6]), tags=('evenrow',))
                                        middlePaymentTree.insert(parent='', index='end',text='', values=(record[0], record[2], record[3], record[4], amountRemaining, record[6]), tags=('evenrow',))
                                else:
                                        amountRemaining = int(record[3]) - int(record[5])
                                        paymentTree.insert(parent='', index='end', text='', values=(record[0], record[2], record[3], record[4], record[5], record[6]), tags=('oddrow',))
                                        middlePaymentTree.insert(parent='', index='end', text='', values=(record[0], record[2], record[3], record[4], amountRemaining, record[6]), tags=('oddrow',))
                                
                                count2 +=1

                                # increment counter


                        # Commit changes
                        conn.commit()

                        # Close our connection
                        conn.close()



        # Add Some Style
                style = ttk.Style()

                # Pick A Theme
                style.theme_use('default')

                # Configure the Treeview Colors
                style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3")

                
        # Change Selected Color
                style.map('Treeview',
                        background=[('selected', "#347083")])

                # Create a Treeview Frame
                paymentTreeFrame = Frame(paymentFrame)
                paymentTreeFrame.pack(pady=10)

                # Create a Treeview Scrollbar
                paymentTreeScrollBar = Scrollbar(paymentTreeFrame)
                paymentTreeScrollBar.pack(side=RIGHT, fill=Y)


                # Create payment Treeview fro the middleFrame


                # Create The Treeview
                paymentTree = ttk.Treeview(paymentTreeFrame, yscrollcommand=paymentTreeScrollBar.set, 
                selectmode="extended")
                #Middle
                #Middle
                middlePaymentTree = ttk.Treeview(middleFrame,selectmode="extended")
                #Middle-xxxxxxxxxxx
                #Middle-xxxxxxxxxxxxxx
                #Minato namikaze
                paymentTree.pack()
                middlePaymentTree.place(x=350,y=15)
                paymentTreeScrollBar.config(command=paymentTree.yview)

                # Define Our Columns
                paymentTree['columns'] = ("ID", "Client Name", "Amount", "date of purchase",
                "Amount Paid", "Remark")
                middlePaymentTree['columns'] = ("ID", "Client Name", "Amount", "date of purchase",
                "Remaining Amount", "Remark")

                # Format Our Columns
                paymentTree.column("#0", width=0, stretch=NO)
                paymentTree.column("ID", anchor=W, width=140)
                paymentTree.column("Client Name", anchor=W, width=140)
                paymentTree.column("Amount", anchor=CENTER, width=100)
                paymentTree.column("date of purchase", anchor=CENTER, width=140)
                paymentTree.column("Amount Paid", anchor=CENTER, width=140)
                paymentTree.column("Remark", anchor=CENTER, width=140)

                
                middlePaymentTree.column("#0", width=0, stretch=NO)
                middlePaymentTree.column("ID", anchor=W, width=100)
                middlePaymentTree.column("Client Name", anchor=W, width=100)
                middlePaymentTree.column("Amount", anchor=CENTER, width=100)
                middlePaymentTree.column("date of purchase", anchor=CENTER, width=100)
                middlePaymentTree.column("Remaining Amount", anchor=CENTER, width=100)
                middlePaymentTree.column("Remark", anchor=CENTER, width=100)




                # Create Headings
                paymentTree.heading("#0", text="", anchor=W)
                paymentTree.heading("ID", text="ID", anchor=W)
                paymentTree.heading("Client Name", text="Client Name", anchor=W)
                paymentTree.heading("Amount", text="Amount", anchor=CENTER)
                paymentTree.heading("date of purchase", text="date of Purchase", anchor=CENTER)
                paymentTree.heading("Amount Paid", text="Amount Paid", anchor=CENTER)
                paymentTree.heading("Remark", text="Remark", anchor=CENTER)



                middlePaymentTree.heading("#0", text="", anchor=W)
                middlePaymentTree.heading("ID", text="ID", anchor=W)
                middlePaymentTree.heading("Client Name", text="Client Name", anchor=W)
                middlePaymentTree.heading("Amount", text="Amount", anchor=CENTER)
                middlePaymentTree.heading("date of purchase", text="date of Purchase", anchor=CENTER)
                middlePaymentTree.heading("Remaining Amount", text="Remaining Amount", anchor=CENTER)
                middlePaymentTree.heading("Remark", text="Remark", anchor=CENTER)



                # Create Striped Row Tags
                paymentTree.tag_configure('oddrow', background="white")
                paymentTree.tag_configure('evenrow', background="lightblue")

                middlePaymentTree.tag_configure('oddrow', background="white")
                middlePaymentTree.tag_configure('evenrow', background="lightblue")

                paymentDataFrame = LabelFrame(paymentFrame, text="Record")
                paymentDataFrame.pack(fill="x", expand="yes", padx=20)


                paymentIdLabel = Label(paymentDataFrame, text="ID")
                paymentIdLabel.grid(row=1, column=6, padx=10, pady=10)
                paymentIdEntry = Entry(paymentDataFrame)
                paymentIdEntry.grid(row=1, column=7, padx=10, pady=10)



                paymentClientNameLabel = Label(paymentDataFrame, text="Client Name")
                paymentClientNameLabel.grid(row=0, column=0, padx=10, pady=10)

                #TOBYRAMA SENJU
                self.clickedClientNamePayment = StringVar()
                if len(self.suppliers)==0:
                        self.clickedClientNamePayment.set("Default")
                        self.suppliers = ["Default"]
                else :
                        self.clickedClientNamePayment.set(self.suppliers[0])

                self.paymentClientNameOptionsMenu = OptionMenu(paymentDataFrame,self.clickedClientNamePayment, *self.suppliers)
                self.paymentClientNameOptionsMenu.grid(row=0, column=1, padx=10, pady=10)



                conn.commit()


                
                #Add a drop down


                paymentAmountLabel = Label(paymentDataFrame, text="Amount")
                paymentAmountLabel.grid(row=0, column=2, padx=10, pady=10)
                paymentAmountEntry = Entry(paymentDataFrame)
                paymentAmountEntry.grid(row=0, column=3, padx=10, pady=10)

                dateOfPayment = Label(paymentDataFrame, text="Date")
                dateOfPayment.grid(row=0, column=4, padx=10, pady=10)
                # dateOfPurchaseEntry = Entry(data_frame)
                # dateOfPurchaseEntry.grid(row=0, column=5, padx=10, pady=10)
                paymentCal = Calendar(paymentDataFrame, selectmode="day", year=2020,month=5,day=22)
                paymentCal.grid(row=0, column=5, padx=10, pady=10)




                modeOfPaymentLabel = Label(paymentDataFrame, text="Amount paid")
                modeOfPaymentLabel.grid(row=1, column=0, padx=10, pady=10)
                modeOfPaymentEntry = Entry(paymentDataFrame)
                modeOfPaymentEntry.grid(row=1, column=1, padx=10, pady=10)



                PaymentRemarkLabel = Label(paymentDataFrame, text="Remark")
                PaymentRemarkLabel.grid(row=1, column=2, padx=10, pady=10)
                PaymentRemarkEntry = Entry(paymentDataFrame)
                PaymentRemarkEntry.grid(row=1, column=3, padx=10, pady=10)



                paymentBackButton = Button(paymentFrame,text="Go back",command=lambda:showFrame(middleFrame))
                paymentBackButton.place(x=2,y=2)


                # Move Row Up
                def paymentUp():
                        rows = paymentTree.selection()
                        for row in rows:
                                paymentTree.move(row, paymentTree.parent(row), paymentTree.index(row)-1)

                # Move Rown Down
                def paymentDown():
                        rows = paymentTree.selection()
                        for row in reversed(rows):
                                paymentTree.move(row, paymentTree.parent(row), paymentTree.index(row)+1)

        # Remove one record
                def paymentRemoveOne():
                        x = paymentTree.selection()[0]
                        paymentTree.delete(x)

                        middlePaymentTree.delete(x)

                        # Create a database or connect to one that exists
                        conn = sqlite3.connect('makeMyBill.db')

                        # Create a cursor instance
                        c = conn.cursor()

                        # Delete From Database
                        c.execute("DELETE from paymentDetails WHERE oid=" + paymentIdEntry.get())

                        # Commit changes
                        conn.commit()

                        # Close our connection
                        conn.close()
                        clear_entries()

                # Add a little message box for fun



        # Remove Many records
                def paymentRemoveMany():
                        # Add a little message box for fun
                        response = messagebox.askyesno("WOAH!!!!", "This Will Delete EVERYTHING SELECTED From The Table\nAre You Sure?!")

                        #Add logic for message box
                        if response == 1:
                                # Designate selections
                                x = paymentTree.selection()

                                # Create List of ID's
                                payment_ids_to_delete = []
                                
                                # Add selections to ids_to_delete list
                                for record in x:
                                        payment_ids_to_delete.append(paymentTree.item(record, 'values')[2])

                                # Delete From Treeview
                                for record in x:
                                        paymentTree.delete(record)

                                # Create a database or connect to one that exists
                                conn = sqlite3.connect('makeMyBill.db')

                                # Create a cursor instance
                                c = conn.cursor()
                                

                                # Delete Everything From The Table
                                c.executemany("DELETE FROM purchaseEntry WHERE id = ?", [(a,) for a in payment_ids_to_delete])

                                # Reset List
                                payment_ids_to_delete = []


                                # Commit changes
                                conn.commit()

                                # Close our connection
                                conn.close()

                                # Clear entry boxes if filled
                                clear_entries()


        # Remove all records
                def paymentRemoveAll():
                        # Add a little message box for fun
                        response = messagebox.askyesno("WOAH!!!!", "This Will Delete EVERYTHING From The Table\nAre You Sure?!")

                        #Add logic for message box
                        if response == 1:
                                # Clear the Treeview
                                for record in paymentTree.get_children():
                                        paymentTree.delete(record)

                                # Create a database or connect to one that exists
                                conn = sqlite3.connect('tree_crm.db')

                                # Create a cursor instance
                                c = conn.cursor()

                                # Delete Everything From The Table
                                c.execute("DROP TABLE paymentDetails")
                                        


                                # Commit changes
                                conn.commit()

                                # Close our connection
                                conn.close()

                                # Clear entry boxes if filled
                                paymentClearEntries()

                                # Recreate The Table
                                paymentCreatetableAgain()
                def paymentClearEntries():
                        # Clear entry boxes
                        paymentIdEntry.delete(0, END)
                        # paymentClientNameEntry.delete(0, END)
                        # d.delete(0, END)
                        paymentAmountEntry.delete(0, END)
                        modeOfPaymentEntry.delete(0, END)
                        PaymentRemarkEntry.delete(0, END)

                def paymentSelectRecords(e):
                # Clear entry boxes
                        paymentIdEntry.delete(0, END)
                        # paymentClientNameEntry.delete(0, END)
                        # d.delete(0, END)
                        paymentAmountEntry.delete(0, END)
                        modeOfPaymentEntry.delete(0, END)
                        PaymentRemarkEntry.delete(0, END)
#LEFT FROM HERE
                # Grab record Number
                        paymentSelected = paymentTree.focus()
                        # Grab record values
                        paymentValues = paymentTree.item(paymentSelected, 'values')

                        # outpus to entry boxes
                        paymentIdEntry.insert(0, paymentValues[0])
                        # paymentClientNameEntry.insert(0, paymentValues[1])
                        paymentAmountEntry.insert(0, paymentValues[2])
                        modeOfPaymentEntry.insert(0, paymentValues[4])
                        PaymentRemarkEntry.insert(0, paymentValues[5])

                def paymentUpdateRecords():
                        # Grab the record number
                        selected = paymentTree.focus()
                        # Update record
                        paymentTree.item(selected, text="", values=
                        (paymentIdEntry.get(), self.clicked2.get(), paymentAmountEntry.get(),
                        paymentCal.get_date(),
                        modeOfPaymentEntry.get(),
                        PaymentRemarkEntry.get()))

                        middlePaymentTree.item(selected, text="", values=
                        (paymentIdEntry.get(), self.clicked2.get(), paymentAmountEntry.get(),
                        paymentCal.get_date(),
                        int(paymentAmountEntry.get())-int(modeOfPaymentEntry.get()),
                        PaymentRemarkEntry.get()))

                        # Update the database
                        # Create a database or connect to one that exists
                        conn = sqlite3.connect('makeMyBill.db')

                        # Create a cursor instance
                        c = conn.cursor()

                        c.execute("""UPDATE paymentDetails SET
                                id = :paymentId,
                                clientName = :paymentClientName,
                                amount = :paymentAmout,
                                date = :paymentDate,
                                modeOfPayment = :paymentMode,
                                remark = :paymentRemark

                                WHERE oid = :oid""",
                                {
                                        'paymentId': paymentIdEntry.get(),
                                        'paymentClientName': self.clicked2.get(),
                                        'paymentAmout': paymentAmountEntry.get(),
                                        'paymentDate': paymentCal.get_date()+'',
                                        'paymentMode': modeOfPaymentEntry.get(),
                                        'paymentRemark': PaymentRemarkEntry.get(),
                                        'oid': paymentIdEntry.get(),
                                })
                        


                        # Commit changes
                        conn.commit()

                        # Close our connection
                        conn.close()


                        # Clear entry boxes
                        paymentIdEntry.delete(0, END)
                        # paymentClientNameEntry.delete(0, END)
                        # d.delete(0, END)
                        paymentAmountEntry.delete(0, END)
                        modeOfPaymentEntry.delete(0, END)
                        PaymentRemarkEntry.delete(0, END)
                def paymentAddRecord():
                        # Update the database
                        # Create a database or connect to one that exists
                        conn = sqlite3.connect('makeMyBill.db')

                        # Create a cursor instance
                        c = conn.cursor()

                        # Add New Record
                        c.execute("INSERT INTO paymentDetails VALUES (:id, :clientName, :amount, :date, :modeOfPayment, :remark)",
                                {
                                        'id': paymentIdEntry.get(),
                                        'clientName': self.clickedClientNamePayment.get(),
                                        'amount': paymentAmountEntry.get(),
                                        'date': paymentCal.get_date()+'',
                                        'modeOfPayment': modeOfPaymentEntry.get(),
                                        'remark': PaymentRemarkEntry.get(),                               })
                        

                        # Commit changes
                        conn.commit()

                        # Close our connection
                        conn.close()

                        # Clear entry boxes
                        paymentIdEntry.delete(0, END)
                        # paymentClientNameEntry.delete(0, END)
                        # d.delete(0, END)
                        paymentAmountEntry.delete(0, END)
                        modeOfPaymentEntry.delete(0, END)
                        PaymentRemarkEntry.delete(0, END)

                        middlePaymentTree.delete(*paymentTree.get_children())
                        paymentTree.delete(*paymentTree.get_children())

                        # Run to pull data from database on start
                        paymentQueryDatabase()



                def paymentCreatetableAgain():
                        # Create a database or connect to one that exists
                        conn = sqlite3.connect('makeMyBill.db')

                        # Create a cursor instance
                        c = conn.cursor()

                        # Create Table
                        c.execute("""CREATE TABLE if not exists paymentDetails (
                                id text,
                                clientName text,
                                amount integer,
                                date text,
                                modeOfPayment text,
                                remark text)
                                """)
                        
                        # Commit changes
                        conn.commit()

                        # Close our connection
                        conn.close()

                paymentButtonFrame = LabelFrame(paymentFrame, text="Commands")
                paymentButtonFrame.pack(fill="x", expand="yes", padx=20)

                paymentUpdateButton = Button(paymentButtonFrame, text="Update Record", command=paymentUpdateRecords)
                paymentUpdateButton.grid(row=0, column=0, padx=10, pady=10)

                paymentAddButton = Button(paymentButtonFrame, text="Add Record", command=paymentAddRecord)
                paymentAddButton.grid(row=0, column=1, padx=10, pady=10)


                paymentRemoveOneButton = Button(paymentButtonFrame, text="Remove One Selected", command=paymentRemoveOne)
                paymentRemoveOneButton.grid(row=0, column=3, padx=10, pady=10)


                paymentMoveUpButton = Button(paymentButtonFrame, text="Move Up", command=paymentUp)
                paymentMoveUpButton.grid(row=0, column=5, padx=10, pady=10)

                paymentMoveDownButton = Button(paymentButtonFrame, text="Move Down", command=paymentDown)
                paymentMoveDownButton.grid(row=0, column=6, padx=10, pady=10)

                payementSelectRecordButton = Button(paymentButtonFrame, text="Clear Entry Boxes", command=paymentClearEntries)
                payementSelectRecordButton.grid(row=0, column=7, padx=10, pady=10)

                # Bind the treeview
                paymentTree.bind("<ButtonRelease-1>", paymentSelectRecords)

                paymentQueryDatabase()














#Payment Frame ends here-------------------#############################______________________________________###################






#SALES FRAME STARTS HERE....................................................................
#SALES FRAME STARTS HERE....................................................................
#SALES FRAME STARTS HERE....................................................................
#SALES FRAME STARTS HERE....................................................................
#SALES FRAME STARTS HERE....................................................................
#SALES FRAME STARTS HERE....................................................................

                # self.billItems = []
                arrayListToCreateABill = []
                def openAddItemwindow():
                        salesWindow = Tk()
                        salesWindow.title("SALES")
                        salesWindow.geometry('800x430+250+250')

                        salesWindowQuantityNameLabel = Label(salesWindow,text="Quantity")
                        salesWindowQuantityNameLabel.grid(row=0, column=0, padx=10, pady=10)
                        
                        salesWindowQuantityNameEntry = Entry(salesWindow)
                        salesWindowQuantityNameEntry.grid(row=0, column=1, padx=10, pady=10)



                        salesWindowMaterialLabel = Label(salesWindow,text="Material")
                        salesWindowMaterialLabel.grid(row=2, column=0, padx=10, pady=10)

                
                        salesWindowPriceLabel = Label(salesWindow,text="Price")
                        salesWindowPriceLabel.grid(row=0, column=2, padx=10, pady=10)
                        salesWindowPriceEntry = Entry(salesWindow)
                        salesWindowPriceEntry.grid(row=0, column=3, padx=10, pady=10)


                
                        self.clickedMaterial = StringVar(salesWindow)
                        if len(self.materials)==0:
                                self.clickedMaterial.set("Default")
                                self.materials = ["Default"]
                        else :
                                self.clickedMaterial.set(self.materials[0])

                        self.materialNamesOptionsMenu = OptionMenu(salesWindow,self.clickedMaterial, *self.materials)
                        self.materialNamesOptionsMenu.grid(row=2, column=1)

                        #Material Option menu from the popup window----------END--xxxxxxxx-------xxxxxxxxxx---------xxxxxxxxx----------

                        #Client Option menu from the popup window--------------------------------------------------------------------
                        
                        salesWindowUnitLabel = Label(salesWindow,text="Unit")
                        salesWindowUnitLabel.grid(row=1, column=2, padx=10, pady=10)

                        clickedUnit = StringVar(salesWindow)
                        clickedUnit.set("kg")
                        self.materialNamesOptionsMenu = OptionMenu(salesWindow,clickedUnit, "Kg","Litres")
                        self.materialNamesOptionsMenu.grid(row=1, column=3)

                        def addToTheFirstAndTheSecondArrayList():
                                salesAddItemQuantity = salesWindowQuantityNameEntry.get()
                                salesAddItemMaterial = self.clickedMaterial.get()
                                salesAddItemPrice = salesWindowPriceEntry.get()
                                salesAddItemUnit = clickedUnit.get()


############################ DATABASE QUERIES ###################################################################

                                conn = sqlite3.connect('makeMyBill.db')

                                c = conn.cursor()
                        #where materialName = '{self.clickedMaterial.get()}'
                                # c.execute(f"SELECT * FROM materials where materialName = '{}' ")
                                c.execute(f"SELECT materialQuantity FROM materials2 where materialName = '{self.clickedMaterial.get()}'")

                                currentQuantityToBill = [i[0] for i in c.fetchall()]
                                # print(str(currentQuantityToBill)+"  updated")


                                # currentQuantityToBill[0] = currentQuantityToBill[0]+int(purchaseQuantityEntry.get())
                                # purchaseQuantityEntry.delete(0, END)

                                if(int(salesAddItemQuantity)>int(currentQuantityToBill[0])):
                                        #HASHIRAMA SENJU
                                        messagebox.showinfo("",f"You don't have enough {self.clickedMaterial.get()}")
                                        salesWindow.destroy()
                                else:
                                        currentQuantityToBill[0] = currentQuantityToBill[0]-int(salesAddItemQuantity)
                                        messagebox.showinfo("",f"Item added ! {self.clickedMaterial.get()}")
                                        tempoList = []
                                        tempoList.append(salesAddItemQuantity)
                                        tempoList.append(salesAddItemMaterial)
                                        tempoList.append(salesAddItemPrice)
                                        tempoList.append(salesAddItemUnit)

                                        arrayListToCreateABill.append(tempoList)



                                        c.execute(f"UPDATE materials2 SET materialQuantity = {currentQuantityToBill[0]} WHERE materialName = '{self.clickedMaterial.get()}'")
                                        salesWindow.destroy()
                                        multipleItemsListBox.delete(0,END)
                                        for item in arrayListToCreateABill:
                                                multipleItemsListBox.insert(END,f"{item[1]}    {item[2]}  Rs    {item[0]}    {item[3]}")

                                # c.execute(f"SELECT materialQuantity FROM materials2 where materialName = '{self.clickedMaterial.get()}'")
                                # currentQuantity2 = [i[0] for i in c.fetchall()]

                                # print(str(currentQuantity2)+"  updated")

                                # Commit changes
                                conn.commit()

                                # Close our connection
                                conn.close()
                                multipleItemsListBox.delete(0,END)
                                for item in arrayListToCreateABill:
                                        multipleItemsListBox.insert(END,f"{item[1]}    {item[2]}  Rs    {item[0]}    {item[3]}")
####################DATABASE QUERIES END HERE########################################################################################





                        #Client Option menu from the popup window-------------END----   xxxxx-----------xxxxxxxxxxxxxxxxx-------xxxxxxxxxx--------

                        addTheBillItemToTheListButton = Button(salesWindow,text="Add Item to the list",command=addToTheFirstAndTheSecondArrayList)
                        addTheBillItemToTheListButton.grid(row=3, column=0)
                
                def uploadToTheDatabase():
                        # conn = sqlite3.connect('makeMyBill.db')

                        # # Create a cursor instance
                        # c = conn.cursor()
                        # c.execute("DELETE FROM billRecords2")
                        # conn.commit()
                        # conn.close()
                        for item in arrayListToCreateABill:
                                # multipleItemsListBox.insert(END,f"{item[1]}    {item[2]}  Rs    {item[0]}    {item[3]}")
                                conn = sqlite3.connect('makeMyBill.db')

                        # Create a cursor instance
                                c = conn.cursor()

                                # Add New Record
                                c.execute("INSERT INTO billRecords2 VALUES (:material, :unit, :quantity, :price, :salesInvoiceDate, :clientName,:dueDate,:remark,:discount,:total)",
                                        {
                                                'material': item[1],
                                                'unit': item[3],
                                                'quantity': item[0],
                                                'price': item[2],
                                                'salesInvoiceDate': str(salesFrameInvoiceDateWidget.get_date()),
                                                'clientName': self.clickedClientSales.get(),    
                                                'dueDate': str(salesFrameDueDateWidget.get_date()),
                                                'remark': remarkEntrySalesFrame.get(),     
                                                'discount': discountEntrySalesFrame.get(),   
                                                'total': self.totalBill,         })
                
                                

                                # Commit changes
                                conn.commit()
                                conn.close()                

                        conn = sqlite3.connect('makeMyBill.db')

                        # Create a cursor instance
                        c = conn.cursor()

                        # Add New Record
                        c.execute("SELECT * FROM billRecords2")

                        #MADARA UCHIHA
                        print(c.fetchall())
                        # billRecords = [i[0] for i in c.fetchall()]
                        # print("DatabaseList as follows")
                        # print(billRecords)
                        

                        # Commit changes
                        conn.commit()
                        conn.close()   
                self.totalBill = 0
                def generateBillSales():
                        # print(arrayListToCreateABill)     
                        # for list in arrayListToCreateABill:


                        clientNameGenerateBillLabelName.config(text=self.clicked2.get())
                        salesInvoiceDateLabelNameLabel.config(text=str(salesFrameInvoiceDateWidget.get_date()))
                        salesDueDateLabelNameLabel.config(text=str(salesFrameDueDateWidget.get_date()))
                        salesDiscountLabelNameLabel.config(text=discountEntrySalesFrame.get())
                        salesRemarkLabelNameLabel.config(text=remarkEntrySalesFrame.get())

                        for item in arrayListToCreateABill:
                                self.totalBill = self.totalBill + (int(item[0])*int(item[2]))
                        discountDecimal = float(f"0.{int(discountEntrySalesFrame.get())}")
                        discountAmount = self.totalBill * discountDecimal
                        self.totalBill = self.totalBill - discountAmount

                        salesTotalBillLabelNameLabel.config(text=str(self.totalBill))
                                
                
                salesFrameMainFrame = LabelFrame(salesFrame)
                salesFrameMainFrame.place(x=10,y=60,height=530,width=1100)
                # This was frame 2



                multipleItemsListBox = Listbox(salesFrameMainFrame)
                multipleItemsListBox.place(x=15,y=50,width=300,height=250)

                
                ############## DEWANG's CODE ABOUT SALES WINDOWS ######################################################################



                generateBillFrame = LabelFrame(salesFrame)
                generateBillFrame.place(x=340,y=110,height=300,width=300)
                # THIS is the generate bill Frame

                clientNameGenerateBill = Label(generateBillFrame,text="Client Name :")
                clientNameGenerateBill.place(x=0,y=0)
                clientNameGenerateBillLabelName = Label(generateBillFrame,text="Mithi")
                clientNameGenerateBillLabelName.place(x=90,y=0)
                salesInvoiceNumberLabel = Label(generateBillFrame,text="Sales Invoice Date :")
                salesInvoiceNumberLabel.place(x=0,y=20)
                salesInvoiceDateLabelNameLabel = Label(generateBillFrame,text="123")
                salesInvoiceDateLabelNameLabel.place(x=110,y=20)
                salesDueDateLabel = Label(generateBillFrame,text="Due date :")
                salesDueDateLabel.place(x=0,y=40)
                salesDueDateLabelNameLabel = Label(generateBillFrame,text="12/12/12")
                salesDueDateLabelNameLabel.place(x=80,y=40)
                salesDiscountLabel = Label(generateBillFrame,text="Discount :")
                salesDiscountLabel.place(x=0,y=60)
                salesDiscountLabelNameLabel = Label(generateBillFrame,text="5%")
                salesDiscountLabelNameLabel.place(x=80,y=60)
                salesRemarkLabel = Label(generateBillFrame,text="Remark :")
                salesRemarkLabel.place(x=0,y=80)
                salesRemarkLabelNameLabel = Label(generateBillFrame,text="Remakr Remark Remark")
                salesRemarkLabelNameLabel.place(x=80,y=80)
                salesTotalBillLabel = Label(generateBillFrame,text="Total :")
                salesTotalBillLabel.place(x=0,y=100)
                salesTotalBillLabelNameLabel = Label(generateBillFrame,text="500")
                salesTotalBillLabelNameLabel.place(x=100,y=100)


                
                

                salesdateSalesFrame = Label(salesFrameMainFrame,text = "Sales Invoice Date")
                salesdateSalesFrame.place(x = 880,y = 10)
                salesFrameInvoiceDateWidget = DateEntry(salesFrameMainFrame)
                salesFrameInvoiceDateWidget.place(x = 870,y = 40)

                duedateSalesFrame = Label(salesFrameMainFrame,text = "Due Date")
                duedateSalesFrame.place(x = 880,y = 100)
                salesFrameDueDateWidget = DateEntry(salesFrameMainFrame)
                salesFrameDueDateWidget.place(x = 870,y = 130)

                discountLabelSalesFrame = Label(salesFrameMainFrame,text = "Discount")
                discountLabelSalesFrame.place(x=710,y=10)
                discountEntrySalesFrame = Entry(salesFrameMainFrame)
                discountEntrySalesFrame.place(x=700,y=40)
                discountLabelSalesFrame = Label(salesFrameMainFrame,text = "Client Name")
                discountLabelSalesFrame.place(x=700,y=100)
                
                self.clickedClientSales = StringVar()
                if len(self.suppliers)==0:
                        self.clickedClientSales.set("Default")
                        self.suppliers = ["Default"]
                else :
                        self.clickedClientSales.set(self.suppliers[0])

                self.paymentClientNameOptionsMenu = OptionMenu(salesFrameMainFrame,self.clickedClientSales, *self.suppliers)
                # self.paymentClientNameOptionsMenu.grid(row=0, column=1, padx=10, pady=10)
                self.paymentClientNameOptionsMenu.place(x=700,y=130)

                

                remarkLabelSalesFrame = Label(salesFrameMainFrame,text = "Remark")
                remarkLabelSalesFrame.place(x=710,y=280)
                remarkEntrySalesFrame = Entry(salesFrameMainFrame)
                remarkEntrySalesFrame.place(x=700,y=310,width=300)



                self.sendMessageEntry = Entry(salesFrameMainFrame)
                self.sendMessageEntry.place(x=15,y=475)
                sendMessageButton = Button(salesFrameMainFrame,text="SEND MESSAGE",command=email_alert)
                sendMessageButton.place(x=150,y=475)

                
                addItemButtonSalesFrame = Button(salesFrameMainFrame,text = "Add Item",command=openAddItemwindow)
                addItemButtonSalesFrame.place(x=15,y=15)

                #This was frame 3

                updateBillOnTheScreenButton = Button(salesFrameMainFrame,text = "Update Bill",command=generateBillSales)
                updateBillOnTheScreenButton.place(x=15,y=370)


                salesFrameAddItemButton = Button(salesFrameMainFrame,text = "Generate Bill",command=uploadToTheDatabase)
                salesFrameAddItemButton.place(x=180,y=370,height=80,width=800)

                #labels for subtotal n all

                ############## DEWANG's CODE ABOUT SALES WINDOWS ######################################################################
                











#SALES FRAME ENDS HERE....................................................................
#SALES FRAME ENDS HERE....................................................................
#SALES FRAME ENDS HERE....................................................................
#SALES FRAME ENDS HERE....................................................................
#SALES FRAME ENDS HERE....................................................................
#SALES FRAME ENDS HERE....................................................................
#SALES FRAME ENDS HERE....................................................................
#SALES FRAME ENDS HERE....................................................................




#REPORT FRAME STARTS HERE -----------------------------------------------------------------------
#REPORT FRAME STARTS HERE -----------------------------------------------------------------------
#REPORT FRAME STARTS HERE -----------------------------------------------------------------------
#REPORT FRAME STARTS HERE -----------------------------------------------------------------------
#REPORT FRAME STARTS HERE -----------------------------------------------------------------------


                def searchFromTheDatabase():

                        conn = sqlite3.connect('makeMyBill.db')

                        # Create a cursor instance
                        c = conn.cursor()
                        # print(self.clicked2)
                        # Add New RecordsearchFromTheDatabase
                        c.execute(f"SELECT * FROM billRecords2 where clientName = '{self.clicked2.get()}' AND salesInvoiceDate = '{reportFrameInvoiceDateWidget.get_date()}'")
                        recsAccordingToClientName = c.fetchall()
                        print(recsAccordingToClientName)
                        #MADARA UCHIHA
                        # billRecords = [i[0] for i in c.fetchall()]
                        # print(billRecords)
                        for item in recsAccordingToClientName:
                                print(f"{item[0]}****{item[1]}****{item[2]}")
                                searchListBox.insert(END,f"{item[0]}        {item[1]}        {item[2]}        {item[3]}        {item[4]}        {item[5]}        {item[6]}        {item[7]}        {item[8]}        {item[9]}")

                        # Commit changes
                        conn.commit()
                        conn.close()   

                self.clicked2 = StringVar()
                if len(self.suppliers)==0:
                        self.clicked2.set("Default")
                        self.suppliers = ["Default"]
                else :
                        self.clicked2.set(self.suppliers[0])

                self.paymentClientNameOptionsMenu = OptionMenu(reportFrame,self.clicked2, *self.suppliers)
                # self.paymentClientNameOptionsMenu.grid(row=0, column=1, padx=10, pady=10)
                self.paymentClientNameOptionsMenu.place(x=15,y=15)

                reportdateSalesFrame = Label(reportFrame,text = "Date :")
                reportdateSalesFrame.place(x = 15,y = 60)
                reportFrameInvoiceDateWidget = DateEntry(reportFrame)
                reportFrameInvoiceDateWidget.place(x = 15,y = 80)

                searchButton = Button(reportFrame,text="Search",command=searchFromTheDatabase)
                searchButton.place(x=15,y=115)

                searchListBox = Listbox(reportFrame)
                searchListBox.place(x=125,y=25,width=800,height=400)
                searchListBox.insert(0,"MATERIAL        UNIT        QUANTITY        PRICE        INVOICE DATE        CLIENT NAME        DUE DATE        REMARK        DISCOUNT        TOTAL BILL")



#REPORT FRAME ENDS HERE---------------------------------------------------------------------------------
#REPORT FRAME ENDS HERE---------------------------------------------------------------------------------
#REPORT FRAME ENDS HERE---------------------------------------------------------------------------------
#REPORT FRAME ENDS HERE---------------------------------------------------------------------------------
#REPORT FRAME ENDS HERE---------------------------------------------------------------------------------
#REPORT FRAME ENDS HERE---------------------------------------------------------------------------------










####CLIENT FRAME STARTS HERE---------------------------------------------------------------------------
####CLIENT FRAME STARTS HERE---------------------------------------------------------------------------
####CLIENT FRAME STARTS HERE---------------------------------------------------------------------------
####CLIENT FRAME STARTS HERE---------------------------------------------------------------------------
####CLIENT FRAME STARTS HERE---------------------------------------------------------------------------
####CLIENT FRAME STARTS HERE---------------------------------------------------------------------------
####CLIENT FRAME STARTS HERE---------------------------------------------------------------------------
####CLIENT FRAME STARTS HERE---------------------------------------------------------------------------


                conn = sqlite3.connect('makeMyBill.db')

                # Create a cursor instance
                c = conn.cursor()

                # Create Table
                c.execute("""CREATE TABLE if not exists clientDetails (
                                clientId text,
                                clientName text,
                                clientSurname text,
                                clientPlace text,
                                clientPhone text,
                                clientEmail text)
                """)

                c.execute("""CREATE TABLE if not exists billRecords2 (
                                                materialName text,
                                                unit text,
                                                quantity integer,
                                                price integer,
                                                salesInvoiceDate text,
                                                clientName text,
                                                dueDate text,
                                                remark text,
                                                discount integer,
                                                total integer)
                                """)

                def clientQueryDatabase():
                        # Create a database or connect to one that exists
                        conn = sqlite3.connect('makeMyBill.db')

                        # Create a cursor instance
                        c = conn.cursor()

                        c.execute("SELECT rowid, * FROM clientDetails")
                        clientRecords =[]
                        clientRecords = c.fetchall()

                        
                        # Add our data to the screen
                        global count3
                        count3 = 0
                        
                        #for record in records:
                                

                        for record in clientRecords:

                                if count3 % 2 == 0:
                                        clientTree.insert(parent='', index='end',text='', values=(record[0], record[2], record[3], record[4], record[5], record[6]), tags=('evenrow',))
                                else:
                                        clientTree.insert(parent='', index='end', text='', values=(record[0], record[2], record[3], record[4], record[5], record[6]), tags=('oddrow',))
                                
                                count3 +=1

                                # increment counter


                        # Commit changes
                        conn.commit()

                        # Close our connection
                        conn.close()



        # Add Some Style
                style = ttk.Style()

                # Pick A Theme
                style.theme_use('default')

                # Configure the Treeview Colors
                style.configure("Treeview",
                background="#D3D3D3",
                foreground="black",
                rowheight=25,
                fieldbackground="#D3D3D3")

                
        # Change Selected Color
                style.map('Treeview',
                        background=[('selected', "#347083")])

                # Create a Treeview Frame
                clientTreeFrame = Frame(clientFrame)
                clientTreeFrame.pack(pady=10)


                # Create a Treeview Scrollbar
                clientTreeScrollBar = Scrollbar(clientTreeFrame)
                clientTreeScrollBar.pack(side=RIGHT, fill=Y)


                # Create The Treeview
                clientTree = ttk.Treeview(clientTreeFrame, yscrollcommand=clientTreeScrollBar.set, 
                selectmode="extended")

                clientTree.pack()

                clientTreeScrollBar.config(command=paymentTree.yview)

                # Define Our Columns
                clientTree['columns'] = ("ID", "Client Name", "Client Surname", "Place",
                 "Phone","Email")

                # Format Our Columns
                clientTree.column("#0", width=0, stretch=NO)
                clientTree.column("ID", anchor=W, width=140)
                clientTree.column("Client Name", anchor=W, width=140)
                clientTree.column("Client Surname", anchor=CENTER, width=100)
                clientTree.column("Place", anchor=CENTER, width=140)
                clientTree.column("Phone", anchor=CENTER, width=140)
                clientTree.column("Email", anchor=CENTER, width=140)


                # Create Headings
                clientTree.heading("#0", text="", anchor=W)
                clientTree.heading("ID", text="ID", anchor=W)
                clientTree.heading("Client Name", text="Client Name", anchor=W)
                clientTree.heading("Client Surname", text="Client Surname", anchor=CENTER)
                clientTree.heading("Place", text="Place", anchor=CENTER)
                clientTree.heading("Phone", text="Phone", anchor=CENTER)
                clientTree.heading("Email", text="Email", anchor=CENTER)


                # Create Striped Row Tags
                clientTree.tag_configure('oddrow', background="white")
                clientTree.tag_configure('evenrow', background="lightblue")

                clientDataFrame = LabelFrame(clientFrame, text="Record")
                clientDataFrame.pack(fill="x", expand="yes", padx=20)


                clientIdLabel = Label(clientDataFrame, text="ID")
                clientIdLabel.grid(row=1, column=6, padx=10, pady=10)
                clientIdEntry = Entry(clientDataFrame)
                clientIdEntry.grid(row=1, column=7, padx=10, pady=10)



                clientClientNameLabel = Label(clientDataFrame, text="Client Name")
                clientClientNameLabel.grid(row=0, column=0, padx=10, pady=10)
                clientClientNameEntry = Entry(clientDataFrame)
                clientClientNameEntry.grid(row=0, column=1, padx=10, pady=10)

                clientClientSurnameLabel = Label(clientDataFrame, text="Client Surname")
                clientClientSurnameLabel.grid(row=0, column=2, padx=10, pady=10)
                clientClientSurnameEntry = Entry(clientDataFrame)
                clientClientSurnameEntry.grid(row=0, column=3, padx=10, pady=10)

                clientPlaceLabel = Label(clientDataFrame, text="Place")
                clientPlaceLabel.grid(row=0, column=4, padx=10, pady=10)
                clientPlaceEntry = Entry(clientDataFrame)
                clientPlaceEntry.grid(row=0, column=5, padx=10, pady=10)




                clientPhoneLabel = Label(clientDataFrame, text="Phone")
                clientPhoneLabel.grid(row=1, column=0, padx=10, pady=10)
                clientPhoneEntry = Entry(clientDataFrame)
                clientPhoneEntry.grid(row=1, column=1, padx=10, pady=10)



                clientEmailLabel = Label(clientDataFrame, text="Email")
                clientEmailLabel.grid(row=1, column=2, padx=10, pady=10)
                clientEmailEntry = Entry(clientDataFrame)
                clientEmailEntry.grid(row=1, column=3, padx=10, pady=10)



                clientBackButton = Button(clientFrame,text="Go back",command=lambda:showFrame(middleFrame))
                clientBackButton.place(x=2,y=2)


                # Move Row Up
                def clientPaymentUp():
                        rows = clientTree.selection()
                        for row in rows:
                                clientTree.move(row, clientTree.parent(row), clientTree.index(row)-1)

                # Move Rown Down
                def clientPaymentDown():
                        rows = clientTree.selection()
                        for row in reversed(rows):
                                clientTree.move(row, clientTree.parent(row), clientTree.index(row)+1)

        # Remove one record
                def clientRemoveOne():
                        x = clientTree.selection()[0]
                        clientTree.delete(x)

                        # Create a database or connect to one that exists
                        conn = sqlite3.connect('makeMyBill.db')

                        # Create a cursor instance
                        c = conn.cursor()

                        # Delete From Database
                        c.execute("DELETE from clientDetails WHERE oid=" + clientIdEntry.get())

                        # Commit changes
                        conn.commit()

                        # Close our connection
                        conn.close()
                        clientClearEntries()

                # Add a little message box for fun



        # Remove Many records
                def clientRemoveMany():
                        # Add a little message box for fun
                        response = messagebox.askyesno("WOAH!!!!", "This Will Delete EVERYTHING SELECTED From The Table\nAre You Sure?!")

                        #Add logic for message box
                        if response == 1:
                                # Designate selections
                                x = clientTree.selection()

                                # Create List of ID's
                                client_ids_to_delete = []
                                
                                # Add selections to ids_to_delete list
                                for record in x:
                                        client_ids_to_delete.append(clientTree.item(record, 'values')[2])

                                # Delete From Treeview
                                for record in x:
                                        clientTree.delete(record)

                                # Create a database or connect to one that exists
                                conn = sqlite3.connect('makeMyBill.db')

                                # Create a cursor instance
                                c = conn.cursor()
                                

                                # Delete Everything From The Table
                                c.executemany("DELETE FROM clientDetails WHERE id = ?", [(a,) for a in client_ids_to_delete])

                                # Reset List
                                client_ids_to_delete = []


                                # Commit changes
                                conn.commit()

                                # Close our connection
                                conn.close()

                                # Clear entry boxes if filled
                                clientClearEntries()


        # Remove all records
                def clientRemoveAll():
                        # Add a little message box for fun
                        response = messagebox.askyesno("WOAH!!!!", "This Will Delete EVERYTHING From The Table\nAre You Sure?!")

                        #Add logic for message box
                        if response == 1:
                                # Clear the Treeview
                                for record in clientTree.get_children():
                                        clientTree.delete(record)

                                # Create a database or connect to one that exists
                                conn = sqlite3.connect('tree_crm.db')

                                # Create a cursor instance
                                c = conn.cursor()

                                # Delete Everything From The Table
                                c.execute("DROP TABLE clientDetails")
                                        


                                # Commit changes
                                conn.commit()

                                # Close our connection
                                conn.close()

                                # Clear entry boxes if filled
                                clientClearEntries()

                                # Recreate The Table
                                clientCreateTableAgain()
                def clientClearEntries():
                        # Clear entry boxes
                        clientIdEntry.delete(0, END)
                        clientClientNameEntry.delete(0, END)
                        # d.delete(0, END)
                        clientClientSurnameEntry.delete(0, END)
                        clientPlaceEntry.delete(0, END)
                        clientPhoneEntry.delete(0, END)
                        clientEmailEntry.delete(0, END)


                def clientSelectRecords(e):
                # Clear entry boxes
                        clientIdEntry.delete(0, END)
                        clientClientNameEntry.delete(0, END)
                        # d.delete(0, END)
                        clientClientSurnameEntry.delete(0, END)
                        clientPlaceEntry.delete(0, END)
                        clientPhoneEntry.delete(0, END)
                        clientEmailEntry.delete(0, END)

                        
#LEFT FROM HERE
                # Grab record Number
                        clientSelected = clientTree.focus()
                        # Grab record values
                        clientValues = clientTree.item(clientSelected, 'values')

                        # outpus to entry boxes
                        clientIdEntry.insert(0, clientValues[0])
                        clientClientNameEntry.insert(0, clientValues[1])
                        clientClientSurnameEntry.insert(0, clientValues[2])
                        clientPlaceEntry.insert(0, clientValues[3])
                        clientPhoneEntry.insert(0, clientValues[4])
                        clientEmailEntry.insert(0, clientValues[4])


                def clientUpdateRecords():
                        # Grab the record number
                        selected = clientTree.focus()
                        # Update record
                        clientTree.item(selected, text="", values=
                        (clientIdEntry.get(), clientClientNameEntry.get(), clientClientSurnameEntry.get(),
                        clientPlaceEntry.get(),
                        clientPhoneEntry.get(),
                        clientEmailEntry.get()))

                        # Update the database
                        # Create a database or connect to one that exists
                        conn = sqlite3.connect('makeMyBill.db')

                        # Create a cursor instance
                        c = conn.cursor()

                        c.execute("""UPDATE clientDetails SET
                                clientId = :clientId,
                                clientName = :clientName,
                                clientSurname = :clientSurname,
                                clientPlace = :clientPlace,
                                clientPhone = :clientPhone,
                                clientEmail = :clientEmail

                                WHERE oid = :oid""",
                                {
                                        'clientId': clientIdEntry.get(),
                                        'clientName': clientClientNameEntry.get(),
                                        'clientSurname': clientClientSurnameEntry.get(),
                                        'clientPlace': clientPlaceEntry.get(),
                                        'clientPhone': clientPhoneEntry.get(),
                                        'clientEmail': clientEmailEntry.get(),
                                        'oid': clientIdEntry.get(),
                                })
                        


                        # Commit changes
                        conn.commit()

                        # Close our connection
                        conn.close()


                        # Clear entry boxes
                        clientIdEntry.delete(0, END)
                        clientClientNameEntry.delete(0, END)
                        # d.delete(0, END)
                        clientClientSurnameEntry.delete(0, END)
                        clientPlaceEntry.delete(0, END)
                        clientEmailEntry.delete(0, END)
                        clientPhoneEntry.delete(0, END)



                def clientAddRecord():
                        # Update the database
                        # Create a database or connect to one that exists
                        conn = sqlite3.connect('makeMyBill.db')

                        # Create a cursor instance
                        c = conn.cursor()

                        # Add New Record
                        c.execute("INSERT INTO clientDetails VALUES (:clientId, :clientName, :clientSurname, :clientPlace, :clientPhone, :clientEmail)",
                                {
                                        'clientId': clientIdEntry.get(),
                                        'clientName': clientClientNameEntry.get(),
                                        'clientSurname': clientClientSurnameEntry.get(),
                                        'clientPlace': clientPlaceEntry.get(),
                                        'clientPhone': clientPhoneEntry.get(),
                                        'clientEmail': clientEmailEntry.get(),                               })
                        

                        # Commit changes
                        conn.commit()
                        conn = sqlite3.connect('makeMyBill.db')

                        c = conn.cursor()
                        c.execute("SELECT clientName FROM clientDetails")
                        self.suppliers = [i[0] for i in c.fetchall()]
                        self.clientNameOptionsMenu = OptionMenu(createBillFrame,self.clicked, *self.suppliers)
                        self.clientNameOptionsMenu.place(x=115,y=105,height=30,width=200)
                        self.paymentClientNameOptionsMenu = OptionMenu(paymentDataFrame,self.clicked2, *self.suppliers)
                        self.paymentClientNameOptionsMenu.grid(row=0, column=1, padx=10, pady=10)
                        conn.commit()
                        # Close our connection
                        conn.close()

                        # Clear entry boxes
                        clientIdEntry.delete(0, END)
                        clientClientNameEntry.delete(0, END)
                        # d.delete(0, END)
                        clientClientSurnameEntry.delete(0, END)
                        clientPlaceEntry.delete(0, END)
                        clientPhoneEntry.delete(0, END)
                        clientEmailEntry.delete(0,END)

                        clientTree.delete(*clientTree.get_children())

                        # Run to pull data from database on start
                        #insder delete

                        clientQueryDatabase()



                def clientCreateTableAgain():
                        # Create a database or connect to one that exists
                        conn = sqlite3.connect('makeMyBill.db')

                        # Create a cursor instance
                        c = conn.cursor()

                        # Create Table
                        c.execute("""CREATE TABLE if not exists clientDetails (
                                clientId text,
                                clientName text,
                                clientSurname integer,
                                clientPlace text,
                                clientPhone text,
                                clientEmail text)
                                """)
                        
                        # Commit changes
                        conn.commit()

                        # Close our connection
                        conn.close()

                clientButtonFrame = LabelFrame(clientFrame, text="Commands")
                clientButtonFrame.pack(fill="x", expand="yes", padx=20)

                clientUpdateButton = Button(clientButtonFrame, text="Update Record", command=clientUpdateRecords)
                clientUpdateButton.grid(row=0, column=0, padx=10, pady=10)

                clientAddButton = Button(clientButtonFrame, text="Add Record", command=clientAddRecord)
                clientAddButton.grid(row=0, column=1, padx=10, pady=10)


                clientRemoveOneButton = Button(clientButtonFrame, text="Remove One Selected", command=clientRemoveOne)
                clientRemoveOneButton.grid(row=0, column=3, padx=10, pady=10)


                clientMoveUpButton = Button(clientButtonFrame, text="Move Up", command=clientPaymentUp)
                clientMoveUpButton.grid(row=0, column=5, padx=10, pady=10)

                clientMoveDownButton = Button(clientButtonFrame, text="Move Down", command=clientPaymentDown)
                clientMoveDownButton.grid(row=0, column=6, padx=10, pady=10)

                clientSelectRecordsButton = Button(clientButtonFrame, text="Clear Entry Boxes", command=clientClearEntries)
                clientSelectRecordsButton.grid(row=0, column=7, padx=10, pady=10)

                # Bind the treeview
                clientTree.bind("<ButtonRelease-1>", clientSelectRecords)

                clientQueryDatabase()










####CLIENT FRAME ENDS HERE---------------------------------------------------------------------------
####CLIENT FRAME ENDS HERE---------------------------------------------------------------------------
####CLIENT FRAME ENDS HERE---------------------------------------------------------------------------
####CLIENT FRAME ENDS HERE---------------------------------------------------------------------------
####CLIENT FRAME ENDS HERE---------------------------------------------------------------------------
####CLIENT FRAME ENDS HERE---------------------------------------------------------------------------
####CLIENT FRAME ENDS HERE---------------------------------------------------------------------------
####CLIENT FRAME ENDS HERE---------------------------------------------------------------------------
####CLIENT FRAME ENDS HERE---------------------------------------------------------------------------











                # sideFrame.pack(side=LEFT,fill="y")   
                # createBillFrame.place(x=225,y=120,width=1132,height=580)

                
                # createBillFrameLabel = Label(createBillFrame,text="Create Bill",bg="#c2e4ed")
                # # createBillFrameLabel.place(x=0,y=0,width=1120)
                # createBillFrameLabel.pack(fill=X)
                
                createBillFrameGoBackButton = Button(createBillFrame, text="Go back"
                ,command=lambda:showFrame(middleFrame))
                createBillFrameGoBackButton.place(x=10,y=25,width=150)

        #      Generate bill function-----------------------------------------------------------------
                # def generateBillOnTheScreen():
                #         generateBillFrame = Frame(createBillFrame, border=6,relief=SUNKEN)
                #         generateBillFrame.place(x=700,y=25,width=400,height=400)
                        
                #         #------------PrintBill Name---------------------------
                #         billNamelabel = Label(generateBillFrame,text="Name :")
                #         billNamelabel.place(x=15,y=15,width=40,height=20)
                #         billNameActual = Label(generateBillFrame,text="Mithilesh Pandit")
                #         billNameActual.place(x=70,y=15,width=120,height=20)
                #         #Print Bill name xxxxxxxxxxx--------------------------

                #         #Printbill material -------------------------------------
                #         materialNamelabel = Label(generateBillFrame,text="Material :")
                #         materialNamelabel.place(x=15,y=50,width=50,height=20)
                #         billNameActual = Label(generateBillFrame,text="Milk")
                #         billNameActual.place(x=70,y=50,width=120,height=20)
                #         #Print bill material --xxxxxxxxxxxxx----------------------

                #         #Printbill Quantity ---------------------------------------
                #         quantityNameLabel = Label(generateBillFrame,text="Quantity :")
                #         quantityNameLabel.place(x=15,y=85,width=50,height=20)
                #         quantityNameActual = Label(generateBillFrame,text="10 litres")
                #         quantityNameActual.place(x=80,y=85,width=120,height=20)   

                #         #Print bill Quantity    ----------xxxxxxxxxx-----------------
                                
                #         #Print bill Unit ------------------------------------------
                #         unitNameLabel = Label(generateBillFrame,text="Unit")
                #         unitNameLabel.place(x=15,y=120,width=50, height=20)
                #         unitNameActual = Label(generateBillFrame,text="2")
                #         unitNameActual.place(x=80,y=120,width=120,height=20)
                #         #Print bill Quantity xxxxxxxxxxx--------------------------

                #         #Print Price ---------------------------------------
                #         priceNameLabel = Label(generateBillFrame,text="Price")
                #         priceNameLabel.place(x=15,y=155,width=50, height=20)
                #         priceNameActual = Label(generateBillFrame,text="150 Rs")
                #         priceNameActual.place(x=80,y=155,width=120,height=20)
                #         #Price Price-------x-x-x-x-x-x-x-x-x-x------------------

                        
                #         #Print Discount ---------------------------------------
                #         discountNameLabel = Label(generateBillFrame,text="Discount")
                #         discountNameLabel.place(x=15,y=190,width=50, height=20)
                #         discountNameActual = Label(generateBillFrame,text="5%")
                #         discountNameActual.place(x=80,y=190,width=120,height=20)
                #         #Price Discount-------x-x-x-x-x-x-x-x-x-x------------------

                        
                #         #Print Remark ---------------------------------------
                #         remarkNameLabel = Label(generateBillFrame,text="Remark :")
                #         remarkNameLabel.place(x=15,y=225,width=50, height=20)
                #         remarkNameActual = Label(generateBillFrame,text="2000 Rs paid in advance next installment is supposed"
                #         +"to be paid before 15th of July. \n Name - Ramesh Singh ",wraplength=270,justify=LEFT)
                #         remarkNameActual.place(x=80,y=225,width=300,height=60)
                #         #Price Remark-------x-x-x-x-x-x-x-x-x-x------------------
                        
                        
                #         # Print SGST --------------------------------------------
                #         sgstNameLabel = Label(generateBillFrame,text="Sgst :") 
                #         sgstNameLabel.place(x=205,y=15,width=50, height=20)
                #         sgstNameActual = Label(generateBillFrame,text="5%")
                #         sgstNameActual.place(x=270,y=15,width=50,height=20)
                #         # generateBillFrame.destroy()
                        #Create Bill Frame ---------------xxxxxxxxxxxxxxxxxxxxxx--------------------------------

                        #Print cgst------------------------------------------------------------------
                        # cgstNameLabel = Label(generateBillFrame,text="Sgst :") 
                        # cgstNameLabel.place(x=205,y=50,width=50, height=20)
                        # cgstNameActual = Label(generateBillFrame,text="5%")
                        # cgstNameActual.place(x=270,y=50,width=50,height=20)
                        # #Print cgst ------xxxxxxxxxx-------------------------------------------------


                        # #Total -----------------------------------------------------------
                        # totalNameLabel = Label(generateBillFrame,text="Total :")
                        # totalNameLabel.place(x=15,y=385,width=50,height=20)
                        # totalNameActual = Label(generateBillFrame,text="2000 Rs")
                        # totalNameActual.place(x=80,y=385,width=50,height=20)
        #Generate Bill function xxxx------------------------xxxxxxxxxxxx---------------------------------------------
                
                # showFrame(middleFrame)
                for frame in (middleFrame,createBillFrame,purchaseEntryFrame,paymentFrame,clientFrame,salesFrame,reportFrame):
                        frame.grid(row=0,column=0,sticky='nsew')

                showFrame(middleFrame)
                #Show frame --------------xxxxxxxxx----------------xxxxxxxxxxx---------------xxxxxxxxxxx-------------

                def clientDetailsWindow():
                        clientDetailsWindow = Tk()
                        clientDetailsWindow.title("Upload client")
                        clientDetailsWindow.geometry('600x230+250+250')


                        clientNameLabel = Label(clientDetailsWindow,text="Client Name")
                        clientNameLabel.place(x=15,y=15,height=30,width=70)
                        clientNameTextbox = Text(clientDetailsWindow)
                        clientNameTextbox.place(x=100,y=15,height=30,width=150)


                        clientSurnameLabel = Label(clientDetailsWindow,text="Client Surname")
                        clientSurnameLabel.place(x=310,y=15,height=30,width=85)
                        clientSurnameTextbox = Text(clientDetailsWindow)
                        clientSurnameTextbox.place(x=410,y=15,height=30,width=150)


                        
                        clientPlace = Label(clientDetailsWindow,text="Place")
                        clientPlace.place(x=15,y=60,height=30,width=85)
                        clientPlace = Text(clientDetailsWindow)
                        clientPlace.place(x=100,y=60,height=30,width=150)



                        clientPhone = Label(clientDetailsWindow,text="Phone")
                        clientPhone.place(x=310,y=60,height=30,width=85)
                        clientPhone = Text(clientDetailsWindow)
                        clientPhone.place(x=410,y=60,height=30,width=150)



                        clientEmail = Label(clientDetailsWindow,text="Email")
                        clientEmail.place(x=15,y=105,height=30,width=85)
                        clientEmail = Text(clientDetailsWindow)
                        clientEmail.place(x=100,y=105,height=30,width=150)



                        clientEmail = Label(clientDetailsWindow,text="2nd Ph no. \n(Optional)")
                        clientEmail.place(x=310,y=105,height=30,width=85)
                        clientEmail = Text(clientDetailsWindow)
                        clientEmail.place(x=410,y=105,height=30,width=150)


                        saveButton = Button(clientDetailsWindow,text="Save")
                        saveButton.place(x=230,y=175,height=30,width=150)



                # createBillFrameAddClient = Button(createBillFrame, text="+ Add Client",command=clientDetailsWindow)
                # createBillFrameAddClient.place(x=180,y=25,width=150)
                #Frame Go back button ----------------------x--------------------------

                #I don't need a frame for this
                clientName = Label(createBillFrame,text="Client Name")
                clientName.place(x=15,y=105,height=30,width=85)
                self.clicked = StringVar()
                self.clicked.set(self.suppliers[0])
                self.clientNameOptionsMenu = OptionMenu(createBillFrame,self.clicked, *self.suppliers)
                self.clientNameOptionsMenu.place(x=115,y=105,height=30,width=200)


                clientMaterial = Label(createBillFrame,text="Material")
                clientMaterial.place(x=330,y=105,height=30,width=85)
                # clientMaterialText = Entry(createBillFrame)
                # clientMaterialText.place(x=430,y=105,height=30,width=150)
                #Itachi Uchiha

                if len(self.materials)==0:
                        self.clickedMaterial.set("Default")
                        self.materials = ["Default"]
                else :
                        self.clickedMaterial.set(self.materials[0])

                self.materialNamesOptionsMenuCreateBill = OptionMenu(createBillFrame,self.clickedMaterial, *self.materials)
                self.materialNamesOptionsMenuCreateBill.place(x=430,y=105,height=30,width=150)

                clientQuantity = Label(createBillFrame,text="Quantity")
                clientQuantity.place(x=15,y=150,height=30,width=85)
                clientQuantityText = Entry(createBillFrame)
                clientQuantityText.place(x=115,y=150,height=30,width=150)


                clientUnit = Label(createBillFrame,text="Unit")
                clientUnit.place(x=330,y=150,height=30,width=85)
                # clientUnitText = Entry(createBillFrame)
                # clientUnitText.place(x=430,y=150,height=30,width=150)

                unitList = list(range(1, 16))


                unitClicked = StringVar()
                unitClicked.set(1)
                clientName = OptionMenu(createBillFrame,unitClicked,*unitList)
                clientName.place(x=430,y=150,height=30,width=150)


                clientDiscount = Label(createBillFrame,text="Discount")
                clientDiscount.place(x=15,y=195,height=30,width=85)
                clientDiscountText = Entry(createBillFrame)
                clientDiscountText.place(x=115,y=195,height=30,width=150)

                clientPrice = Label(createBillFrame,text="Price")
                clientPrice.place(x=325,y=195,height=30,width=85)
                clientPriceText = Entry(createBillFrame)
                clientPriceText.place(x=425,y=195,height=30,width=150)

                clientRemark = Label(createBillFrame,text="Remark")
                clientRemark.place(x=15,y=240,height=30,width=85)
                clientRemarkText = Entry(createBillFrame)
                clientRemarkText.place(x=115,y=240,height=90,width=475)


                #GENERATE BILL FRAME THIS IS ISOLATED
                generateBillFrame = Frame(createBillFrame, border=6,relief=SUNKEN)

                billNameActual = Label(generateBillFrame,text="Mithilesh Pandit")
                billMaterialActual = Label(generateBillFrame,text="Milk")
                quantityNameActual = Label(generateBillFrame,text="10 litres")
                unitNameActual = Label(generateBillFrame,text="2")
                priceNameActual = Label(generateBillFrame,text="150 Rs")
                discountNameActual = Label(generateBillFrame,text="5%")
                remarkNameActual = Label(generateBillFrame,text="2000 Rs paid in advance next installment is supposed"
                +"to be paid before 15th of July. \n Name - Ramesh Singh ",wraplength=270,justify=LEFT)

                totalNameActual = Label(generateBillFrame,text="")

                self.phoneNumberEntry = Entry(createBillFrame)
                self.phoneNumberEntry.place(x=750,y=450,width=150)
                sendEmailButton = Button(createBillFrame, text="Send Message",command=email_alert)
                sendEmailButton.place(x=900,y=450)



                def updateText(name,material,quantity,unit,discount,price,remark):
                        billNameActual.config(text=name)
                        billMaterialActual.config(text=material)
                        quantityNameActual.config(text=quantity)
                        unitNameActual.config(text=unit)
                        priceNameActual.config(text=price)
                        discountNameActual.config(text=discount)
                        remarkNameActual.config(text=remark)





                        quantity = int(quantity)
                        discount = int(discount)
                        price = int(price)
                        totalDiscount = (discount/100 *price)
                        total = (price * quantity)-totalDiscount
                        totalNameActual.config(text=total)
                        self.totalBill = total
                        # print(self.totalBill)

                        # global billString
                        # billString = billString + str(total)


                clientGenerateBillButton = Button(createBillFrame,text="Generate Bill"
                ,command=lambda:updateText(self.clicked.get(),self.clickedMaterial.get(),clientQuantityText.get(),unitClicked.get(),clientDiscountText.get(),clientPriceText.get(),clientRemarkText.get()))


                clientGenerateBillButton.place(x=15,y=400,width=600)

                generateBillFrame.place(x=700,y=25,width=400,height=400)
                
                #------------PrintBill Name---------------------------
                billNamelabel = Label(generateBillFrame,text="Name :")
                billNamelabel.place(x=15,y=15,width=40,height=20)
                billNameActual.place(x=70,y=15)
                #Print Bill name xxxxxxxxxxx--------------------------

                #Printbill material -------------------------------------
                materialNamelabel = Label(generateBillFrame,text="Material :")
                materialNamelabel.place(x=15,y=50,width=50,height=20)
                billMaterialActual.place(x=70,y=50)
                #Print bill material --xxxxxxxxxxxxx----------------------

                #Printbill Quantity ---------------------------------------
                quantityNameLabel = Label(generateBillFrame,text="Quantity :")
                quantityNameLabel.place(x=15,y=85,width=50,height=20)
                quantityNameActual.place(x=80,y=85)   

                #Print bill Quantity    ----------xxxxxxxxxx-----------------
                        
                #Print bill Unit ------------------------------------------
                unitNameLabel = Label(generateBillFrame,text="Unit")
                unitNameLabel.place(x=15,y=120,width=50, height=20)
                unitNameActual.place(x=80,y=120)
                #Print bill Quantity xxxxxxxxxxx--------------------------

                #Print Price ---------------------------------------
                priceNameLabel = Label(generateBillFrame,text="Price")
                priceNameLabel.place(x=15,y=155,width=50, height=20)
                priceNameActual.place(x=80,y=155)
                #Price Price-------x-x-x-x-x-x-x-x-x-x------------------

                
                #Print Discount ---------------------------------------
                discountNameLabel = Label(generateBillFrame,text="Discount")
                discountNameLabel.place(x=15,y=190,width=50, height=20)
                discountNameActual.place(x=80,y=190)
                #Price Discount-------x-x-x-x-x-x-x-x-x-x------------------

                
                #Print Remark ---------------------------------------
                remarkNameLabel = Label(generateBillFrame,text="Remark :")
                remarkNameLabel.place(x=15,y=225,width=50, height=20)
                remarkNameActual.place(x=80,y=225)
                #Price Remark-------x-x-x-x-x-x-x-x-x-x------------------
                
                
                # # Print SGST --------------------------------------------
                # sgstNameLabel = Label(generateBillFrame,text="Sgst :") 
                # sgstNameLabel.place(x=205,y=15,width=50, height=20)
                # sgstNameActual = Label(generateBillFrame,text="5%")
                # sgstNameActual.place(x=270,y=15,width=50,height=20)
                
                # cgstNameLabel = Label(generateBillFrame,text="Sgst :") 
                # cgstNameLabel.place(x=205,y=50,width=50, height=20)
                # cgstNameActual.place(x=270,y=50,width=50,height=20)
                # #Print cgst ------xxxxxxxxxx-------------------------------------------------


                #Total -----------------------------------------------------------
                totalNameLabel = Label(generateBillFrame,text="Total :")
                totalNameLabel.place(x=15,y=285,width=50,height=20)
                totalNameActual.place(x=80,y=285)
                #Raising a frame ahead----------------------
        #Raising a frame ahead




        ####################BUTTONSXXXXXXXXXXXXXXXXXXXXXX#####################################

        ####MIDDLE FRAME TABLES START HERE------------------------------------------------------------
        ####MIDDLE FRAME TABLES START HERE------------------------------------------------------------
        ####MIDDLE FRAME TABLES START HERE------------------------------------------------------------


















        ####MIDDLE FRAME TABLES END HERE------------------------------------------------------------
        ####MIDDLE FRAME TABLES END HERE------------------------------------------------------------
        ####MIDDLE FRAME TABLES END HERE------------------------------------------------------------
        


# ///////////////xxxxxxxxxxxxxxxxxxx/////////////xxxxxxxxxxxxxxxxxxx///////////////////////////////        

if __name__=='__main__':
    root = Tk()
    obj = Bill_App(root)
    root.mainloop()
