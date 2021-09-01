import time
import pyautogui

try:
    for i in range(1000):
        time.sleep(1)
        pyautogui.screenshot(f'screenshots/{i}.png')
except KeyboardInterrupt:
    pass
