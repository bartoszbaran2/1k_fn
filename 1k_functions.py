def get_date(year, month, day):
    date = str(day) + '/' + str(month) + '/' + str(year)
    return date


def calculate_average(values):
    return None if len(values) == 0 else sum(values) / len(values)


def calc_seconds_in_your_age(age):
    return 60 * 60 * 24 * 7 * 52 * age


def get_even_number_from_list(list_of_numbers):
    result = []


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


def get_hash_value(item):
    return hash(item)


def get_help(item):
    return help(item)


def get_id(item):
    return id(item)


def get_user_name():
    username = input('Enter your name: ')
    return username


def add_two_lists(numbers1, numbers2):
    result = list(map(lambda x, y: x + y, numbers1, numbers2))
    return result


def get_max_from_list(numbers):
    return max(numbers)


def get_min_from_list(numbers):
    return min(numbers)


def read_text_file(path, mode):
    result = open(path, mode)
    return result.read()


def find_unicode(char):
    return ord(char)


def power_numbers(number1, number2, module):
    return pow(number1, number2, module)


def reverse_iterable(iterable):
    return list(reversed(iterable))


def round_float(number, digits):
    return round(number, digits)


def get_your_initials(name):
    return name[slice(0, 1)]*2


def get_unique_list(list_of_numbers):
    return set(list_of_numbers)


print(get_date(1992, 20, 3))
print(calculate_average([20, 40, 60]))
print(calc_seconds_in_your_age(30))

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
print(get_hash_value('ala ma kota'))
# print(get_help('print'))
print(get_id(5))
# print(get_user_name())
print(add_two_lists([1, 2, 3], [10, 10, 10]))
print(get_max_from_list([10, 15, 20]))
print(get_min_from_list([10, 15, 20]))
print(read_text_file('text.txt', 'r'))
print(find_unicode('B'))
print(power_numbers(7, 2, 5))
print(reverse_iterable((2, 3, 4, 5)))
print(round_float(5.6666, 3))
print(get_your_initials('bartek'))
print(get_unique_list([2, 3, 4, 4, 4, 5]))
