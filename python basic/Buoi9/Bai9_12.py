a_list = [6, 0, 9, 8, 7, 4, 13, 20, 30, 1, 5, 4, 6]


def find_x(a_list, x):
    _index = []
    if x not in a_list:
        return -1
    else:
        for i in range(len(a_list)):
            if a_list[i] == x:
                _index.append(i)
        return _index


print(find_x(a_list, 6))

# Bài 12-plus: Viết hàm
#         def create_matrix(n, m)
#     xử lý việc tạo ra ma trận n hàng, m cột với giá trị phần tử tại (i, j) = i*j

import random


def create_matrix(n, m):
    return [[random.randrange(10) for j in range(m)] for i in range(n)]


n, m = 5, 4
res = create_matrix(n, m)
print(f"Matrix {n}x{m}:")
for i in range(n):
    print(res[i])


# Bài 12: Viết hàm
#         def find_x(a_list, x)
#     trả lại tất cả các vị trí mà x xuất hiện trong a_list, nếu không có thì trả lại -1


def find_x(a_list, x):
    res = []
    for i in range(len(a_list)):
        if a_list[i] == x:
            res.append(i)
    return res if res else -1
