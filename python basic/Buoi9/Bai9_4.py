def is_prime(n):
    """
    Kiểm tra xem phải là số nguyên tố hay không
    """
    if n == 1:
        return True
    elif n == 2:
        return False
    else:
        for i in range(3, n):
            if n % i == 0:
                return False
        return True


def min_prime(n):
    """
    Tìm số nguyên tố bé nhất và lớn hơn n
    """
    a = n
    while True:
        if is_prime(a) == True and a > n:
            return f"Số nguyên tố bé nhất và lớn hơn n là {a}"
        else:
            a += 1


print(min_prime(6))

# Bài 04. Dùng hàm is_prime(n) đã có trong bài học để xây dựng đoạn chương trình:
#     1. Nhập vào số nguyên dương n từ bàn phím
#     2. Tìm và in ra số nguyên tố bé nhất và lớn hơn n


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def next_prime(n):
    while True:
        n += 1
        if is_prime(n):
            return n
