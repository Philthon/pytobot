import time
import tkinter as tk
import tkinter.ttk as ttk
import webbrowser
from tkinter import Label, Toplevel
from tkinter.filedialog import askopenfilename, asksaveasfilename

import pyautogui
import pynput.keyboard as kb
import pynput.mouse as ms
from pynput.keyboard import Key
from pynput.mouse import Button
from ttkthemes import ThemedStyle

from constants import image_data

mouse = ms.Controller()
keyboard = kb.Controller()


def callback(url):
    webbrowser.open_new(url)


def open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Pytobot - {filepath}")


def save_file():
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Pytobot - {filepath}")


def run_file():
    text = txt_edit.get(1.0, tk.END)
    automationlist = text.split(",")
    wait = 1
    i = 2
    xloop = 1
    while xloop < i:
        xloop = xloop + 1
        for index, elem in enumerate(automationlist):
            if index + 1 < len(automationlist) and index - 1 >= 0:
                curr_el = str(elem)
                if curr_el == "\nwait":
                    wait = int(automationlist[index + 1])
                elif curr_el == "\nclickl":
                    next_el0 = int(automationlist[index + 1])
                    next_el1 = int(automationlist[index + 2])
                    pyautogui.click(next_el0, next_el1, button="left")
                    time.sleep(wait)
                elif curr_el == "\nclickr":
                    next_el0 = int(automationlist[index + 1])
                    next_el1 = int(automationlist[index + 2])
                    pyautogui.click(next_el0, next_el1, button="right")
                    time.sleep(wait)
                elif curr_el == "\nmove":
                    next_el0 = int(automationlist[index + 1])
                    next_el1 = int(automationlist[index + 2])
                    pyautogui.moveTo(next_el0, next_el1)
                    time.sleep(wait)
                elif curr_el == "\nwrite":
                    next_el0 = str(automationlist[index + 1])
                    keyboard.type(next_el0)
                    time.sleep(wait)
                elif curr_el == "\nenter":
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    time.sleep(wait)
                elif curr_el == "\ncopy":
                    keyboard.press(Key.ctrl)
                    keyboard.press("c")
                    keyboard.release("c")
                    keyboard.release(Key.ctrl)
                    time.sleep(wait)
                elif curr_el == "\npaste":
                    keyboard.press(Key.ctrl)
                    keyboard.press("v")
                    keyboard.release("v")
                    keyboard.release(Key.ctrl)
                    time.sleep(wait)
                elif curr_el == "\ndelete":
                    keyboard.press(Key.delete)
                    keyboard.release(Key.delete)
                    time.sleep(wait)
                elif curr_el == "\nbackspace":
                    keyboard.press(Key.backspace)
                    keyboard.release(Key.backspace)
                    time.sleep(wait)
                elif curr_el == "\nsleep5sec":
                    time.sleep(5)
                elif curr_el == "\nsleep30sec":
                    time.sleep(30)
                elif curr_el == "\nsleep5min":
                    time.sleep(300)
                elif curr_el == "\nloop1":
                    MsgBox = tk.messagebox.askquestion(
                        "Looping", "Continue Looping?", icon="warning"
                    )
                    if MsgBox == "yes":
                        run_file()
                    else:
                        return
                elif curr_el == "\nloopx":
                    i = int(automationlist[index + 1]) + 1
                elif curr_el == "\nloop8":
                    run_file()
                elif curr_el == "\ndclick":
                    next_el0 = int(automationlist[index + 1])
                    next_el1 = int(automationlist[index + 2])
                    pyautogui.doubleClick(next_el0, next_el1)
                    time.sleep(wait)
                elif curr_el == "\nclickholdleft":
                    mouse.press(Button.left)
                    time.sleep(wait)
                elif curr_el == "\nclickreleaseleft":
                    mouse.release(Button.left)
                    time.sleep(wait)
                elif curr_el == "\ncopyall":
                    keyboard.press(Key.ctrl)
                    keyboard.press("a")
                    keyboard.release("a")
                    keyboard.press("c")
                    keyboard.release("c")
                    keyboard.release(Key.ctrl)
                    time.sleep(wait)
                elif curr_el == "\nctrlhold":
                    keyboard.press(Key.ctrl)
                    time.sleep(wait)
                elif curr_el == "\nctrlrelease":
                    keyboard.release(Key.ctrl)
                    time.sleep(wait)
                elif curr_el == "\ntab":
                    keyboard.press(Key.tab)
                    keyboard.release(Key.tab)
                    time.sleep(wait)
                elif curr_el == "\nesc":
                    keyboard.press(Key.esc)
                    keyboard.release(Key.esc)
                    time.sleep(wait)
                elif curr_el == "\nup":
                    keyboard.press(Key.up)
                    keyboard.release(Key.up)
                    time.sleep(wait)
                elif curr_el == "\ndown":
                    keyboard.press(Key.down)
                    keyboard.release(Key.down)
                    time.sleep(wait)
                elif curr_el == "\nleft":
                    keyboard.press(Key.left)
                    keyboard.release(Key.left)
                    time.sleep(wait)
                elif curr_el == "\nright":
                    keyboard.press(Key.right)
                    keyboard.release(Key.right)
                    time.sleep(wait)
                elif curr_el == "\nprintscreen":
                    keyboard.press(Key.print_screen)
                    keyboard.release(Key.print_screen)
                    time.sleep(wait)
                elif curr_el == "\ncmd":
                    keyboard.press(Key.cmd)
                    keyboard.release(Key.cmd)
                    time.sleep(wait)
                elif curr_el == "\ncmdhold":
                    keyboard.press(Key.cmd)
                elif curr_el == "\ncmdrelease":
                    keyboard.release(Key.cmd)
                elif curr_el == "\nscroll":
                    next_el0 = int(automationlist[index + 1])
                    pyautogui.scroll(next_el0)
                    time.sleep(wait)
                elif curr_el == "\n#":
                    time.sleep(0)


