A = [[3, 0, 0], [0, 3, 1], [2, 0, 1]]  # Với mxn
B = [[1, 3, 0], [0, 0, 3], [4, 0, 0]]  # Với nxp
C = []
for m in range(3):  # Cho chạy hàng
    row = []  # Sau mỗi vòng lặp thì nó tạo ra một hàng mới
    for p in range(3):  # Cho chạy cột
        c = 0  # sau mỗi vòng lặp nó tạo một cái c mới
        for n in range(3):  # Tạo ra số vòng lặp nhân
            c += A[m][n] * B[n][p]  # C[m][p]
        row.append(c)  # Đưa từng giá trị sau khi cộng vào list
    C.append(row)  # Đưa row vào trong matrix


print(C)
