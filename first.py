import tkinter as tk
from PIL import ImageTk
from numpy import random
from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys
import tkinter as tk
from PIL import ImageTk
import webbrowser
import random
from tkinter import ttk
from tkinter import *
from tkinter import filedialog as fd
from plyer import notification
from tkinter import messagebox
from PIL import Image, ImageTk
import time
from math import *
from tkinter import Tk
import sqlite3
from prettytable import PrettyTable
import tkinter.messagebox as mymessagebox

bg_colour = "#3d6466"
recognizer = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 150)


# initiallize app with basic settings
root = tk.Tk()
root.title("Study Assist")
root.geometry("700x650")
 
# create a frame widgets
frame0 = tk.Frame(root, width=700, height=650, bg=bg_colour)
frame1 = tk.Frame(root, width=700, height=650, bg=bg_colour)
frame2 = tk.Frame(root, width=700, height=650, bg=bg_colour)
frame3 = tk.Frame(root, width=700, height=650, bg=bg_colour)
frame4 = tk.Frame(root, width=700, height=650, bg=bg_colour)
frame5 = tk.Frame(root, width=700, height=650, bg=bg_colour)
frame6 = tk.Frame(root, width=700, height=650, bg=bg_colour)


#frame for the login page 
def load_frame0():
    frame0.tkraise()

    def login():
        username = username_entry.get()
        password = password_entry.get()

        conn = sqlite3.connect('users.db')
        c = conn.cursor()

        c.execute('SELECT * FROM userlogin WHERE username=? AND password=?', (username, password))
        user = c.fetchone()

        if user is not None:
            message_label.config(text='Login successful')
            load_frame1()
        else:
            message_label.config(text='Login failed')

        conn.close()

    username_label = tk.Label(frame0, text='Username')
    username_label.pack()
    username_entry = tk.Entry(frame0)
    username_entry.pack()

    password_label = tk.Label(frame0, text='Password')
    password_label.pack()
    password_entry = tk.Entry(frame0, show='*')
    password_entry.pack()

    login_button = tk.Button(frame0, text='Login', command=lambda : login())
    login_button.pack()   

    message_label = tk.Label(frame0, text='')
    message_label.pack()




#frame for the landing page of the app
def load_frame1(): 
    
    # stack frame 1 above frame 2
    frame1.tkraise()
    # prevent widgets from modifying the frame
    frame1.pack_propagate(False)

    # create logo widget for app logo
    logo_img = ImageTk.PhotoImage(file="student-toppers.jpg")
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.place(x=25, y=10, height=126, width=340)
    #create calculator button logo
    btn1_img = ImageTk.PhotoImage(file="calc1.png")
    btn1_widget = tk.Label(frame1, image=btn1_img, bg=bg_colour)
    btn1_widget.image = btn1_img
    #create chatbot button logo
    btn2_img = ImageTk.PhotoImage(file="chatbot3.png")
    btn2_widget = tk.Label(frame1, image=btn2_img, bg=bg_colour)
    btn2_widget.image = btn2_img
    #create todo button logo
    btn3_img = ImageTk.PhotoImage(file="todo2.png")
    btn3_widget = tk.Label(frame1, image=btn3_img, bg=bg_colour)
    btn3_widget.image = btn3_img
    #create calendar button logo
    btn4_img = ImageTk.PhotoImage(file="calendar.png")
    btn4_widget = tk.Label(frame1, image=btn4_img, bg=bg_colour)
    btn4_widget.image = btn4_img
    #create notify button logo
    btn5_img = ImageTk.PhotoImage(file="notif.png")
    btn5_widget = tk.Label(frame1, image=btn5_img, bg=bg_colour)
    btn5_widget.image = btn5_img
    

    # create label widget for app heading
    tk.Label(
        frame1, 
        text="StudyAssist",
        bg=bg_colour,
        fg="white",
        font=("Helvetica", 34)
        ).place(x=370, y=20, height=110, width=300)

    # create calc button widget
    tk.Button(
        frame1,
        text="",
        image=btn1_img,
        font=("Ubuntu", 20),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_frame3()
        ).place(x=25, y=160, height=123, width=118)
    tk.Label(
        frame1, 
        text="Calculator",
        bg=bg_colour,
        fg="white",
        font=("Shanti", 14)
        ).place(x=35, y=285)
    
    # create chatbot button widget
    tk.Button(
        frame1,
        text="",
        image=btn2_img,
        font=("Ubuntu", 20),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_frame2()
        ).place(x=533, y=470, height=110, width=140)
    tk.Label(
        frame1, 
        text="Chatbot",
        bg=bg_colour,
        fg="white",
        font=("Shanti", 14)
        ).place(x=563, y=585)

    # create to do list button widget
    tk.Button(
        frame1,
        text="",
        image=btn3_img,
        font=("Ubuntu", 20),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:load_frame4()
        ).place(x=25, y=320, height=118, width=122)
    tk.Label(
        frame1, 
        text="To-Do List",
        bg=bg_colour,
        fg="white",
        font=("Shanti", 14)
        ).place(x=31, y=442)

    # create academic calendar button widget
    tk.Button(
        frame1,
        text="",
        image=btn4_img,
        font=("Ubuntu", 20),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: load_frame5()
        ).place(x=25, y=480, height=118, width=122)
    tk.Label(
        frame1, 
        text="Academic calendar",
        bg=bg_colour,
        fg="white",
        font=("Shanti", 14)
        ).place(x=23, y=604)

    # create notify button widget
    tk.Button(
        frame1,
        text="",
        image=btn5_img,
        font=("Ubuntu", 20),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda: load_frame6()
        ).place(x=543, y=170, height=125, width=125)
    tk.Label(
        frame1, 
        text="Set Notifications",
        bg=bg_colour,
        fg="white",
        font=("Shanti", 14)
        ).place(x=540, y=300)





