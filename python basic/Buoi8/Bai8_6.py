my_dict = {9: 3, 8: 5, 3: 6, 5: 4, 4: 7}
list_value = list(my_dict.values())
list_value.sort(reverse=True)
print(list_value)
for i in range(0, 3, 1):
    for k, v in my_dict.items():
        if list_value[i] == v:
            print(f"Value lớn thứ {i + 1} trong dict là {k} : {v}")

dict_07 = {-2: 9, 4: -1, 2: 3, -1: 2, 3: -3, 6: 4, -9: 5, 0: 9, -8: 3}
values_max_sorted = sorted(dict_07.values(), reverse=True)[0:3]
result = set()
for k, v in dict_07.items():
    if v in values_max_sorted:
        result.add((k, v))
print(f"Kết quả của bài toán {result}")
