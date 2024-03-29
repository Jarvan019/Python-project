from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
from time import strftime
from datetime import datetime

class Roombooking:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x605+230+220")


#=======================================Variables=================
        self.var_contact=StringVar()
        self.var_check_in=StringVar()
        self.var_check_out=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()


#=======================================title=================
        lbl_title=Label(self.root,text="Room Booking Details",font=("times new roman",18,"bold"),bg="black",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

#=====================================Logo======================
        img2=Image.open(r"C:\Users\ACER\Desktop\Python finale 4.6.2\hotel images\logohotel.png")
        img2=img2.resize((100,40),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=4,y=4,width=100,height=40) 
#================================LabelFrame
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="room details",font=("arial",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=450,height=520)

#==============Labels and Entries




# Customer Contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,font=("arial",12,"bold"),width=24)
        entry_contact.grid(row=0,column=1,sticky=W)
    
# Check_in Date
        check_in_date=Label(labelframeleft,font=("arial",12,"bold"),text="Check_in Date:",padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_check_in,font=("arial",12,"bold"),width=29)
        txtcheck_in_date.grid(row=1,column=1)

# Check_out Date
        lbl_Check_out=Label(labelframeleft,font=("arial",12,"bold"),text="Check_out Date:",padx=2,pady=6)
        lbl_Check_out.grid(row=2,column=0,sticky=W)
        txt_Check_out=ttk.Entry(labelframeleft,textvariable=self.var_check_out,font=("arial",12,"bold"),width=29)
        txt_Check_out.grid(row=2,column=1)

# Room type
        label_RoomType=Label(labelframeleft,font=("arial",12,"bold"),text="Room Type:",padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)

        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomType["values"]=("Single","Double","laxary")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

#Available Room
        lblRoomAvailable=Label(labelframeleft,font=("arial",12,"bold"),text="Available Room:",padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        txtRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,font=("arial",12,"bold"),width=29)
        txtRoomAvailable.grid(row=4,column=1)

# Meal
        lblMeal=Label(labelframeleft,font=("arial",12,"bold"),text="Meal:",padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)

        combo_Meal=ttk.Combobox(labelframeleft,textvariable=self.var_meal,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Meal["values"]=("Breakfast","Lunch","Dinner","All Day Meal")
        combo_Meal.current(0)
        combo_Meal.grid(row=5,column=1)

# No of Days
        lblNoOfDays=Label(labelframeleft,font=("arial",12,"bold"),text="No Of Days",padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,font=("arial",12,"bold"),width=29)
        txtNoOfDays.grid(row=6,column=1)

# Paid Tax
        lblPaidtax=Label(labelframeleft,font=("arial",12,"bold"),text="Paid Tax:",padx=2,pady=6)
        lblPaidtax.grid(row=7,column=0,sticky=W)
        txtPaidtax=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,font=("arial",12,"bold"),width=29)
        txtPaidtax.grid(row=7,column=1)

# Subtotal
        lblSubtotal=Label(labelframeleft,font=("arial",12,"bold"),text="Sub Total",padx=2,pady=6)
        lblSubtotal.grid(row=8,column=0,sticky=W)
        txtSubtotal=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,font=("arial",12,"bold"),width=29)
        txtSubtotal.grid(row=8,column=1)

# Total Cost
        lblTotalcost=Label(labelframeleft,font=("arial",12,"bold"),text="Total Cost:",padx=2,pady=6)
        lblTotalcost.grid(row=9,column=0,sticky=W)
        txtTotalcost=ttk.Entry(labelframeleft,textvariable=self.var_total,font=("arial",12,"bold"),width=29)
        txtTotalcost.grid(row=9,column=1)




#=============================Buttons===================##############################################################
        btn_frame=Frame(labelframeleft,bd=0,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=440,height=40)

#==========================ADD Button=============================
        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand1")
        btnAdd.grid(row=0,column=0,padx=4)

#==========================Delete Button=============================
        btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand1")
        btnDelete.grid(row=0,column=2,padx=4)
#==========================Reset Button=============================
        btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="black",fg="gold",width=9,cursor="hand1")
        btnReset.grid(row=0,column=3,padx=4)

