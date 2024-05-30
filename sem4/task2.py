n = int(input())

list1 = list()
for i in range(n):
    x = int(input())
    list1.append(x)
    
max_n = max(list1)
min_n = min(list1)    
for i in range(len(list1)):
    if list1[i] == max_n:
        list1[i] = min_n
        
        print(list1)
