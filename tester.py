import time
import pyautogui

pyautogui.moveTo(300,300)
time.sleep(2)
p1 = pyautogui.locateCenterOnScreen('test1.png',grayscale = True,region=(1980, 34, 1000, 700))
print(p1)
print()
