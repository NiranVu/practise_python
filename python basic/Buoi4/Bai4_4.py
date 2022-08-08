# Nhập 3 số a, b, c bất kì
a = float(input("Nhập số a = "))
b = float(input("Nhập số b = "))
c = float(input("NHập số c = "))

# Kiểm tra 3 số đó có phải là độ dài của cạnh một tam giác hay không?
if a + b > c and a + c > b and b + c > a:

    # Kiểm tra xem đúng là tam giác vuông hay không
    if (
        a ** 2 == b ** 2 + c ** 2
        or b ** 2 == a ** 2 + c ** 2
        or c ** 2 == b ** 2 + a ** 2
    ):
        print("Đây là tam giác vuông")
    else:
        print("Đây là tam giác khác")

else:
    print("Đây không phải là một tam giác")