#frame for chatbot
def load_frame2():
    # stack frame 2 above frame 1
    frame2.tkraise()

    def create_memo():
        global recognizer
        tk.Label(second_frame, text="What do you want to write on your memo?", bg="orange", fg="white",font=("Shanti", 10),
            height=2, borderwidth=2, relief="solid").pack( anchor="w")
        speaker.say("What do you want to write on your memo?")
        speaker.runAndWait()

        done = False

        while not done:
            try:

                with speech_recognition.Microphone() as mic:

                    recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = recognizer.listen(mic)

                    note = recognizer.recognize_google(audio)
                    note = note.lower()
                    tk.Label(second_frame, text=note, bg="pink", fg="white",font=("Shanti", 10),
                        height=2, borderwidth=2, relief="solid").pack(anchor="e")
                    tk.Label(second_frame, text="Choose a filename!", bg="orange", fg="white",font=("Shanti", 10),
                        height=2, borderwidth=2, relief="solid").pack( anchor="w")
                    speaker.say("Choose a filename!")
                    speaker.runAndWait()

                    recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = recognizer.listen(mic)

                    filename = recognizer.recognize_google(audio)
                    filename = filename.lower()
                    tk.Label(second_frame, text=filename, bg="pink", fg="white",font=("Shanti", 10),
            height=2, borderwidth=2, relief="solid").pack(anchor="e")

                with open(f"{filename}.txt", 'w') as f:
                    f.write(note)
                    done = True
                    tk.Label(second_frame, text="I have created the memo successfully.", bg="orange", fg="white",font=("Shanti", 10),
                        height=2, borderwidth=2, relief="solid").pack( anchor="w")
                    speaker.say(f"I have created the memo successfully.")
                    speaker.runAndWait()

            except speech_recognition.UnknownValueError:
                recognizer = speech_recognition.Recognizer()
                tk.Label(second_frame, text="I could not understand you!, Please try again!", bg="orange", fg="white",font=("Shanti", 10),
                        height=2, borderwidth=2, relief="solid").pack( anchor="w")
                speaker.say("I could not understand you!, Please try again!")
                speaker.runAndWait()


    def math_material():
        tk.Label(second_frame, text="Redirecting to maths study material...", bg="orange", fg="white",font=("Shanti", 10),
            height=2, borderwidth=2, relief="solid").pack(anchor="w")
        speaker.say("Redirecting to maths study material")
        webbrowser.open("https://drive.google.com/drive/folders/1N1ZotoYd-7vk5wG1QJXozwWQYG7hrV7V?usp=share_link")
        speaker.runAndWait()


    def coa_material():
        tk.Label(second_frame, text="Redirecting to COA study material...", bg="orange", fg="white",font=("Shanti", 10),
            height=2, borderwidth=2, relief="solid").pack(anchor="w")
        speaker.say("Redirecting to COA study material")
        webbrowser.open("https://drive.google.com/drive/folders/144JDfA-Xkpq8JIV8HvBPiHLKhlBo_Ymz?usp=share_link")
        speaker.runAndWait()


    def cn_material():
        tk.Label(second_frame, text="Redirecting to Computer networks study material...", bg="orange", fg="white",font=("Shanti", 10),
            height=2, borderwidth=2, relief="solid").pack(anchor="w")
        speaker.say("Redirecting to Computer networks study material")
        webbrowser.open("https://drive.google.com/drive/folders/1lPfelUppby60W-ntNzRhjXqti5b4bN3E?usp=share_link")
        speaker.runAndWait()


    def automata_material():
        tk.Label(second_frame, text="Redirecting to automata theory study material...", bg="orange", fg="white",font=("Shanti", 10),
            height=2, borderwidth=2, relief="solid").pack(anchor="w")
        speaker.say("Redirecting to Automata theory study material")
        webbrowser.open("https://drive.google.com/drive/folders/1mydvkIB0V5ulXEZH5vi8N7sJLHVxjNVJ?usp=share_link")
        speaker.runAndWait()


    def os_material():
        tk.Label(second_frame, text="Redirecting to operating systems study material...", bg="orange", fg="white",font=("Shanti", 10),
            height=2, borderwidth=2, relief="solid").pack(anchor="w")
        speaker.say("Redirecting to Operating systems study material")
        webbrowser.open("https://drive.google.com/drive/folders/1C4OCl6PN_3m4QpJkYBj6xo3EpOL3PYeT?usp=share_link")
        speaker.runAndWait()

    def time_table():
        tk.Label(second_frame, text="Here's your timetable for the semester...", bg="orange", fg="white",font=("Shanti", 10),
            height=2, borderwidth=2, relief="solid").pack(anchor="w")
        speaker.say("Here's your timetable for the semester")
        style = ttk.Style()
        style.theme_use('clam')
        # Add a Treeview widget
        tree = ttk.Treeview(second_frame, column=("c0", "c1", "c2", "c3", "c4", "c5"), show='headings', height=8)
        tree.column("# 1", anchor=CENTER,stretch=NO, width=70)
        tree.heading("# 1", text="Timing")
        tree.column("# 2", anchor=CENTER,stretch=NO, width=70)
        tree.heading("# 2", text="Monday")
        tree.column("# 3", anchor=CENTER,stretch=NO, width=70)
        tree.heading("# 3", text="Tuesday")
        tree.column("# 4", anchor=CENTER,stretch=NO, width=70)
        tree.heading("# 4", text="Wednesday")
        tree.column("# 5", anchor=CENTER,stretch=NO, width=70)
        tree.heading("# 5", text="Thursday")
        tree.column("# 6", anchor=CENTER,stretch=NO, width=70)
        tree.heading("# 6", text="Friday")
        # Insert the data in Treeview widget
        tree.insert('', 'end', text="0", values=('8:00-9:00', 'Math', 'COA', 'CN', 'OS', 'AT'))
        tree.insert('', 'end', text="1", values=('9:00-10:00', 'COA', 'CN','AT', 'Math','OS' ))
        tree.insert('', 'end', text="2", values=('10:00-11:00', 'Math', 'CN', 'OS', 'AT', 'COA'))
        tree.insert('', 'end', text="3", values=('11:00-12:00', 'AT', 'Math', 'COA', 'CN', 'OS'))
        tree.insert('', 'end', text="4", values=('1:00-2:00', 'CN', 'COA','AT', 'OS','Math' ))
        tree.insert('', 'end', text="5", values=('2:00-3:00', 'OS', 'AT','Math', 'COA', 'CN'))
        tree.pack(anchor="w")
        speaker.runAndWait()


    def hello():
        greet_reply = ["Hello. What can i do for you?", "Hey, How can i help you?", "Hi, how may i help you?"]
        msg1 = random.choice(greet_reply)
        tk.Label(second_frame, text=msg1, bg="orange", fg="white",font=("Shanti", 10),
            height=2, borderwidth=2, relief="solid").pack(anchor="w")
        speaker.say(msg1)
        speaker.runAndWait()


    def quit():
        bye_reply = ["See you again, Bye!", "See you later , Bye!", "Goodbye!", "Bye!"]
        msg2 = random.choice(bye_reply)
        tk.Label(second_frame, text=msg2, bg="orange", fg="white",font=("Shanti", 10),
            height=2, borderwidth=2, relief="solid").pack( anchor="w")
        speaker.say(msg2)
        speaker.runAndWait()
        sys.exit(0)


    mappings = {
        "greeting": hello,
        "create_memo": create_memo,
        "math": math_material,
        "coa": coa_material,
        "cn": cn_material,
        "automata": automata_material,
        "os": os_material,
        "timetable" : time_table,
        "exit": quit
    }    


    assistant = GenericAssistant('intents.json', intent_methods=mappings)
    assistant.train_model()

    def button_connect():
        try:
            with speech_recognition.Microphone() as mic:
                global recognizer
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                message = recognizer.recognize_google(audio)

                #display msg
                tk.Label(second_frame, text=message, bg="pink", fg="white",font=("Shanti", 10),
                        height=2, borderwidth=2, relief="solid").pack(anchor="e")

                message = message.lower()

            assistant.request(message)
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()

    # main
    main_frame = Frame(frame2)
    main_frame.pack(pady = 130, fill=BOTH)

    # canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(fill=BOTH, expand=1)

    # scrollbar
    my_scrollbar = tk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # configure the canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind(
        '<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all"))
    )

    second_frame = Frame(my_canvas, width = 700, height = 6000)
    my_canvas.create_window((60, 0), window=second_frame, anchor="n")


    label1 = tk.Label(frame2, text="StudyBot",bg=bg_colour, font=('Arial', 28))
    label1.place(x=50, y=45)

    mic_img = ImageTk.PhotoImage(file="mic1.png")
    mic_widget = tk.Label(frame2, image=mic_img)
    mic_widget.image = mic_img

    btn_mic = tk.Button(frame2, text="Mic", command=lambda: button_connect(), image=mic_img, width=5, font=("Arial", 14))
    btn_mic.place(x=300, y=10, width=115, height=115)
        
    # 'back' button widget
    tk.Button(
        frame2,
        text="BACK",
        font=("Ubuntu", 15),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        command=lambda:load_frame1()
        ).place(x=505, y= 45)




