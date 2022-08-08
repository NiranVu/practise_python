my_list = [
    (2,),
    (4, 1),
    (0, 5),
    (0, 0, 9),
    (0, -2),
    (5, 9),
    (1, 0),
    (9, -1),
    (3,),
    (9, -2),
]
a = my_list.copy()
for i in range(len(my_list)):  # Loại tuple ko đủ 2 phần tử
    if len(my_list[i]) < 2:
        a.remove(my_list[i])
print(a)
# Tìm kiếm tuple nhỏ nhất
b = 0
c = []
for i in range(len(a)):
    if b > a[i][1]:
        b = a[i][1]
        c.append(a[i][1])
c.sort()
d = []
for j in range(len(a)):
    if c[0] == a[j][1]:
        d.append(a[j])
print(f"tuple nhỏ nhất = {d}")

# C2:
list_demo = [(0, 1), (3, 2, 0), (0, -1), (4, 5), (9, 2), (4, 1)]
minn = list_demo[0][1]
item_min = list_demo[0]
for item in list_demo:
    if item[1] < minn:
        minn = item[1]
        item_min = item
print(f"Tuple có phần tử thứ 2 là nhỏ nhất {item_min}")
