	my_list = [{
    'item': 'item1',
    'amount': 400
}, {
    'item': 'item2',
    'amount': 300
}, {
    'item': 'item1',
    'amount': 200
} ,{
    'item': 'item1',
    'amount': 750
}, {
    'item': 'item3',
    'amount': 500
}, {
    'item': 'item3',
    'amount': 300
}]
dict_wish = {}
#Lấy từng giá trị cụ thể mong muốn
for i in range(len(my_list)):
    _item_i = my_list[i]['item']
    _amount_i = my_list[i]['amount']
    c = _amount_i
#Đem so sánh rồi cộng vào
    for j in range(len(my_list)):
        _item_j = my_list[j]['item']
        _amount_j = my_list[j]['amount']
        if _item_i == _item_j and i != j:
            c += _amount_j
            dict_wish.update({_item_i : c})
        elif _item_i != _item_j and _item_i not in dict_wish:
            dict_wish.update({_item_i : _amount_i})


print(dict_wish)


input = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
output = {}
for ele in input:
    name = ele['item']
    amount = ele['amount']
    if name in output:
        output[name] += amount
    else:
        output[name] = amount
print(f'Kết quả: {output}')