# my_list = [1, 2, 3, 'Duc']
# copy_list = my_list.copy()
# copy_list.insert(0, ' ')
# num = int(input('Nhập số lần bạn mong muốn thêm vào list = '))
# for i in range(num):
#     a = input('Nhập phần tử bạn muốn thêm vào list: ')
#     if a >= '0' and a <= '9':
#         a = int(a)
#         copy_list.insert(i, a)
#     else:
#         copy_list.insert(i, a)
# print(f'{copy_list}') !!!!!!!Bài này bị hiểu sai đề bài

list_04 = [0, 2, 3, 7, 8, 5, 4, 6, 9, 0, 1]
l = int(input("Nhập độ dài phần đầu: "))
head = list_04[:l]
tail = list_04[l:]
print(f"Phần đầu: {head}, Phần sau: {tail}")
