list1=[1,2,3,4,5,6,7,8,9]
list2= [1,2,8,9,12,46,76,82,15,20,30]
d={}
for i in list1:
    for j in list2:
        if j%i==0:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
print(d)