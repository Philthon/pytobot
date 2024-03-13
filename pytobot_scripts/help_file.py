import tkinter as tk
from tkinter import scrolledtext
from tkinter import PhotoImage
from constants import logo


def help_file(window):
    new_window = tk.Toplevel(window)

    txt_edit = scrolledtext.ScrolledText(new_window, wrap="none")
    txt_edit.config(padx=5, pady=5, font="Nunito 11", undo=True, wrap="none")
    txt_edit.pack(fill="both", expand=True)
    new_window.title("Help File")
    pytobot_logo = PhotoImage(data=logo)
    new_window.iconphoto(False, pytobot_logo)
    new_window.resizable(True, True)
    window_width = 750
    window_height = 400
    new_window.geometry(f"{window_width}x{window_height}")

    screen_width = new_window.winfo_screenwidth()
    screen_height = new_window.winfo_screenheight()
    center_x = int((screen_width - window_width) / 2)
    center_y = int((screen_height - window_height) / 2)
    new_window.geometry(f"+{center_x}+{center_y}")

    txt_edit.tag_configure("bold", font=("Nunito", 12, "bold"))
    txt_edit.tag_configure("underline", font=("Nunito", 12, "underline"))
    txt_edit.tag_configure("header", font=("Nunito", 14, "bold"))

    txt_edit.insert(tk.INSERT, "Welcome to Pytobot!\n\n", "header")
    txt_edit.insert(tk.INSERT, "What is Pytobot?\n", "bold")
    txt_edit.insert(tk.INSERT, "Pytbot helps to automate your boring tasks!\n\n")
    txt_edit.insert(tk.INSERT, "What can I do with Pytbot?\n", "bold")
    txt_edit.insert(
        tk.INSERT,
        "You can can automate repetitive tasks by creating a script and running it.\n",
    )
    txt_edit.insert(tk.INSERT, "How do I use Pytobot?\n", "bold")

    txt_edit.insert(tk.INSERT, "You can use the following commands:\n\n")

    txt_edit.insert(tk.INSERT, "Syntax:\n", "bold")

    txt_edit.insert(tk.INSERT, "One command per line.\n\n")

    txt_edit.insert(tk.INSERT, "Mouse Commands:\n", "bold")
    text_string = """\
MouseClickLeft(500, 1000)
Left mouse click at screen coordinates (x, y)

MouseClickRight(500, 1000)
Right mouse click at screen coordinates (x, y)

MouseMove(500, 1000)
Move the mouse to screen coordinates (x, y)

MouseDoubleClickLeft(500, 500)
Double left click at screen coordinates (x, y)

MouseScroll(5)
Mouse scroll 5 digits up (positive) or down (negative)

MouseClickLeftHold
Click and hold the left mouse button

MouseClickLeftRelease
Click and release the left mouse button

MouseClickDragLeft(500, 1000 -> 600, 1100)
Click and drag the left mouse button to screen coordinates (x, y)

"""

    txt_edit.insert(tk.INSERT, text_string)

    txt_edit.insert(tk.INSERT, "Keyboard Commands:\n", "bold")
    text_string = """\
KeyboardEnter
Presses the Enter key

KeyboardTab
Presses the Tab key

KeyboardSpace
Presses the Space key

KeyboardBackspace
Presses the Backspace key

KeyboardDelete
Presses the Delete key

KeyboardArrowUp
Presses the up arrow key

KeyboardArrowDown
Presses the down arrow key

KeyboardArrowLeft
Presses the left arrow key

KeyboardArrowRight
Presses the right arrow key

KeyboardWrite("word or phrase")
Types the specified word or phrase

KeyboardCtrlHold
Holds down the Ctrl key

KeyboardCtrlRelease
Releases the Ctrl key

KeyboardCmd
Holds down the Cmd key (e.g., for switching apps)

"""
    txt_edit.insert(tk.INSERT, text_string)

    txt_edit.insert(tk.INSERT, "Copy and Paste Functions:\n", "bold")
    text_string = """\
Copy
Copy (same as Ctrl+C)

Paste("name")
Paste (same as Ctrl+V) by default the clipboard

Paste
Paste (same as Ctrl+V) by default the clipboard

Cut
Cut (same as Ctrl+X)

SelectAllAndCopy
Select all and copy (same as Ctrl+A and Ctrl+C)

"""
    txt_edit.insert(tk.INSERT, text_string)

    txt_edit.insert(tk.INSERT, "Program Functions:\n", "bold")
    text_string = """\
ProgramOpen("notepad")
Open a program (e.g., - - Notepad) Some programs may have different names
than displayed e.g. Affinity Designer is Designer

ProgramClose("notepad")
Close a program

ProgramActivate("notepad")
Activate a program

ProgramMinimize("notepad")
Minimize a program

ProgramMaximize("notepad")
Maximize a program

ProgramBringToFront("notepad")
Bring a program to the front

ExecutePytobotScript("sample.txt")
Execute another Pytobot script

"""
    txt_edit.insert(tk.INSERT, text_string)

    txt_edit.insert(tk.INSERT, "Other Functions:\n", "bold")
    text_string = """\
Sleep(5)
Wait for 5 seconds

TakeScreenshot
Take a screenshot and save it in Pictures\\Screenshots

ClickOnImage("C:\\path\\to\\image.png")
Click on an image on the screen e.g. an image of a button that you want to click on

"""
    txt_edit.insert(tk.INSERT, text_string)

    txt_edit.insert(tk.INSERT, "Variables:\n", "bold")
    text_string = """\
SetVariable(YourVariable = "value")
Set a variable

SetVariable(YourVariable = Clipboard())
Set a variable from the clipboard

"""
    txt_edit.insert(tk.INSERT, text_string)

    txt_edit.insert(tk.INSERT, "Available Comparison Operators:\n", "bold")
    text_string = """\
==  # Equal to
!=  # Not equal to
>   # Greater than
<   # Less than
>=  # Greater than or equal to
<=  # Less than or equal to

"""
    txt_edit.insert(tk.INSERT, text_string)

    txt_edit.insert(tk.INSERT, "Available Logical Operators:\n", "bold")
    text_string = """\
If(1 == 1) {
    # Do something
} ElseIf(age == 2) {
    # Do something else
} Else {
    # Do something else
}

Loop(5) {
    # Do something
}

"""
    txt_edit.insert(tk.INSERT, text_string)

    txt_edit.insert(tk.INSERT, "Comments:\n", "bold")
    text_string = """\
# Write a comment by using the hashtag symbol at the beginning of a line.

"""
    txt_edit.insert(tk.INSERT, text_string)

    txt_edit.insert(tk.INSERT, "Stopping the Pytobot execution:\n", "bold")
    text_string = """\
You can stop Pytobot by pressing the ESC key.

"""
    txt_edit.insert(tk.INSERT, text_string)

    txt_edit.insert(tk.INSERT, "Shortcuts:\n", "bold")
    text_string = """\
Pytobot has to be in the foreground to detect shortcuts.
ALT Left and 1 Prints click and mouse coordinates.
"""
    txt_edit.insert(tk.INSERT, text_string)

    txt_edit.configure(state="disabled")


if __name__ == "__main__":
    user_email = "testuser@email.com"
    window = tk.Tk()
    help_file(window)
    window.mainloop()
