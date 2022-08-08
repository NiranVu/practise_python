set_1 = {3, 9, 5, 3.9, 6.5, 4.5, "string", "Duc", (9, 6, "Duc")}
set_2 = {9, 4, 4.9, 6.9, 3.9, "string", (9, 6, "Duc")}

set_1.difference_update(set_2)
print(set_1)  # nó bằng với a = set_1.difference_update(set_2)
set_1.intersection_update(set_2)
print(set_1)  # nó bằng với a = set_1.intersection(set_2)
a = set_1.isdisjoint(set_2)
print(a)
b = set_1.issubset(set_2)
print(b)
c = set_1.issuperset(set_2)
print(c)
set_1.symmetric_difference_update(set_2)
print(set_1)  # nó băng với a = set_1.symmetric_difference_update(set_2)
