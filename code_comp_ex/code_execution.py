from code_comp_ex.userApp import userApp

import time
from pynput import keyboard as kb
import os
from datetime import datetime
import pyautogui
from pynput.keyboard import Key

global curr_el
curr_el = ""


def on_release_run(key: kb.Key) -> bool:
    global run_stop_code_execution, curr_el
    if key == kb.Key.esc:
        if curr_el != "KeyboardEsc":
            run_stop_code_execution = True
            curr_el = "ESC"


def get_coordinates(curr_el) -> None:
    x = int(curr_el.split("(")[1].split(",")[0].strip())
    y = int(curr_el.split("(")[1].split(",")[1].split(")")[0].strip())
    return x, y


def code_execution(code_string: str) -> None:
    keyboard = kb.Controller()
    global run_stop_code_execution, curr_el
    run_stop_code_execution = False
    try:
        kb_listener_run = kb.Listener(on_release=on_release_run)
        kb_listener_run.start()
        time.sleep(0.5)
        automationlist = code_string.strip().split("\n")
        wait = 1
        for elem in automationlist:
            if run_stop_code_execution is True:
                break
            curr_el = str(elem).strip()

            if "Mouse" in curr_el:
                if "MouseClickLeft" in curr_el:
                    x, y = get_coordinates(curr_el)
                    pyautogui.click(x, y, button="left")
                    time.sleep(wait)
                elif "MouseClickRight" in curr_el:
                    x, y = get_coordinates(curr_el)
                    pyautogui.click(x, y, button="right")
                    time.sleep(wait)
                elif "MouseClickLeftHold" in curr_el:
                    x, y = get_coordinates(curr_el)
                    pyautogui.mouseDown(x, y, button="left")
                    time.sleep(wait)
                elif "MouseClickLeftRelease" in curr_el:
                    x, y = get_coordinates(curr_el)
                    pyautogui.mouseUp(x, y, button="left")
                    time.sleep(wait)
                elif "MouseDoubleClickLeft" in curr_el:
                    x, y = get_coordinates(curr_el)
                    pyautogui.doubleClick(x, y)
                    time.sleep(wait)
                elif "MouseClickDragLeft" in curr_el:
                    x1, y1 = get_coordinates(curr_el.split("->")[0])
                    x2 = int(curr_el.split("->")[1].split(",")[0].strip())
                    y2 = int(curr_el.split("->")[1].split(",")[1].split(")")[0].strip())
                    pyautogui.moveTo(x1, y1)
                    pyautogui.mouseDown(button="left")
                    pyautogui.moveTo(x2, y2)
                    pyautogui.mouseUp(button="left")
                    time.sleep(wait)
                elif "MouseMove" in curr_el:
                    x, y = get_coordinates(curr_el)
                    pyautogui.moveTo(x, y)
                    time.sleep(wait)
                elif "MouseScroll" in curr_el:
                    x = int(curr_el.split("(")[1].split(")")[0].strip())
                    pyautogui.scroll(x)
                    time.sleep(wait)

            elif "Keyboard" in curr_el:
                if "KeyboardWrite" in curr_el:
                    text = curr_el.split("(")[1].split(")")[0].strip().replace('"', "")

                    start_time = time.time()
                    pyautogui.typewrite(text, interval=0.1)
                    end_time = time.time()
                    typing_duration = end_time - start_time
                    time.sleep(typing_duration)
                    time.sleep(wait)
                elif curr_el == "KeyboardEnter":
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    time.sleep(wait)
                elif curr_el == "KeyboardTab":
                    keyboard.press(Key.tab)
                    keyboard.release(Key.tab)
                    time.sleep(wait)
                elif curr_el == "KeyboardSpace":
                    keyboard.press(Key.space)
                    keyboard.release(Key.space)
                    time.sleep(wait)
                elif curr_el == "KeyboardBackspace":
                    keyboard.press(Key.backspace)
                    keyboard.release(Key.backspace)
                    time.sleep(wait)
                elif curr_el == "KeyboardDelete":
                    keyboard.press(Key.delete)
                    keyboard.release(Key.delete)
                    time.sleep(wait)
                elif curr_el == "KeyboardArrowUp":
                    keyboard.press(Key.up)
                    keyboard.release(Key.up)
                    time.sleep(wait)
                elif curr_el == "KeyboardArrowDown":
                    keyboard.press(Key.down)
                    keyboard.release(Key.down)
                    time.sleep(wait)
                elif curr_el == "KeyboardArrowLeft":
                    keyboard.press(Key.left)
                    keyboard.release(Key.left)
                    time.sleep(wait)
                elif curr_el == "KeyboardArrowRight":
                    keyboard.press(Key.right)
                    keyboard.release(Key.right)
                    time.sleep(wait)
                elif curr_el == "KeyboardCtrlHold":
                    keyboard.press(Key.ctrl)
                    time.sleep(wait)
                elif curr_el == "KeyboardCtrlRelease":
                    keyboard.release(Key.ctrl)
                    time.sleep(wait)
                elif curr_el == "KeyboardCmd":
                    keyboard.press(Key.cmd)
                    keyboard.release(Key.cmd)
                    time.sleep(wait)
                elif curr_el == "KeyboardEsc":
                    keyboard.press(Key.esc)
                    keyboard.release(Key.esc)
                    time.sleep(wait)

            else:
                if "Sleep" in curr_el:
                    x = int(curr_el.split("(")[1].split(")")[0].strip())
                    for i in range(x):
                        time.sleep(0.4)
                        if run_stop_code_execution is True:
                            break
                        time.sleep(0.3)
                        if run_stop_code_execution is True:
                            break
                        time.sleep(0.3)
                        if run_stop_code_execution is True:
                            break
                elif "Copy" in curr_el:
                    keyboard.press(Key.ctrl)
                    keyboard.press("c")
                    keyboard.release("c")
                    keyboard.release(Key.ctrl)
                    time.sleep(wait)
                elif curr_el == "Paste":
                    keyboard.press(Key.ctrl)
                    keyboard.press("v")
                    keyboard.release("v")
                    keyboard.release(Key.ctrl)
                    time.sleep(wait)
                elif 'Paste("' in curr_el:
                    curr_el = curr_el.split("(")[1].split(")")[0].strip()
                    curr_el = curr_el.replace('"', "")
                    keyboard.type(curr_el)
                    time.sleep(wait)
                elif curr_el == "Cut":
                    keyboard.press(Key.ctrl)
                    keyboard.press("x")
                    keyboard.release("x")
                    keyboard.release(Key.ctrl)
                    time.sleep(wait)
                elif curr_el == "SelectAllAndCopy":
                    keyboard.press(Key.ctrl)
                    keyboard.press("a")
                    keyboard.release("a")
                    keyboard.press("c")
                    keyboard.release("c")
                    keyboard.release(Key.ctrl)
                    time.sleep(wait)
                elif "ClickOnImage" in curr_el:
                    curr_el_path = (
                        curr_el.split("(")[1].split(")")[0].strip().replace('"', "")
                    )
                    i = 10
                    while i > 7:
                        if pyautogui.locateCenterOnScreen(
                            curr_el_path, confidence=i / 10
                        ):
                            pyautogui.click(
                                pyautogui.locateCenterOnScreen(
                                    curr_el_path, confidence=i / 10
                                )
                            )
                            break
                        else:
                            i -= 1
                            continue

                    time.sleep(wait)
                elif curr_el == "TakeScreenshot":
                    if not os.path.exists(
                        os.path.join(
                            os.path.join(os.environ["USERPROFILE"]),
                            "Pictures\\Screenshots",
                        )
                    ):
                        os.makedirs(
                            os.path.join(
                                os.path.join(os.environ["USERPROFILE"]),
                                "Pictures\\Screenshots",
                            )
                        )
                    now = datetime.now()
                    pyautogui.screenshot(
                        os.path.join(
                            os.path.join(os.environ["USERPROFILE"]),
                            "Pictures\\Screenshots",
                        )
                        + "\\pytobot - {}.png".format(now.strftime("%d-%m-%Y %H-%M-%S"))
                    )
                elif "ProgramOpen" in curr_el:
                    curr_el_path = (
                        curr_el.split("(")[1].split(")")[0].strip().replace('"', "")
                    )
                    app = userApp(curr_el_path)
                    app.start()
                    time.sleep(wait)
                elif "ProgramClose" in curr_el:
                    curr_el_path = curr_el.split('("')[1].split('")')[0].strip()
                    app = userApp(curr_el_path)
                    app.close()
                    time.sleep(wait)
                elif "ProgramMinimize" in curr_el:
                    curr_el_path = curr_el.split("(")[1].split(")")[0].strip()
                    app = userApp(curr_el_path)
                    app.minimize()
                    time.sleep(wait)
                elif "ProgramMaximize" in curr_el:
                    curr_el_path = curr_el.split("(")[1].split(")")[0].strip()
                    app = userApp(curr_el_path)
                    app.maximize()
                    time.sleep(wait)
                elif "ProgramBringToFront" in curr_el:
                    curr_el_path = curr_el.split("(")[1].split(")")[0].strip()
                    app = userApp(curr_el_path)
                    app.bring_window_to_front()
                    time.sleep(wait)

        kb_listener_run.stop()
        return run_stop_code_execution

    except Exception as e:
        kb_listener_run.stop()
        return f"{str(e)}"
