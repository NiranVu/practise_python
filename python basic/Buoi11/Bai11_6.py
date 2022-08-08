a = []
with open("D:\project\index4.txt", mode="r", encoding="utf-8") as text_1:
    for line in text_1:
        for i in line:
            a.append(i)

print(a)
