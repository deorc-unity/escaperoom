from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmPasswordEntry.delete(0,END)
    check.set(0)
    
def user_login():
    register_window.destroy()
    import userLogin
    
def connect_database():
    if emailEntry.get()=='' and usernameEntry.get()=='' and passwordEntry.get()=='' and confirmPasswordEntry.get()=='':
        messagebox.showerror('ERROR','Please fill all the details')
    
    elif emailEntry.get()=='':
        messagebox.showerror('ERROR','Email not entered')
        
    elif usernameEntry.get()=='':
        messagebox.showerror('ERROR','Username not entered')
        
    elif passwordEntry.get()=='':
        messagebox.showerror('ERROR','Password not entered')
        
    elif confirmPasswordEntry.get()=='':
        messagebox.showerror('ERROR','Please enter the password again')
        
    elif passwordEntry.get() != confirmPasswordEntry.get():
        messagebox.showerror('ERROR','Password mismatch')
        confirmPasswordEntry.delete(0,END)
    
    elif check.get()==0:
        messagebox.showerror('ERROR','Accept the terms and conditions')
        
    else:
        try:
            con = pymysql.connect(host='deorcunity.mysql.pythonanywhere-services.com', user='deorcunity', password='hola123@4')
            mycursor = con.cursor()
            
        except:
            messagebox.showerror('ERROR','Failed to establish connection to database')
            return
        
        try:
            query = 'create database registration_details'
            mycursor.execute(query)
            
            query = 'use registration_details'
            mycursor.execute(query)
            
            query = 'create table users(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(20), softskill varchar(20))'
            mycursor.execute(query)
            
        except:
            mycursor.execute('use registration_details')
            
        query = 'select * from users where username=%s'
        mycursor.execute(query, usernameEntry.get())
        
        row = mycursor.fetchone()
        
        if row!=None:
            messagebox.showerror('ERROR','Username already exists')
            
        else:
            query = 'insert into users(email,username,password) values(%s,%s,%s)'
            mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('SUCCESS','Registration Successful')
            
            clear()
            register_window.destroy()
            import userLogin
            
            
    
register_window = Tk()
register_window.resizable(False,False)
register_window.title('Register')

regbg = ImageTk.PhotoImage(file='userRegisterbg.jpg')
bgLabel = Label(register_window, image=regbg)
bgLabel.grid(row=0,column=0)

heading=Label(register_window,text='CREATE AN ACCOUNT',font=('Cambria',16,'bold'),bg='black',fg='white')
heading.place(x=272,y=140)

emailLabel = Label(register_window, text='Email', font=('Cambria',12,'bold'),bg='black',fg='white')
emailLabel.place(x=276,y=180)
emailEntry = Entry(register_window, width=25, font=('Cambria',10,'bold'),bg='white',fg='black')
emailEntry.place(x=279,y=205)

usernameLabel = Label(register_window, text='Username', font=('Cambria',12,'bold'),bg='black',fg='white')
usernameLabel.place(x=276,y=240)
usernameEntry = Entry(register_window, width=25, font=('Cambria',10,'bold'),bg='white',fg='black')
usernameEntry.place(x=279,y=265)

passwordLabel = Label(register_window, text='Password', font=('Cambria',12,'bold'),bg='black',fg='white')
passwordLabel.place(x=276,y=300)
passwordEntry = Entry(register_window, width=25, font=('Cambria',10,'bold'),bg='white',fg='black')
passwordEntry.place(x=279,y=325)

confirmPasswordLabel = Label(register_window, text='Confirm Password', font=('Cambria',12,'bold'),bg='black',fg='white')
confirmPasswordLabel.place(x=276,y=360)
confirmPasswordEntry = Entry(register_window, width=25, font=('Cambria',10,'bold'),bg='white',fg='black')
confirmPasswordEntry.place(x=279,y=385)


check = IntVar()
termsAndConditions = Checkbutton(register_window, text='I agree to the terms & conditions',font=('Cambria',10,'bold'),bg='black',fg='red',activebackground='black',activeforeground='red',cursor='hand2',variable=check)
termsAndConditions.place(x=270,y=410)

signupButton = Button(register_window, text='Signup',font=('Cambria',14,'bold'),bd=0,bg='white',fg='black',width=18,activebackground='white',activeforeground='black',command=connect_database)
signupButton.place(x=276,y=445)

alreadyHaveAnAccount = Label(register_window,text='Already have an account?', font=('Cambria',9,'bold'),bg='black',fg='white')
alreadyHaveAnAccount.place(x=276,y=485)

loginButton = Button(register_window,text='Log in',cursor='hand2',font=('Cambria',9,'bold underline'),fg='red',bg='black',bd=0,activebackground='black',activeforeground='red',command=user_login)
loginButton.place(x=422,y=484)

register_window.mainloop()