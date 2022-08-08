with open("D:\project\index1.txt", mode="r", encoding="utf-8") as text_1:
    with open("D:\project\index3.txt", mode="w", encoding="utf-8") as text_3:
        for line in text_1:
            text_3.write(line)

with open("D:\project\index2.txt", mode="r", encoding="utf-8") as text_2:
    with open("D:\project\index3.txt", mode="a", encoding="utf-8") as text_4:
        for line in text_2:
            text_4.write(line)

with open("D:\project\index3.txt", mode="r", encoding="utf-8") as read1:
    print(read1.read())
