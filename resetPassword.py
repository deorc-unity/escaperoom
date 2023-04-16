from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

reset_window = Tk()
reset_window.resizable(False,False)
reset_window.title('Register')

regbg = ImageTk.PhotoImage(file='userRegisterbg.jpg')
bgLabel = Label(reset_window, image=regbg)
bgLabel.grid(row=0,column=0)

heading=Label(reset_window,text='RESET PASSWORD',font=('Cambria',16,'bold'),bg='black',fg='white')
heading.place(x=285,y=140)

usernameLabel = Label(reset_window, text='Username', font=('Cambria',12,'bold'),bg='black',fg='white')
usernameLabel.place(x=276,y=200)
usernameEntry = Entry(reset_window, width=25, font=('Cambria',10,'bold'),bg='white',fg='black')
usernameEntry.place(x=279,y=225)

passwordLabel = Label(reset_window, text='Password', font=('Cambria',12,'bold'),bg='black',fg='white')
passwordLabel.place(x=276,y=260)
passwordEntry = Entry(reset_window, width=25, font=('Cambria',10,'bold'),bg='white',fg='black')
passwordEntry.place(x=279,y=285)

confirmPasswordLabel = Label(reset_window, text='Confirm Password', font=('Cambria',12,'bold'),bg='black',fg='white')
confirmPasswordLabel.place(x=276,y=320)
confirmPasswordEntry = Entry(reset_window, width=25, font=('Cambria',10,'bold'),bg='white',fg='black')
confirmPasswordEntry.place(x=279,y=345)

signupButton = Button(reset_window, text='Reset',font=('Cambria',14,'bold'),bd=0,bg='white',fg='black',width=18,activebackground='white',activeforeground='black')
signupButton.place(x=276,y=405)

reset_window.mainloop()