s = input("Nhập từ mà bạn mong muốn: ")
b = s[0] + s[1] + " " + s[-2] + s[-1]

if len(s) >= 2:
    print(f"Chuỗi 2 ký tự đầu và 2 ký tự cuối là {b}")
else:
    print(f"Chuỗi rỗng")
