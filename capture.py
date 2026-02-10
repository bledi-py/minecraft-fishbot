import mss
import numpy as np
import cv2

from config import ROI
from window import get_minecraft_window

sct = mss.mss()

def grab_frame():
    win = get_minecraft_window()
    if not win:
        return None

    monitor = {
        "left": win["left"] + ROI["left"],
        "top": win["top"] + ROI["top"],
        "width": ROI["width"],
        "height": ROI["height"]
    }

    img = np.array(sct.grab(monitor))
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
    return img
