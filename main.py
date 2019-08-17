from pyautogui import click
from keyboard import is_pressed

if __name__ == '__main__':
	print('Press \'o\' to start and \'p\' to stop or hold \'v\'\nPress \'[\' and \']\' at the same time to quit')

	on = False

	while True:
		if is_pressed('[') and is_pressed(']'):
			break
		if is_pressed('o'):
			on = True
		if is_pressed('p'):
			on = False
		if on or is_pressed('v'):
			click()