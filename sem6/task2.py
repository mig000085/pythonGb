from math import pi
def find_farthest_orbit(list_of_orbits):
    list1 = [i for i in list_of_orbits if i[0] != i[1]]
    list_s = [(pi * i[0] * i[1]) for i in list1]
    max_s = list_s.index(max(list_s))
    
    return list1[max_s]
    
    
    
    
    
orbits = [(1, 3), (2.5, 10),(7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
    