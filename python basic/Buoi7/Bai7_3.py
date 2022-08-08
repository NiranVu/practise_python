my_list = [
    3.14,
    "string",
    3,
    ["list", 0],
    ("90",),
    {3, 3.14, "set"},
    (3.14, 3, "tuple"),
]
_count = 0

for i in my_list:
    if type(i) != tuple:
        _count += 1
    else:
        break

print(f"Số phần tử trong list không phải tuple = {_count}")
