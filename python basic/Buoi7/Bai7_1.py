my_tuple = (1, 3.14, "tuple", [1, 9, "list"], {3.14, "set"})
a = list(my_tuple)
print(a)
print(type(a))

my_list = [1, "string", 3.14, ("tuple", 3.14), {"set", 3.14, 3}]
b = tuple(my_list)
print(b)
print(type(b))
