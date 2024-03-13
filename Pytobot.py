import os
import time
import tkinter as tk
import tkinter.ttk as ttk
import webbrowser
from datetime import datetime
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import scrolledtext

from tkinter import PhotoImage
from constants import logo, startup_message

import cv2
import pyautogui
import pynput.keyboard as kb
import pynput.mouse as ms
import json
import threading

from pytobot_scripts.start_up_script import create_local_folders
from pytobot_scripts.take_sc_box import take_sc_box
from pytobot_scripts.request_message_from_website import request_message_from_website
from pytobot_scripts.help_file import help_file
from pytobot_scripts.constants_pytobot import keyboard_mapping
from pytobot_scripts.recording_popup import show_recording_popup

from code_comp_ex.code_compilation import code_compilation


def on_press(key: kb.Key) -> None:
    txt_edit.yview_moveto(1.0)
    window.update_idletasks()
    txt_edit_previous_line = str(txt_edit.get("end - 2 lines", "end - 1 lines"))
    try:
        if hasattr(key, "name"):
            if key.name == "shift":
                return
        if "KeyboardWrite" in txt_edit_previous_line:
            txt_edit.delete("end - 2 lines", "end - 1 lines")
            if hasattr(key, "name"):
                if key.name == "space" and txt_edit_previous_line[-2:] == '")':
                    new_text = txt_edit_previous_line[:-2] + " " + '")' + "\n"
                    txt_edit.insert("end", new_text)
                elif key.name == "space" and txt_edit_previous_line[-3:] == '")\n':
                    new_text = txt_edit_previous_line[:-3] + " " + '")' + "\n"
                    txt_edit.insert("end", new_text)
                else:
                    pytobot_key = keyboard_mapping.get(key.name.lower())
                    if pytobot_key is not None:
                        new_text = txt_edit_previous_line + pytobot_key + "\n"
                        txt_edit.insert("end", new_text)
            elif txt_edit_previous_line[-2:] == '")':
                txt_edit_previous_line = txt_edit_previous_line[:-2]
                txt_edit.insert(
                    "end", txt_edit_previous_line + str(key.char) + '")' + "\n"
                )
            elif txt_edit_previous_line[-3:] == '")\n':
                txt_edit_previous_line = txt_edit_previous_line[:-3]
                txt_edit.insert(
                    "end", txt_edit_previous_line + str(key.char) + '")' + "\n"
                )

            else:
                new_text = txt_edit_previous_line + str(key.char) + '")' + "\n"
                txt_edit.insert("end", new_text)
        else:
            if hasattr(key, "name"):
                if key.name == "space":
                    txt_edit.insert("end", 'KeyboardWrite(" ")' + "\n")
                elif key.name == "print_screen":
                    txt_edit.insert("end", ("TakeScreenshot" + "\n"))
                else:
                    pytobot_key = keyboard_mapping.get(key.name.lower())
                    if pytobot_key is not None:
                        txt_edit.insert("end", pytobot_key + "\n")
            elif ord(key.char) == 19:
                txt_edit.insert("end", 'KeyboardWrite("s")' + "\n")
            elif ord(key.char) == 1:
                txt_edit.insert("end", 'KeyboardWrite("a")' + "\n")
            elif ord(key.char) == 3:
                txt_edit.delete("end - 2 lines", "end - 1 lines")
                txt_edit.insert("end", "Copy" + "\n")
            elif ord(key.char) == 22:
                txt_edit.delete("end - 2 lines", "end - 1 lines")
                txt_edit.insert("end", "Paste" + "\n")
            elif ord(key.char) == 26:
                txt_edit.insert("end", 'KeyboardWrite("z")' + "\n")
            elif ord(key.char) == 24:
                txt_edit.delete("end - 2 lines", "end - 1 lines")
                txt_edit.insert("end", "Cut" + "\n")
            else:
                txt_edit.insert("end", 'KeyboardWrite("' + str(key.char) + '")' + "\n")

    except AttributeError:
        txt_edit.insert("end", str(key.name) + '")' + "\n")

    last_command_label.config(font=("Nunito", 12))
    last_command_label.config(text=txt_edit.get("end - 2 lines", "end - 1 lines"))


