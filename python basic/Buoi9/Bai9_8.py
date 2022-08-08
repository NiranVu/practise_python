def chang_upper_lower(_str):
    result = ""
    a = str(_str)
    for i in range(len(_str)):
        if a[i] >= "a" and a[i] <= "z":
            result += a[i].upper()
        elif a[i] >= "A" and a[i] <= "Z":
            result += a[i].lower()
        else:
            result += a[i]
    return result


print(chang_upper_lower("Duc VDMASPOvvmosdv[p"))

# Bài 08: Viết hàm
#         def change_upper_lower(str)
#     chuyển toàn bộ các ký tự in hoa sang in thường và in thường thành in hoa trong str


def change_upper_lower(str):
    res = []
    for c in str:
        if "a" <= c <= "z":
            res.append(chr(ord(c) - 32))
        elif "A" <= c <= "Z":
            res.append(chr(ord(c) + 32))
        else:
            res.append(c)
    return "".join(res)
