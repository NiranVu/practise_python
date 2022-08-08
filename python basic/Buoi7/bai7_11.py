# C1:
_str = input("Nhập câu bạn muốn vào: ")
edit_str = _str.strip()
# a = []
# c = len(edit_str)
# b = 0
# space = 0
# #Đếm khoảng cách vì đem khoảng cách + 1 là ra số chữ
# for i in range(c):
#     if edit_str[i] == ' ':
#         space += 1
# num_word = space + 1
# #Duyệt tách từng chữ đưa vào list
# for j in range(num_word): #cho lặp lại số vòng chữ
#     word = ''
#     for k in range (b, c): #tách chữ cho vào list
#         if edit_str[k] != ' ':
#             b += 1
#             word += edit_str[k]
#         else:
#             b += 1
#             break
#     a.append(word)
# #Kiếm từ dài nhất
# mark = a[0]
# for l in range(len(a)):
#     if len(a[l]) > len(mark):
#         mark = a[l]
# print(f'Trong câu có chữ dài nhất là {mark}')

# C2:
a = []
word = ""
for i in range(len(_str)):
    if _str[i] != "":
        word += _str[i]
    else:
        a.append(word)
        word = ""
# Sau khi tách từng chữ ra được rồi chỉ việc tìm từ dài nhất thôi
# C3:
str_input = input("Nhập câu văn: ")
list_word = str_input.strip().split(" ")  # Tách theo khoảng trắng để ra được các từ đơn
maxx = list_word[0]
for item in list_word:
    if len(item.strip()) > len(maxx):
        maxx = item.strip()
print(f"Từ dài nhất trong câu: {maxx}")
