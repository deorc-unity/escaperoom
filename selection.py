from tkinter import *
from PIL import ImageTk

def user_login():
    main_window.destroy()
    import userLogin
    
def admin_login():
    main_window.destroy()
    import adminLogin

main_window = Tk()
main_window.resizable(False, False)
main_window.title('SSA - Who are you?')

backgroudImage = ImageTk.PhotoImage(file='selectionImg.jpg')
backgroundLabel = Label(main_window, image=backgroudImage)
backgroundLabel.grid(row=0, column=0)

adminButton = Button(main_window,bd=5, width=6, text='Admin', font=('Cambria',16,'bold'),cursor='hand2',bg='black',fg='red',activebackground='black',activeforeground='red',command=admin_login)
adminButton.place(x=316,y=252)

userButton = Button(main_window,bd=5, width=6, text='User', font=('Cambria',16,'bold'),cursor='hand2',bg='black',fg='red',activebackground='black',activeforeground='red',command=user_login)
userButton.place(x=428,y=252)

main_window.mainloop()


