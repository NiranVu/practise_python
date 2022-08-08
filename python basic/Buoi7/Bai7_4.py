my_list = [(2, 5), (4, 1), (0, 5), (0, 0), (0, 5), (5, 9)]
# C1:
# sorted_follow_last_value = []
# Lấy các giá trị cuối ra sắp xếp
# for i in range(len(my_list)):
# Loại bỏ giá trị trùng lặp
# if my_list[i][-1] not in sorted_follow_last_value:
#     sorted_follow_last_value.append(my_list[i][-1])
# sorted_follow_last_value.sort()
# print(sorted_follow_last_value)
# #So các giá trị sắp xếp rồi chuyển lại thành tuple đưa vào trong list
# result_list = []
# for j in range(len(sorted_follow_last_value)):
#     for i in range(len(my_list)):
#         if sorted_follow_last_value[j] == my_list[i][-1]:
#             result_list.append(my_list[i])
#         else:
#             continue
# print(result_list)

# C2:
c = []
# Lập list giá trị cuối được sắp xếp
for i in range(len(my_list)):
    c.append(my_list[i][-1])
a = set(c)  # Bỏ các số lặp
b = list(a)
b.sort()
# Lấy tuple gióng theo các giá trị đã sắp xếp rồi quăng vào list mới
result_list = []
for j in range(len(b)):
    for i in range(len(my_list)):
        if b[j] == my_list[i][-1]:
            result_list.append(my_list[i])
print(f"sắp xếp tuple trong list = {result_list}")

# C3
list_sample = [(2, 5), (4, 1), (0, 0)]
for i in range(len(list_sample)):
    for j in range(i + 1, len(list_sample)):
        if list_sample[i][-1] > list_sample[j][-1]:
            list_sample[i], list_sample[j] = list_sample[j], list_sample[i]
print(list_sample)
