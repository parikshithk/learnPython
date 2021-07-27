import pyautogui as gui

width, height = gui.size()
print(width, height)
print(gui.position())

gui.moveTo(10, 10, duration=1.5)
gui.moveRel(200, 0, duration=2)
gui.rightClick()

gui.click(578, 575)
gui.typewrite('# Hello there!', interval=0.1)

gui.screenshot('screenshot.png')