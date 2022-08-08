my_string = "Duc la ai a a a b bc bn"
split_str = my_string.split(" ")
set_str = set(split_str)
covert_set_list = list(set_str)
dict_count = {}
for i in range(len(covert_set_list)):
    # if len(covert_set_list[i]) == 1:
    v = split_str.count(covert_set_list[i])
    dict_count.update({covert_set_list[i]: v})

print(dict_count)


from string import punctuation
import re

input_09 = (
    """Mot cau van trong doan van. Day la vi du ve sinh doan van de tach tu don."""
)
r = re.compile(r"[\s{}]+".format(re.escape(punctuation)))
set_word = r.split(input_09)
result = {}
for w in set_word:
    result[w] = set_word.count(w)
print(f"Kết quả của bài toán: {result}")
