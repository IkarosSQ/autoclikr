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
root.configure(background ="#1C2833")
label = tk.Label(root, text="Press the button or - to start/stop clicking", font=("Arial Bold", 10), bg="#1C2833", fg="#D5D8DC")
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

auto_clicker = AutoClicker()

def keypress(key):
    print(key)
    if key == KeyCode(char='-'):
        updatebuttons()
        auto_clicker.clicking = not auto_clicker.clicking

def toggle_clicking():
    updatebuttons()
    print(auto_clicker.clicking, "text")
    auto_clicker.clicking = not auto_clicker.clicking

def updatebuttons():
    if click_button["state"] == "normal":
        click_button["state"] = "disabled"
        click_button["text"] = "enable(-)"
        click_button1["state"] = "normal"
        click_button1["text"] = "disable(-)"
        
    else:
        click_button1["state"] = "disabled"
        click_button1["text"] = "disable(-)"
        click_button["state"] = "normal"
        click_button["text"] = "enable(-)"
        
    

click_button = tk.Button(root, text="enable(-)", background = "#212F3D", foreground = "#D5D8DC", command=toggle_clicking)
click_button1 = tk.Button(root, text="disable(-)", background = "#212F3D", foreground = "#D5D8DC",  command=toggle_clicking, state = "disabled")
click_button.pack(side = "left", expand = True)
click_button1.pack(side = "right", expand = True)

auto_clicker.start()

listener = Listener(on_press=keypress)
listener.start()


root.mainloop()
