def count_odd_num(n):
    if n < 10:
        if n % 2 == 0:
            return 0
        else:
            return +1
    # if n == 0:
    #     return 0
    else:
        if (n % 10) % 2 == 0:
            return count_odd_num(n // 10)
        else:
            return count_odd_num(n // 10) + 1


print(count_odd_num(134))

# Bài 09: Viết hàm đệ quy đếm và trả về số lượng chữ số lẻ của số nguyên dương n cho trước.
#         Ví dụ: Hàm trả về 4 nếu n là 19922610 (do n có 4 số lẻ là 1, 9, 9, 1)


def count_odd(n):
    if n < 10:
        return n % 2
    else:
        return (n % 10) % 2 + count_odd(n // 10)
