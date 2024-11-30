def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(78095)
print(result)
result1 = get_multiplied_digits(5006783)
print(result1)
result2 = get_multiplied_digits(5)
print(result2)