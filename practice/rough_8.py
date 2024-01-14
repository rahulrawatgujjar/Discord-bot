import datetime
import time
current_time=datetime.datetime.now()
# print(str(current_time)[:19])
# print(current_time.year)
year="2022"
month="04"
day="29"
hour="18"
hour,minute,second=input().split(" ")
rem_time=f"{year}-{month}-{day} {hour}:{minute}:{second}"
while(True):
    print(str(datetime.datetime.now())[:19])
    if(str(datetime.datetime.now())[:19]==rem_time):

        print("hello")
        break
    time.sleep(1)


# 2022-04-29 18:51:41