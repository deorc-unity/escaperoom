from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql
import pygame
import tkinter as tk
import time

def forgot_password():
    
    def reset_password():
        if usernameEntry.get()=='' or newpasswordEntry.get()=='' or newconfirmPasswordEntry.get()=='':
            messagebox.showerror('ERROR','Please fill all details',parent=window)
            
        elif newpasswordEntry.get() != newconfirmPasswordEntry.get():
            messagebox.showerror('ERROR','Password mismatch')
            
        else:
            con = pymysql.connect(host='deorcunity.mysql.pythonanywhere-services.com',user='deorcunity',password='hola123@4',database='deorcunity$registrationdetails')
            mycursor = con.cursor()
            
            query = 'select * from users where username=%s'
            mycursor.execute(query,usernameEntry.get())
            
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('ERROR','Username does not exists')
            
            else:
                query = 'update users set password=%s where username=%s'
                mycursor.execute(query,(newpasswordEntry.get(), usernameEntry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password reset successful')
                window.destroy()
                
    window = Toplevel()
    window.title('Reset Password')
    
    resetbg = ImageTk.PhotoImage(file='userRegisterbg.jpg')
    bg_Label = Label(window, image=resetbg)
    bg_Label.grid(row=0,column=0)
    
    heading=Label(window,text='RESET PASSWORD',font=('Cambria',16,'bold'),bg='black',fg='white')
    heading.place(x=285,y=140)

    usernameLabel = Label(window, text='Username', font=('Cambria',12,'bold'),bg='black',fg='white')
    usernameLabel.place(x=276,y=200)
    usernameEntry = Entry(window, width=25, font=('Cambria',10,'bold'),bg='white',fg='black')
    usernameEntry.place(x=279,y=225)

    newpasswordLabel = Label(window, text='Password', font=('Cambria',12,'bold'),bg='black',fg='white')
    newpasswordLabel.place(x=276,y=260)
    newpasswordEntry = Entry(window, width=25, font=('Cambria',10,'bold'),bg='white',fg='black')
    newpasswordEntry.place(x=279,y=285)

    newconfirmPasswordLabel = Label(window, text='Confirm Password', font=('Cambria',12,'bold'),bg='black',fg='white')
    newconfirmPasswordLabel.place(x=276,y=320)
    newconfirmPasswordEntry = Entry(window, width=25, font=('Cambria',10,'bold'),bg='white',fg='black')
    newconfirmPasswordEntry.place(x=279,y=345)

    resetButton = Button(window, text='Reset',font=('Cambria',14,'bold'),bd=0,bg='white',fg='black',width=18,activebackground='white',activeforeground='black',command=reset_password)
    resetButton.place(x=276,y=405)
    
    window.mainloop()
    
def user_login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('ERROR','Password or Username not entered')
        
    else:
        try:
            con = pymysql.connect(host='deorcunity.mysql.pythonanywhere-services.com', user='deorcunity', password='hola123@4')
            mycursor = con.cursor()
            
        except:
            messagebox.showerror('ERROR','Failed to establish connection with database')
            return
        
        query = 'use registration_details'
        mycursor.execute(query)
        
        query = 'select * from users where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(), passwordEntry.get()))
        
        row = mycursor.fetchone()
        if(row == None):
            messagebox.showerror('ERROR','Invalid username or password')
            
        else:
            usernametmp = usernameEntry.get()
            user_login_window.destroy()
            
            #play game
            soft_skills_set = ['empathy', 'eye for detail', 'critical thinking', 'organization skills', 'decision making', 'time management']
            soft_skills = [ ]

            def generate_popup(clue, title, correct, unlocked, skill_index):    
                # popup setup
                root = tk.Tk()
                root.title(clue)
                root.geometry("500x300")
                root.eval('tk::PlaceWindow . center')
                ans_var = tk.StringVar()

                # popup submission
                def submit():
                    answer = ans_var.get()
                    print("The answer submitted is : " + answer)
                    if answer.lower() == correct.lower():
                        print("That's the answer!!!")
                        ans_var.set(correct)
                        
                        if skill_index!=-1:
                            skill = soft_skills_set[skill_index]
                            if skill in soft_skills:
                                pass
                            else:
                                soft_skills.append(skill)
                                
                        display = tk.Label(root, text = unlocked)
                        display.grid(row=5,column=1)
                        
                        if(clue == 'door1'):
                            msg = ', '.join(soft_skills)
                            
                            query = 'select softskill from users where username=%s'
                            mycursor.execute(query,usernametmp)
                            
                            softrow = mycursor.fetchone()
                            if softrow == None:
                                query='insert into users(softskill) values(%s) where username=%s'
                                mycursor.execute(query,(msg,usernametmp))
                                
                            else:
                                query = 'update users set softskill=%s where username=%s'
                                mycursor.execute(query,(msg, usernametmp))
                            
                            messagebox.showinfo('HURRAAY!!!','The soft skills you have are: '+msg)
                            con.commit()
                            con.close()
                            time.sleep(3)
                            exit()
                            
                        elif clue == 'door2':
                            msg = ', '.join(soft_skills)
                            
                            query = 'select softskill from users where username=%s'
                            mycursor.execute(query,usernametmp)
                            
                            softrow = mycursor.fetchone()
                            if softrow == None:
                                query='insert into users(softskill) values(%s) where username=%s'
                                mycursor.execute(query,(msg,usernametmp))
                                
                            else:
                                query = 'update users set softskill=%s where username=%s'
                                mycursor.execute(query,(msg, usernametmp))
                                
                            messagebox.showinfo('OOOPPPS','You choose the door to darkness\nYOU LOST\nSoft skills you have are: '+msg)
                            con.commit()
                            con.close()
                            time.sleep(3)
                            exit()

                    else:
                        ans_var.set("")

                # popup display
                message = tk.Label(root, text = title)
                ans_entry = tk.Entry(root, textvariable = ans_var, font = ('calibre',10,'normal'))
                sub_btn = tk.Button(root, text = 'Submit', command = submit)
                root.grid_columnconfigure(0, weight=1)
                root.grid_columnconfigure(2, weight=1)
                message.grid(row=1, column=1)
                ans_entry.grid(row=2,column=1)
                sub_btn.grid(row=3,column=1)
                
                root.mainloop()
                
            class location:
                def __init__(self, lx, rx, ty, by):
                    self.lx = lx
                    self.rx = rx
                    self.ty = ty
                    self.by = by

            sofa = location(108, 318, 300, 421)
            telephone = location(594, 638, 250, 286)
            pillow = location(1101, 1256, 418, 596)
            wheel = location(717, 798, 184, 272)
            whiteRoom = location(241, 284, 193, 284)
            clock = location(132, 211, 58, 259)
            door1 = location(908, 1035, 104, 422)
            door2 = location(343, 416, 171, 335)
            floor = location(577, 821, 399, 535)

            def escape_room():
                
                pygame.display.set_caption('Escape room: The right door')
                pygame.init()
                gameDisplay = pygame.display.set_mode((1265,601))
                pygame.display.set_caption('Escape Room')
                Clock = pygame.time.Clock()
                
                gameDisplay.blit(pygame.image.load("escaperoom.png"),(0,0))

                ending = False
                while not ending:

                    mx, my = pygame.mouse.get_pos()
                    
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            ending = True
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if door1.lx <= mx <= door1.rx and door1.ty <= my <= door1.by:
                                generate_popup("door1",
                                            "\nCODE: _ _  _  _ _\n",
                                            "11112",
                                            "\nCongratulations. You escaped in time.",5)
                                break
                            
                            if door2.lx <= mx <= door2.rx and door2.ty <= my <= door2.by:
                                generate_popup("door2",
                                            "\nCODE: _ _  _  _ _\n",
                                            "11112",
                                            "\nBAD LUCK!!! YOU LOST",-1)
                                break
                            
                            if floor.lx <= mx <= floor.rx and floor.ty <= my <= floor.by:
                                generate_popup("Escape the room",
                                            "\nMerk and you are room-mates. After a long busy day, you both were sleeping. \nAt some point of time at night you woke up hearing to Merk's \nscream. You cannot find Merk in the room. You hear strange noises \nand you get a gut feeling of leaving the room ASAP. There are two exit \ndoors. You need to escape from the right door before it's too late. \nYou find some written papers fallen all over the room\nType 'help' for more info:\n",
                                            "help",
                                            "\nClick around the room to investigate clues.\nSolve puzzles and take notes along the way.\nHave fun!",-1)
                                break
                            if pillow.lx <= mx <= pillow.rx and pillow.ty <= my <= pillow.by:
                                generate_popup("Pillow",
                                            "\nYou find something is written on the pillow.\nHey, I don't have much time.\n Today morning I encoded our door locks with new combinations. DONT ASK WHY?\nI have hidden some riddles around which contains the lock combinations. \nFind them and get out ASAP, if you are hearing strange noises and cannot \nfind me.In how many parts is the code separared?\n",
                                            "3",
                                            "\nArrange the combination w.r.t this -> TIMES I saw on a WHEEL",3)
                                break
                            if sofa.lx <= mx <= sofa.rx and sofa.ty <= my <= sofa.by:
                                generate_popup("Sofa",
                                            "\nIt feels like a clue. 'Until I am measured I am not known. \nYet how you miss me when I have flown.'\n",
                                            "time",
                                            "\nTime... ummmmm. HEY!!! it is that time when I heard Merk's\n scream. Is it a part of the code? Possible",0)
                                break
                            if telephone.lx <= mx <= telephone.rx and telephone.ty <= my <= telephone.by:
                                generate_popup("Telephone",
                                            "\nI see a paper. Oh come on, when did Merk find so much time to write \nriddles to save me.'I am in the room. You saw me thrice, try to\n see me from the \nother side. How many of me do you see'\n",
                                            "9",
                                            "\nI see 9 only 1 time. Is 1 a part of the code. Yeah!!! I checked the code display.",1)
                                break
                            if clock.lx <= mx <= clock.rx and clock.ty <= my <= clock.by:
                                generate_popup("Clock",
                                            "\nwhat is the time? Ah, what's that? 'YOU SEE DECEMBER ON WHEEL'\n",
                                            "12",
                                            "\nOh lord the clock is stuck but I feel my time is about to end.\n I never knew our room was full of code numbers.\n What will I do with 12? *thuds!!!*",2)
                                break
                            
                            if whiteRoom.lx <= mx <= whiteRoom.rx and whiteRoom.ty <= my <= whiteRoom.by:
                                generate_popup("Lights ON",
                                            "What a mess!! Looks like Merk was in a hurry. What are these scratches? \nMerk was here before leaving, I guess. \n'What do you think?(yes/no)'\n",
                                            "yes",
                                            "\nI see the door has some sharp marks on it. .....What should I do?",-1)
                                break
                            if wheel.lx <= mx <= wheel.rx and wheel.ty <= my <= wheel.by:
                                generate_popup("Wheel",
                                            "\nThe safe looks locked. No Robbery? This part looks untonched. \n'What do you think?(yes/no)'\n",
                                            "yes",
                                            "\nI should try this door",4)
                                break
                            print(event)
                            
                    pygame.display.update()

                pygame.quit()
                quit()
                
            escape_room()
    
def user_register():
    user_login_window.destroy()
    import userRegister
    
def back():
    user_login_window.destroy()
    import selection
    
def hide():
    eyeOpen.config(file='eyeCLose.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)
    
def show():
    eyeOpen.config(file='eyeOpen.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)
    
user_login_window = Tk()
user_login_window.resizable(False,False)
user_login_window.title('User Login')

user_background_img = ImageTk.PhotoImage(file='userBackground.jpg')
userBgLabel = Label(user_login_window, image=user_background_img)
userBgLabel.grid(row=0,column=0)

backImage = PhotoImage(file='back.png')
backButton = Button(user_login_window, image=backImage, bd=0, text='<-',fg='white',activebackground='black',activeforeground='white',bg='black',command=back)
backButton.place(x=2,y=3)

heading = Label(user_login_window, text='USER LOGIN', font=('Cambria',23,'bold'),fg='white',bg='black')
heading.place(x=305,y=100)

usernameHeading = Label(user_login_window, text='Username',font=('Cambria',13,'bold'),fg='white',bg='black')
usernameHeading.place(x=305,y=160)
usernameEntry = Entry(user_login_window,width=18,font=('Cambria',13,'bold'))
usernameEntry.place(x=308,y=185)

passwordHeading = Label(user_login_window,text='Password',font=('Cambria',13,'bold'),fg='white',bg='black')
passwordHeading.place(x=305,y=220)
passwordEntry = Entry(user_login_window,width=18,font=('Cambria',13,'bold'))
passwordEntry.place(x=308,y=245)

eyeOpen = PhotoImage(file='eyeOpen.png')
eyeButton = Button(user_login_window,image=eyeOpen,bg='white',bd=0,activebackground='white',cursor='hand2',command=hide)
eyeButton.place(x=457,y=247)

forgotPassword = Button(user_login_window,text='Forgot Password ?',bd=0,bg='black',activebackground='black',activeforeground='white',fg='white',font=('Cambria',9,'bold'),cursor='hand2',command=forgot_password)
forgotPassword.place(x=390, y=275)

loginButton = Button(user_login_window,text='Login',width=16,font=('Cambria',14,'bold'),fg='black',bg='white',activebackground='white',bd=0,activeforeground='black',cursor='hand2',command=user_login)
loginButton.place(x=307,y=320)

orLabel = Label(user_login_window, text='------------ OR ------------',fg='white',bg='black',font=('Cambria',14,''))
orLabel.place(x=308,y=360)

fakeImage = PhotoImage(file='fakeLabel.png')
fbLabel = Label(user_login_window, image=fakeImage, bg='black')
fbLabel.place(x=310,y=390)

register = Label(user_login_window, text='Don\'t have an account?',font=('Cambria',9,'bold'),fg='white',bg='black')
register.place(x=308, y=440)

registerButton = Button(user_login_window, text='Register',font=('Cambria',9,'bold underline'),fg='red',bg='black',activeforeground='red',activebackground='black',cursor='hand2',bd=0,command=user_register)
registerButton.place(x=440, y=440)

user_login_window.mainloop()