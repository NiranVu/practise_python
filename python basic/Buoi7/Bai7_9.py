my_tuple = (2.7, 2, -3.14, 5.6, 0, -9.1)
a = list(my_tuple)
b = sorted(a)
_sum = 0
for i in range(len(my_tuple)):
    _sum += my_tuple[i]

print(f"Giá trị lớn nhất trong tuple = {b[-1]}")
print(f"Tổng các giá trị trong tuple = {round(_sum, 3)}")

# C2:
tuple_float = (0.1, -2.17, 200 / 11, 3.3, 5 / 6, -4 / 7, 11.01)
maxx = tuple_float[0]
tong = 0
for item in tuple_float:
    tong += item
    if item > maxx:
        maxx = item
print(f"Tổng là {tong}, GTLN là {maxx}")
