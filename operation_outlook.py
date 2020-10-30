import pyautogui

email = '9bensos@royalhospitalschool.org'
password = 'Olufunbi07'
print(pyautogui.size())

print(pyautogui.position())
pyautogui.moveTo(762,759,duration=0.1)
pyautogui.click()

pyautogui.moveTo(1046,48,duration=1)
pyautogui.click()

pyautogui.press('delete')
pyautogui.typewrite('outlook.com\n',interval=0.1)
pyautogui.moveTo(1120,131,duration=1.5)
pyautogui.click()

pyautogui.moveTo(599,364,duration=1.5)
pyautogui.click()
pyautogui.typewrite(email)

pyautogui.moveTo(793,526,duration=1)
pyautogui.click()

pyautogui.moveTo(599,364,duration=1.5)
pyautogui.click()
pyautogui.typewrite(password)
print(pyautogui.position())
