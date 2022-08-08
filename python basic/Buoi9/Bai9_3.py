def is_perfect(n):
    """
    Kiểm tra xme là số hoàn hảo hay không
    """
    _sum = 0
    for i in range(1, n, 1):
        if n % i == 0:
            _sum += i
        else:
            continue
    if _sum == n:
        return True
    return False


print(is_perfect(28))


# Bài 03: Viết hàm
#         def is_perfect(n)
#     để kiểm tra xem số tự nhiên n có phải là số hoàn hảo hay ko, trả lại True nếu có, False nếu không.
#     Ghi chú: Xem định nghĩa về số hoàn hảo: http://hanoimoi.com.vn/Tin-tuc/Thieu-nhi/592454/so-hoan-hao-la-gi


def is_perfect(n):
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0:
            tong_uoc += i
    return True if tong_uoc == n else False
