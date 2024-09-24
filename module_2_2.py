first = int(input("Ввидете 1 число: "))
second = int(input("Ввидите 2 число: "))
third  = int(input('Ввидете 3 число: '))
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)