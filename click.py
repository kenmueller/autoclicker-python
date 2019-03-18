import pyautogui as mouse
import keyboard

print('Press \'o\' to start and \'p\' to stop')

on = False

while True:
	if keyboard.is_pressed('o'):
		on = True
	if keyboard.is_pressed('p'):
		on = False
	if on:
		mouse.click()