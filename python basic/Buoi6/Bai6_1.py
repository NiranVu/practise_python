my_list = [1, 3, 4, 5, 6, 9, "Duc"]
edit_list = my_list.copy()
sum_list = 0
multi_list = 1
# Kiếm tra xem có chuỗi trong list không
for i in range(len(edit_list)):
    if type(edit_list[i]) == str:
        del edit_list[i]
# Tính tổng, tích
for i in range(len(edit_list)):
    sum_list += edit_list[i]
    multi_list *= edit_list[i]

print(f"Tổng của phần tử trong list = {sum_list}")
print(f"Tích của phần tử trong list = {multi_list}")
