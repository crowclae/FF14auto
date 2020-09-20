import time
import pyautogui

pyautogui.moveTo(300,300)
time.sleep(2)
p1 = pyautogui.locateCenterOnScreen('test2.png',region=(1000, 600, 1000, 500),grayscale = True,confidence = 0.5)
print(p1)
print()
