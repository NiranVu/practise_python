# C1: Nếu trong tuple toàn các phần tử bất biến
tuple_0 = (1, 6, "string", 9, "Duc")
a = set(tuple_0)
if len(tuple_0) != len(a):
    print("Trong tuple có phần tử giống nhau")
else:
    print("Trong tuple không có phần tử nào giống nhau")

# C2:
tuple_the_same = (0, 0.0, 0 ** 1, 0 * 9, 0 / 2)
if tuple_the_same.count(tuple_the_same[0]) == len(tuple_the_same):
    print("Tất cả các phần tử trong tuple CÓ giống nhau")
else:
    print("Tất cả các phần tử trong tuple KHÔNG giống nhau")

# #C2: nếu trong tuple có các phần tử không bất biến
# tuple_1 = ([1, 3.5, 'list'], 2, [3, 5])
# c = 0 #> 0 là có phần tử giống nhau, = 0 không có phần tử giống nhau
# for i in range(len(tuple_1)):
#     # for j in range(len(tuple_1)):
#     #     if tuple_1[i] == tuple_1[j]: #Có vẻ cái này nó chỉ so sánh type chứ không so sánh phần tử phía trong
#     #         c += 1
#     #     else:
#     #         continue
#     if
# if c > 0:
#     print('Trong tuple có phần tử giống nhau')
# else:
#     print('Trong tuple không có phần tử nào giống nhau')
# #Thôi e bí :D có gì e hỏi a sau
