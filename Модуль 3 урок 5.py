def get_multiplied_digits(number):
    str_number = str(number)
    s1 = str_number.replace("0", "1")
    if len(s1) > 1:
        first = int(s1[0])
        return first * get_multiplied_digits(int(s1[1:]))
    else:
        return int(s1)


result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)
