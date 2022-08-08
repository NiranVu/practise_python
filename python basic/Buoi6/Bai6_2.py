# # num = int(input('số lượng phần tử bạn mong muốn: '))
# # a = input('Nhập các phần tử trong list: ')
# # my_list = []

# print(f'List = {my_list}')

my_list = [1, 3, 4, 6, 9, 20]
# C1:
sorted_list = sorted(my_list)
print(
    f"Giá trị lớn nhất trong list = {sorted_list[len(sorted_list) - 1]}"
)  # - 1 vì len cho ra số thứ tự chứ không ra index
print(f"Giá trị nhỏ nhất trong list = {sorted_list[-len(sorted_list)]}")

# C2:
one_list = [1, 0, 9, 4, 5, 2, 7, 8, 3]
maxx = one_list[0]
minn = one_list[0]
for item in one_list:
    if maxx < item:
        maxx = item
    elif minn > item:
        minn = item

# Hoàn toàn có thể dùng hàm được cung cấp sẵn max(), min() để tim GTLN, GTNN
