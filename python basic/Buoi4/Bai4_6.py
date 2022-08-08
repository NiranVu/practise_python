import math

while True:
    x = int(input("Nhập một số tự nhiên = "))
    if x > 0:

        # Cách với while:
        # sum_n = 0
        # n = 0
        # while sum_n <= x:
        #     n += 1
        #     sum_n += n
        # print(f'n = {n-1}') #Đưa thủ công xuống 1 vòng lặp
        # print(f'sum = {sum_n - n}')
        # break

        # Cách lưu biến
        # tong = 0
        # z = 0
        # sum = 0
        # n = 0
        # while sum <= x:
        #    n += 1
        #    sum += n
        #    z = n
        #    tong = sum
        #    if sum > x: #Nhận thấy sau khi sum <= x thì nó sẽ làm 1 vòng lặp làm tăng lên 1 lần sum với n nữa nên phải dùng biến phụ để đưa nó xuống 1 vòng lặp
        #        tong = sum - n
        #        z = n - 1
        #        break
        # print(f'n = {z}')
        # print(f'tong = {tong}')
        # break

        # cách kiểm tra trong điều kiện
        sum_n = 0
        n = 0
        while sum_n + (n + 1) <= x:
            n += 1
            sum_n += n
        print(f"n = {n}")
        print(f"tổng = {sum_n}")
    print("Bạn không nhập số tự nhiên yêu cầu nhập lại")
