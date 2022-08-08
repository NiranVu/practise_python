web_list = ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
a = []
for i in web_list:
    c = ""
    for j in range(-1, -len(i), -1):
        if i[j] != ".":
            c += i[j]
        else:
            break
    a.append(c[::-1])
print(a)

# C2:
list_domain = ["www.hust.edu.vn", "www.wikipedia.org", "www.asp.net", "www.amazon.com"]
list_hauto = []
for item in list_domain:
    list_hauto.append(
        item.split(".")[-1]
    )  # Xem chi tiết về hàm split trong bài học về String. Ở đây tách theo dấu chấm
print(f"Danh sách hậu tố của tên miền {tuple(list_hauto)}")
