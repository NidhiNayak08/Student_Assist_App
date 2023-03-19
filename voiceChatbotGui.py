from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as tts
import sys
import tkinter as tk
from PIL import ImageTk


recognizer = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 150)

todo_list = ['Go shopping', 'Clean room', 'Record video']

def create_note():
    global recognizer
    tk.Label(root, text="What do you want to write on your note?", bg="orange", fg="white",font=("Shanti", 13),
          height=2, borderwidth=3, relief="solid").pack( anchor="w")
    speaker.say("What do you want to write on your note?")
    speaker.runAndWait()

    done = False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                note = recognizer.recognize_google(audio)
                note = note.lower()
                tk.Label(root, text=note, bg="pink", fg="white",font=("Shanti", 13),
                    height=2, borderwidth=3, relief="solid").pack(anchor="e")
                tk.Label(root, text="Choose a filename!", bg="orange", fg="white",font=("Shanti", 13),
                    height=2, borderwidth=3, relief="solid").pack( anchor="w")
                speaker.say("Choose a filename!")
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                filename = recognizer.recognize_google(audio)
                filename = filename.lower()
                tk.Label(root, text=filename, bg="pink", fg="white",font=("Shanti", 13),
          height=2, borderwidth=3, relief="solid").pack(anchor="e")

            with open(f"{filename}.txt", 'w') as f:
                f.write(note)
                done = True
                tk.Label(root, text="I have created the note {filename} successfully.", bg="orange", fg="white",font=("Shanti", 13),
                    height=2, borderwidth=3, relief="solid").pack( anchor="w")
                speaker.say(f"I have created the note {filename} successfully.")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            tk.Label(root, text="I could not understand you!, Please try again!", bg="orange", fg="white",font=("Shanti", 13),
                    height=2, borderwidth=3, relief="solid").pack( anchor="w")
            speaker.say("I could not understand you!, Please try again!")
            speaker.runAndWait()


def add_todo():

    global recognizer

    tk.Label(root, text="What to do do you want to add?", bg="orange", fg="white",font=("Shanti", 13),
        height=2, borderwidth=3, relief="solid").pack( anchor="w")
    speaker.say("What to do do you want to add?")
    speaker.runAndWait()

    done = False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                item = recognizer.recognize_google(audio)
                item = item.lower()

                todo_list.append(item)
                done = True

                tk.Label(root, text="I have added {item} to the to do list!", bg="orange", fg="white",font=("Shanti", 13),
                    height=2, borderwidth=3, relief="solid").pack( anchor="w")
                speaker.say(f"I have added {item} to the to do list!")
                speaker.runAndWait

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            tk.Label(root, text="I could not understand you!, Please try again!", bg="orange", fg="white",font=("Shanti", 13),
                    height=2, borderwidth=3, relief="solid").pack( anchor="w")
            speaker.say("I could not understand you!, Please try again!")
            speaker.runAndWait()


def show_todo():
    tk.Label(root, text="Items on your to do list are the following", bg="orange", fg="white",font=("Shanti", 13),
        height=2, borderwidth=3, relief="solid").pack( anchor="w")
    speaker.say("Items on your to do list are the following")
    for item in todo_list:
        speaker.say(item)
    speaker.runAndWait()


def hello():
    tk.Label(root, text="Hello. What can i do for you?", bg="orange", fg="white",font=("Shanti", 13),
          height=2, borderwidth=3, relief="solid").pack(anchor="w")
    speaker.say("Hello. What can i do for you?")
    speaker.runAndWait()


def quit():
    tk.Label(root, text="Bye!!", bg="orange", fg="white",font=("Shanti", 13),
          height=2, borderwidth=3, relief="solid").pack( anchor="w")
    speaker.say("Bye")
    speaker.runAndWait()
    sys.exit(0)


mappings = {
    "greeting": hello,
    "create_note": create_note,
    "add_todo": add_todo,
    "show_todos": show_todo,
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
            message = message.lower()
            
            #display msg
            tk.Label(root, text=message, bg="pink", fg="white",font=("Shanti", 13),
          height=2, borderwidth=3, relief="solid").pack(anchor="e")

        assistant.request(message)
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()

#gui code
root = tk.Tk()
root.geometry("500x400")

label1 = tk.Label(root, text="StudyAssist", font=('Arial', 28))
label1.place(x=50, y=35)
#blank label with pack()
label1 = tk.Label(root, text=" ", font=('Arial', 28))
label1.pack(pady=50)

mic_img = ImageTk.PhotoImage(file="mic.png")
mic_widget = tk.Label(root, image=mic_img)
mic_widget.image = mic_img

btn_mic = tk.Button(root, text="Mic", command=lambda: button_connect(), image=mic_img, width=5, font=("Arial", 14))
btn_mic.place(x=300, y=10, width=100, height=100)

root.mainloop()