#==========================Fetch Button=============================
        FetchDatabtn=Button(labelframeleft,command=self.Fetch_contact,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        FetchDatabtn.place(x=375,y=4)

#==========================BillButton=============================
        btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnBill.grid(row=10,column=0,sticky=W)

#===========================================Table Frame##########################################################

        Table_Frame = LabelFrame(self.root,bd=2,relief=RIDGE,text="",padx=2,font=("times new roman",12,"bold"))
        Table_Frame.place(x=455,y=280,width=835,height=290)

        lblSearchBy=Label(Table_Frame,font=("arial",30,"bold"),text="Customer Database ",fg="black")
        lblSearchBy.grid(row=0,column=0,sticky=W)

#=====================================Rightside Image===================================================
        img3=Image.open(r"C:\Users\ACER\Desktop\Python finale 4.6.2\hotel images\bed.jpg")
        img3=img3.resize((520,300),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=55,width=520,height=200) 

        #===============================================Show Data Table######################################################
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        Scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_details=ttk.Treeview(details_table,column=("Contact","check_in","check_out","roomtype","roomavailable","meal","noOfdays"),
        xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)
        
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.room_details.xview)
        Scroll_y.config(command=self.room_details.yview)

        self.room_details.heading("Contact",text="Contact")
        self.room_details.heading("check_in",text="Check-in")
        self.room_details.heading("check_out",text="Check-out")
        self.room_details.heading("roomtype",text="Roomtype")
        self.room_details.heading("roomavailable",text="Room No")
        self.room_details.heading("meal",text="Meal")
        self.room_details.heading("noOfdays",text="NoOfDays")
        
        self.room_details.column("Contact",width=100)
        self.room_details.column("check_in",width=100)
        self.room_details.column("check_out",width=100)
        self.room_details.column("roomtype",width=100)
        self.room_details.column("roomavailable",width=100)
        self.room_details.column("meal",width=100)
        self.room_details.column("noOfdays",width=100)

        self.fetch_data()
        self.room_details["show"]="headings"
        self.room_details.pack(fill=BOTH,expand=1)

        self.room_details.bind("<ButtonRelease-1>",self.get_cuersor)
        


#==================ALL DATA FETCH================================================
#fetch contact
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter contact number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="",database="pos_db")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()

            if row ==None:
                messagebox.showerror("Error","This number was not found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataFrame=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataFrame.place(x=455,y=55,width=300,height=180)

                lblName=Label(showDataFrame,text="Name",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lblName=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lblName.place(x=90,y=0)

#fetch gender
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="pos_db")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblName=Label(showDataFrame,text="Gender",font=("arial",12,"bold"))
                lblName.place(x=0,y=30)

                lblName=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lblName.place(x=90,y=30)
#fetch Email
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="pos_db")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblName=Label(showDataFrame,text="Email",font=("arial",12,"bold"))
                lblName.place(x=0,y=60)

                lblName=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lblName.place(x=90,y=60)
#fetch Nationality
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="pos_db")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblName=Label(showDataFrame,text="Nationality",font=("arial",12,"bold"))
                lblName.place(x=0,y=90)

                lblName=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lblName.place(x=90,y=90)

#fetch Address
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="pos_db")
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()

                lblName=Label(showDataFrame,text="Address",font=("arial",12,"bold"))
                lblName.place(x=0,y=120)

                lblName=Label(showDataFrame,text=row,font=("arial",12,"bold"))
                lblName.place(x=90,y=120)


    def add_data(self):
        if self.var_contact.get()=="" or self.var_check_in.get()=="" or self.var_check_out.get()=="" or self.var_roomtype.get()=="" or   self.var_roomavailable.get()=="" or self.var_meal.get()=="" or self.var_noofdays.get()=="":
              
         messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="",database="pos_db")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_contact.get(),
                    self.var_check_in.get(),
                    self.var_check_out.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_noofdays.get(),
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Room has been booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"something went wrong:{str(es)}",parent=self.root)

# fetch data from database

    def fetch_data(self):
     conn=mysql.connector.connect(host="localhost",username="root",database="pos_db")
     my_cursor=conn.cursor()
     my_cursor.execute("select * from room")
     rows=my_cursor.fetchall()
     if len(rows)!=0:
      self.room_details.delete(* self.room_details.get_children())
      for i in rows:
       self.room_details.insert("",END,values=i)
       conn.commit()
     conn.close()

    def get_cuersor(self,events=""):
       cursor_row=self.room_details.focus()
       content=self.room_details.item(cursor_row)
       row=content["values"]

       self.var_contact.set(row[0])
       self.var_check_in.set(row[1])
       self.var_check_out.set(row[2])
       self.var_roomtype.set(row[3])
       self.var_roomavailable.set(row[4])
       self.var_meal.set(row[5])
       self.var_noofdays.set(row[6])

