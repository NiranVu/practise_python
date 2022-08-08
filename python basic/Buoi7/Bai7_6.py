my_tuple = (3, -6, "string", [1, 2, 3], "Duc", 3.14, {"set", 1, 3, 3.14}, (1, 3, 6))
if len(my_tuple) >= 4:
    print(f"Phần tử thứ 4 là {my_tuple[3]}")
    print(f"Phần tử thứ 4 từ cuối lên là {my_tuple[-4]}")
else:
    print("Tuple của bạn không đủ phần tử")
