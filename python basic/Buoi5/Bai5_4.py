s = input("Nhập từ bạn mong muốn: ")
a = s[::-1]
b = ""
print(f"a = {a}")
for i in range(len(a)):
    if a[i] >= "a" and a[i] <= "z":
        b += a[i].upper()
    elif a[i] >= "A" and a[i] <= "Z":
        b += a[i].lower()
    else:
        b += a[i]

print(f"Chuỗi mới sẽ là {b}")

s_06 = input("Nhập vào một chuỗi: ")
s_new = ""
for c in s_06:
    if "a" <= c <= "z":
        s_new += chr(ord(c) - 32)
    elif "A" <= c <= "Z":
        s_new += chr(ord(c) + 32)
    else:
        s_new += c
print("Chuỗi mới: " + s_new)
print("Bài 04 - DONE!")

# Cách 2: Dùng hàm swapcase()
s_new_new = s_06.swapcase()
print(s_new_new)
