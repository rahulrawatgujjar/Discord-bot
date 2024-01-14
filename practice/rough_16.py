# import webbrowser as wb
# import mouse
# import time
# wb.open("https://www.google.com/android/find?u=0&utm_source=Google&utm_medium=onebox")
# time.sleep(30)
# print(mouse.get_position())
# mouse.move(326, 255)
# while(True):
#     mouse.move(326, 255)
#     mouse.click()
#     time.sleep(10)
#     # mouse.move(1048, 628)
#     # mouse.click()
#     # mouse.click()
#     # mouse.click()
#     time.sleep(50)

t=int(input())
for i in range(t):
    pa,pb,qa,qb=list(map(int,input().split(" ")))
    if pa>pb:
        if qa>qb:
            if pa>qa:
                print("Q")
            elif pa==qa:
                print("TIE")
            else:
                print("P")
        else:
            if pa>qb:
                print("Q")
            elif pa==qb:
                print("TIE")
            else:
                print("P")
    else:
        if qa>qb:
            if pb>qa:
                print("Q")
            elif pb==qa:
                print("TIE")
            else:
                print("P")
        else:
            if pb>qb:
                print("Q")
            elif pb==qb:
                print("TIE")
            else:
                print("P")