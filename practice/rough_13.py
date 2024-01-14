# import os
# os.system(""" shutdown /r /t 10 /c "Your computer has been hacked by me" """)
# os.open("powershell.exe")
import pyautogui as pg
pg.press("winleft")
# time.sleep(1)
pg.write("powershell")
# time.sleep(1)
pg.press("enter")
# time.sleep(1)
pg.write("rundll32.exe user32.dll, LockWorkStation")
# time.sleep(1)
pg.press("enter")

# from pywhatkit.core import core
# core.close_tab(1)