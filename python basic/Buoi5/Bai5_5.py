s = input("Nhập từ bạn mong muốn: ")
b = ""
c = ""
if s > b and s > c:
    for i in range(len(s)):
        if s[i] >= "0" and s[i] <= "9":
            b += s[i]
        else:
            c += s[i]
    print(f"Số trong chuỗi là {b}", end=" ")
    print()
    print(f"Chữ trong chuỗi là {c}", end=" ")
else:
    print("Chuỗi rỗng")
