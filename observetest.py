import pyautogui
import pyperclip
import time





pyautogui.hotkey('ctrl', '1')
pyautogui.hotkey('ctrl', 'alt','i') 

pyperclip.copy('@workspace /explain #terminalLastCommand')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

#print('observesuccess')
pyautogui.hotkey('ctrl', '1')


