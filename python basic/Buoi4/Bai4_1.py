# Nhập 3 số a, b, c bất kì từ bán phím
a = float(input("Nhập số a = "))
b = float(input("Nhập số b = "))
c = float(input("Nhập số c = "))

import math

# Giải nghiệm phương trình bậc 2: ax^2 + bx + c = 0
if a == 0:  # TH a = 0 thì sẽ thành phương trình bậc 1
    x = (-c) / b  # Nên đặt ở đây hơn là đặt ở ngoài
    print(f"Phương thành có nghiệm là {round(x, 2)}")
else:  # TH a != thì sẽ thành phương trình bậc 2 nguyên bản
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        print(f"Phương trình có 2 nghiệm là x1 = {x1} và x2 = {x2}")
    elif delta == 0:
        x = (-b) / (2 * a)
        print(f"Phương trình có nghiệm kép là {x}")
    else:
        print("Phương trình vô nghiệm")


# Mình bị thiếu trường hợp a == 0 hay/và c == 0 hay/và b ==0
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        print(f"Phương trình có nghiệm: x_0 = {-c/b}")
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Phương trình vô nghiệm thực")
    elif delta == 0:
        print(f"Phương trình có nghiệm kép x_0 = {-b/(2*a)}")
    else:
        sqrt_delta = math.sqrt(delta)
        print(
            f"Phương trình có 2 nghiệm: x_1 = {(-b + sqrt_delta)/(2*a)}, x_2 = {(-b - sqrt_delta)/(2*a)}"
        )
