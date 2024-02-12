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
root.background = "#34495E"
root.foreground = "#D5D8DC"
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

auto_clicker = AutoClicker()

def keypress(key):
    if key == KeyCode(char=''):
        updatebuttons()
        auto_clicker.clicking = not auto_clicker.clicking

def toggle_clicking():
    updatebuttons()
    print(auto_clicker.clicking, "text")
    auto_clicker.clicking = not auto_clicker.clicking

def updatebuttons():
    if click_button["state"] == "normal":
        click_button["state"] = "disabled"
        click_button["text"] = "enable(f6)"
        click_button1["state"] = "normal"
        click_button1["text"] = "disable(f6)"
        
    else:
        click_button1["state"] = "disabled"
        click_button1["text"] = "disable(f6)"
        click_button["state"] = "normal"
        click_button["text"] = "enable(f6)"
        
    

click_button = tk.Button(root, text="enable(f6)", background = "#273746", foreground = "#D5D8DC", command=toggle_clicking)
click_button1 = tk.Button(root, text="disable(f6)", background = "#273746", foreground = "#D5D8DC",  command=toggle_clicking, state = "disabled")
click_button.pack(side = "left", expand = True)
click_button1.pack(side = "right", expand = True)

auto_clicker.start()

listener = Listener(on_press=keypress)
listener.start()

listener.stop()

root.mainloop()