# frame for calc
def load_frame3():
    frame3.tkraise()
    
    class Calculator:
        def __init__(self, master):
            self.master = master

            # Create the entry field for the calculator
            self.entry = tk.Entry(master, width=35, borderwidth=5, font=("Arial", 20), justify="right")
            self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

            # Create buttons for the calculator
            self.create_button("sin", 1, 0)
            self.create_button("cos", 1, 1)
            self.create_button("tan", 1, 2)
            self.create_button("(", 1, 3)
            self.create_button(")", 1, 4)

            self.create_button("7", 2, 0)
            self.create_button("8", 2, 1)
            self.create_button("9", 2, 2)
            self.create_button("/", 2, 3)
            self.create_button("C", 2, 4)

            self.create_button("4", 3, 0)
            self.create_button("5", 3, 1)
            self.create_button("6", 3, 2)
            self.create_button("*", 3, 3)
            self.create_button("sqrt", 3, 4)

            self.create_button("1", 4, 0)
            self.create_button("2", 4, 1)
            self.create_button("3", 4, 2)
            self.create_button("-", 4, 3)
            self.create_button("^", 4, 4)

            self.create_button(".", 5, 0)
            self.create_button("0", 5, 1)
            self.create_button("=", 5, 2)
            self.create_button("+", 5, 3)

        def create_button(self, text, row, col):
            button = tk.Button(self.master, text=text, padx=30, pady=20, command=lambda: self.button_click(text))
            button.grid(row=row, column=col)

        def button_click(self, text):
            if text == "C":
                self.entry.delete(0, tk.END)
            elif text == "=":
                try:
                    result = eval(self.entry.get())
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, result)
                except:
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, "Error")
            elif text == "sqrt":
                try:
                    result = sqrt(float(self.entry.get()))
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, result)
                except:
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, "Error")
            elif text == "^":
                self.entry.insert(tk.END, "**")
            elif text in ["sin", "cos", "tan"]:
                self.entry.insert(tk.END, f"{text}(")
            else:
                self.entry.insert(tk.END, text)

    # 'back' button widget
    tk.Button(
        frame3,
        text="BACK",
        font=("Ubuntu", 15),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        command=lambda:load_frame1()
        ).place(x=555, y= 455)
    
    global calculator 
    calculator = Calculator(frame3)


