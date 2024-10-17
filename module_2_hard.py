def password(number):
    passsword = ''
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                passsword += str(i) + str(j)
    return passsword
print('Введите число: ')
print(password(int(input())))
