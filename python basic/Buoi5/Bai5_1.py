s = input("Nhập từ bạn mong muốn: ")
if len(s) > 0:
    a = s.replace(s[0], "$")
    print(f"Chuỗi mới sẽ là {a}")

# Nếu muốn chỉ thay đổi bên trong còn chừa lại ký tự đầu thì:
if len(s) > 0:
    a = s[2:].replace(s[0], "$")
    print(f"{a}")
