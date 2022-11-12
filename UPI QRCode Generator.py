from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image, ImageFont, ImageDraw
import qrcode
import tkinter.messagebox as Messagebox

class Frames(object):
    def __init__(self):
        self.query1=StringVar()
        self.query2=StringVar()        
        self.query3=StringVar()
        self.query4=StringVar()
        self.query5=StringVar()
        
    def generate(self):
        pa=self.query4.get()
        pn=self.query3.get()
        am=self.query2.get()
        tn=self.query1.get()
        upi=self.query5.get()
        
        try:
            if(pa==''):
                Messagebox.showinfo('Status',"Error! UPI Address cannot be empty")
                return
            if(pn==''):
                Messagebox.showinfo('Status',"Error! Payee Name cannot be empty")
                return
            
            amount=float(am)
            address=pa+'@'+upi
            img=qrcode.make('upi://pay?pa={}&pn={}&am={}&tn={}'.format(address,pn,am,tn))
            img.save('upi_qrcode.png')
        
            qr=Image.open('upi_qrcode.png')
        
            title_font = ImageFont.truetype("arial.ttf", 20)
            draw = ImageDraw.Draw(qr)
            draw.text(( 40, 10), "Payee Name - {}".format(pn), (0), font=title_font)
            if(am!=''):
                draw.text(( 40, 380), "Amount - Rs. {}".format(am), (0), font=title_font)
            qr.show()
            
        except Exception as e:
            Messagebox.showinfo('Status',"Error occured!!")

    def mainframe(self,root):
        L1=Label(root, text='QR Code Generator',bg='pink',font=('bold',25))
        L1.place(x=100,y=130)

        Label1=Label(root,text='Enter VPA or UPI ID (required)',bg='pink',font=('bold',15))
        Label1.place(x=50,y=200)
        Entry1=Entry(root,width=20,textvariable=self.query4,font=('bold',15))
        Entry1.place(x=50,y=230)
        Label12=Label(root,text='@',bg='pink',font=('bold',15))
        Label12.place(x=280,y=230)
        idchoice = ttk.Combobox(root,text=self.query5,font=('bold',15),width = 10)
        idchoice['values'] = ('apl','axisbank','axl','barodampay','dbs','hdfcbank','ibl','icici','idfcbank','kotak','okaxis','okhdfcbank','okicici','oksbi','paytm','postbank','sbi','upi','ybl')
        idchoice.place(x=310,y=230)

        Label2=Label(root,text='Enter Payee/Merchant Name (required)',bg='pink',font=('bold',15))
        Label2.place(x=50,y=270)
        Entry2=Entry(root,width=30,textvariable=self.query3,font=('bold',15))
        Entry2.place(x=50,y=300)

        Label3=Label(root,text='Enter Amount (optional)',bg='pink',font=('bold',15))
        Label3.place(x=50,y=340)
        L3=Label(root,text= '₹',bg='pink',font=('bold',20))
        L3.place(x=50,y=365)
        Entry3=Entry(root,width=20,textvariable=self.query2,font=('bold',15))
        Entry3.place(x=80,y=372)

        Label4=Label(root,text='Enter Transaction Notes (optional)',bg='pink',font=('bold',15))
        Label4.place(x=50,y=410)
        Entry4=Entry(root,width=30,textvariable=self.query1,font=('bold',15))
        Entry4.place(x=50,y=440)

        Button1=Button(root, text='Generate',font=('bold',17),bg='lightgreen',relief='raised',command=self.generate)
        Button1.place(x=100,y=510)
        Button2=Button(root, text ='Exit',font=('bold',17),bg='red',fg='white',command=root.destroy)
        Button2.place(x=300,y=510)


root=Tk()
root.title('UPI QR code Generator')
root.geometry('500x600')
root.resizable(False, False)
root.configure(bg='pink')
canvas=Canvas(root, width=300,height=154,highlightthickness=0,bg='pink') 
canvas.place(x=130,y=10)
img=ImageTk.PhotoImage(file='upi_logo.jpg')
canvas.create_image(10,10,anchor=NW,image=img)
app=Frames()
app.mainframe(root)


root.mainloop()