# frame for to do
def load_frame4():
    frame4.tkraise()

    class ToDoList:
        def __init__(self):
            self.tasks = []
            
            self.task_var = tk.StringVar()
            self.task_entry = tk.Entry(frame4, textvariable=self.task_var, width=40)
            self.task_entry.grid(row=0, column=0, padx=5, pady=5)
            add_task_button = tk.Button(frame4, text="Add Task", command=self.add_task)
            add_task_button.grid(row=0, column=1, padx=5, pady=5)
            
            self.task_list = tk.Listbox(frame4, height=15, width=50)
            self.task_list.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
            
            self.delete_button = tk.Button(frame4, text="Delete Task", command=self.delete_task)
            self.delete_button.grid(row=2, column=0, padx=5, pady=5)
            
            self.complete_button = tk.Button(frame4, text="Mark as Complete", command=self.complete_task)
            self.complete_button.grid(row=2, column=1, padx=5, pady=5)
        
        def add_task(self):
            task = self.task_var.get()
            if task:
                self.tasks.append(task)
                self.task_list.insert(tk.END, task)
                self.task_var.set("")
        
        def delete_task(self):
            task_index = self.task_list.curselection()
            if task_index:
                task_index = task_index[0]
                self.tasks.pop(task_index)
                self.task_list.delete(task_index)
        
        def complete_task(self):
            task_index = self.task_list.curselection()
            if task_index:
                task_index = task_index[0]
                self.task_list.itemconfig(task_index, fg="gray")
                self.task_list.selection_clear(task_index)
        
    ToDoList()
    class ToDoList:
        def __init__(self):
            self.tasks = []
            self.task_vars = []
            self.window = tk.Tk()
            self.window.title("Student Assistant - To-Do List")
            
            self.task_var = tk.StringVar()
            self.task_entry = tk.Entry(self.window, textvariable=self.task_var, width=40)
            self.task_entry.grid(row=0, column=0, padx=5, pady=5)
            add_task_button = tk.Button(self.window, text="Add Task", command=self.add_task)
            add_task_button.grid(row=0, column=1, padx=5, pady=5)
            
            self.task_list = tk.Frame(self.window)
            self.task_list.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
            
            self.delete_button = tk.Button(self.window, text="Delete Task", command=self.delete_task)
            self.delete_button.grid(row=2, column=0, padx=5, pady=5)
        # 'back' button widget
    tk.Button(
        frame4,
        text="BACK",
        font=("Ubuntu", 15),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        command=lambda:load_frame1()
        ).place(x=505, y= 45)   
       



