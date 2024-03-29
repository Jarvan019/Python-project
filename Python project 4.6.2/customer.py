from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox


class Cust_Win:
#+++++++++++++++++++++++++++++++++++++++++++++++every def used########################################################################
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x605+230+220")


#====================================#######################variables###############################################################\
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_address=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_number=StringVar()

######################################################################title==========================================================
        lbl_title = Label(self.root,text="ADD Customer Details",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)


##############################################################Logo==========================================================
        img2= Image.open(r"C:\Users\ACER\Desktop\Python finale 4.6.2\hotel images\logohotel.png")
        img2 = img2.resize((100,40),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=5,width=95,height=40)


##############################################################Label Frame==========================================================
        labelframeleft = LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",padx=2,font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)



##############################################################Labels and entrys==========================================================
        #CustRef
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref: ",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        
        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,width=29,font=("arial",12,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)

        # cust name
        cname=Label(labelframeleft,font=("arial",12,"bold"),text="Customer Name: ",padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        txtcname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,font=("arial",13,"bold"),width=29)
        txtcname.grid(row=1,column=1)

        #Nickname 
        lblmname=Label(labelframeleft,font=("arial",12,"bold"),text="Nickname: ",padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_mother,font=("arial",13,"bold"),width=29)
        txtmname.grid(row=2,column=1)

        #gender combobox
        label_gender=Label(labelframeleft,font=("arial",12,"bold"),text="Gender: ",padx=2,pady=6)
        label_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)


        #postcode
        lblPostCode=Label(labelframeleft,font=("arial",12,"bold"),text="PostCode: ",padx=2,pady=6)
        lblPostCode.grid(row=4,column=0,sticky=W)
        txtPostCode=ttk.Entry(labelframeleft,textvariable=self.var_post,font=("arial",13,"bold"),width=29)
        txtPostCode.grid(row=4,column=1)

        #mobile number
        lblMobile=Label(labelframeleft,font=("arial",12,"bold"),text="Mobile: ",padx=2,pady=6)
        lblMobile.grid(row=5,column=0,sticky=W)
        txtMobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,font=("arial",13,"bold"),width=29)
        txtMobile.grid(row=5,column=1)

        #email
        lblEmail=Label(labelframeleft,font=("arial",12,"bold"),text="Email: ",padx=2,pady=6)
        lblEmail.grid(row=6,column=0,sticky=W)
        txtEmail=ttk.Entry(labelframeleft,textvariable=self.var_email,font=("arial",13,"bold"),width=29)
        txtEmail.grid(row=6,column=1)

        #nationality
        lblNationality=Label(labelframeleft,font=("arial",12,"bold"),text="Nationality: ",padx=2,pady=6)
        lblNationality.grid(row=7,column=0,sticky=W)

        combo_Nationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Nationality["value"]=("American","Filipino","Indian","Japanese","Chinese")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)



        #id proof type combobox
        lblIdProof=Label(labelframeleft,font=("arial",12,"bold"),text="Id Proof Type: ",padx=2,pady=6)
        lblIdProof.grid(row=8,column=0,sticky=W)

        combo_id=ttk.Combobox(labelframeleft,textvariable=self.var_id_proof,font=("arial",12,"bold"),width=27,state="readonly")
        combo_id["value"]=("Driver's License","Passport","Student Id","Senior Citizen Id","PWD ID")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)

        #id number
        lblIdNumber=Label(labelframeleft,font=("arial",12,"bold"),text="Id Number: ",padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,textvariable=self.var_id_number,font=("arial",13,"bold"),width=29)
        txtIdNumber.grid(row=9,column=1)

        #address
        lblAdress=Label(labelframeleft,font=("arial",12,"bold"),text="Adress: ",padx=2,pady=6)
        lblAdress.grid(row=10,column=0,sticky=W)
        txtAdress=ttk.Entry(labelframeleft,textvariable=self.var_address,font=("arial",13,"bold"),width=29)
        txtAdress.grid(row=10,column=1)


