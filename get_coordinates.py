import pyautogui
screenWidth, screenHeight = pyautogui.size()
print(f"Screen width: {screenWidth}, Screen height: {screenHeight}")

currentMouseX, currentMouseY = pyautogui.position() 
print("Move your mouse to the desired location and press Ctrl+C to get the coordinates.")
try:
    while True:
        x, y = pyautogui.position()
        print(f"Current Position: X: {x}, Y: {y}", end='\r')
except KeyboardInterrupt:
    print("\nScript terminated.")
