#! python3
from PIL import Image
import pyautogui
import sys
import time
import webbrowser
from functions import getClip6digit, getMail, randomize


# open Proton e-mail
webbrowser.open('https://account.proton.me/signup?plan=free')
time.sleep(5)

# user
_username_=randomize('-s',5)+randomize('-s',5)+randomize('-s',5)
pyautogui.typewrite(_username_ + '\t\t')
print("Username:" + _username_)

# pass
_password_=randomize('-p',16)
pyautogui.typewrite(_password_+'\t'+_password_+'\t')
print("Password:" + _password_)

# repeat pass
pyautogui.typewrite(_password_ + '\t')
time.sleep(3)

pyautogui.typewrite('\n')
time.sleep(3)
pyautogui.typewrite('\t\t\t\n')

# new window
pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('t'); pyautogui.keyUp('ctrlleft')
time.sleep(2)

# open the fake mail gen w/s
pyautogui.typewrite('https://dropmail.me/\n')

# copy mail from w/s
time.sleep(5)
newMail = True
while True:
    if not newMail:
        pyautogui.keyDown('ctrlleft'); pyautogui.typewrite('r'); pyautogui.keyUp('ctrlleft')
        time.sleep(2)
    pyautogui.typewrite('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t')
    pyautogui.click()  # being with laptop, I added left mouse click func for now. btw, coordinants script of Email can be found and cliked
    time.sleep(2)
    # pyautogui.keyDown('ctrlleft')
    # pyautogui.keyDown('shiftleft')
    # pyautogui.keyDown('shiftright')
    # pyautogui.press('down')
    # pyautogui.keyUp('shiftleft')
    # pyautogui.keyUp('shiftright')
    # pyautogui.keyUp('ctrlleft')
    pyautogui.keyDown('ctrlleft'); pyautogui.typewrite('c'); pyautogui.keyUp('ctrlleft')
    time.sleep(2)
    newMail = getMail()
    if newMail:
        print("10 min mail: " + newMail)
        break

# back to Proton
pyautogui.keyDown('ctrlleft'); pyautogui.keyDown('shiftleft')
pyautogui.typewrite('\t'); pyautogui.keyUp('ctrlleft'); pyautogui.keyUp('shiftleft')
time.sleep(1)

# Insert the mail
pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('v'); pyautogui.keyUp('ctrlleft')
pyautogui.typewrite('\n')
# pyautogui.press('backspace')  <= removed, it ruined

time.sleep(5)

# back to mail gen w/s
pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('\t'); pyautogui.keyUp('ctrlleft')
time.sleep(1)

# ctrl + a everything for getClip6digit() function
pyautogui.keyDown('ctrlleft');  pyautogui.typewrite('a'); pyautogui.keyUp('ctrlleft')
pyautogui.keyDown('ctrlleft'); pyautogui.typewrite('c'); pyautogui.keyUp('ctrlleft')

# back to Proton
pyautogui.keyDown('ctrlleft'); pyautogui.keyDown('shiftleft'); pyautogui.typewrite('\t') 
pyautogui.keyUp('ctrlleft'); pyautogui.keyUp('shiftleft')
time.sleep(10)

# insert the 6-digit code extracted from the Clipboard
pyautogui.typewrite(str(getClip6digit()) + '\n')

# rest several actions for acc creation
time.sleep(4)
pyautogui.typewrite('\n')
time.sleep(5)
pyautogui.typewrite('\t\t\t\t\n')
time.sleep(1)
pyautogui.typewrite('\t\n')

print(_username_+"@proton.me:" + _password_)

# write down username and password
with open("accLog.txt", "a") as f:
    f.write(_username_ + "@proton.me:" + _password_ + "\n")