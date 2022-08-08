def count_upper_lower(_str):
    """
    Đếm số lượng từ viết hoa viết thường trong một chuỗi đưa vào
    """
    a = str(_str)
    uppper = 0
    lower = 0
    for i in range(len(a)):
        if a[i] >= "a" and a[i] <= "z":
            lower += 1
        elif a[i] >= "A" and a[i] <= "Z":
            uppper += 1
    return f"Số lượng viết hoa là {uppper} và số lượng chữ cái viết thường là {lower}"


print(count_upper_lower("FMAPDVMPOafmnopdgfvmsdpovKMFOPAFMVOP"))


# Bài 05: Viết hàm
#         def count_upper_lower(str)
#     trả lại số lượng chữ cái viết hoa, số lượng chữ cái viết thường trong chuỗi str


def count_upper_lower(str):
    hoa = thuong = 0
    for i in str:
        if "A" <= i <= "Z":
            hoa += 1
        elif "a" <= i <= "z":
            thuong += 1
    return hoa, thuong
