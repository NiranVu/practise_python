tuple_1 = (1, "string", "Duc", 6)
tuple_2 = (
    0,
    9,
    "Anh",
)
c = 0  # Nếu > 0 là có phần tử chung, = 0 là không có phần tử chung
for i in range(len(tuple_1)):
    for j in range(len(tuple_2)):
        if tuple_1[i] == tuple_2[j]:
            c += 1
if c > 0:
    print("2 tuple có phần tử chung")
else:
    print("2 tuple không có phần tử chung")

# C2:
tuple_1 = (0, 3, 5, 7, 9, 10)
tuple_2 = (4, 5, 9, 10, 12, -4)
flag = False
for item in tuple_1:
    if item in tuple_2:
        flag = True
print(f"2 tuple có phần tử chung hay không? {flag}")
