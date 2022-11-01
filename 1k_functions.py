import math
import random
from datetime import datetime


def coin_toss():
    return random.choice(["Heads", "Tails"])


def is_even_odd(x):
    return 'even' if (x % 2 == 0) else 'odd'


def celsius_to_fahrenheit(temperature):
    return temperature * 9/5 + 32


def fahrenheit_to_celsius(temperature):
    return (temperature - 32) * (5/9)


def celsius_to_kelvin(temp_c):
    return temp_c + 273.15


def fahr_to_kelvin(temp_f):
    temp_c = fahrenheit_to_celsius(temp_f)
    temp_k = celsius_to_kelvin(temp_c)
    return temp_k


def get_BMI(weight, height):
    return weight / height ** 2


def calculate_tip(bill, percent):
    tip = bill * percent/100
    return tip


def arithmetic_mean(first, *values):
    return (first + sum(values)) / (1 + len(values))


def absolute_value(num):
    return num if num >= 0 else -num


def area_circle(radius):
    pi = 3.14159
    area = pi * radius**2
    return area


def area_cylinder(radius, height):
    circle_area = area_circle(radius)
    height_area = 2 * radius * math.pi * height
    return 2*circle_area + height_area


def volume_cylinder(radius,height):
    area = area_circle(radius)
    return area * height


def find_area(r):
    Pi = 3.14
    return Pi * (r*r)


