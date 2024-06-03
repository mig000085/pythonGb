def sane_by (characteristic, object):
    result = True
    list1 = [characteristic(x) for x in object]
    for i in range(len(list1) - 1):
        if list1[i] != list1[i+1]:
            result = False
    return result




values = [0, 2, 10, 6]
if sane_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')