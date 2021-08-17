from tkinter import *

class BillingApp:
     def __init__(self,root):
         self.root = root
         self.root.geometry("1200x555")
         self.root.configure(bg="#f1f4ff")
         self.root.title("Evo Billing System")



         lblfrmDetails = LabelFrame(self.root, text="Customer Info", bg="#5e1cdd", fg="#ffffff")
         lblfrmDetails.place(x=0, y=10, height=45, width=1200)

         lblCustName = Label(lblfrmDetails, text="Customer Full Name", bg="#5e1cdd", fg="#ffffff").grid(row=0, column=0, padx=10)
         entCustomer = Entry(lblfrmDetails, width=30, relief=FLAT).grid(row=0,column=1,padx=10)
         lblCustContact = Label(lblfrmDetails, text="Contact No.", bg="#5e1cdd", fg="#ffffff").grid(row=0, column=2, padx=10)
         entCustContact = Entry(lblfrmDetails,width=30, relief=FLAT).grid(row=0,column=3,padx=10)
         lblBillNo = Label(lblfrmDetails,text="Bill No.",bg="#5e1cdd",fg="#ffffff").grid(row=0,column=4,padx=10)
         entBillNo = Entry(lblfrmDetails,width=15, relief=FLAT).grid(row=0,column=5,padx=10)

#SNACKS PANE
         lblfrmSnaks = LabelFrame(self.root,text="Snaks")
         lblfrmSnaks.place(x=0,y=55,width=300,height=400)

         lblItem1 = Label(lblfrmSnaks, text="MaryLand").grid(row=0,column=0,pady=10)
         entItem1 = Entry(lblfrmSnaks,width=8).grid(row=0,column=1,padx=10)

         lblItem2 = Label(lblfrmSnaks, text="PlantainChips").grid(row=1, column=0, pady=10)
         entItem2 = Entry(lblfrmSnaks, width=8).grid(row=1, column=1, padx=10)

         lblItem3 = Label(lblfrmSnaks, text="Hubnobs").grid(row=2, column=0, pady=10)
         entItem3 = Entry(lblfrmSnaks, width=8).grid(row=2, column=1, padx=10)

         # lblItem4 = Label(lblfrmSnaks, text="Crosent").grid(row=3, column=0, pady=10)
         # entItem4 = Entry(lblfrmSnaks, width=8).grid(row=3, column=1, padx=10)

#COSMETICS PANE
         lblfrmCosmetics = LabelFrame(self.root, text="Snaks")
         lblfrmCosmetics.place(x=300, y=55, width=300, height=400)

         lblItem4 = Label(lblfrmCosmetics, text="Safeguard").grid(row=0, column=0, pady=10)
         entItem4 = Entry(lblfrmCosmetics, width=8).grid(row=0, column=1, padx=10)

         lblItem5 = Label(lblfrmCosmetics, text="Nivea").grid(row=1, column=0, pady=10)
         entItem5 = Entry(lblfrmCosmetics, width=8).grid(row=1, column=1, padx=10)

         lblItem6 = Label(lblfrmCosmetics, text="Jergens").grid(row=2, column=0, pady=10)
         entItem6 = Entry(lblfrmCosmetics, width=8).grid(row=2, column=1, padx=10)

         # lblItem4 = Label(lblfrmCosmetics, text="Epiderm").grid(row=3, column=0, pady=10)
         # entItem4 = Entry(lblfrmCosmetics, width=8).grid(row=3, column=1, padx=10)
         #
         # lblItem5 = Label(lblfrmCosmetics, text="Dettol").grid(row=4, column=0, pady=10)
         # entItem5 = Entry(lblfrmCosmetics, width=8).grid(row=4, column=1, padx=10)