def area_of_triangle(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt((s*(s-a)*(s-b)*(s-c)))


def rhombus_area(p, q):
    result = (p*q) / 2
    return result


def maximum(*numbers):
    if len(numbers) == 0:
        return None
    else:
        maxnum = numbers[0]
        for n in numbers[1:]:
            if n > maxnum:
                maxnum = n
        return maxnum


def add_tax(price, tax_rate):
    return price + (price * tax_rate)


def add_numbers(*num):
    sum_ = 0
    for n in num:
        sum_ = n + sum_
    return f'Sum is:{sum_}'


def calculate_si_amount(principal, rate, time):
    interest =  (principal*rate*time)/100
    return principal+interest


def generate_random_number(start_value, stop_value):
    return random.randint(0, 100)


def volume_sphere(r):
    return (4/3) * math.pi * r ** 3


def volume_cuboid(w, h, l):
    return w * h * l


def volume_cone(r, h):
    return math.pi * r ** 2 * h / 3


def volume_pyramid(w, h, l):
    return (1/3) * w * h * l


def calculate_trapezoid(a, b, height):
    trapezoid_area = ((a + b) / 2) * height
    return trapezoid_area


def dog_age(human_age):
    if human_age <= 2:
        return human_age * 10.5
    else:
        return 21 + (human_age - 2) * 4


global_variable = 'I am available everywhere'


def local_and_global_function():
    print(global_variable)  # because is global
    local_variable = "only available within this function"
    print(local_variable)


def cube(x):
    return x * x * x


def power_number(number, power):
    return number ** power


def power_list(numbers_list, power):
    result = []
    for i in numbers_list:
        result.append(i ** power)
    return result


def volume_of_cuboid(length, breadth, height):
    return length * breadth * height


def get_date(year, month, day):
    date = str(day) + '/' + str(month) + '/' + str(year)
    return date


def calculate_average(values):
    return None if len(values) == 0 else sum(values) / len(values)


def calc_seconds_in_your_age(age):
    return 60 * 60 * 24 * 7 * 52 * age


def get_even_number_from_list(list_of_numbers):
    result = []


def get_module_name():
    return __doc__


def get_module_file():
    return __file__


def swap_value(x, y):
    temp = x
    x = y
    y = temp


def max_of_two(x, y):
    if x > y:
        return x
    return y


def max_of_three(x, y, z):
    return max_of_two(x, max_of_two(y, z))


def calculate_cuboid(a, b, c):
    return a * b * c


def convert_cm_to_dm(cm):
    return cm * 0.001


def write_a_book(character, setting, special_skill):
    return character + " is in " + setting + " practicing her " + special_skill


def check_leap_year(year):
    if year % 4 == 0:
        return str(year) + " is a leap year."
    else:
        return str(year) + " is not a leap year."


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def get_ing(wd):
    return wd + 'ing'


def same_initial(wd1, wd2):
    if wd1[0].lower() == wd2[0].lower():
        return True
    else:
        return False


def in_both(wd1, wd2):
    common = []
    for c in wd1:
        if c in wd2:
            common.append(c)
    return sorted(common)


def odd_or_even(a):
    if a > 0:
        return "Positive"
    elif a <0:
        return "Negative"
    else:
        return "Zero"


def count_vowels(in_string):
    num_vowels = 0
    vowels = "aeiouAEIOU"

    for char in in_string:
        if char in vowels:
            num_vowels += 1
    return num_vowels


def is_bounded(x, lower, upper):
    return lower <= x <= upper


def count_even(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += 1
    return total


def max_or_min(x, y, mode="max"):
    if mode == "max":
        return max(x, y)
    elif mode == "min":
        return min(x, y)
    else:
        return None


def print_current_date():
    current_date = datetime.now().date()
    print(current_date)


def get_average(*args):
    return sum(args) / len(args)


def check_anagrams(word1, word2):
    return sorted(word1) == sorted(word2)


def capitalize_sentences(sentences):
    result = sentences.copy()
    for index, item in enumerate(result):
        result[index] = item.capitalize()
    return result


def fibonacci(n):
    if n < 1:
        return 0
    if n < 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def cuboid_surface_area(a, b, c):
    result = 2 * a + 2 * b + 2 * c
    return result


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


print(coin_toss())
print(is_even_odd(5))
print(celsius_to_fahrenheit(20))
print(fahrenheit_to_celsius(67))
print(celsius_to_kelvin(30))
print(fahrenheit_to_celsius(45))
print(get_BMI(99, 200))
print(calculate_tip(50, 10))
print(arithmetic_mean(45, 32, 89, 78))
print(absolute_value(-5))
print(area_circle(10))
print(area_cylinder(10, 100))
print(volume_cylinder(10, 100))
print(find_area(10))
print(area_of_triangle(10, 15, 10))
print(rhombus_area(10, 15))
print(maximum([12, 14, 16]))
print(add_tax(100, 23))
print(add_numbers(2, 3, 4))
print(calculate_si_amount(100, 40, 56))
print(generate_random_number(10, 13))
print(volume_sphere(13))
print(volume_cuboid(13, 12, 11))
print(volume_cone(13, 14))
print(volume_pyramid(13, 14, 11))
print(calculate_trapezoid(2, 4, 5))
print(dog_age(30))
local_and_global_function()
print(cube(3))
print(power_number(2, 2))
print(power_list([2, 3, 4], 2))
print(volume_of_cuboid(10, 10, 10))
print(get_date(1992, 20, 3))
print(calculate_average([20, 40, 60]))
print(calc_seconds_in_your_age(30))
print(get_module_name())
print(get_module_file())
# print(swap_value(4, 5))
print(max_of_two(45, 55))
print(max_of_three(45, 55, 67))
print(calculate_cuboid(30, 21, 25))
print(get_absolute_value(15750))
print(write_a_book('spiderman', 'home', 'life'))
print(check_leap_year(2022))
print(add(10, 15))
print(subtract(10, 15))
print(multiply(10, 15))
print(divide(10, 15))
print(get_ing('walk'))
print(same_initial('apple', 'orange'))
print(in_both('pear', 'apple'))
print(odd_or_even(-2))
print(count_vowels("Hi my name is Ryan"))
print(is_bounded(5, 10, 15))
print(count_even((5, 10, 15)))
print(max_or_min(14, 24, 'min'))
print_current_date()
print(get_average(15, 23))
print(check_anagrams('kajak', 'kajak'))
print(capitalize_sentences(['ala ma kota', 'Litwo ojczyzno moja']))
print(fibonacci(10))
print(cuboid_surface_area(10, 15, 20))

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
