import time
import os 
import winshell
time.sleep(60)
os.chdir(r"C:\Application")
current_directory=os.getcwd()
os.remove(rf"{current_directory}\Friday_bot.exe")
os.remove(rf"{current_directory}\Bot.vbs")
os.remove(rf"{current_directory}\Bot.bat")
os.remove(rf"{current_directory}\self_destruct.vbs")
os.remove(rf"{current_directory}\self_destruct.bat")
time.sleep(1)
winshell.recycle_bin().empty(confirm=False,show_progress=False,sound=False)
