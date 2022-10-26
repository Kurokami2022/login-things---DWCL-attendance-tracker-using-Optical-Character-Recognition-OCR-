from tkinter import *

main = Tk()
main.title('Sign Up')
main.geometry('925x500+300+200')
main.configure(bg="yellow")
main.resizable(False, False)

fr2 = PhotoImage(file='frame.png')
Label(main, image=fr2, height=470, width=570, bg='yellow').place(x=10, y=10)
logo = PhotoImage(file='dwclogo.png')
Label(main, image=logo, height=300, width=300, bg='yellow').place(x=570, y=10)
divine = Label(main, text='DIVINE\nWORD COLLEGE\nOF LAOAG', bg='yellow', fg='black',
               font=('Copperplate Gothic Bold', 30))
divine.place(x=535, y=290)
frame = Frame(main, width=350, height=350, bg="#00c6fc")
frame.place(x=90, y=80)

heading = Label(frame, text='Sign Up', fg='Yellow', bg='#00c6fc', font=('Copperplate Gothic Bold', 40, 'bold'))
heading.place(x=60, y=0)

Label(main, text='Email:', bg='#00c6fc', fg='black', font=('Cambria', 11, 'bold')).place(x=120, y=180)

email = Entry(frame, width=30, fg='black', bg='#00c6fc', border=0, font=('cambria', 11))
email.place(x=80, y=100)

Frame(frame, width=250, height=2, bg='black').place(x=74, y=120)

Label(main, text='Password:', bg='#00c6fc', fg='black', font=('Cambria', 11, 'bold')).place(x=90, y=230)

password = Entry(frame, show="*", width=30, fg='black', bg='#00c6fc', border=0, font=('cambria', 11))
password.place(x=80, y=153)

Frame(frame, width=250, height=2, bg='black').place(x=80, y=170)

Label(main, text='Confirm\nPassword:', bg='#00c6fc', fg='black', font=('Cambria', 11, 'bold')).place(x=90, y=265)

confirm = Entry(frame, show="*", width=30, fg='black', bg='#00c6fc', border=0, font=('cambria', 11))
confirm.place(x=80, y=200)

Frame(frame, width=250, height=2, bg='black').place(x=74, y=220)

Button(frame, width=30, pady=7, text='Sign Up', bg='yellow', cursor='hand2', fg='#00c6fc', border=0, font=('Copperplate Gothic Bold', 8)).place(x=70, y=250)
label = Label(frame, text="Already have an account?", fg='black', bg='#00c6fc', font=("Cambria", 9))
label.place(x=80, y=290)

login = Button(frame, width=6, text='Log In', border=0, bg='#00c6fc', cursor='hand2', fg='yellow',
               font=('Copperplate Gothic Bold', 9))
login.place(x=215, y=290)

main.mainloop()