def on_release(key: kb.Key) -> bool:
    global kb_listener, ms_listener
    txt_edit.yview_moveto(1.0)
    window.update_idletasks()
    if hasattr(key, "name"):
        previous_line = txt_edit.get("end - 2 lines", "end - 1 lines")
        previous_line2 = txt_edit.get("end - 3 lines", "end - 2 lines")
        if (
            "KeyboardCmdHold" in previous_line2
            and 'KeyboardWrite("v")' in previous_line
        ):
            txt_edit.delete("end - 3 lines", "end - 1 lines")
            txt_edit.insert("end", "Paste" + "\n")
        elif (
            "KeyboardCmdHold" in previous_line2
            and 'KeyboardWrite("x")' in previous_line
        ):
            txt_edit.delete("end - 3 lines", "end - 1 lines")
            txt_edit.insert("end", "Cut" + "\n")
        elif (
            "KeyboardCmdHold" in previous_line2
            and 'KeyboardWrite("c")' in previous_line
        ):
            txt_edit.delete("end - 3 lines", "end - 1 lines")
            txt_edit.insert("end", "Copy" + "\n")
        elif key.name == "ctrl_l" or key.name == "ctrl_r":
            if (
                "Paste" not in previous_line
                and "Cut" not in previous_line
                and "Copy" not in previous_line
            ):
                txt_edit.insert("end", "KeyboardCmdRelease" + "\n")

    last_command_label.config(font=("Nunito", 12))
    last_command_label.config(text=txt_edit.get("end - 2 lines", "end - 1 lines"))

    if key == kb.Key.esc:
        kb_listener.stop()
        ms_listener.stop()
        global window_recording_popup
        window_recording_popup.destroy()
        window.state("normal")
        window.focus_force()
        info_label_var_function("Recording stopped.")
        return False


def on_click(x: str, y: str, button: object, pressed: bool) -> None:
    txt_edit.yview_moveto(1.0)
    window.update_idletasks()
    if pressed:
        global click_timer, click_timer_previous
        click_timer_previous = click_timer
        click_timer = time.time()
        milliseconds_passed = int((click_timer - click_timer_previous) * 1000)
        txt_edit_previous_line = txt_edit.get("end - 2 lines", "end - 1 lines")
        if milliseconds_passed < 500 and "MouseClickLeft" in txt_edit_previous_line:
            txt_edit.delete("end - 2 lines", "end - 1 lines")
            txt_edit.insert("end", f"MouseDoubleClickLeft({x},{y})\n")
        elif button.name == "left":
            txt_edit.insert("end", f"MouseClickLeft({x},{y})\n")
        elif button.name == "right":
            txt_edit.insert("end", f"MouseClickRight({x},{y})\n")
    if not pressed:
        txt_edit_previous_line = txt_edit.get("end - 2 lines", "end - 1 lines")
        if (
            str(x) in txt_edit_previous_line
            and str(y) in txt_edit_previous_line
            and button.name == "left"
        ):
            pass
        elif (
            "MouseClickLeft" in txt_edit_previous_line
            and str(x) not in txt_edit_previous_line
            and str(y) not in txt_edit_previous_line
            and button.name == "left"
        ):
            txt_edit.delete("end - 2 lines", "end - 1 lines")
            previous_x = int(txt_edit_previous_line.split("(")[1].split(",")[0].strip())
            previous_y = int(
                txt_edit_previous_line.split("(")[1].split(",")[1].split(")")[0].strip()
            )
            txt_edit.insert(
                "end", f"MouseClickDragLeft({previous_x},{previous_y} -> {x},{y})\n"
            )
        elif "MouseClickDragLeft" in txt_edit_previous_line:
            txt_edit.delete("end - 2 lines", "end - 1 lines")
            previous_x = int(
                txt_edit_previous_line.split("->")[0].split(",")[0].strip()
            )
            previous_y = int(
                txt_edit_previous_line.split("->")[0]
                .split(",")[1]
                .split(")")[0]
                .strip()
            )
            txt_edit.insert(
                "end", f"MouseClickDragLeft({previous_x},{previous_y} -> {x},{y})\n"
            )

    last_command_label.config(font=("Nunito", 12))
    last_command_label.config(text=txt_edit.get("end - 2 lines", "end - 1 lines"))


def on_scroll(x: str, y: str, dx: int, dy: int) -> None:
    txt_edit.yview_moveto(1.0)
    window.update_idletasks()
    txt_edit_previous_line = txt_edit.get("end - 2 lines", "end - 1 lines")
    if "scroll," in txt_edit_previous_line:
        scroll_number = int(txt_edit_previous_line.split(",")[1])
        if dy == 1:
            txt_edit.delete("end - 2 lines", "end - 1 lines")
            txt_edit.insert("end", f"MouseScroll({scroll_number + 120})\n")
        elif dy == -1:
            txt_edit.delete("end - 2 lines", "end - 1 lines")
            txt_edit.insert("end", f"MouseScroll({scroll_number - 120})\n")
    else:
        txt_edit.insert("end", f"MouseScroll({dy * 120})\n")


