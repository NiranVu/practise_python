n = int(input("Nhập số n = "))

# #Khúc trên tam giác
# for i in range(1, n + 1): #Tạo loop việc xuống dòng
#    for j in range(1, n + 1): #Tạo loop cho cùng dòng
#        if i >= j:
#           print(j, end = ' ')
#    print()

for i in range(
    n, 0, -1
):  # cái này nỏ bỏ số 1 đi nên phải +1 or là đổi số 1 thành sống 0
    for j in range(
        1, n - i + 2
    ):  # +2 vì vd n = 6 thì 6 - 6 = 0 +2 thì từ range(1, 2) lấy được số 1
        print(j, end=" ")
    print()


# #Khúc xuống tam giác
# for i in range(1, n):
#    for j in range(1, n - i + 1):
#        print (j, end = ' ')
#    print()

for i in range(n, 1, -1):
    for j in range(1, i):
        print(j, end=" ")
    print()
