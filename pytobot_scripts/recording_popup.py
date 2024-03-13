from tkinter import Label, PhotoImage, Toplevel
from constants import logo


def show_recording_popup(window):
    global window_recording_popup
    window_recording_popup = Toplevel(window)
    pytobot_logo = PhotoImage(data=logo)
    window_recording_popup.iconphoto(True, pytobot_logo)
    window_recording_popup.title("Recording...")
    window_recording_popup.attributes("-topmost", True)
    screen_width = window_recording_popup.winfo_screenwidth()
    screen_height = window_recording_popup.winfo_screenheight()
    window_recording_popup_width = 400
    window_recording_popup_height = 100
    screen_height = int(screen_height - window_recording_popup_height * 2)
    screen_width = int(screen_width - window_recording_popup_width * 1.1)
    window_recording_popup.geometry(
        f"{window_recording_popup_width}x{window_recording_popup_height}+{screen_width}+{screen_height}"
    )
    window_recording_popup.resizable(False, False)
    window_recording_popup.configure(background="white")

    last_command_label = Label(
        window_recording_popup, text="", font=("Nunito", 12, "bold"), background="white"
    )
    last_command_label.pack(pady=5)

    info_label = Label(
        window_recording_popup,
        text="Press ESC to Stop Recording",
        font=("Roboto", 10),
        background="white",
    )
    info_label.pack(pady=5)

    return window_recording_popup, last_command_label
