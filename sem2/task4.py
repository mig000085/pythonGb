n = int(input())
min = -1
max = 30001
for i in range(n):
    x = int(input())
    if x > max:
        max = x
    if x < min:
        min = x
print(max, min)