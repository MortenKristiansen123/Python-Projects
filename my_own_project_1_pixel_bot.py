# pixel_bot, in this case its for humanbenchmark.com

import pyautogui
import random
import time

# the point x=1545, y=385 is a point on the screen in humanbenchmark.com that is clickable
# I found out where that was by using the pyautogui module and the function pyautogui.position() by holding my cursor over the point I wanted to click
# and then running the function in the terminal. It returned the coordinates of the point I was hovering over.
# Then i used the print(pyautogui.pixel(1545, 385)) to see what color it was, which was (75, 219, 106) ~ green

# version 1 - no delay
# while True:
#   if (pyautogui.pixel(1545, 385)) == (75, 219, 106):
#      pyautogui.click()
#     break  # MAKE SURE HAVE THE BREAK STATEMENT TABBED FAR OUT ENOUGH TO BE OUTSIDE THE IF STATEMENT
# I added a break statement to stop the loop after one click, so it doesn't keep clicking in an infinite loop.

# version 2 - with randomized delay
while True:
    if pyautogui.pixel(1545, 385) == (75, 219, 106):
        # Random delay between 0.5 and 2 seconds
        delay = random.uniform(0.13, 0.17)
        time.sleep(delay)
        pyautogui.click()
        break  # MAKE SURE HAVE THE BREAK STATEMENT TABBED FAR OUT ENOUGH TO BE OUTSIDE THE IF STATEMENT
    # I added a break statement to stop the loop after one click, so it doesn't keep clicking in an infinite loop.
