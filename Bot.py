import pyautogui
import time
import keyboard
import win32api, win32con


# Get  the position of the Tiles by hovering the Mouse.
# This is achieved by import pyautogui and running pyautogui.displayMousePosition()
# This will give the Tile coordinates and the colour (RGB)

# Tile 1 Position: X: 291 Y:565 RGB: (87, 89, 117)
# Tile 2 Position: X: 421 Y:565 RGB: (83, 85, 117)
# Tile 3 Position: X: 534 Y:565 RGB: (79, 82, 117)
# Tile 4 Position: X: 645 Y:565 RGB: (80, 83, 117)

# May be different depending on the position of your game on your screen


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while not keyboard.is_pressed('q'):

    if pyautogui.pixel(291, 565)[0] == 0:
        click(291, 565)
    if pyautogui.pixel(421, 565)[0] == 0:
        click(421, 565)
    if pyautogui.pixel(534, 565)[0] == 0:
        click(534, 565)
    if pyautogui.pixel(645, 565)[0] == 0:
        click(645, 565)