# frame for academic calendar
def load_frame5():
    frame5.tkraise()
    labelText = tk.Label(frame5, text="Academic Calendar for 2023-24")
    labelText.pack()
    style = ttk.Style()
    style.theme_use('clam')

    # Add a Treeview widget
    tree = ttk.Treeview(frame5, column=("c1", "c2"), show='headings', height=8)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="Event")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Date")

    # Insert the data in Treeview widget
    tree.insert('', 'end', text="1", values=('Prarambh', '12th Jan 23'))
    tree.insert('', 'end', text="2", values=('Illusion', '13th Jan 23'))
    tree.insert('', 'end', text="3", values=('First defaulter’s List', '9th Feb 23'))
    tree.insert('', 'end', text="4", values=('Internal Assessment Test 1 ', '15th - 17th Feb 23'))
    tree.insert('', 'end', text="5", values=('Marathi Rajya Bhasha Diwas ', '27th Feb 23'))
    tree.insert('', 'end', text="6", values=('Internal Assessment Test 2 ', '23-27th March 23'))
    tree.insert('', 'end', text="7", values=('Utsav and Annual Day ', '27th -30th March 23'))
    tree.insert('', 'end', text="8", values=('Internal Assessment Test 3 ', '17-20th April 23'))
    tree.insert('', 'end', text="9", values=('Submissions and mock vivas ', '14th-21st April 22'))
    tree.insert('', 'end', text="10", values=('Internship Mela ', '5th - 6th April 23'))
    tree.insert('', 'end', text="11", values=('Oral/Practical Examination ', '24th April-4th May 23'))
    tree.insert('', 'end', text="12", values=('Theory Examination ', '10th May - 23rd May 23'))
    tree.insert('', 'end', text="13", values=('Commencement of New Term ', '10th July 23'))
    tree.pack()

    # 'back' button widget
    tk.Button(
        frame5,
        text="BACK",
        font=("Ubuntu", 15),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        command=lambda:load_frame1()
        ).place(x=505, y= 345)



