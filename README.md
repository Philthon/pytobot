# Welcome to Pytobot!

Pytobot is a Python-based automation tool that allows you to automate tasks on your computer. You can use Pytobot to automate repetitive tasks, such as opening programs, typing, clicking, and more. Pytobot is easy to use and requires no programming knowledge (once installed).

# Installation:
- Download and install Pytobot from [Pytobot's website](https://pytobot-website.vercel.app/).
- Clone GitHub repository and run `pip install -r requirements.txt` in the terminal.
- Run Pytobot.py

# Syntax:
One command per line. Sample code at the end. You can use the following operators:

# Mouse Commands:
- MouseClickLeft(500, 1000)                   # Left mouse click at screen coordinates (x, y)
- MouseClickRight(500, 1000)                  # Right mouse click at screen coordinates (x, y)
- MouseMove(500, 1000)                        # Move the mouse to screen coordinates (x, y)
- MouseDoubleClickLeft(500, 500)              # Double left click
- MouseScroll(5)                              # Mouse scroll 5 digits up (positive) or down (negative)
- MouseClickLeftHold                          # Click and hold the left mouse button
- MouseClickLeftRelease                       # Click and release the left mouse button
- MouseClickDragLeft(500, 1000 -> 600, 1100)  # Click and drag the left mouse button to screen coordinates (x, y)

# Keyboard Commands:
- KeyboardEnter                               # Press the Enter key
- KeyboardTab                                 # Press the Tab key
- KeyboardSpace                               # Press the Space key
- KeyboardBackspace                           # Press the Backspace key
- KeyboardDelete                              # Press the Delete key
- KeyboardArrowUp                             # Press the up arrow key
- KeyboardArrowDown                           # Press the down arrow key
- KeyboardArrowLeft                           # Press the left arrow key
- KeyboardArrowRight                          # Press the right arrow key
- KeyboardWrite("word or phrase")             # Type the specified word or phrase
- KeyboardCtrlHold                            # Hold down the Ctrl key
- KeyboardCtrlRelease                         # Release the Ctrl key
- KeyboardCmd                                 # Press the CMD key (e.g., for switching apps)

# Copy and Paste Functions:
- Copy                                        # Copy (same as Ctrl+C)
- Paste("name")                               # Paste the quoted text
- Paste                                       # Paste (same as Ctrl+V) by default the clipboard
- Cut                                         # Cut (same as Ctrl+X)
- SelectAllAndCopy                            # Select all and copy (same as Ctrl+A and Ctrl+C)


# Program Functions:
- ProgramOpen("notepad")                      # Open a program (e.g., - - Notepad) Some programs may have different names than displayed in the taskbar e.g. Affinity Designer is Designer
- ProgramClose("notepad")                     # Close a program
- ProgramActivate("notepad")                  # Activate a program
- ProgramMinimize("notepad")                  # Minimize a program
- ProgramMaximize("notepad")                  # Maximize a program
- ProgramBringToFront("notepad")              # Bring a program to the front
- ExecutePytobotScript("sample.txt")          # Execute another Pytobot script

# Other Functions:
- Sleep(5)                                    # Wait for 5 seconds
- TakeScreenshot                              # Take a screenshot and save it in Pictures\\Screenshots
- ClickOnImage("C:\\path\\to\\image.png")     # Click on an image on the screen e.g. an image of a button that you want to click on

# Variables:
- SetVariable(YourVariable = "value")         # Set a variable
- SetVariable(YourVariable = Clipboard())     # Set a variable from the clipboard

# Logical Statements:

# Available Comparison Operators:
- ==  # Equal to
- !=  # Not equal to
- \>   # Greater than
- <   # Less than
- \>=  # Greater than or equal to
- <=  # Less than or equal to

- If(1 == 1) {
    \# Do something
} ElseIf(age == 2) {
    \# Do something else
} Else {
    \# Do something else
}   \# Else statement

- Loop(5) {
    \# Do something
}   \# Loop statement

# Comments:
\# This is how you can write a comment.

# Stopping the Pytobot execution:
- You can stop Pytobot by pressing the ESC key.

# Shortcuts:
- Pytobot has to be in the foreground to detect shortcuts.

- ALT Left and 1 Prints click and mouse coordinates

# Sample Script:
\#Sample Comment  
KeyboardCmd  
KeyboardWrite("edge")  
KeyboardEnter  
KeyboardWrite("Tell me a fun fact")  
KeyboardEnter  
