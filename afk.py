import time
import pyautogui

while True:
  time.sleep(1800)
  pyautogui.keyDown('e')
  time.sleep(5)
  pyautogui.keyUp('e')
