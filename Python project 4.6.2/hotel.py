from tkinter import*
from PIL import Image,ImageTk
from customer import Cust_Win
from room import Roombooking

class HotelManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1600x800+0+0")



        
##############################################################1st Image======================================================
        img1= Image.open(r"C:\Users\ACER\Desktop\Python finale 4.6.2\hotel images\hotel1.png")
        img1 = img1.resize((1600,140),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1600,height=140)


##############################################################Logo==========================================================
        img2= Image.open(r"C:\Users\ACER\Desktop\Python finale 4.6.2\hotel images\logohotel.png")
        img2 = img2.resize((250,140),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=250,height=140)

##############################################################title==========================================================
        lbl_title = Label(self.root,text="Hotel Management System",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1600,height=50)

##############################################################Main Frame==========================================================

        main_frame = Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1600,height=650)

##############################################################Menu==========================================================
        lbl_title = Label(main_frame,text="Menu",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=250)


##############################################################Button Frame==========================================================

        btn_frame = Frame(main_frame,bd=4,relief=RIDGE,background="royalblue")
        btn_frame.place(x=0,y=35,width=230,height=150)

        cust_btn = Button(btn_frame,text="Customer",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=5)

        room_btn = Button(btn_frame,text="Room",command=self.Roombooking,width=22,height=1,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=5)

        details_btn = Button(btn_frame,text="Details",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)
        
        report_btn = Button(btn_frame,text="Report",width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn = Button(btn_frame,text="Logout",command=self.terminate_program,width=22,font=("times new roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=2,column=0,pady=5)

##############################################################Right side image==========================================================


        img3 = Image.open(r"C:\Users\ACER\Desktop\Python finale 4.6.2\hotel images\slide3.jpg")
        img3 = img3.resize((1310,630),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=630)

##############################################################Down side image==========================================================

        img4 = Image.open(r"C:\Users\ACER\Desktop\Python finale 4.6.2\hotel images\myh.jpg")
        img4 = img4.resize((230,300),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=180,width=230,height=300)

        img5 = Image.open(r"C:\Users\ACER\Desktop\Python finale 4.6.2\hotel images\khana.jpg")
        img5 = img5.resize((230,300),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg1 = Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=420,width=230,height=300) 

##############################################################Opens customer page========================================================
    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window) 

    def Roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window) 

    def terminate_program(self):
        exit()
    







if __name__ == "__main__":
    root = Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()
