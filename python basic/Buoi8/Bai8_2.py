# C1:
my_dict = {9: 3, 8: 5, 3: 6, 5: 4, 4: 7}
list_key = list(my_dict.keys())
list_key.sort(reverse=True)
for i in range(0, 3, 1):
    for k, v in my_dict.items():
        if list_key[i] == k:
            print(f"Key lớn thứ {i + 1} trong dict là {k} : {v}")

# C2:
dict_03 = {-2: 9, 4: -1, 2: 3, -1: 2, 3: -3, 6: 4, -9: 5, 0: 9, -8: 3}
keys_sorted = sorted(dict_03.keys(), reverse=True)
# Trích key lấy value
result = [
    (keys_sorted[0], dict_03[keys_sorted[0]]),
    (keys_sorted[1], dict_03[keys_sorted[1]]),
    (keys_sorted[2], dict_03[keys_sorted[2]]),
]
print(f" phần tử có key lớn nhất {result}")