def run_record_help():
    newWindow = Toplevel(window)
    window.iconphoto(True, tk.PhotoImage(data=image_data))
    style = ThemedStyle(newWindow)
    style.set_theme("arc")
    newWindow.title("Support Window")
    newWindow.geometry("450x350")
    txt_edit = tk.Text(newWindow)
    txt_edit.grid(row=0, column=1, sticky="nsew")
    text = (
        "\nBelow you can find all available shortcuts. \nThe main program window has to be in the \nforeground to detect your shortcuts."
        + "\n\nALT Left and 1 - Prints click and mouse coordinates \nALT Left and 2 - copy \nALT Left and 3 - paste \nALT Left and 4 - enter \nALT Left and 5 - write \nALT Left and 6 - doubleclick \nALT Left and 7 - clickpress \nALT Left and 8 - clickrelease \nALT Left and 9 - sleep5sec \nALT Left and 0 - sleep30sec \nALT Right and 0 - delete \nALT Right and 9 - loop1 \nALT Right and 8 - loop8"
    )
    txt_edit.insert(tk.END, text)


def run_record_mouse(self):
    currentMouseX, currentMouseY = pyautogui.position()
    txt_edit.insert(
        tk.END, "clickl," + str(currentMouseX) + "," + str(currentMouseY) + ",\n"
    )


def run_record_copy(self):
    txt_edit.insert(tk.END, "copy,\n")


def run_record_paste(self):
    txt_edit.insert(tk.END, "paste,\n")


def run_record_enter(self):
    txt_edit.insert(tk.END, "enter,\n")


def run_record_write(self):
    txt_edit.insert(tk.END, "write,\n")


def run_record_doubleclick(self):
    txt_edit.insert(tk.END, "dclick,\n")


def run_record_clickpress(self):
    txt_edit.insert(tk.END, "clickpress,\n")


def run_record_clickrelease(self):
    txt_edit.insert(tk.END, "clickrelease,\n")


def run_record_sleep5sec(self):
    txt_edit.insert(tk.END, "sleep5sec,\n")


def run_record_sleep30sec(self):
    txt_edit.insert(tk.END, "sleep30sec,\n")


def run_record_delete(self):
    txt_edit.insert(tk.END, "delete,\n")


def run_record_loop1(self):
    txt_edit.insert(tk.END, "loop1,\n")


def run_record_loop8(self):
    txt_edit.insert(tk.END, "loop8,\n")


def run_sample():
    text = "start,\ncmd,\nwrite,Pytobot.website,\nenter,\nsleep5sec,\nmove,500,500,\nscroll,-500,"
    txt_edit.insert(tk.END, text)


