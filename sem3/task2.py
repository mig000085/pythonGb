list1 = [5, 4, 6, 7, -10]

k = int(input())
k = k % len(list1)
list_res = []
for i in range(k):
    list_res.append(list1[len(list1) -1 -i])
print(list_res)

for i in range(len(list1) - k):
    list_res.append(list1[i])
    print(list_res)