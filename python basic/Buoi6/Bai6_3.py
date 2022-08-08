_str = input("Nhập chuỗi s = ")
my_list = [1, 2, 3]
copy_list = my_list.copy()
edit_list = []


for i in range(len(my_list)):
    b = str(copy_list[i])
    b += _str
    edit_list.append(b)

print(f"List cũ = {my_list}")
print(f"List mới = {edit_list}")


# Cái này a đã cho str trước trong list rồi nên việc xử lí thành str ko còn qua trọng
the_list = ["girl", "mot", "hai", "Hai", "Huy", "Cuong", "PythonCore"]
s = input("Nhập chuỗi s: ")

# Cách 1:
new_list = []
for item in the_list:
    new_list.append(s + item)
print(f"List mới: {new_list}")

# Cách 2: list comprehension
new_list = [s + item for item in the_list]
print(f"List mới: {new_list}")
