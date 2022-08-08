import random

# Lần chơi đầu
suc_xac1 = random.randrange(1, 7)
suc_xac2 = random.randrange(1, 7)
result = suc_xac1 + suc_xac2
print(result)
if result == 7 or result == 11:
    print("Bạn là người chiến thắng")
elif result == 2 or result == 3 or result == 12:
    print("Bạn là người thua")
else:
    print("Mời bạn qua màn tiếp theo")
    print(
        "Luật: Để giành được THẮNG, người chơi tiếp tục tung 2 con xúc xắc cho đến khi ra được tổng = ĐIỂM trong lần đầu tiên; nếu tung ra được tổng = 7 => Người chơi THUA"
    )
    while True:
        after_suc_xac1 = random.randrange(1, 7)
        after_suc_xac2 = random.randrange(1, 7)
        after_result = after_suc_xac1 + after_suc_xac2
        print(after_result)
        if after_result:
            if after_result == result:
                print("Bạn chiến thắng")
                break
            if after_result == 7:
                print("Bạn thua cuộc")
                break

# Bài 01: Xem code đã có trong file btvn_01_dog.py.
# Viết đoạn chương trình vào tiếp trong file đó để giải quyết yêu cầu sau:
#     - Tạo ra 3 đối tượng Dog với các thuộc tính về age khác nhau:
#         name        age
#         Fake         2
#         Mickey       7
#         Fuk          5
#     - Sau đó, viết một hàm get_biggest_number(*args) nhận vào nhiều tham số, sau đó trả về số lớn nhất.
#     - Và dựa trên hàm này, hay tìm và in ra có dạng như sau:
#         The oldest dog is 7 years old.


class Dog:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age
