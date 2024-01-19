import tkinter as tk
from random import random
from threading import Thread
from time import sleep
from pynput.mouse import Controller, Button
from pynput.keyboard import KeyCode, Listener

root = tk.Tk()
root.title("AutoClickr")
root.geometry("300x100")
root.resizable(False, False)
root.attributes("-topmost", 1)
label = tk.Label(root, text="Press the button or - to start/stop clicking", font=("Arial Bold", 10))
label.pack()

delay = 0.00001
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

def toggle_clicking():
    AutoClicker.clicking = not AutoClicker.clicking


click_button = tk.Button(root, text="Toggle Clicking", command=toggle_clicking)
click_button.pack()

AutoClicker().start()

listener = Listener(on_press=keypress)
listener.start()

root.mainloop()
