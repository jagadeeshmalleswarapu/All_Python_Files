import pyautogui

pyautogui.alert("Hiiiiiiiiiii")
res = pyautogui.locateOnScreen("D:\locateOnScreen1.png")
print(res)
print(pyautogui.center(res))

centerCor = pyautogui.center(res)

pyautogui.moveTo(centerCor)

# res2 = pyautogui.locateCenterOnScreen("D:\locateOnScreen2.png",confidence=0.9) #To use confidence we need to install
#pip install opencv-python
# print("Res2",res2)

