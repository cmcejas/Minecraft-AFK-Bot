import time
import pydirectinput

while True:
  time.sleep(1800)
  pydirectinput.keyDown('e')
  time.sleep(5)
  pydirectinput.keyUp('e')