def help_file():
    newWindow = Toplevel(window)
    window.iconphoto(True, tk.PhotoImage(data=image_data))
    style = ThemedStyle(newWindow)
    style.set_theme("arc")
    newWindow.title("Help Window")
    newWindow.rowconfigure(0, minsize=690, weight=1)
    newWindow.columnconfigure(1, minsize=800, weight=1)
    txt_edit = tk.Text(newWindow)
    txt_edit.grid(row=0, column=1, sticky="nsew")
    text = (
        "\n\t\tBasic Operators:\n\nstart, \t\t\t- Always start your code with 'start,'\nclickl,500,1000, \t\t\t- left mouse click at screen coordinates x,y\nclickr,500,1000, \t\t\t- right mouse click at screen coordinates x,y \nmove, \t\t\t- moves the mouse to x,y position on screen\ndclick,500,500, \t\t\t- double left click \ncopy, \t\t\t- same as ctrl & c\ncopyall, \t\t\t- same as ctrl & a and then ctrl & c \npaste, \t\t\t- same as ctrl & v"
        + "\nenter, \t\t\t- enter on keyboard\nwrite,word or phrase, \t\t- you can write anything you want between the commas\nbackspace, \t\t\t- same as backspace \ndelete, \t\t\t- same as delete \n\n\t\tAdvanced Operators:\n\nscroll,number, \t\t\t- mouse scroll X digits up(positive digit) or down(negative digit)\nclickholdleft, \t\t\t- clicks and holds the left mouse button\nclickreleaseleft, \t\t\t- clicks and releases the left mouse button\nsleep5sec, \t\t\t- waits for 5 seconds\nsleep30sec,\t\t\t- waits for 30 seconds\nsleep5min, \t\t\t- waits for 5 minutes\nloop1, \t\t\t- loops once\nloopx,2, \t\t\t- loops x times\nloop8, \t\t\t- loop until you kill the program"
        + "\ntab, \t\t\t- tab on keyboard\nesc, \t\t\t- esc on keyboard\nctrlhold, \t\t\t- holds down the ctrl button for other short cuts. \n\t\t\tE.g. ctrlhold,write,x,ctrlrelease, - for cut\nctrlrelease, \t\t\t- releases the ctrl button\nup, \t\t\t- up arrow on keyboard\ndown, \t\t\t- down arrow on keyboard\nleft, \t\t\t- left arrow on keyboard\nright, \t\t\t- right arrow on keyboard\nprintscreen, \t\t\t- printscreen on keyboard\ncmd, \t\t\t- windows button / command button\ncmdhold, \t\t\t- holds the cmd button e.g. cmdhold,write,2,cmdrelease, switches apps\ncmdrelease, \t\t\t- releases the cmd button\nwait,5, \t\t\t- changes the default waiting time (1) in seconds after each command"
        + "\n#YourComment, \t\t\t- #this is how you can write a comment. Don't use commas in your comment \n\t\t\tbut at the end,"
    )
    txt_edit.insert(tk.END, text)


def support_file():
    newWindow = Toplevel(window)
    window.iconphoto(True, tk.PhotoImage(data=image_data))
    newWindow.configure(bg="white")
    style = ThemedStyle(newWindow)
    style.set_theme("arc")
    newWindow.title("Support Window")
    newWindow.rowconfigure(0, minsize=400, weight=1)
    newWindow.columnconfigure(1, minsize=400, weight=1)
    Label(
        newWindow,
        bg="white",
        font=("roboto", 10, "bold"),
        padx=1,
        pady=0,
        text=("\nThere is more!"),
    ).pack(side="top")
    Label(
        newWindow,
        bg="white",
        font=("roboto", 10),
        padx=1,
        pady=0,
        text=("Check out Pytobot's GitHub! \nDownload the latest version!"),
    ).pack(side="top")
    link2 = Label(
        newWindow,
        text="GitHub",
        fg="blue",
        cursor="hand2",
        bg="white",
        font=("roboto", 10),
        padx=1,
        pady=0,
    )
    link2.pack()
    link2.bind("<Button-1>", lambda e: callback("https://github.com/Philthon/pytobot"))
    Label(
        newWindow,
        bg="white",
        font=("roboto", 10, "bold"),
        padx=1,
        pady=0,
        text=("\nSupport this project via:"),
    ).pack(side="top")
    Label(
        newWindow,
        bg="white",
        font=("roboto", 10),
        padx=1,
        pady=0,
        text=("If this program helped you then buy me a coffee:"),
    ).pack(side="top")
    link1 = Label(
        newWindow,
        text="buymeacoffee.com",
        fg="blue",
        cursor="hand2",
        bg="white",
        font=("roboto", 10),
        padx=1,
        pady=0,
    )
    link1.pack()
    link1.bind("<Button-1>", lambda e: callback("https://www.buymeacoffee.com/pytobot"))
    Label(
        newWindow,
        bg="white",
        font=("roboto", 10, "bold"),
        padx=1,
        pady=0,
        text=("\nVersion:"),
    ).pack(side="top")
    Label(
        newWindow,
        bg="white",
        font=("roboto", 10),
        padx=1,
        pady=0,
        text=("This is version 1.0"),
    ).pack(side="top")
    Label(
        newWindow,
        bg="white",
        font=("roboto", 10, "bold"),
        padx=1,
        pady=0,
        text=("\nAuthor:"),
    ).pack(side="top")
    Label(
        newWindow, bg="white", font=("roboto", 10), padx=1, pady=0, text=("PAK")
    ).pack(side="top")
    Label(
        newWindow,
        bg="white",
        font=("roboto", 10, "bold"),
        padx=1,
        pady=0,
        text=("\nCredits:"),
    ).pack(side="top")
    Label(
        newWindow,
        bg="white",
        font=("roboto", 10),
        padx=1,
        pady=0,
        text=("Icon credit: \nhttps://www.flaticon.com/authors/freepik \n\n\n"),
    ).pack(side="top")


