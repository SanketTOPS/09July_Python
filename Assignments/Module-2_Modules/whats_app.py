"""import pywhatkit

pywhatkit.sendwhatmsg_instantly("+919724799469","Hello Students!")"""

import pyautogui
import time

message = "Hello! This is an automated message 🚀"
times = 10   # how many times to send

time.sleep(5)  # 5 sec to switch to WhatsApp window/chat

for i in range(times):
    pyautogui.typewrite(message)  # type the message
    pyautogui.press("enter")      # press Enter to send
    time.sleep(1)  # small delay

