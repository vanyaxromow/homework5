immutable_var = 1, 2, 3, 4, 5, 'Name', False
print(immutable_var)
# immutable_var[0] = 13 элементы кортежа неизменяемы
mutable_list = [144, 12, 155, 'First']
mutable_list[0] = 'Name'
mutable_list.append('Time')
mutable_list.extend('RUS')
mutable_list.remove(12)
print(mutable_list)
