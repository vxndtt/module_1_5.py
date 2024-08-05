tuple_ = 1, 2, True, 'Fall'
immutable_var = tuple_
print(immutable_var)
#tuple_[2] = 3 (Не является изменяемым значением, не является сложением или умножением, действие невозможно)
mutable_list = [23, False, 'List']
print(mutable_list)
mutable_list[1] = True
print(mutable_list)