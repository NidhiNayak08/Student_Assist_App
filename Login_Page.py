import tkinter
import mysql.connector
from tkinter import Tk
import tkinter.messagebox as mymessagebox

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "123456",
    database= "python_database"
    )
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE python_database")
class Form(tkinter.Frame):

    def __init__(self,parent):

        tkinter.Frame.__init__(self,parent)
        self.parent = parent
        self.initialize_interface()

    def initialize_interface(self):

        self.parent.title("Login") # title of the form
        self.parent.config(background="lavender") # background color
        self.parent.geometry("800x500") # size of the form
        self.parent.resizable(False,False) # disables resize of hegiht and width

        global username #our variables
        global password #we use global for the other function to use it

        username = tkinter.StringVar() # we indicate what type of variables we declared 
        password = tkinter.StringVar() #which is string type

        self.labelUser = tkinter.Label(self.parent,text="Username: ", background = "dark slate gray", foreground = "White", font="Arial 8 bold")
        self.labelUser.place(x=25,y=25)

        self.entryUser = tkinter.Entry(self.parent,textvariable=username)
        self.entryUser.place(x=100,y=25)

        self.labelPass = tkinter.Label(self.parent,text="Password: ", background = "dark slate gray", foreground = "White", font="Arial 8 bold")
        self.labelPass.place(x=25,y=50)

        self.entryPass = tkinter.Entry(self.parent,textvariable=password)
        self.entryPass.place(x=100,y=50)
        self.entryPass.config(show="*");

        self.buttonLogin = tkinter.Button(self.parent,text="LOGIN", font = "Arial 8 bold",command=logs)
        self.buttonLogin.place(height=45,width=60 ,x=230,y=25)

def logs():
    mycursor = mydb.cursor()
   

    sql = "SELECT * FROM login WHERE username = '%s' AND password = '%s'" % (username.get(),password.get())

    mycursor.execute(sql)

    if mycursor.fetchone():

        # print("Successfully")
        mymessagebox.showinfo("Success", "Successfully Login")

    else:

        # print("Invalid Credentials")
        mymessagebox.showerror("Error", "Invalid User Name And Password")
    
    # mycursor.execute("SELECT * FROM login where usrname = '"+ username.get() +"' and passwrd = '"+ password.get() +"';")
    # myresult = mycursor.fetchone()
    # if myresult==None:
    #    mymessagebox.showerror("Error", "Invalid User Name And Password")

    # else:
    #    mymessagebox.showinfo("Success", "Successfully Login")
            
    # mydb.close()
    # mycursor.close()

def main():

    root = tkinter.Tk()
    b= Form(root)
    b.mainloop()


if __name__ == "__main__":
    main()