# 0 1 1 2 3 5 8 13
n = int(input())
n0 = 0
n1 = 0
n2 = 1 
i = 2

while n0 < n:
    n0 = n1 + n2
    n1 = n2
    n2 = n0
    i += 1
    if n0 > n:
        i = -1  
print(i)  