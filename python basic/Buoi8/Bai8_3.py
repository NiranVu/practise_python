my_dict = {}
while True:
    num = int(input("Nhập số phần tử bạn muốn thêm vào dict: "))
    if num >= 3:
        print("Bạn đã nhập đúng số lần cần thiết mời bạn nhập dữ liệu tiếp")
        break
    print("Bạn đã nhập sai số lần cần thiết mời bạn nhập lại")
for i in range(num):
    k = input("Nhập key bạn mong muốn: ")
    valu = []
    while True:
        num_valu = int(input("Nhập số phần tử bạn muốn trong list value của dict: "))
        if num_valu >= 5:
            print("mời bạn nhập những phần tử trong list")
            break
        print("Bạn nhập thiếu mời bạn nhập lại phần tử trong list")
    for j in range(num_valu):
        v_l_d = input(f"Nhập phần tử thứ {j + 1} trong list bạn muốn: ")
        valu.append(v_l_d)
    my_dict.update({k: valu})
print(my_dict)


# my_dict = {
#     1: [5, 6, 9, 'list 1', 'Mot', 4],
#     2: [9, 7, 3, 4, 'Hai', 'Duc'],
#     3: [7, 5, 4, 3,'Ba', 7],
#     4: [4, 6, 2, 1, 'Bon', 'string']
# }
v = list(my_dict.values())
for i in range(len(v)):
    print(f"Phần tử thứ 5 trong value của mỗi phần tử trong dict là {v[i][4]}")

# C2:
dict_04 = {
    "key1": [0, 2, 4, 1, 3, 5, 6],
    "key2": [0, -2, 4, 1, -3, 5, 0],
    "key3": [-2, 4, 1, -3, -5, 0],
    "key4": [0, -2, -4, 1, -3, 5],
    "key5": [0, 4.314, 1, -3, 5, 0.1],
}
for k, v in dict_04.items():
    print(f"Phần tử thứ 5 của value trong phần tử với key = {k} là: {v[4]}")