#=============================Buttons===================##############################################################
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=415,height=40)

        btnAdd=Button(btn_frame,text="Add",font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand1",command=self.add_data)
        btnAdd.grid(row=0,column=0,padx=2)

        btnUpdate=Button(btn_frame,text="Update",font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand1",command=self.update)
        btnUpdate.grid(row=0,column=1,padx=2)

        btnDelete=Button(btn_frame,text="Delete",font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand1",command=self.mDelete)
        btnDelete.grid(row=0,column=2,padx=2)

        btnReset=Button(btn_frame,text="Reset",font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand1",command=self.reset)
        btnReset.grid(row=0,column=3,padx=2)


#===========================================Table Frame##########################################################

        Table_Frame = LabelFrame(self.root,bd=2,relief=RIDGE,text="",padx=2,font=("times new roman",12,"bold"))
        Table_Frame.place(x=435,y=50,width=860,height=490)

        lblSearchBy=Label(Table_Frame,font=("arial",30,"bold"),text="Customer Database ",bg="black",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W)

       # self.serch_var=StringVar()
        #combo_Serach=ttk.Combobox(Table_Frame,textvariable=self.serch_var,font=("arial",12,"bold"),width=27,state="readonly")
       # combo_Serach["value"]=("Mobile","Ref")
        #combo_Serach.current(0)
        #combo_Serach.grid(row=0,column=1,padx=2)

       # self.txt_search=StringVar()
       # txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=24)
       # txtSearch.grid(row=0,column=2,padx=2)

        #btnSearch=Button(Table_Frame,text="Search",command=self.search,font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        #btnSearch.grid(row=0,column=3,padx=1)

        #btnShowAll=Button(Table_Frame,text="Show all",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="gold",width=7)
        #btnShowAll.grid(row=0,column=4,padx=1)


#===============================================Show Data Table######################################################
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        Scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile","email","nationality",
                                                                   "idproof","idnumber","address"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.Cust_Details_Table.xview)
        Scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Ref No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Nickname")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="PostCode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")
        
        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)
        
        self.Cust_Details_Table["show"]="headings"
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_ceursor)
        self.fetch_data()



    def add_data(self):
       if self.var_mobile.get()==""or self.var_mother.get()=="":
           messagebox.showerror("Error","All fields are required",parent=self.root)
       else:
            try:
             conn=mysql.connector.connect(host="localhost",username="root",password="",database="pos_db")
             my_cursor=conn.cursor()
             my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_ref.get(),
                                                                                                self.var_cust_name.get(),
                                                                                                self.var_mother.get(),
                                                                                                self.var_gender.get(),
                                                                                                self.var_post.get(),
                                                                                                self.var_mobile.get(),
                                                                                                self.var_email.get(),
                                                                                                self.var_nationality.get(),
                                                                                                self.var_id_proof.get(),
                                                                                                self.var_id_number.get(),
                                                                                                self.var_address.get()
                                                                                                ))
             conn.commit()
             self.fetch_data()
             conn.close()
             messagebox.showinfo("Success","Customer has been added",parent=self.root)
            except Exception as es:
               messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)
        
    def fetch_data(self):
       conn=mysql.connector.connect(host="localhost",username="root",password="",database="pos_db")
       my_cursor=conn.cursor()
       my_cursor.execute("SELECT * FROM customer")
       rows=my_cursor.fetchall()
       if len(rows)!=0:
          self.Cust_Details_Table.delete(* self.Cust_Details_Table.get_children())
          for i in rows:
             self.Cust_Details_Table.insert("",END,values=i)
             conn.commit()
       conn.close() 

    def get_ceursor(self,event=""):
        ceursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(ceursor_row)
        row=content["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_address.set(row[10])
       
    def update(self):
       if self.var_mobile.get()=="":
          messagebox.showerror("Error","Please enter mobile number",parent=self.root)
       else:
          conn=mysql.connector.connect(host="localhost",username="root",password="",database="pos_db")
          my_cursor=conn.cursor()
          my_cursor.execute("update customer set Name=%s,Mother=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s WHERE ref=%s",(
                                                                                                                                                                
                                                                                                                                                                self.var_cust_name.get(),
                                                                                                                                                                self.var_mother.get(),
                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                self.var_post.get(),
                                                                                                                                                                self.var_mobile.get(),
                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                self.var_nationality.get(),
                                                                                                                                                                self.var_id_proof.get(),
                                                                                                                                                                self.var_id_number.get(),
                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                self.var_ref.get()
                                                                                                                                                        ))       
          conn.commit()
          self.fetch_data()
          conn.close()
          messagebox.showinfo("Update","Customer details have been updated successfully",parent=self.root) 

    def mDelete(self):
       mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this Customer",parent=self.root)
       if mDelete>0:
          conn=mysql.connector.connect(host="localhost",username="root",password="",database="pos_db")
          my_cursor=conn.cursor()
          query="delete from customer WHERE Ref=%s"
          value=(self.var_ref.get(),)
          my_cursor.execute(query,value)
       else:
          if not mDelete:
             return
       conn.commit()
       self.fetch_data()
       conn.close()

    def reset(self):
        self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_mother.set(""),
       
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
 

        self.var_id_number.set(""),
        self.var_address.set("")
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
      
    def search(self):

        conn=mysql.connector.connect(host="localhost",username="root",password="",database="pos_db")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from customer where"+str(self.serch_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows=my_cursor.fetchall()
        if len (rows)!=0:
           self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
           for i in rows:
              self.Cust_Details_Table.insert("",END,"values=i")
              conn.commit()
           conn.close()
                                                                  
                                                                


if __name__ == "__main__":
 root = Tk()
 obj=Cust_Win(root)
 root.mainloop()

