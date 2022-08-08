def reverse_string(_str):
    """
    Đảo ngược chuỗi str được nhập vào
    """
    a = _str[::-1]
    return a


print(reverse_string("bla bla la la bala bala"))

# Bài 02: Viết hàm
#         def reverse_string(str)
#     trả lại chuỗi đảo ngược của chuỗi str


def reverse_string(str):
    return str[::-1]


print(f'KQ: {reverse_string("chuoi can dao nguoc")}')
