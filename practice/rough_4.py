from selenium import webdriver
import os
from time import sleep
import time
import pyautogui as pg  
current_directory=os.getcwd()

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')
options.add_argument('--allow-running-insecure-content')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=rf"{current_directory}\chromedriver.exe")
# driver = webdriver.Chrome(executable_path="chromedriver")
# driver.get("https://www.google.com")
driver.get("https://www.flipkart.com")

# time.sleep(2)
# pg.press("esc")
time.sleep(2)
button=driver.find_element_by_link_text("Mobiles")
button.click()
# time.sleep(2)
# driver.get_screenshot_as_file("screenshot.png")



time.sleep(2)
# pg.press("esc")
# time.sleep(2)
# button=driver.
# button.click()
# time.sleep(2)
# button=driver.find_element_by_link_text("Mobiles")
# button.click()
# time.sleep(2)
driver.get_screenshot_as_file("screenshot.png")