my_list = ["sd", "Cmdklcmdc", "p", "mm", ""]
_count = 0
for i in range(len(my_list)):
    a = len(my_list[i])
    # b = my_list[i].startswith(my_list[i][-1])
    c = my_list[i].endswith(my_list[i][0])  # Cái này gặp lỗi nếu phần tử rỗng
    if a >= 2 and c == True:
        _count += 1

print(
    f"Số chuỗi thỏa độ dài từ 2 trở lên và ký tự đầu tiên và cuối cùng bằng nhau là: {_count}"
)

# C2:
count = 0
for item in my_list:
    if len(item) >= 2 and item[0] == item[-1]:
        count += 1
print(f"Có {count} thỏa mãn")
