from tkinter import *

root = Tk()
root.geometry('925x500+300+200')
root.configure(bg='yellow')
root.title('Log in')
root.resizable(False, False)

fr = PhotoImage(file='frame.png')
frame = Label(root, image=fr, height=470, width=570, bg='yellow').place(x=10, y=10)
logo = PhotoImage(file='dwclogo.png')
side = Label(root, image=logo, height=300, width=300, bg='yellow').place(x=570, y=10)
divine = Label(root, text='DIVINE\nWORD COLLEGE\nOF LAOAG', bg='yellow', fg='black',
               font=('Copperplate Gothic Bold', 30))
divine.place(x=535, y=290)

heading = Label(frame, text='Log In', fg='Yellow', bg='#00c6fc', font=('Copperplate Gothic Bold', 40, 'bold'))
heading.place(x=170, y=50)

Label(root, text="Email:", bg='#00c6fc', fg='black', font=('Cambria', 13, 'bold')).place(x=95, y=157)
email = Entry(frame, width=28, fg='black', border=0, bg="#00c6fc", font=('Cambria', 12))
email.place(x=150, y=160)
Frame(frame, width=250, height=2, bg='black').place(x=150, y=180)

Label(root, text="Password:", bg='#00c6fc', fg='black', font=('Cambria', 13, 'bold')).place(x=70, y=225)
password = Entry(frame, show="*", width=25, fg='black', border=0, bg="#00c6fc", font=('Copperplate Gothic Bold', 12))
password.place(x=160, y=230)

Frame(frame, width=245, height=2, bg='black').place(x=159, y=250)

log = Button(frame, width=20, pady=7, text='Log In', bg='yellow', fg='#00c6fc', border=0,
             font=('Copperplate Gothic Bold', 8))
log.place(x=170, y=284)
label = Label(frame, text="Don't have an account?", fg='black', bg='#00c6fc', font=("cambria", 9))
label.place(x=160, y=345)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='#00c6fc', cursor='hand2', fg='yellow',
                 font=('Copperplate Gothic Bold', 10))
sign_up.place(x=290, y=343)

fp = Button(frame, width=20, text='Forgot Password?', border=0, bg='#00c6fc', cursor='hand2', fg='yellow',
            font=('Copperplate Gothic Bold', 10))
fp.place(x=160, y=380)

root.mainloop()
