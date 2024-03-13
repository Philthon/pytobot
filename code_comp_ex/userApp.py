import os
import subprocess
import time

import pyautogui
import pygetwindow


def find_in_directory(partial_name, directory):
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if all(word.lower() in file.lower() for word in partial_name.split()):
                    return os.path.join(root, file)
    except Exception as e:
        print(f"Error while searching in {directory}: {e}")


def get_path(program_name, file_type=None):
    if not program_name.endswith(".exe"):
        program_name += ".exe"

    common_directories = [
        r"C:\Program Files",
        r"C:\Program Files (x86)",
        r"C:\ProgramData",
        r"C:\Windows\System32",
        r"C:\Program Files\WindowsApps",
    ]

    for directory in common_directories:
        file_path = find_in_directory(program_name, directory)
        if file_path:
            return file_path

    for path in os.environ["PATH"].split(os.pathsep):
        file_path = os.path.join(path, program_name)
        if os.path.isfile(file_path):
            return file_path

    return None


class userApp:
    def __init__(self, name, window_number=0, image=None, file_type=None):
        self.name = name
        file_path = get_path(name)
        if file_path:
            self.path = file_path
        else:
            raise FileNotFoundError(f"Could not find {name}.")
        self.window_number = window_number
        self.image = image
        self.file_type = file_type

    def start(self):
        try:
            os.startfile(self.path)
            time.sleep(2)
        except FileNotFoundError:
            return f"Could not start {self.name}."

    def close(self):
        try:
            path_close = self.path
            path_close = path_close.split("\\")[-1]
            subprocess.run(["taskkill", "/IM", path_close, "/F"], check=True)
            return
        except Exception:
            print(f"Could not close {self.name}.")
        try:
            windows = pygetwindow.getWindowsWithTitle(self.name)
            windows.pop(self.window_number).close()
            return
        except Exception:
            return f"Could not close {self.name}."

    def maximize(self, window_number=0):
        try:
            windows = pygetwindow.getWindowsWithTitle(self.name)

            if windows:
                window = windows[window_number]
                window.maximize()
            else:
                print("No Notepad windows found.")
        except FileNotFoundError:
            return f"Could not maximize {self.name}."

    def minimize(self, window_number=0):
        try:
            windows = pygetwindow.getWindowsWithTitle(self.name)

            if windows:
                window = windows[window_number]
                window.minimize()
            else:
                print("No Notepad windows found.")
        except FileNotFoundError:
            return f"Could not minimize {self.name}."

    def click_image(self, image):
        try:
            pyautogui.click(pyautogui.center(pyautogui.locateOnScreen(image)))
        except FileNotFoundError:
            return "Could not find image."

    def bring_window_to_front(self):
        try:
            window = pygetwindow.getWindowsWithTitle(self.name)
            if window:
                window[0].minimize()
                time.sleep(0.1)
                window[0].restore()
                window[0].activate()
        except FileNotFoundError:
            return f"Could not bring {self.name} to front."
