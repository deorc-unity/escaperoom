from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk
import pymysql

def admin_login():
    if adminUsername.get()=='' or adminPassword.get()=='':
        messagebox.showerror('ERROR','Password or Username not entered')
        
    elif adminUsername.get()=='admin@gmail.com' and adminPassword.get()=='root':
        admin_window.destroy()
        window = Tk()
        #window.resizable(False,False)
        window.title('User Details')
        window.geometry("800x600")
        
        con = pymysql.connect(host='deorcunity.mysql.pythonanywhere-services.com', user='deorcunity', password='hola123@4',database='deorcunity$registrationdetails')
        mycursor = con.cursor()
        
        query = 'select * from users'
        mycursor.execute(query)
        
        tree = ttk.Treeview(window)
        tree['show']='headings'
        
        theme = ttk.Style(window)
        theme.theme_use("clam")
        
        tree["columns"] = ("id","email","username","password","softskill")
        
        tree.column("id",width=50,minwidth=50,anchor=CENTER)
        tree.column("email",width=100,minwidth=100,anchor=CENTER)
        tree.column("username",width=150,minwidth=150,anchor=CENTER)
        tree.column("password",width=125,minwidth=125,anchor=CENTER)
        tree.column("softskill",width=150,minwidth=150,anchor=CENTER)
        
        tree.heading("id", text="ID")
        tree.heading("email", text="E-mail")
        tree.heading("username", text="Username")
        tree.heading("password", text="Password")
        tree.heading("softskill", text="Softskills")
        
        i = 0
        for ro in mycursor:
            tree.insert('',i,text="",values=(ro[0],ro[1],ro[2],ro[3],ro[4]))
            i = i + 1
        tree.pack()
        
        email = StringVar()
        username = StringVar()
        password = StringVar()
        
        def add_data(tree):
            frame = Frame(window, width = 400, height = 270, background = 'grey')
            frame.place(x=201,y=250)
    
            l1 = Label(frame, text="Email", width=8, font=('Times',11,'bold'))
            e1 = Entry(frame,textvariable=email,width=25)
            l1.place(x=50,y=30)
            e1.place(x=170,y=30)
            
            l2 = Label(frame, text="Username", width=8, font=('Times',11,'bold'))
            e2 = Entry(frame,textvariable=username,width=25)
            l2.place(x=50,y=70)
            e2.place(x=170,y=70)
            
            l3 = Label(frame, text="Password", width=8, font=('Times',11,'bold'))
            e3 = Entry(frame,textvariable=password,width=25)
            l3.place(x=50,y=110)
            e3.place(x=170,y=110)
            
            def insert_data():
                try:
                    con = pymysql.connect(host='localhost', user='root', password='root',database='registration_details')
                    mycursor = con.cursor()
                except:
                    messagebox.showerror('ERROR','Failed to establish connection with database')
                    return
                
                query = 'select * from users where username=%s'
                mycursor.execute(query, e2.get())
                
                row = mycursor.fetchone()
                
                if row!=None:
                    messagebox.showerror('ERROR','Username already exists')
                    
                else:
                    query = 'insert into users(email,username,password) values(%s,%s,%s)'
                    mycursor.execute(query,(e1.get(),e2.get(),e3.get()))
                    con.commit()
                    con.close()
                    tree.insert('','end',text="",values=(mycursor.lastrowid,e1.get(),e2.get(),e3.get(),None))
                    messagebox.showinfo('SUCCESS','New user registered')
                    
                    e1.delete(0,END)
                    e2.delete(0,END)
                    e3.delete(0,END)
                    frame.destroy()
                  
            submitButton = Button(frame, text="Submit", command=insert_data)
            submitButton.configure(font=('Times',11,'bold'),bg='green',fg='white')
            submitButton.place(x=100, y=170)
            
            cancelButton = Button(frame, text="Cancel", command=frame.destroy)
            cancelButton.configure(font=('Times',11,'bold'),bg='red',fg='white')
            cancelButton.place(x=200, y=170)
            
        def delete_data(tree):
            selected_item = tree.selection()
            print(tree.item(selected_item)['values'])
            the_ids = tree.item(selected_item)['values'][0]
            delete_query = 'delete from users where id = %s'
            sel_data = (the_ids,)
            mycursor.execute(delete_query, sel_data)
            con.commit()
            tree.delete(selected_item)
            messagebox.showinfo('DELETED','user details deletion successful')
                
        def update_data(tree):
            selected_item = tree.focus()
            values = tree.item(selected_item,"values")
            print(values)
            
            frame = Frame(window, width = 400, height = 270, background = 'grey')
            frame.place(x=201,y=250)
    
            l1 = Label(frame, text="Email", width=8, font=('Times',11,'bold'))
            e1 = Entry(frame,textvariable=email,width=25)
            l1.place(x=50,y=30)
            e1.place(x=170,y=30)
            
            l2 = Label(frame, text="Username", width=8, font=('Times',11,'bold'))
            e2 = Entry(frame,textvariable=username,width=25)
            l2.place(x=50,y=70)
            e2.place(x=170,y=70)
            
            l3 = Label(frame, text="Password", width=8, font=('Times',11,'bold'))
            e3 = Entry(frame,textvariable=password,width=25)
            l3.place(x=50,y=110)
            e3.place(x=170,y=110)
            
            e1.insert(0,values[1])
            e2.insert(0,values[2])
            e3.insert(0,values[3])
            
            def select_data():
                tree.item(selected_item,values=(values[0],e1.get(),e2.get(),e3.get(),None))
                mycursor.execute('update users set email=%s, username=%s, password=%s where id=%s',(e1.get(),e2.get(),e3.get(),values[0]))
                con.commit()
                messagebox.showinfo('UPDATED','Update Successful')
                e1.delete(0,END)
                e2.delete(0,END)
                e3.delete(0,END)
                frame.destroy()
                
            submitButton = Button(frame, text="Update", command=select_data)
            submitButton.configure(font=('Times',11,'bold'),bg='blue',fg='white')
            submitButton.place(x=100, y=170)
            
            cancelButton = Button(frame, text="Cancel", command=frame.destroy)
            cancelButton.configure(font=('Times',11,'bold'),bg='red',fg='white')
            cancelButton.place(x=200, y=170)
        
        insertButton = Button(window, text="Insert",command=lambda: add_data(tree))
        insertButton.configure(font=('calibri',14,'bold'),bg='green',fg='white')
        insertButton.place(x=284,y=288)
        
        deleteButton = Button(window, text="Delete",command=lambda: delete_data(tree))
        deleteButton.configure(font=('calibri',14,'bold'),bg='red',fg='white')
        deleteButton.place(x=384,y=288)
        
        updateButton = Button(window, text="Update",command=lambda: update_data(tree))
        updateButton.configure(font=('calibri',14,'bold'),bg='blue',fg='white')
        updateButton.place(x=484,y=288)
        
        window.mainloop()
        
    else:
        messagebox.showerror('ERROR','Invalid details. ACCESS DENIED!!!')
    
