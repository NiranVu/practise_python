while True:
    epsilon = float(input("Nhập số epsilon = "))
    if epsilon < 1 and epsilon > 0:
        # Cách 1: dùng với library math
        # Tính e = 1 + 1/1! + 1/2! + ... + 1/n! quá trình dừng khi 1/n! < epsilon
        e = 0
        n = 0
        import math

        while 1 / (math.factorial(n)) > epsilon:
            e += 1 / (math.factorial(n))
            n += 1
        print(f"Tổng e = {e}")

        break
    print("Bạn nhập số epsilon sai yêu cầu nhập lại")
# Cách 2: không dùng với math
epsilon = float(input("Nhập epsilon = "))
fact_max = 1 / epsilon  # Đổi lại điều kiện dừng lặp
i = 1
factorial = 1
value_e = 1
while factorial <= fact_max:
    value_e += 1 / factorial
    i += 1
    factorial *= i  # đưa lên cho giống với giai thừa
print(f"Giá trị của e ~ {value_e}")
