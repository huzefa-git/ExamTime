lst = [5,4,1,2,6,7]
for i in range(len(lst)):
    for j in range(len(lst)):
        if lst[i]<lst[j]:
            lst[i],lst[j] = lst[j],lst[i]
for i in range(len(lst)):
    print(lst[i],end="")