def record_keyboard() -> None:
    global kb_listener, ms_listener
    kb_listener = kb.Listener(on_press=on_press, on_release=on_release)
    ms_listener = ms.Listener(on_click=on_click, on_scroll=on_scroll)
    ms_listener.start()
    kb_listener.start()


def keylogger_main() -> None:
    info_label_var_function("Recording... Press ESC to stop.")
    global window_recording_popup, last_command_label
    window_recording_popup, last_command_label = show_recording_popup(window)
    window.state("iconic")
    record_keyboard()
    window.lift()


def callback(url: str) -> None:
    webbrowser.open_new(url)


def open_file() -> None:
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


def save_file() -> None:
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


def run_record_mouse(self: object) -> None:
    currentMouseX, currentMouseY = pyautogui.position()
    txt_edit.insert(
        tk.END,
        "MouseClickLeft(" + str(currentMouseX) + "," + str(currentMouseY) + ")\n",
    )


def run_sample() -> None:
    text_insert = txt_edit.get(1.0, tk.END)
    if len(text_insert) > 1:
        text_insert = text_insert.split("\n")
        new_text = []
        for text in text_insert:
            text = "# " + text + "\n"
            new_text.append(text)

        new_text = "".join(new_text)
        txt_edit.delete(1.0, tk.END)
        txt_edit.insert(tk.END, new_text + "\n")

    text = '#Sample Comment:\nKeyboardCmd\nKeyboardWrite("browser")\nKeyboardEnter\nSleep(3)\nKeyboardWrite("Tell me a fun fact")\nKeyboardEnter'
    txt_edit.insert(tk.END, text)


def help_file_btn_func() -> None:
    help_file(window)


def capture() -> None:
    image = take_sc_box()
    now = datetime.now()
    filename = asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
        initialdir=os.path.join(os.path.expanduser("~"), "Pictures/pytobot"),
        initialfile="pytobot-{}.png".format(now.strftime("%Y-%m-%d %H-%M-%S")),
    )
    if filename is not None:
        cv2.imwrite(filename, image)


def run_record() -> None:
    keylogger_main()


