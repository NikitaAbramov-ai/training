def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
    # 1.Функция с параметрами по умолчанию:
print_params()
print_params(b=25)
print_params(c=[1,2,3])

    #2.Распаковка параметров:
values_list = [2,"Число", True]
values_dict = {'a':'Число', 'b':True, 'c':2}
print_params(*values_list)
print_params(**values_dict)

    #3.Распаковка + отдельные параметры:
values_list_2 = [3,'Цифра']
print_params(*values_list_2, 42)