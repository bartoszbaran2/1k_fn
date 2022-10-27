# built-in

def get_absolute_value(item):
    if isinstance(item, (list, tuple)):
        return [abs(number) for number in item]
    else:
        return abs(item)


def get_binary(number):
    return bin(int(number))


def get_character(item):
    return [chr(code) for code in item] if isinstance(item, (list, tuple)) else chr(item)


def div_with_rest(num1, num2):
    return divmod(num1, num2)


# built-in
print(get_absolute_value(-5.4))
print(get_binary(-55))
print(get_character([8364, 49]))
print(div_with_rest(5, 5))
