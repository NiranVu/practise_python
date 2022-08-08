# Nhập số nguyên dương n bất kì < 1000, kiểm tra dữ liệu đầu vào nếu sai thì yêu cầu nhập lại
while True:
    n = int(input("Nhập số nguyên dương n = "))
    if n > 0:
        print("Bạn đã nhập đúng")

        # Cách 1: tính trong while:
        # #Tính tổng các chữ số n (theo e hiểu là từ 0 đến n)
        # sum = 0
        # for n in range(0, n + 1, 1):
        #     sum += n
        # print(f'Tổng từ 0 đến n = {sum}')
        s = 0
        # for i in range(n):
        # while n > 0:
        #     tach_so = n % 10 #lấy dư để lấy cố cuối cùng
        #     s += tach_so #tính vào tổng
        #     n //= 10 #lấy phần nguyên để cắt đi số cuối
        # print(f'Tổng các chữ số = {s}')
        break
    print("Bạn đã nhập sai yêu cầu nhập lại")

# cách 2: đặt ngoài vòng while
tong = 0
while n > 0:
    tong += n % 10
    n //= 10
print(f"Tổng các chữ số của {n} là {tong}")
