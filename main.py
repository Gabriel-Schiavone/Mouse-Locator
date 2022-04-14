import pyautogui
import keyboard
import time

while True:
    if keyboard.is_pressed(' '):
        print("The mouse is at X:" + str(pyautogui.position().x) + " Y:" + str(pyautogui.position().y))
        time.sleep(.5)
