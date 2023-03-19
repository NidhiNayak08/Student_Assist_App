import tkinter as tk


root = tk.Tk()
root.geometry("500x400")

label1 = tk.Label(root, text="Study Assist", font=('Arial', 28))
label1.pack(padx=20, pady=20)

btn_mic = tk.Button(root, text="Mic", command=lambda: button_connect(), width=5, font=("Arial", 14))
btn_mic.pack()

root.mainloop()