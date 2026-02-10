import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

KEYWORDS = ["fishing", "bobber", "splash"]

def detect_fish_bite(prev_frame, frame):
    if frame is None:
        return False, ""

    img = cv2.resize(frame, None, fx=2, fy=2)
    img = cv2.GaussianBlur(img, (3, 3), 0)
    _, img = cv2.threshold(img, 160, 255, cv2.THRESH_BINARY)

    text = pytesseract.image_to_string(
        img,
        config="--psm 6 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    )

    text = text.lower().strip()

    if len(text) < 5:
        return False, ""

    if all(k in text for k in KEYWORDS):
        return True, text

    return False, text
