import tkinter as tk
from PIL import ImageTk
from numpy import random
import pyglet

bg_colour = "#3d6466"
calculation = ""

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
	logo_widget.place(x=10, y=5, height=126, width=340)
	#create calculator button logo
	btn1_img = ImageTk.PhotoImage(file="calc.png")
	btn1_widget = tk.Label(frame1, image=btn1_img, bg=bg_colour)
	btn1_widget.image = btn1_img
    #create calculator button logo
	btn2_img = ImageTk.PhotoImage(file="student2.jpg")
	btn2_widget = tk.Label(frame1, image=btn2_img, bg=bg_colour)
	btn2_widget.image = btn2_img
	

	# create label widget for instructions
	tk.Label(
		frame1, 
		text="StudyAssist",
		bg=bg_colour,
		fg="white",
		font=("Shanti", 28)
		).place(x=380, y=20, height=100, width=200)

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
		).place(x=25, y=250, height=165, width=160)

    # create button2 button widget
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
		).place(x=25, y=430, height=165, width=160)
	


#frame for chatbot
def load_frame2():
	# stack frame 2 above frame 1
	frame2.tkraise()
    
	# create logo widget
	logo2_img = ImageTk.PhotoImage(file="download.png")
	logo2_widget = tk.Label(frame2, image=logo2_img, bg=bg_colour)
	logo2_widget.image = logo2_img
	logo2_widget.pack(pady=20)
        
	
    
	# 'back' button widget
	tk.Button(
		frame2,
		text="BACK",
		font=("Ubuntu", 18),
		bg="#28393a",
		fg="white",
		cursor="hand2",
		command=lambda:load_frame1()
		).pack(pady=20)




# frame for calc
def load_frame3():
    frame3.tkraise()
    
    def add_to_calculation(symbol):
        global calculation 
        calculation += str(symbol)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)

    def evaluate_calculation():
        global calculation
        try:
            calculation = str(eval(calculation))
            text_result.delete(1.0, "end")
            text_result.insert(1.0, calculation)
        except:
            clear_field()
            text_result.insert(1.0, "Error")

    def clear_field():
        global calculation
        calculation = ""
        text_result.delete(1.0, "end")

    text_result = tk.Text(frame3, height=2, width=18, font=("Arial", 24))
    text_result.grid(padx=10, pady=20, columnspan=5)
    btn_1 = tk.Button(frame3, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
    btn_1.grid(row=2, column=1)
    btn_2 = tk.Button(frame3, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
    btn_2.grid(row=2, column=2)
    btn_3 = tk.Button(frame3, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
    btn_3.grid(row=2, column=3)
    btn_4 = tk.Button(frame3, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
    btn_4.grid(row=3, column=1)
    btn_5 = tk.Button(frame3, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
    btn_5.grid(row=3, column=2)
    btn_6 = tk.Button(frame3, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
    btn_6.grid(row=3, column=3)
    btn_7 = tk.Button(frame3, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
    btn_7.grid(row=4, column=1)
    btn_8 = tk.Button(frame3, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
    btn_8.grid(row=4, column=2)
    btn_9 = tk.Button(frame3, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
    btn_9.grid(row=4, column=3)
    btn_0 = tk.Button(frame3, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
    btn_0.grid(row=5, column=2)
    btn_plus = tk.Button(frame3, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
    btn_plus.grid(row=2, column=4)
    btn_minus = tk.Button(frame3, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
    btn_minus.grid(row=3, column=4)
    btn_mult = tk.Button(frame3, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
    btn_mult.grid(row=4, column=4)
    btn_div = tk.Button(frame3, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
    btn_div.grid(row=5, column=4)
    btn_open = tk.Button(frame3, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
    btn_open.grid(row=5, column=1)
    btn_close = tk.Button(frame3, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
    btn_close.grid(row=5, column=3)
    btn_clear = tk.Button(frame3, text="Clear", command=clear_field, width=10, font=("Arial", 14))
    btn_clear.grid(row=6, column=1, columnspan=2)
    btn_equals = tk.Button(frame3, text="=", command=evaluate_calculation, width=5, font=("Arial", 14))
    btn_equals.grid(row=6, column=3, columnspan=2)
    

# initiallize app with basic settings
root = tk.Tk()
root.title("Study Assist")
root.geometry("700x600")
 
# create a frame widgets
frame1 = tk.Frame(root, width=700, height=600, bg=bg_colour)
frame2 = tk.Frame(root, width=700, height=600, bg=bg_colour)
frame3 = tk.Frame(root, width=700, height=600, bg=bg_colour)

# place frame widgets in window
for frame in (frame1, frame2, frame3):
	frame.grid(row=0, column=0, sticky="nesw")

# load the first frame
load_frame1()

# run app
root.mainloop()