from tkinter import *
from tkinter import messagebox
import mysql.connector as conn


mydb = conn.connect(host="localhost",user="root",password="ineuron@22")
cursor = mydb.cursor()
cursor.execute('use pythondb1')
def Aunthenticate():

    usernameText = usernameEntry.get()
    user_pwd = pwd_entry.get()
    global user_acc_num
    user_acc_num = acc_num_entry.get()
    cursor.execute('select * from account where pwd=%s and user_id=%s', [user_pwd,usernameText])
    tup=cursor.fetchall()
    if len(tup) == 0:
        messagebox.showerror('showerror','please enter correct username and password')
    else:
        Label(tkWindow,text='Login successful , select below options').grid(row=21,column=20)
        user_Balance= Button(tkWindow,text='Balance',command=balance)
        user_Balance.grid(row=22, column=20)
        T_button = Button(tkWindow,text='Transfer',command=transfer)
        T_button.grid(row=22,column=21)



def transfer():
    global account_entry
    global amount_entry
    global new_wind
    new_wind = Tk()
    new_wind.geometry('400x250')
    new_wind.title('Amount Transfer')
    account_label = Label(new_wind, text='Acc_number')
    account_label.grid(row=1, column=1)
    account_entry = Entry(new_wind)
    account_entry.grid(row=1, column=2)

    amount_label = Label(new_wind, text='Amt')
    amount_label.grid(row=2, column=1,pady=20)

    amount_entry = Entry(new_wind)
    amount_entry.grid(row=2, column=2)

    amount_t = Button(new_wind,text='transfer_amount',command=amount_transfer)
    amount_t.grid(row=3,column=0)





def balance():
   cursor.execute('select balance from account where account_number=%s', [user_acc_num])
   b=cursor.fetchall()
   b_lable=Label(tkWindow,text=b)
   b_lable.grid(row=23,column=20)




def amount_transfer():
    anum = account_entry.get()
    amount = amount_entry.get()
    cursor.execute('select account_number from account where account_number=%s',[anum])
    validate=cursor.fetchall()

    if anum == user_acc_num or len(validate) == 0:
        messagebox.showerror('showerror', 'please enter correct account number')

    else:
        cursor.execute("update account set balance=balance-%s where account_number=%s", [amount, user_acc_num])
        cursor.execute('update account set balance=balance+%s where account_number=%s', [amount, anum])
        mydb.commit()
        cursor.execute('select Balance from account where account_number=%s', [user_acc_num])
        bal = cursor.fetchall()
        confirm = Label(new_wind, text='Amount transfer is done successfull your current balance is {}'.format(bal[0]))
        confirm.grid(row=5, column=0)







# window
tkWindow = Tk()
tkWindow.geometry('1200x550')
tkWindow.title('Python Examples')


# label
useraccno=Label(tkWindow,text='ACCOUNT_NUMBER')
usernameLabel = Label(tkWindow, text="USERID")
user_pwd = Label(tkWindow, text="PASSWORD")
# entry for user input
usernameEntry = Entry(tkWindow)
pwd_entry = Entry(tkWindow)
acc_num_entry=Entry(tkWindow)

#displaylabel = Label(tkWindow, text="")

# submit button
submitButton = Button(tkWindow, text="Submit", command=Aunthenticate)
# submitButton.pack('bottom')

# place label, entry, and button in grid
useraccno.grid(row=0,column=0)
usernameLabel.grid(row=1, column=0)
user_pwd.grid(row=2, column=0)

acc_num_entry.grid(row=0,column=1)
usernameEntry.grid(row=1, column=1)
pwd_entry.grid(row=2,column=1)

submitButton.grid(row=3, column=0)

# main loop
tkWindow.mainloop()