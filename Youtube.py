import pyautogui
import time
time.sleep(2)
# print(pyautogui.position())

channel_name = pyautogui.prompt(text="",title="Enter the channel name")
print(channel_name)
# Opens new tab
pyautogui.hotkey("ctrl","t")

# Search youtube
pyautogui.write("https://www.youtube.com")
pyautogui.hotkey("enter")
