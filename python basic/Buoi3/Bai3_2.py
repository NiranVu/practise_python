#Nhập 3 số thực x, y, z
x = float(input('Nhập x = '))
y = float(input('Nhập y = '))
z = float(input('Nhập z = '))
#Tính giá trị biểu thức F = (x+y+z)/(x^2+y^2+1) - |x-z*cos(y)|
import math
a = x + y + z
b = x ** 2 + y ** 2 + 1
c = x - z * math.cos(y)
f = (a) / (b) - math.fabs(c)
print(f'Gia tri cua F = <{f}>')

	F = (x + y + z)/(x**2 + y**2 + 1) - abs(x - z * math.cos(y))
print(f"Gia tri cua F = {F}")