from GoogleNews import GoogleNews
googlenews=GoogleNews()
import calendar
import datetime
current_time = datetime.datetime.now()

googlenews=GoogleNews(lang="hi",region="IN",start=f"{current_time.month}/{current_time.day}/{current_time.year}",encode="utf-8")
topic="mobiles"
googlenews.search(topic)
res=googlenews.results()
# print(res)
for element in res:
    print(element["title"])
    print(element["date"])
    print(element["desc"])
    print(element["link"])
    print(element["img"])
    print("\n")

# googlenews.results(sort=True)
# print(googlenews.get_news())


# Python3 code to demonstrate
# attributes of now()
	
# importing datetime module for now()
	
# using now() to get current time
	
# Printing attributes of now().
# print ("The attributes of now() are : ")
	
# print ("Year : ", end = "")
# print (current_time.year)
	
# print ("Month : ", end = "")
# print (current_time.month)
	
# print ("Day : ", end = "")
# print (current_time.day)
