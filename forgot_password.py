from tkinter import *
import ast
from tkinter import messagebox

fg = Tk()
fg.title('Forgot password')
fg.geometry('925x500+300+200')
fg.configure(bg="yellow")
fg.resizable(False, False)

def search():
    search_email = email.get()
    file = open('data.txt', 'r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    if search_email in r.keys():
        # ========window===============
        fp = Toplevel(fg)
        fp.title('Forgot Password')
        fp.geometry('925x500+300+200')
        fp.configure(bg="yellow")
        fp.resizable(False, False)

        def okay():
            emailname = email.get()
            passw = password.get()
            confirm_pass = confirm.get()

            if passw == "":
                Label(fp, text='Please enter your password',
                      bg='#00c6fc', fg='red', font=('imprint MT shadow', 12, 'bold')).place(x=120, y=300)
            elif confirm_pass == "":
                Label(fp, text='Please confirm your password.',
                      bg='#00c6fc', fg='red', font=('imprint MT shadow', 12, 'bold')).place(x=100, y=250)
            elif passw == "" and confirm_pass == "":
                Label(fp, text='Please fill out information',
                      bg='#00c6fc', fg='red', font=('imprint MT shadow', 12, 'bold')).place(x=100, y=250)
            else:
                if passw == confirm_pass:
                    try:
                        file = open('data.txt', 'r+')
                        d = file.read()
                        r = ast.literal_eval(d)

                        dict2 = {emailname: passw}
                        r.update(dict2)
                        file.truncate(0)
                        file.close()

                        file = open('data.txt', 'w')
                        w = file.write(str(r))

                        messagebox.showinfo('Forgot password', 'Password Successfully Changed')
                        fp.destroy()
                    except:
                        file = open('data.txt', 'w')
                        dic = str({'email': 'password'})
                        file.write(dic)
                        file.close()
                else:
                    Label(fp, text='Password did not match.',
                          bg='#00c6fc', fg='red', font=('imprint MT shadow', 12, 'bold')).place(x=100, y=250)

        fr3 = PhotoImage(file='frame.png')
        Label(fp, image=fr3, height=470, width=570, bg='yellow').place(x=10, y=10)
        logo = PhotoImage(file='dwclogo.png')
        Label(fp, image=logo, height=300, width=300, bg='yellow').place(x=570, y=10)
        divine = Label(fp, text='DIVINE\nWORD COLLEGE\nOF LAOAG', bg='yellow', fg='black',
                       font=('Copperplate Gothic Bold', 30))
        divine.place(x=535, y=290)

        # ===========frame=======================
        frame = Frame(fp, width=370, height=350, bg="#00c6fc")
        frame.place(x=120, y=50)

        # =========Heading=================================
        heading = Label(fp, text='Forgot Password', fg='Yellow', bg='#00c6fc',
                        font=('Copperplate Gothic Bold', 25, 'bold'))
        heading.place(x=95, y=60)

        # ==============password============================
        Label(fp, text="New Password:", bg='#00c6fc', fg='black', font=('Cambria', 11, 'bold')).place(x=57, y=147)
        password = Entry(frame, show="*", width=28, fg='black', border=0, bg="#00c6fc", font=('Cambria', 11))
        password.place(x=50, y=100)
        Frame(frame, width=250, height=2, bg='black').place(x=50, y=120)

        # ==============confirm password====================
        Label(fp, text="Confirm\nNew Password:", bg='#00c6fc', fg='black', font=('Cambria', 11, 'bold')).place(
            x=57, y=230)
        confirm = Entry(frame, show="*", width=28, fg='black', border=0, bg="#00c6fc", font=('Cambria', 11))
        confirm.place(x=50, y=202)
        Frame(frame, width=250, height=2, bg='black').place(x=50, y=220)

        # ===========Confirm===================
        Button(frame, width=30, pady=7, text='Confirm', bg='yellow', cursor='hand2', fg='#00c6fc', border=0,
               command=okay, font=('Copperplate Gothic Bold', 8)).place(x=30, y=290)
        fp.mainloop()
    else:
        Label(fg, text='We were unable to find an account that\nmatches the information you provided.',
              bg='#00c6fc', fg='red', font=('imprint MT shadow', 12, 'bold')).place(x=100, y=250)

fr3 = PhotoImage(file='frame.png')
Label(fg, image=fr3, height=470, width=570, bg='yellow').place(x=10, y=10)
logo = PhotoImage(file='dwclogo.png')
Label(fg, image=logo, height=300, width=300, bg='yellow').place(x=570, y=10)
divine = Label(fg, text='DIVINE\nWORD COLLEGE\nOF LAOAG', bg='yellow', fg='black',
               font=('Copperplate Gothic Bold', 30))
divine.place(x=535, y=290)

# ===========frame(squre)=======================
frame = Frame(fg, width=400, height=350, bg="#00c6fc")
frame.place(x=100, y=50)

# =========Heading=================================
heading = Label(frame, text='Forgot Password', fg='Yellow', bg='#00c6fc', font=('Copperplate Gothic Bold', 25, 'bold'))
heading.place(x=-5, y=50)

# ========email===================================
Label(fg, text="Please enter your Email:", bg='#00c6fc', fg='black', font=('Cambria', 11, 'bold')).place(x=175,
                                                                                                           y=170)
email = Entry(frame, width=32, fg='black', border=0, bg="#00c6fc", font=('Cambria', 11))
email.place(x=51, y=162)
Frame(frame, width=220, height=2, bg='black').place(x=50, y=180)

# ===========Confirm===================
Button(frame, width=25, pady=7, text='Search', bg='yellow', cursor='hand2', fg='#00c6fc', border=0,
       command=search, font=('Copperplate Gothic Bold', 10)).place(x=40, y=250)
fg.mainloop()