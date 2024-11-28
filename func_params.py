def print_params (a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(False, 25, 'sky')
print_params('star', 38)
print_params('candy')
print_params(b=25)
print_params(c=[1,2,3])

values_list = ['bird', False, 58]
values_dict = {'a': True, 'b': 64, 'c': 'forest'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['cat', False]
print_params(*values_list_2, 42)