def generic_popup(message, link=None) -> None:
    popup_window = tk.Toplevel()
    popup_window.title("Message")
    if len(message) <= 500:
        window_width = len(message) + 60
        window_height = len(message) + 90
    else:
        window_width = len(message) + 60
        window_height = len(message) + 90

    if window_width < 350:
        window_width = 350
    if window_height < 100:
        window_height = 100

    popup_window.geometry(f"{window_width}x{window_height}")
    popup_window.configure(background="white")
    popup_window.iconphoto(True, pytobot_logo)
    popup_window.attributes("-topmost", True)

    popup_window.update_idletasks()
    width = popup_window.winfo_width()
    height = popup_window.winfo_height()
    x = (popup_window.winfo_screenwidth() // 2) - (width // 2)
    y = (popup_window.winfo_screenheight() // 2) - (height // 2)
    popup_window.geometry("{}x{}+{}+{}".format(width, height, x, y))
    popup_window.grab_set()

    if link is None:
        message_label = tk.Label(
            popup_window, text=message, font=("Nunito", 12), bg="white"
        )
        message_label.pack(pady=10, padx=10)
        message_label.configure(wraplength=300)
    elif link is not None:
        text = tk.Text(popup_window, wrap="word", font=("Nunito", 12), bg="white")
        text.pack(pady=10, padx=10)
        text.insert(tk.END, message)
        text.configure(state="disabled")
        link_start = message.find(link)
        link_end = link_start + len(link)
        text.tag_add("link", f"1.{link_start}", f"1.{link_end}")
        text.tag_config("link", foreground="blue", underline=True)
        text.tag_bind("link", "<Button-1>", lambda e: callback("mailto:" + link))
        text.configure(height=window_height - 10, width=window_width - 10)

    button_frame = tk.Frame(popup_window)
    button_frame.pack(side=tk.BOTTOM, pady=5)

    ok_button = ttk.Button(
        button_frame,
        text="OK",
        command=lambda: on_close(),
    )

    ok_button.pack()

    def on_close():
        popup_window.grab_release()
        popup_window.destroy()
        window.focus_force()

    popup_window.protocol("WM_DELETE_WINDOW", on_close)


def open_about() -> None:
    generic_popup(
        "Hello! Thank you for checking out Pytobot! \
        Pytobot is a tool to automate all of your boring & repetitive tasks! \
        We would love to improve Pytobot, so please send your feedback to \
        pytobot@outlook.com\n\n\
        You are currently using Pytobot: 0.0.1 \
        ".replace(
            "        ", ""
        ),
        link=" pytobot@outlook.com",
    )


def info_label_var_function(message: str) -> None:
    info_label_var.set(message)
    window.update_idletasks()


def code_execution_prep(text: str) -> None:
    window.state("iconic")
    result = code_compilation(text)
    if result is not None:
        info_label_var_function(result)
    window.state("normal")
    window.lift()
    window.focus_force()


def pytobot():
    global click_timer
    click_timer = 0

    # start up
    create_local_folders()

    # Main Window
    global window
    window = tk.Tk()
    global pytobot_logo
    pytobot_logo = PhotoImage(data=logo)
    window.iconphoto(True, pytobot_logo)

    window.title("Pytobot")
    window.rowconfigure(1, minsize=100, weight=1)
    window.columnconfigure(1, minsize=400, weight=1)
    window.option_add("*Font", "Nunito")

    global txt_edit
    txt_edit = scrolledtext.ScrolledText(window, wrap="none")
    txt_edit.config(padx=5, pady=5)
    txt_edit.insert("end", startup_message)

    global info_label_var
    info_label_var = tk.StringVar(
        value="This is where you can see information about your code execution."
    )
    info_label = tk.Label(
        window,
        height=3,
        textvariable=info_label_var,
        font=("Nunito", 10),
        bg="white",
        fg="#333333",
        borderwidth=0.1,
        relief="flat",
        padx=5,
        pady=5,
        anchor="center",
    )
    window.tk_setPalette(background="white")

    style = ttk.Style()
    style.configure(
        "TButton",
        font=("Nunito", 10),
        background="white",
        anchor="center",
        padding=(5, 5, 5, 5),
        height=2,
        relief="flat",
    )

    # Buttons
    style = ttk.Style()
    style.configure("TFrame", background="white", borderwidth=0, relief="flat", padx=5)
    btn_frame = ttk.Frame(window, relief=tk.RIDGE, style="TFrame")
    btn_open = ttk.Button(
        btn_frame, text="Open", command=open_file, style="TButton", width=10
    )
    btn_save = ttk.Button(
        btn_frame, text="Save", command=save_file, style="TButton", width=10
    )
    btn_run = ttk.Button(
        btn_frame,
        text="Run",
        command=lambda: code_execution_prep(txt_edit.get(1.0, tk.END)),
        style="TButton",
        width=10,
    )
    btn_record = ttk.Button(
        btn_frame, text="Record", command=run_record, style="TButton", width=10
    )
    btn_capture = ttk.Button(
        btn_frame, text="Screenshot", command=capture, style="TButton", width=10
    )
    btn_help = ttk.Button(
        btn_frame, text="Help", command=help_file_btn_func, style="TButton", width=10
    )
    btn_sample = ttk.Button(
        btn_frame, text="Sample", command=run_sample, style="TButton", width=10
    )
    btn_about = ttk.Button(
        btn_frame, text="About", command=open_about, style="TButton", width=10
    )

    btn_open.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
    btn_save.grid(row=2, column=0, sticky="ew", padx=10, pady=5)
    btn_run.grid(row=3, column=0, sticky="ew", padx=10, pady=5)
    btn_record.grid(row=4, column=0, sticky="ew", padx=10, pady=5)
    btn_help.grid(row=5, column=0, sticky="ew", padx=10, pady=5)
    btn_sample.grid(row=6, column=0, sticky="ew", padx=10, pady=5)
    btn_capture.grid(row=7, column=0, sticky="ew", padx=10, pady=5)
    btn_about.grid(row=8, column=0, sticky="ew", padx=10, pady=5)

    info_label.grid(row=3, column=1, columnspan=2, sticky="w", padx=5, pady=5)
    btn_frame.grid(row=0, column=0, rowspan=4, sticky="ns")
    txt_edit.grid(row=0, column=1, sticky="nsew", rowspan=2)

    window.bind("<Alt_L>1", run_record_mouse)

    def get_message():
        response = request_message_from_website()
        if response.status_code == 200:
            response_text = response.text
            if len(response_text) > 3:
                message_text = response_text.replace("'", '"')
                message = json.loads(message_text)
                message = message["message"]
                if message != "":
                    if "pytobot@outlook.com" in message:
                        window.after(
                            10, lambda: generic_popup(message, "pytobot@outlook.com")
                        )
                    else:
                        window.after(10, lambda: generic_popup(message))

    message_thread = threading.Thread(target=get_message)
    message_thread.start()

    window.mainloop()


if __name__ == "__main__":
    pytobot()
