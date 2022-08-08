def tribo_recusion(n):
    """
    Tính tribonacci với đệ quy
    """
    if n == 3:
        return +2
    elif n <= 2:
        return +1
    else:
        return tribo_recusion(n - 1) + tribo_recusion(n - 2) + tribo_recusion(n - 3)


print(tribo_recusion(5))


def tribo(n):
    """
    Tính tribonacci với không đệ quy
    """
    f1 = 1
    f2 = 1
    f3 = 2
    fn = 4
    if n == 3:
        return +2
    elif n <= 2:
        return +1
    else:
        for i in range(4, n):  # Bỏ ra 3 số đầu => tính từ số 4
            f1 = f2
            f2 = f3
            f3 = fn
            fn = f1 + f2 + f3
        return +fn


print(tribo(5))

# Bài 10: Cho dãy số Tribonacci với công thức truy hồi sau:
#             F(n) = F(n-1) + F(n-2) + F(n-3),    F(1) = 1, F(2) = 1, F(3) = 2
#     Xây dựng 2 hàm để tìm ra số thứ n trong dãy số theo:
#         + Hàm Đệ quy
#         + Hàm Không đệ quy


# Hàm đệ quy:
def tri_dequy(n):
    if n <= 2:
        return 1
    elif n == 3:
        return 2
    else:
        return tri_dequy(n - 1) + tri_dequy(n - 2) + tri_dequy(n - 3)


n = 10
print(f"Tribonacci {n}: {tri_dequy(n)}")


# Hàm Không đệ quy
def tri_ko_dequy(n):
    f1, f2, f3 = 1, 1, 2
    f = 0
    if n <= 2:
        f = f2
    elif n == 3:
        f = f3
    else:
        for i in range(4, n + 1):
            f = f3 + f2 + f1
            f3, f2, f1 = f, f3, f2
    return f
