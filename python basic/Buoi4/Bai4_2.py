import math

x = float(input("Nhập số thực x = "))
while True:  # Kiểm tra nếu không phải số nguyên dương
    n = int(input("Nhập số nguyên dương n = "))
    if n > 0:
        # Cách 1: đặt trong while
        # #Tính tổng S_1 = 1 + x + x^2 + x^3 + ... + x^n
        # sum_s_1 = 1
        # for n in range(1, n + 1, 1):
        #     sum_s_1 += x ** n
        # print(f'Tổng S_1 = {sum_s_1}')

        # #Tính tổng S_2 = 1 - x + x^2 - x^3 + ... + (-1)^n.x^n
        # sum_s_2 = 1
        # for n in range(1, n + 1, 1):
        #     sum_s_2 += ((- 1) **n) * (x ** n)
        # print(f'Tổng S_2 = {sum_s_2}')

        # #Tính tổng S_3 = S_3 = 1 + x/1! + x^2/2! + ... + x^n/n!
        # sum_s_3 = 1
        # for n in range(1, n + 1, 1):
        #     sum_s_3 += (x ** n) / (math.factorial(n))
        # print(f'Tổng của S_3 = {sum_s_3}')
        break
    print("Bạn đã nhập sai số n mong bạn nhập lại")

# Cách 2: đặt ngoài while
# Tính tổng S_1 = 1 + x + x^2 + x^3 + ... + x^n
sum_s_1 = 1
for n in range(1, n + 1, 1):
    sum_s_1 += x ** n
print(f"Tổng S_1 = {sum_s_1}")

# Tính tổng S_2 = 1 - x + x^2 - x^3 + ... + (-1)^n.x^n
sum_s_2 = 1
for n in range(1, n + 1, 1):
    sum_s_2 += ((-1) ** n) * (x ** n)
print(f"Tổng S_2 = {sum_s_2}")

# Tính tổng S_3 = S_3 = 1 + x/1! + x^2/2! + ... + x^n/n!
sum_s_3 = 1
for n in range(1, n + 1, 1):
    sum_s_3 += (x ** n) / (math.factorial(n))
print(f"Tổng của S_3 = {sum_s_3}")