# frame for notify app
def load_frame6():
    frame6.tkraise()

    img = Image.open("notify-label.png")
    tkimage = ImageTk.PhotoImage(img)

    # get details
    def get_details():
        get_title = title.get()
        get_msg = msg.get()
        get_time = time1.get()
        # print(get_title,get_msg, tt)

        if get_title == "" or get_msg == "" or get_time == "":
            messagebox.showerror("Alert", "All fields are required!")
        else:
            int_time = int(float(get_time))
            min_to_sec = int_time * 60
            messagebox.showinfo("notifier set", "set notification ?")
            frame6.destroy()
            time.sleep(min_to_sec)

            notification.notify(title=get_title,
                                message=get_msg,
                                app_name="Notifier",
                                app_icon="ico.ico",
                                toast=True,
                                timeout=10)

    img_label = Label(frame6, image=tkimage).grid()

    # Label - Title
    t_label = Label(frame6, text="Title to Notify",font=("poppins", 10))
    t_label.place(x=12, y=70)

    # ENTRY - Title
    title = Entry(frame6, width="25",font=("poppins", 13))
    title.place(x=123, y=70)

    # Label - Message
    m_label = Label(frame6, text="Display Message", font=("poppins", 10))
    m_label.place(x=12, y=120)

    # ENTRY - Message
    msg = Entry(frame6, width="40", font=("poppins", 13))
    msg.place(x=123,height=30, y=120)

    # Label - Time
    time_label = Label(frame6, text="Set Time", font=("poppins", 10))
    time_label.place(x=12, y=175)

    # ENTRY - Time
    time1 = Entry(frame6, width="5", font=("poppins", 13))
    time1.place(x=123, y=175)

    # Label - min
    time_min_label = Label(frame6, text="min", font=("poppins", 10))
    time_min_label.place(x=175, y=180)

    # Button
    but = Button(frame6, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
                relief="raised",
                command=get_details)
    but.place(x=170, y=230)
    
    # 'back' button widget
    tk.Button(
        frame6,
        text="BACK",
        font=("Ubuntu", 15),
        bg="#28393a",
        fg="white",
        cursor="hand2",
        command=lambda:load_frame1()
        ).place(x=505, y= 45)
    frame6.resizable(0,0)



# place frame widgets in window
for frame in (frame0, frame1, frame2, frame3, frame4, frame5, frame6):
    frame.grid(row=0, column=0, sticky="nesw")

# load the first frame
load_frame0()


# run app
root.mainloop()