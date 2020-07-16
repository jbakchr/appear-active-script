import time
import random
import pyautogui

# Get screen height and width
screenWidth, screenHeight = pyautogui.size()
print("screen width and height:", screenWidth, screenHeight)

# Get mouse position
mouseX, mouseY = pyautogui.position()
print("Intial mouse X and Y:", mouseX, mouseY)

while True:
    # Sleep
    time.sleep(0.2)

    # Get mouse position again
    presentMouseX, presentMouseY = pyautogui.position()
    print("present X and Y:", presentMouseX, presentMouseY)

    # Check if present mouse position is the same as the initial one
    if mouseX == presentMouseX and mouseY == presentMouseY:

        # Get random X and Y
        randomX = random.randrange(0, screenWidth)
        randomY = random.randrange(0, screenHeight)

        # Move mouse
        pyautogui.moveTo(randomX, randomY, 0.5)

        # update mouseX and mouseY
        mouseX, mouseY = pyautogui.position()
