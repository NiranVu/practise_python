a = [1, 2, 1, 3, 2, 7, 4, 2, 5, 5]
c = []
for i in range(len(a)):
    if a[i] not in c:
        c.append(a[i])
print(f"Chuỗi bài hát dài nhất mà không có lặp lại {c}")
