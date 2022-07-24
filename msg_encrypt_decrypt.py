from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password=code.get()

    if password=="55555":
        screen2=Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="green")

        message=text1.get(1.0,END)
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")

        Label(screen2,text="Decrypt",font="arial",fg="white",bg="green").place(x=10,y=0)
        text2=Text(screen2,font="Robote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,decrypt)

    elif password=="":
        messagebox.showerror("enryption","Input Password")
    
    elif password !="55555":
        messagebox.showerror("encryption","Invalid Password")


def encrypt():
    password=code.get()

    if password=="55555":
        screen1=Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message=text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(screen1,text="Encrypt",font="arial",fg="white",bg="#ed3833").place(x=10,y=0)
        text2=Text(screen1,font="Robote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,encrypt)

    elif password=="":
        messagebox.showerror("enryption","Input Password")
    
    elif password !="55555":
        messagebox.showerror("encryption","Invalid Password")



def main_screen():

    global screen
    global code
    global text1

    screen=Tk()
    screen.geometry("500x500")

    #icon
    #image_icon=PhotoImage(file="keys.png")
    #screen.iconphoto(False,image_icon)
    screen.title("msg_encrypy_decrypt")


    def reset():
        code.set("")
        text1.delete(1.0,END)

    Label(text="Enter text for Encryption and Decryption",fg="black",font=("calibri",13)).place(x=10,y=10)
    text1=Text(font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=470,height=105)

    Label(text="Enter secret key for encryption and decryption",fg="black",font=("calibri",10)).place(x=10,y=170)

    code =StringVar()
    Entry(textvariable=code,width=22,bd=0,font=("ariel",25),show="*").place(x=10,y=200)

    Button(text="ENCRYPT",height="2",width=20,bg="red",fg="white",bd=0,command=encrypt).place(x=10,y=250)
    Button(text="DECRYPT",height="2",width=20,bg="green",fg="white",bd=0,command=decrypt).place(x=250,y=250)
    Button(text="RESET",height="2",width=48,bg="blue",fg="white",bd=0,command=reset).place(x=10,y=300)

    screen.mainloop()

main_screen()
