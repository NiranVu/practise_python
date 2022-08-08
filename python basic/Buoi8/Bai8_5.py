my_dict = {"name": "Duc", "age": 21, "salary": 200, "city": "Ho Chi Minh"}
request = ["name", "salary"]
output = {}
for i in range(len(request)):
    for k, v in my_dict.items():
        if request[i] == k:
            output.update({k: v})
print(output)


sample = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
keys = ["name", "salary"]
result = {k: sample[k] for k in keys}
print(f"Kết quả của bài toán {result}")
