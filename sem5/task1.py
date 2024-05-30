n = int(input())
list1 = list()
for i in range(n):
    x = int(input())
    list1.append(x)
    
    m = int(input())
list2 = list()
for i in range(m):
    x = int(input())
    list2.append(x)
    
count = 0
for i in range(n):
    for j in range(m):
        if list1[i] == list2[j]:
            count += 1
    if count == 0:
        print(list1[i])
    count = 0
                    