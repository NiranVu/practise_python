my_string = input("Nhập chuỗi bạn mong muốn: ")
my_set = set(my_string)
# print(f'my_set = {my_set}')
covert_set_list = list(my_set)
# print(f'covert_set_list = {covert_set_list}')
my_list = list(my_string)
# print(f'my_list = {my_list}')
dict_count = {}
for i in range(len(covert_set_list)):
    appear_string = my_list.count(covert_set_list[i])
    dict_count.update({covert_set_list[i]: appear_string})

print(dict_count)

input_str = "Stringings"
set_char = set(input_str)
result = {}
for c in set_char:
    result[c] = input_str.count(c)
print(f"Kết quả bài toán {result}")
