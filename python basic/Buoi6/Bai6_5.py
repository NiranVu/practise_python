my_list = [1, 3, 3, 9, "python", "python", "python", 8, 6, 9, 9, 9]
a = 0
for i in range(len(my_list)):
    b = my_list.count(my_list[i])
    if b > a:
        a = b
        c = my_list[i]
print(f"Phần tử xuất hiện nhiều nhát trong list là: {c}")
