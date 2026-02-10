import time
import cv2

from capture import grab_frame
from detection import detect_fish_bite
from actions import reel_in
from config import FRAME_DELAY, COOLDOWN


print("Starting Minecraft fishing bot")
print("Make sure Minecraft is open, windowed and focused")
print("Press Q in debug window to quit")

time.sleep(2)

prev_frame = None
debug_counter = 0

while True:
    frame = grab_frame()

    if frame is None:
        print("Waiting for Minecraft window...")
        time.sleep(1)
        continue

    debug_counter += 1
    if debug_counter % 5 == 0:
        cv2.imshow("debug subtitle ROI", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    bite, text = detect_fish_bite(prev_frame, frame)

    if text:
        print("OCR:", text)

    if bite:
        print("got something !")
        reel_in()          
        time.sleep(0.4)
        reel_in()          
        time.sleep(COOLDOWN)

    prev_frame = frame
    time.sleep(FRAME_DELAY)

cv2.destroyAllWindows()
