def is_pangram(_str, alphabet):
    """
    Kiểm tra có phải là pangram không
    """
    convert_str = str(_str)
    lower_str = convert_str.lower()
    str_set = set(lower_str)
    alphabet_set = set(alphabet)
    if str_set.issuperset(alphabet_set) or str_set == alphabet_set:
        return True
    return False


print(is_pangram("abc012", "abc012"))

# Bài 06: Viết hàm
#         def is_pangram(str, alphabet)
#     đề kiểm tra xem chuỗi str có phải là Pangram không, trả lại True nếu có, False nếu không
#     Ghi chú: Pangram là chuỗi chứa mỗi chữ cái trong bảng alphabet ít nhất 1 lần


def is_pangram(str, alphabet):
    for c in alphabet:
        if c not in str:
            return False
    return True
