a = [1, 3, "Duc", "9"]
b = [6, 5, "duc", "8", 6]
c = 0  # 0 là 2 list khác nhau, >0 là 2 list giống nhau
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[i]:
            c += 1

if c == 0:
    print("2 list khác nhau")
else:
    print("2 list giống nhau")


chung = False
for item in a:
    if item in b:
        chung = True
        break
print(f"Hai list có phần tử chung không? {chung}")