#=====================================Minor Error==========================================================

    def mDelete(self):
       mDelete=messagebox.askyesno("Hotel Management System","Do you want to delete this Booked Room",parent=self.root)
       if mDelete>0:
          conn=mysql.connector.connect(host="localhost",username="root",password="",database="pos_db")
          my_cursor=conn.cursor()
          query="delete from room WHERE Contact=%s"
          value=(self.var_contact.get(),)
          my_cursor.execute(query,value)
       else:
          if not mDelete:
             return
       conn.commit()
       self.fetch_data()
       conn.close()


#================================================================================================    
    def reset(self):
        self.var_contact.set(""),
        self.var_check_in.set(""),
        self.var_check_out.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set(""),
        self.var_paidtax.set(""),
        self.var_total.set(""),
        self.var_actualtotal.set(""),


    def total(self):

        if(self.var_meal.get()=="Breakfast" or "breakfast" and self.var_roomtype.get()=="laxary" or "Laxary"):
         q1=float(300)
         q2=float(700)
         q3=float(self.var_noofdays.get())
         q4=float(q1 + q2)
         q5=float(q3 + q4)
         Tax="Php"+str("%.2f"%((q5)*0.9))
         ST="Php"+str("%.2f"%((q5)))
         TT="Php"+str("%.2f"%(q5+((q5)*0.9)))
         self.var_paidtax.set(Tax)
         self.var_actualtotal.set(ST)
         self.var_total.set(TT)

         
        if(self.var_meal.get()=="Lunch" or "lunch" and self.var_roomtype.get()=="laxary" or "Laxary"):
         q1=float(500)
         q2=float(700)
         q3=float(self.var_noofdays.get())
         q4=float(q1 + q2)
         q5=float(q3 + q4)
         Tax="Php"+str("%.2f"%((q5)*0.9))
         ST="Php"+str("%.2f"%((q5)))
         TT="Php"+str("%.2f"%(q5+((q5)*0.9)))
         self.var_paidtax.set(Tax)
         self.var_actualtotal.set(ST)
         self.var_total.set(TT)

         if(self.var_meal.get()=="Dinner" or "dinner" and self.var_roomtype.get()=="laxary" or "Laxary"):
          q1=float(700)
          q2=float(700)
          q3=float(self.var_noofdays.get())
          q4=float(q1 + q2)
          q5=float(q3 + q4)
          Tax="Php"+str("%.2f"%((q5)*0.9))
          ST="Php"+str("%.2f"%((q5)))
          TT="Php"+str("%.2f"%(q5+((q5)*0.9)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)

         if(self.var_meal.get()=="Breakfast" or "breakfast" and self.var_roomtype.get()=="Single" or "single"):
          q1=float(300)
          q2=float(700)
          q3=float(self.var_noofdays.get())
          q4=float(q1 + q2)
          q5=float(q3 + q4)
         Tax="Php"+str("%.2f"%((q5)*0.9))
         ST="Php"+str("%.2f"%((q5)))
         TT="Php"+str("%.2f"%(q5+((q5)*0.9)))
         self.var_paidtax.set(Tax)
         self.var_actualtotal.set(ST)
         self.var_total.set(TT)

         
        if(self.var_meal.get()=="Lunch" or "lunch" and self.var_roomtype.get()=="Single" or "single"):
         q1=float(400)
         q2=float(700)
         q3=float(self.var_noofdays.get())
         q4=float(q1 + q2)
         q5=float(q3 + q4)
         Tax="Php"+str("%.2f"%((q5)*0.9))
         ST="Php"+str("%.2f"%((q5)))
         TT="Php"+str("%.2f"%(q5+((q5)*0.9)))
         self.var_paidtax.set(Tax)
         self.var_actualtotal.set(ST)
         self.var_total.set(TT)

         if(self.var_meal.get()=="Dinner" or "dinner" and self.var_roomtype.get()=="Single" or "single"):
          q1=float(600)
          q2=float(700)
          q3=float(self.var_noofdays.get())
          q4=float(q1 + q2)
          q5=float(q3 + q4)
          Tax="Php"+str("%.2f"%((q5)*0.9))
          ST="Php"+str("%.2f"%((q5)))
          TT="Php"+str("%.2f"%(q5+((q5)*0.9)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)

          if(self.var_meal.get()=="Breakfast" or "breakfast" and self.var_roomtype.get()=="Double" or "double"):
           q1=float(300)
           q2=float(700)
           q3=float(self.var_noofdays.get())
           q4=float(q1 + q2)
           q5=float(q3 + q4)
           Tax="Php"+str("%.2f"%((q5)*0.9))
           ST="Php"+str("%.2f"%((q5)))
           TT="Php"+str("%.2f"%(q5+((q5)*0.9)))
           self.var_paidtax.set(Tax)
           self.var_actualtotal.set(ST)
           self.var_total.set(TT)

         
        if(self.var_meal.get()=="Lunch" or "lunch" and self.var_roomtype.get()=="Double" or "double"):
         q1=float(500)
         q2=float(700)
         q3=float(self.var_noofdays.get())
         q4=float(q1 + q2)
         q5=float(q3 + q4)
         Tax="Php"+str("%.2f"%((q5)*0.9))
         ST="Php"+str("%.2f"%((q5)))
         TT="Php"+str("%.2f"%(q5+((q5)*0.9)))
         self.var_paidtax.set(Tax)
         self.var_actualtotal.set(ST)
         self.var_total.set(TT)

         if(self.var_meal.get()=="Dinner" or "dinner" and self.var_roomtype.get()=="Double" or "double"):
          q1=float(700)
          q2=float(700)
          q3=float(self.var_noofdays.get())
          q4=float(q1 + q2)
          q5=float(q3 + q4)
          Tax="Php"+str("%.2f"%((q5)*0.9))
          ST="Php"+str("%.2f"%((q5)))
          TT="Php"+str("%.2f"%(q5+((q5)*0.9)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)

         if(self.var_meal.get()=="ALL Day Meal" or "all day meal" and self.var_roomtype.get()=="Double" or "double"):
          q1=float(1000)
          q2=float(700)
          q3=float(self.var_noofdays.get())
          q4=float(q1 + q2)
          q5=float(q3 + q4)
          Tax="Php"+str("%.2f"%((q5)*0.9))
          ST="Php"+str("%.2f"%((q5)))
          TT="Php"+str("%.2f"%(q5+((q5)*0.9)))
          self.var_paidtax.set(Tax)
          self.var_actualtotal.set(ST)
          self.var_total.set(TT)

          if(self.var_meal.get()=="ALL Day Meal" or "all day meal" and self.var_roomtype.get()=="Signle" or "single"):
           q1=float(1000)
           q2=float(700)
           q3=float(self.var_noofdays.get())
           q4=float(q1 + q2)
           q5=float(q3 + q4)
           Tax="Php"+str("%.2f"%((q5)*0.9))
           ST="Php"+str("%.2f"%((q5)))
           TT="Php"+str("%.2f"%(q5+((q5)*0.9)))
           self.var_paidtax.set(Tax)
           self.var_actualtotal.set(ST)
           self.var_total.set(TT)

          if(self.var_meal.get()=="ALL Day Meal" or "all day meal" and self.var_roomtype.get()=="laxary" or "laxary"):
           q1=float(1000)
           q2=float(700)
           q3=float(self.var_noofdays.get())
           q4=float(q1 + q2)
           q5=float(q3 + q4)
           Tax="Php"+str("%.2f"%((q5)*0.9))
           ST="Php"+str("%.2f"%((q5)))
           TT="Php"+str("%.2f"%(q5+((q5)*0.9)))
           self.var_paidtax.set(Tax)
           self.var_actualtotal.set(ST)
           self.var_total.set(TT)


    
    
    def search(self):
       conn=mysql.connector.connect(host="localhost",username="root",password="",database="pos_db")
       my_cursor=conn.cursor()

       my_cursor.execute("select * from room where"+str(self.serch_var.get())+"LIKE '%"+str(self.txt_search.get())+"%'")
       rows=my_cursor.fetchall()
       if len (rows)!=():
          self.room_details.delete(* self.room_details.get_children())
          for i in rows:
             self.room_details.insert("",END,values=i)
             conn.commit()
             conn.close()


if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()