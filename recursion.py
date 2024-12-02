def get_multiplied_digits(number):
    str_number = str(number)
    if '0' in str_number:
        str_number = str_number.replace('0', '')
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    if len(str_number) <= 1:
        return first

result = get_multiplied_digits(78095)
print(result)
result1 = get_multiplied_digits(5006783)
print(result1)
result2 = get_multiplied_digits(403020)
print(result2)
result3 = get_multiplied_digits(5)
print(result3)