def github_link():
    newWindow = Toplevel(window)
    window.iconphoto(True, tk.PhotoImage(data=image_data))
    newWindow.configure(bg="white")
    style = ThemedStyle(newWindow)
    style.set_theme("arc")
    newWindow.title("Cotribute")
    newWindow.rowconfigure(0, minsize=400, weight=1)
    newWindow.columnconfigure(1, minsize=400, weight=1)
    Label(
        newWindow,
        bg="white",
        font=("roboto", 10, "bold"),
        padx=10,
        pady=10,
        text=("Want to help out?"),
    ).pack(side="top")
    Label(
        newWindow,
        bg="white",
        font=("roboto", 10),
        padx=10,
        pady=0,
        text=("Awesome!\n\nCheck out the GitHub repo:"),
    ).pack(side="top")
    link2 = Label(
        newWindow,
        text="https://github.com/Philthon/pytobot",
        fg="blue",
        cursor="hand2",
        bg="white",
        font=("roboto", 10),
        padx=10,
        pady=10,
    )
    link2.pack()
    link2.bind("<Button-1>", lambda e: callback("https://github.com/Philthon/pytobot"))


# Main Window
window = tk.Tk()
window.iconphoto(True, tk.PhotoImage(data=image_data))
style = ThemedStyle(window)
style.set_theme("arc")


window.title("Pytobot")
window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure(1, minsize=400, weight=1)

txt_edit = tk.Text(window)

# Buttons
btn_frame = ttk.Frame(window, relief=tk.RIDGE)
btn_open = ttk.Button(btn_frame, text="Open", command=open_file)
btn_save = ttk.Button(btn_frame, text="Save", command=save_file)
btn_run = ttk.Button(btn_frame, text="Run", command=run_file)
btn_help = ttk.Button(btn_frame, text="Help", command=help_file)
btn_sample = ttk.Button(btn_frame, text="Sample", command=run_sample)
btn_record_help = ttk.Button(btn_frame, text="Shortcuts", command=run_record_help)
btn_support = ttk.Button(btn_frame, text="Support", command=support_file)
btn_root_link = ttk.Button(btn_frame, text="Contribute?", command=github_link)


btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_run.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_record_help.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
btn_help.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
btn_sample.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
btn_support.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
btn_root_link.grid(row=7, column=0, sticky="ew", padx=5, pady=5)

btn_frame.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

# BindKeys
window.bind("<Alt_L>1", run_record_mouse)
window.bind("<Alt_L>2", run_record_copy)
window.bind("<Alt_L>3", run_record_paste)
window.bind("<Alt_L>4", run_record_enter)
window.bind("<Alt_L>5", run_record_write)
window.bind("<Alt_L>6", run_record_doubleclick)
window.bind("<Alt_L>7", run_record_clickpress)
window.bind("<Alt_L>8", run_record_clickrelease)
window.bind("<Alt_L>9", run_record_sleep5sec)
window.bind("<Alt_L>0", run_record_sleep30sec)
window.bind("<Alt_R>0", run_record_delete)
window.bind("<Alt_R>9", run_record_loop1)
window.bind("<Alt_R>8", run_record_loop8)

window.mainloop()
