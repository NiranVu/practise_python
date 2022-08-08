s = input("Nhập từ bạn mong muốn: ")
max_ = " "
min_ = "z"
for i in range(len(s)):
    if s[i] >= max_:
        max_ = s[i]
    elif s[i] < max_ and s[i] <= min_:
        min_ = s[i]

print(f"Kí tự lớn nhất {max_}")
print(f"Kí tự nhỏ nhất {min_}")


s_05 = input("Nhập vào một chuỗi: ")
if s_05:
    c_max, c_min = s_05[0], s_05[0]
    for c in s_05:
        if c > c_max:
            c_max = c
        elif c < c_min:
            c_min = c
    print(f"Ký tự lớn nhất {c_max} và nhỏ nhất {c_min}")
# Bài này có thể dùng hàm max()/min()
