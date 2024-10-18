
def summa_(data_structure):
    summa = 0
    if data_structure == []:
        return summa
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            summa += summa_(key)
            summa += summa_(value)
    elif isinstance(data_structure, (tuple, set, list)):
        for i in data_structure:
            summa += summa_(i)
    elif isinstance(data_structure, (int, float)):
        summa += data_structure
    elif isinstance(data_structure, str):
        summa += len(data_structure)
    return summa

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = summa_(data_structure)
print('Result:', result)
