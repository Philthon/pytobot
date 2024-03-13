import cv2
import mss
import numpy as np
import pyautogui


def take_screenshot():
    screen_width, screen_height = pyautogui.size()
    monitor = {"top": 0, "left": 0, "width": screen_width, "height": screen_height}
    sct = mss.mss()
    screenshot = np.array(sct.grab(monitor))
    return screenshot


def crop_image(img, x1, y1, x2, y2):
    cropped_img = img[y1:y2, x1:x2]
    return cropped_img


def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, mode, img, base_img, cropped_img

    if event == cv2.EVENT_LBUTTONDOWN:
        global drawing
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing is True:
            img = base_img.copy()
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2, cv2.LINE_AA)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
        global cropped_img
        cropped_img = crop_image(base_img, ix, iy, x, y)
        cv2.destroyAllWindows()
        global cv2_window
        cv2_window = False


def take_sc_box():
    global base_img, img, cv2_window
    base_img = take_screenshot()
    img = base_img.copy()
    cv2.namedWindow("image", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.setMouseCallback("image", draw_rectangle)
    cv2_window = True
    while cv2_window is True:
        cv2.imshow("image", img)
        if (
            cv2.waitKey(20) & 0xFF == 27
            or cv2.getWindowProperty("image", cv2.WND_PROP_VISIBLE) < 1
        ):
            break
    cv2.destroyAllWindows()
    return cropped_img
