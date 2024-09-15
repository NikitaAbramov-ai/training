immutable_var = 1,2,"a","b"
print(immutable_var)
    #immutable_var[0] = 200              В круглых скобка не изменяемый список
mutable_list = [1,2,3,"apple"]
print(mutable_list)
mutable_list.append("banana")
mutable_list.remove(2)
mutable_list[0] = 200
print(mutable_list)
