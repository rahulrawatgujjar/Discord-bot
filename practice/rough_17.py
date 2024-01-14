
# import json
# import requests
# from bs4 import BeautifulSoup
# # params=requests.get("https://www.flipkart.com/moto-g71-5g-arctic-blue-128-gb/p/itm725289299f711?pid=MOBG6FWDJKXCTBV4&lid=LSTMOBG6FWDJKXCTBV49C7SLF&marketplace=FLIPKART&q=motorola+g71&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=search-autosuggest&iid=4a588f07-42da-4c16-aa7d-19d9edf01ac5.MOBG6FWDJKXCTBV4.SEARCH&ppt=sp&ppn=sp&ssid=7o55m4da0w0000001654522226367&qH=2366f0d2feaaf217")
# payload={"url":"https://www.flipkart.com/moto-g71-5g-arctic-blue-128-gb/p/itm725289299f711?pid=MOBG6FWDJKXCTBV4&lid=LSTMOBG6FWDJKXCTBV49C7SLF&marketplace=FLIPKART&q=motorola+g71&store=tyy%2F4io&srno=s_1_1&otracker=search&otracker1=search&fm=search-autosuggest&iid=4a588f07-42da-4c16-aa7d-19d9edf01ac5.MOBG6FWDJKXCTBV4.SEARCH&ppt=sp&ppn=sp&ssid=7o55m4da0w0000001654522226367&qH=2366f0d2feaaf217"}
# r=requests.post(url="https://pricehistory.in/",data=json.dumps(payload)).text
# response=json.loads(r)
# # soup=BeautifulSoup(r.content,"html.parser")
# # print(soup)

# print(response)

import time
import keyboard as kb
from selenium import webdriver
# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
engine=webdriver.Chrome(executable_path=rf"chromedriver.exe")
# engine.get("https://www.flipkart.com")
# time.sleep(5)
# kb.press("esc")
# time.sleep(2)
# search_btn=engine.find_element_by_name("q")
# search_btn.send_keys("moto g82")
# search_btn.submit()
# time.sleep(5)
# btn_2=engine.find_element_by_class_name("_1fQZEK")
# btn_2.click()

engine.get("https://pricehistory.in")
time.sleep(2)
kb.write("https://www.flipkart.com/moto-g71-5g-arctic-blue-128-gb/p/itm725289299f711?pid=MOBG6FWDJKXCTBV4&lid=LSTMOBG6FWDJKXCTBV49C7SLF&marketplace=FLIPKART&q=moto+g71&store=tyy%2F4io&srno=s_1_1&otracker=AS_Query_OrganicAutoSuggest_6_6_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_6_6_na_na_na&fm=organic&iid=14437c49-0357-4ca0-b4f3-2b795b98efe1.MOBG6FWDJKXCTBV4.SEARCH&ppt=hp&ppn=homepage&ssid=5pjto83fcg0000001654604804273&qH=22795013913a71f2")
time.sleep(1)
b2=engine.find_element_by_id("trackPriceBtn")
b2.click()
engine.get_screenshot_as_file("screenshot.png")
