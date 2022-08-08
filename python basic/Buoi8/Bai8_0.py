my_dict = {
    1: -6,
    2: 9,
    3: 10,
}
multi_values = 1
for k, v in my_dict.items():
    multi_values *= v

print(f"Tích các value: {multi_values}")
