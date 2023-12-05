import numpy as np

list = [[1,2,3],[4,5,6],[7,8,9]]
n=0
l2=[]
for i in range(len(list[0])):
    l=[]
    for item in list:
        l.append(item[i])
    l2.append(l)
    
print(l2)
    
    