n = int(input())
k = 0
max = 0
for i in range(n):
    x = int(input())
    if x > 0:
        k += 1
    else:
        if max < k:
            max = k
        k = 0
        
print(max)