#ELECTRONICS PANE
         lblfrmElectronics = LabelFrame(self.root, text="Electronics")
         lblfrmElectronics.place(x=600, y=55, width=300, height=400)

         lblItem7 = Label(lblfrmElectronics, text="LG Led TV").grid(row=0, column=0, pady=10)
         entItem7 = Entry(lblfrmElectronics, width=8).grid(row=0, column=1, padx=10)

         lblItem8 = Label(lblfrmElectronics, text="Panasonic Blender").grid(row=1, column=0, pady=10)
         entItem8 = Entry(lblfrmElectronics, width=8).grid(row=1, column=1, padx=10)

         lblItem9 = Label(lblfrmElectronics, text="Q-link Fan").grid(row=2, column=0, pady=10)
         entItem9 = Entry(lblfrmElectronics, width=8).grid(row=2, column=1, padx=10)

         # lblItem4 = Label(lblfrmElectronics, text="Something AC").grid(row=3, column=0, pady=10)
         # entItem4 = Entry(lblfrmElectronics, width=8).grid(row=3, column=1, padx=10)
         #
         # lblItem5 = Label(lblfrmElectronics, text="Freezer").grid(row=4, column=0, pady=10)
         # entItem5 = Entry(lblfrmElectronics, width=8).grid(row=4, column=1, padx=10)

#BILL PANE
         lblfrmBillArea = LabelFrame(self.root, text="Billing", relief=FLAT, pady=10)
         lblfrmBillArea.place(x=900, y=55, width=300, height=410)

         scrollY = Scrollbar(lblfrmBillArea, orient=VERTICAL)
         self.txtArea = Text(lblfrmBillArea,yscrollcommand=scrollY.set)
         scrollY.pack(side=RIGHT, fill=Y)
         scrollY.configure(command=self.txtArea.yview)
         self.txtArea.pack(fill=BOTH,expand=1)

#BILLING MENU PANE
         lblfrmBillMenu=LabelFrame(self.root,text="Billing Summary",relief=FLAT, bd=5,pady=10)
         lblfrmBillMenu.place(x=0,y=455, height=100,width=800,)

         #TOTAL SNACKS SUMMARY
         lblTotalSnacks = Label(lblfrmBillMenu,text="Snacks Total Price").grid(row=0,column=0)
         entTotalSnacks = Entry(lblfrmBillMenu,width=20).grid(row=0,column=1,padx=10)

         # TOTAL COSMETICS SUMMARY
         lblTotalCosmetics = Label(lblfrmBillMenu, text="Cosmetics Total Price").grid(row=0, column=2)
         lblTotalCosmetics = Entry(lblfrmBillMenu, width=20).grid(row=0, column=3, padx=10)

         # TOTAL ELECTRONICS SUMMARY
         lblTotalElectronics = Label(lblfrmBillMenu, text="Electronics Total Price").grid(row=0, column=4)
         entTotalElectronics = Entry(lblfrmBillMenu, width=20).grid(row=0, column=5, padx=10)

         #Snacks Tax
         lblSnacksTax = Label(lblfrmBillMenu,text="Snacks Tax").grid(row=1,column=0,pady=10)
         entSnacksTax = Entry(lblfrmBillMenu,width=20).grid(row=1,column=1)

         # Cosmetics Tax
         lblCosmeticsTax = Label(lblfrmBillMenu, text="Cosmetics Tax").grid(row=1, column=2, pady=10)
         entCosmeticsTax = Entry(lblfrmBillMenu, width=20).grid(row=1, column=3)

         # Electronics Tax
         lblElectronicsTax = Label(lblfrmBillMenu, text="Electronics Tax").grid(row=1, column=4, pady=10)
         entElectronicsTax = Entry(lblfrmBillMenu, width=20).grid(row=1, column=5)

# BUTTONS FRAME
         lblfrmButtons = LabelFrame(self.root, text="Operations",relief=RIDGE)
         lblfrmButtons.place(x=800,y=455,height=100, width=400)

         #Button Total
         btnTotal = Button(lblfrmButtons, text="Total Payable", width=10).grid(row=0,column=0,padx=10,pady=25)

         # Button Reset
         btnReset = Button(lblfrmButtons, text="Reset", width=10).grid(row=0, column=1, padx=10, pady=25)

         # Button Exit
         btnExit = Button(lblfrmButtons, text="Exit", width=10).grid(row=0, column=2, padx=10, pady=25)



root = Tk()
obj = BillingApp(root)
root.mainloop()