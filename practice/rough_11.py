# import geocoder
# g=geocoder.ip("me")
# print(g)
# print(g.latlng)


# Python Program to Get IP Address
# import socket   
# hostname = socket.gethostname()   
# IPAddr = socket.gethostbyname(hostname)   
# print("Your Computer Name is:" + hostname)   
# print("Your Computer IP Address is:" + IPAddr)  
# import webbrowser
# import pyautogui as pg
# webbrowser.open("https://www.google.com/search?q=where+am+i")
# ss=pg.screenshot("")


import subprocess, sys
path=r"D:\Drive\try.ps1"
p = subprocess.Popen(["powershell.exe",path],stdout=sys.stdout)
p = subprocess.Popen('powershell.exe -ExecutionPolicy RemoteSigned -file "try.ps1"', stdout=sys.stdout)
p.communicate()


# import subprocess
 
# traverse the info
# Id = subprocess.check_output(['systeminfo']).decode('utf-8')
# # print(Id)
# print(len(Id))

# new = []
# # print(Id)
# for element in Id:
#     # element=element.replace("\r","")
#     # print(element)
#     print(element.replace("\r",""))
# print("\n\n\n")
# # arrange the string into clear info
# for item in Id:
#     new.append(str(item.split("\r")[:-1]))
# for i in new:
#     print(i[2:-2])