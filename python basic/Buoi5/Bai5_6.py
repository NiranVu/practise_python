s = input("Nhập từ bạn mong muốn: ")
b = input("Nhập kí tự bạn mong muốn: ")
for i in range(len(s)):
    if s[i] == b:
        print(f"{i + 1}", end=" ")
        # Nếu muốn xuất bài bản xuất hiện hay không thì phải đặt cờ
