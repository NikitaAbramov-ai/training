my_dict = {'Denis': 2003,"Max": 2002,"Nikita": 2000}
print(my_dict)
print(my_dict["Denis"])
print(my_dict.get("Vika", "Нету такого имени!"))
my_dict.update({'Nina': 1999,
                'Lera': 2002})
del my_dict['Max']
print(my_dict)

my_set = {1,2,3,"a",4,1,2,3,"b","a","a"}
print(my_set)
my_set.add("c")
my_set.remove(2)
print(my_set)
