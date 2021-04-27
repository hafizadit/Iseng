import pyautogui, time

time.sleep(5)

baca = open("lirik.txt","r")

for i in baca:
    pyautogui.typewrite(i)
    pyautogui.press("enter")