def back():
    admin_window.destroy()
    import selection

def hide():
    eyeOpen.config(file='eyeClose.png')
    adminPassword.config(show='*')
    eyeButton.config(command=show)
    
def show():
    eyeOpen.config(file='eyeOpen.png')
    adminPassword.config(show='')
    eyeButton.config(command=hide)
    
admin_window = Tk()
admin_window.resizable(False,False)
admin_window.title('Admin Login')

adminImg = ImageTk.PhotoImage(file='pxfuel.jpg')
adminLabel = Label(admin_window, image=adminImg)
adminLabel.grid(row=0, column=0)

backImage = PhotoImage(file='back.png')
backButton = Button(admin_window, image=backImage, bd=0, text='<-',fg='white',activebackground='black',activeforeground='white',bg='black',command=back)
backButton.place(x=2,y=3)

heading = Label(admin_window, text='ADMIN LOGIN', font=('Cambria',23,'bold'),fg='white',bg='black')
heading.place(x=319,y=168)

adminUsernameHeading = Label(admin_window,text='Username',font=('Cambria',13,'bold'),fg='white',bg='black')
adminUsernameHeading.place(x=329,y=225)
adminUsername = Entry(admin_window, width=18, font=('Cambria',13,'bold'))
adminUsername.place(x=330,y=250)

adminPasswordHeading = Label(admin_window,text='Password',font=('Cambria',13,'bold'),fg='white',bg='black')
adminPasswordHeading.place(x=329,y=285)
adminPassword = Entry(admin_window, width=18, font=('Cambria',13,'bold'))
adminPassword.place(x=330,y=310)

eyeOpen = PhotoImage(file='eyeOpen.png')
eyeButton = Button(admin_window,image=eyeOpen,bd=0,bg='white',activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=479,y=312)

loginAdmin = Button(admin_window, width=16, text='Login',cursor='hand2',font=('Cambria',14,'bold'),bg='white',fg='black',bd=2, activebackground='white',command=admin_login)
loginAdmin.place(x=329,y=360)

admin_window.mainloop()
