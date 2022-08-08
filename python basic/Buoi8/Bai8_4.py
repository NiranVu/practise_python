dict_1 = {1: 9, 2: 6, 3: 1, 6: 4, "list": "dict 1"}
dict_2 = {3: 4, 9: "Duc", "list": "dict 1", 6: 4}
for k1, v1 in dict_1.items():
    for k2, v2 in dict_2.items():
        if k1 == k2 and v1 == v2:
            print(f"Phần tử giống nhau giữa 2 dict là {k1} : {v1}")

# C2:
dict_051 = {1: 1, 2: 2, 3: 3, 4: 5, 6: 7, "list": "dict 1"}
dict_052 = {1: -1, 2: -2, -3: 3, 4: 5, 6: -7, "list": "dict 1"}
result = set()  # Cách này để add vào set với bộ giá trị cho dễ nhìn
for k, v in dict_051.items():
    if k in dict_052 and v == dict_052[k]:
        result.add((k, v))
print(f"Các phần tử key-value xuất hiện trong cả 2 dict: {result}")
