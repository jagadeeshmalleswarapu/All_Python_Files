import pyautogui
import time

# FAIL - SAFE 
pyautogui.FAILSAFE = False # If ts is true, it stops the execution when mouse will go to corner of the screen

get_text = open("./sample.txt")
time.sleep(5)
for i_text in get_text:
    pyautogui.write(i_text)
