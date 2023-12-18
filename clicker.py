#remember to use this command in python terminal: "& C:/Users/Bruker/AppData/Local/Microsoft/WindowsApps/python3.11.exe c:/Users/Bruker/Desktop/autoclikr/clicker.py"
import tkinter as tk
from random import random
from threading import Thread
from time import sleep
from pynput.mouse import Controller, Button
from pynput.keyboard import KeyCode, Listener


delay = 0.0001
mouse = Controller()

class AutoClicker(Thread):
    clicking = False

    def run(self):
        while True:
            if self.clicking:
                mouse.click(Button.left, 1)
            sleep(delay * random() + 1/2 * delay)

def keypress(key):
    if key == KeyCode(char='-'):
        AutoClicker.clicking = not AutoClicker.clicking

root = tk.Tk()
root.geometry("445x445")
root.background = "#222222"
root.title("Ikaros' autoClicker")

start_button =tk.Button(root, text="Start ('-')", command=AutoClicker().start())
start_button.pack()

root.mainloop()

with Listener(on_press=keypress) as listener:
    listener.join()