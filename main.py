import time
import pyautogui
import pydirectinput

try:
    while True:
        if pyautogui.locateOnScreen('images/1.png', confidence=0.9) is not None:
            pydirectinput.press('down')
            pydirectinput.press('down')
            pydirectinput.press('down')
            pydirectinput.press('enter')
            time.sleep(2)
            
            pydirectinput.press('down')
            pydirectinput.press('right')
            pydirectinput.press('right')
            pydirectinput.press('right')
            pydirectinput.press('right')
            pydirectinput.press('enter')
            time.sleep(2)

            pydirectinput.press('enter')
        if pyautogui.locateOnScreen('images/2.png', confidence=0.9) is not None:
            time.sleep(2)
            pydirectinput.press('enter')
except KeyboardInterrupt:
    pass
