my_dict = {1: 6, 2: 9, 3: 7, 4: 3}
v = my_dict.values()
_max = max(v)
_min = min(v)
for k, v in my_dict.items():
    if v == _max:
        print(f"Giá trị lớn nhất là {k} : {v}")
    elif v == _min:
        print(f"Giá trị nhỏ nhất là {k} : {v}")

# C2:
from math import inf

dict_01 = {-2: 9, 0: 1, 2: 3, "k": 4, "x": 5, -1: 2, 3: -3}
maxx = -inf
minn = inf
for k, v in dict_01.items():
    if v < minn:
        minn = v
    if v > maxx:
        maxx = v
print(f"Value max = {maxx}, min = {minn}")
