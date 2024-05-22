list1 =[{"V": "S001"}, {"V": "S005"}, {"VI": "S001"}, {"VI": "S005"},
        {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

set_1 = set()
for i in list1:
    for j in i:
        set_1.add(i[j])
        print(set_1)