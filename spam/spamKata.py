import pyautogui, time

time.sleep(5)

x = "ini spam"

for i in range(5):
    pyautogui.typewrite(x)
    pyautogui.press("enter")