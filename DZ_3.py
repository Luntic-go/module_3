values_list = ['string', 2, False]
values_dict = {
    'a': True,
    'b': 'string',
    'c': 3}
values_list_2 = [54.32, 'Строка' ]
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25)
print('======================================')
print_params(c = [1,2,3])
print('======================================')
print_params(*values_list)
print('======================================')
print_params(**values_dict)
print('======================================')
print_params(*values_list_2, 42)
