import matplotlib.pyplot as plt
import os
# third argument is used to plot different types of graph
plt.plot([1,2,3,4,5],[1,4,9,16,25])
plt.plot([1,2,3,4,5],[1,4,9,16,25],'ro')
# plt.plot([1,2,3,4,5],[1,4,9,16,25],'r--')
# plt.plot([1,2,3,4,5],[1,4,9,16,25],'bs')
# plt.plot([1,2,3,4,5],[1,4,9,16,25],'g^')
plt.ylabel("y varialble")
plt.xlabel("x varialble")
# plt.show()
d=os.getcwd()
# print(d)
# plt.savefig(f"{d}\graph_1.png")

arr="1,2,3,4"
arr_2=arr.split(",")
# arr_2=int(arr_2)
for i in range(len(arr_2)):
    arr_2[i]=int(arr_2[i])


print(arr_2)

