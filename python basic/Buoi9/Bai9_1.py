def max_min(*numbers):
    """
    Xem xét max min của nhiều số nhập vào
    """
    a = max(numbers)
    b = min(numbers)
    return f"max: {a}, min: {b}"


print(max_min(5, 6, 9, 10, 15, 2, 3, 4))

# Bài 01: Viết hàm
#         def max_min(*numbers)
#     trả lại cả giá trị max, min của nhiều số được truyền vào


def max_min(*numbers):
    maxx = minn = numbers[0]
    for it in numbers:
        if it > maxx:
            maxx = it
        if it < minn:
            minn = it
    return (maxx,)
