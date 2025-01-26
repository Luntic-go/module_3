def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        if int(str_number[0]) != 0:
            return first * get_multiplied_digits(int(str_number[1:]))
        else:
            return get_multiplied_digits(int(str_number[1:]))
    else:
        if first == 0:
            first = 1
        return first


result1 = get_multiplied_digits(40203)
result2 = get_multiplied_digits(402030)

print(result1)
print(result2)
