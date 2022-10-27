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


def count_iterations(iterable, start_param=0):
    return list(enumerate(iterable, start_param))


def calculate_expression(op=''):
    if op == '': op = input('enter math operation to perform: ')
    return eval(op)


def filter_adult_persons(persons_dict):
    adult_persons = filter(lambda person: person[1] >= 18, persons_dict.items())
    return [person[0] for person in adult_persons]


def say_hello(name, title=''):
    text = 'Hello {title} {name}'.format(title=title.capitalize(), name=name.capitalize())
    return text


def get_global_with_own_args(func_name, **kwargs):
    return globals()[func_name](**kwargs)


# built-in
print(get_absolute_value(-5.4))
print(get_binary(-55))
print(get_character([8364, 49]))
print(div_with_rest(5, 5))
print(count_iterations('janusz', 8))
print(calculate_expression('3 * 12'))
print(filter_adult_persons({'tomek': 16, 'ania': 24, 'jarek': 36, 'marek': 4}))
print(say_hello('adam'))
print(get_global_with_own_args('say_hello', name='janusz', title='mr'))
