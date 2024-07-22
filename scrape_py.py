import time
import pyautogui
from appscript import app, its

# Focus the Notion window
notion = app('Notion')
notion.activate()
print("Notion activated")

screenWith, screenHeight = pyautogui.size()
print(f"Screen width: {screenWith}, Screen height: {screenHeight}")

currentMouseX, currentMouseY = pyautogui.position() 

time.sleep(2)  # Wait for Notion to activate

# Verify the first click action
print("Moving to the first item in the list")
pyautogui.moveTo(90, 662)  
pyautogui.click()
time.sleep(2)  # Wait to observe the click

# Iterate over the items in the trash
for y in range (50):
    if y != 0:
        print("Refreshing the list")
        pyautogui.moveTo(90, 662)  
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)


    for i in range(5): 
        print(f"Eliminating element {i+1}")
        
        # Click on the first item in the list
        pyautogui.moveTo(678, 662)  
        pyautogui.click()
        time.sleep(0.5)

        # Confirm deletion
        print("Confirming elimination")
        pyautogui.moveTo(680, 565)  
        pyautogui.click()    
        time.sleep(1)  # Wait to observe the confirmation
        print(f"Element {i+1} eliminated")

print("Elimination completed.")
