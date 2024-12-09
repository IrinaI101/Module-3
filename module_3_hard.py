def calculate_structure_sum(args):
    sum_data = 0
    for i in args:
        if isinstance(i, (list, set, tuple)):
            sum_data += calculate_structure_sum(i)
        elif isinstance(i, dict):
            sum_data += calculate_structure_sum(i.keys())
            sum_data += calculate_structure_sum(i.values())
        elif isinstance(i, str):
            sum_data += len(i)
        elif isinstance(i, (int, float)):
            sum_data += i
    return sum_data

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)










