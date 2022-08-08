a = [1, 9, 6, 9, 10, 4, 3]
b = 0
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] > a[j] and i < j:
            b += 1
            print(f"Cặp giá trị là {a[i]} tại {i} và {a[j]} tại {j}")

print(f"Số phần tử thỏa A[i] > A[j] và i < j là {b}")

n = len(a)
count = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            count += 1
print(f"Có {count} cặp số thỏa mãn")
