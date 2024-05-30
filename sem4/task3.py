def prime(n):
    flag = True
    i = 2
    while i < n and flag:
        if n % i == 0:
            flag = False
            
        i += 1
        
    if flag:
        return 'yes'
    else:
        return 'no'

n = int(input())
print(prime(n))