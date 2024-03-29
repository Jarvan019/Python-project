from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from hotel import HotelManagementSystem
class Login_Window:
    def __init__(self,root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\ACER\Desktop\Python finale 4.6.2\hotel images\back.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relheight=1,relwidth=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=550)

        img1=Image.open(r"C:\Users\ACER\Desktop\Python finale 4.6.2\hotel images\LoginIconAppl.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=175,width=100,height=100)

        get_str=Label(frame,text="get started",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=100)

        # label
        username=lbl=Label(frame,text="username",font=("times new roman",20,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=200,width=270)

        password=lbl=Label(frame,text="password",font=("times new roman",20,"bold"),fg="white",bg="black")
        password.place(x=70,y=255)

        self.txtpass=Entry(frame,font=("times new roman",15,"bold"))
        self.txtpass.place(x=40,y=295,width=270)

        # icon images
        img2=Image.open(r"C:\Users\ACER\Desktop\Python finale 4.6.2\hotel images\288592.png")
        img2=img2.resize((30,30),Image.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg2.place(x=650,y=330,width=35,height=35)

        img3=Image.open(r"C:\Users\ACER\Desktop\Python finale 4.6.2\hotel images\86842844-user-login-icon-.jpg")
        img3=img3.resize((30,30),Image.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg3.place(x=650,y=430,width=35,height=35)

# LOGIN BUTTON
        loginbtn=Button(frame,text="LOGIN",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,borderwidth=0,fg="white",bg="red",activebackground="red",activeforeground="white")
        loginbtn.place(x=110,y=350,width=120,height=35)

# Register BUTTON
        #registerbtn=Button(frame,text="New user registration",font=("times new roman",10,"bold"),borderwidth=0,bd=3,relief=RIDGE,fg="white",bg="black",activebackground="white",activeforeground="red")
        #registerbtn.place(x=110,y=400,width=130,height=35)

# reset password BUTTON
        registerbtn=Button(frame,text="forgot password",font=("times new roman",10,"bold"),borderwidth=0,bd=3,relief=RIDGE,fg="white",bg="black",activebackground="white",activeforeground="red")
        registerbtn.place(x=110,y=450,width=130,height=35,)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
         messagebox.showerror("Error","all fields are required")

        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
          messagebox.showinfo("Success","welcome to code ko to")

          self.new_window=Toplevel(self.root)
          self.app=HotelManagementSystem(self.new_window) 
          self.close_window()
          

        else:
           messagebox.showerror("Invalid","invalid username & password")

    def close_window(self):
            root.destroy
if __name__=="__main__":
    root=Tk()
    obj=Login_Window(root)
    root.mainloop()