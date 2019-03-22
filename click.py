import pyautogui as mouse
import keyboard

print('Press \'o\' to start and \'p\' to stop or hold \'v\'')

on = False

while True:
	if keyboard.is_pressed('o'):
		on = True
	if keyboard.is_pressed('p'):
		on = False
	if on or keyboard.is_pressed('v'):
		mouse.click()