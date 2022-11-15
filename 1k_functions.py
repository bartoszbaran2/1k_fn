import math
import random
import re
import statistics
import string
from datetime import datetime, timedelta, date


def coin_toss():
    return random.choice(["Heads", "Tails"])


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = [r, g, b]
    return rgb


def random_color2():
    hexadecimal = ["#" + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
    return "A Random color is :", hexadecimal


def boolean_to_string(b):
    return 'True' if b else 'False'


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


def get_bmi(weight, height):
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


def volume_cylinder(radius, height):
    area = area_circle(radius)
    return area * height


def find_area(r):
    pi = 3.14
    return pi * (r*r)


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
    interest = (principal*rate*time)/100
    return principal+interest


def generate_random_number(start_value, stop_value):
    return random.randint(start_value, stop_value)


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


def h_to_min(hours):
    return hours * 60


def calculate_rectangle_area(a, b):
    return a * b


def calculate_parallelogram_area(width, height):
    return width * height


def calculate_triangle_area(height, width):
    return (height * width) / 2


def calculate_trapezoid_area(a, b, h):
    return (a + b) * h / 2


def calculate_ellipse_area(major_axis, minor_axis):
    return math.pi * major_axis * minor_axis


def circular_sector_area(angle, radius):
    return angle * (math.pi * radius / 360)


def regular_hexagon_area(side):
    return 3 * side * math.sqrt(3)


def deltoid_area(height, width):
    return height * width / 2


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


def is_fibonacci(n):
    s = []
    a, b = 0, 1
    while a <= n:
        s = [a]
        a, b = b, a + b
    if n in s:
        return True
    else:
        return False


def calculation_two_numbers(a, b):
    addition = a + b
    substraction = a - b
    return addition, substraction


def total_list_value(lst):
    acc = 0
    for x in lst:
        acc = acc + x
    return acc


def is_longer_then_5(lst):
    if len(lst) >= 5:
        return "Longer than 5"
    else:
        return "Less than 5"


def reverse_string(my_str):
    reversed_str = ''
    for char in my_str:
        reversed_str = char + reversed_str
    return reversed_str


def mirror_string(p_phrase):
    string_length = len(p_phrase)
    r_phrase = p_phrase[string_length::-1]
    return p_phrase + r_phrase


def is_number_in_range(num, low, high):
    for i in range(low,high+1):
        if num == i:
            return 'Number is within the range'
        else:
            return 'Number is out of range'


def unique_list(array):
    x = set(array)
    return list(x)


def is_palindrome(s):
    reverse_s=s[::-1]
    if s == reverse_s:
        return 'string is palindrome'
    else:
        return'not a palindrome'


def remove_letter(letter, text):
    if letter in text:
        return text.replace(letter, "")
    else:
        return text


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
    elif a < 0:
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


def get_current_date():
    current_date = datetime.now().date()
    return current_date


def get_current_date_time():
    datetime_object = datetime.now()
    return datetime_object


def get_current_time():
    return datetime.now().strftime('%H:%M:%S')


employees = [{
        'name': 'Jane',
        'salary': 90000,
        'job_title': 'developer'
    }, {
        'name': 'Bill',
        'salary': 50000,
        'job_title': 'writer'
    }, {
        'name': 'Kathy',
        'salary': 120000,
        'job_title': 'executive'
    }, {
        'name': 'Anna',
        'salary': 100000,
        'job_title': 'developer'
    }, {
        'name': 'Dennis',
        'salary': 95000,
        'job_title': 'developer'
    }, {
        'name': 'Albert',
        'salary': 70000,
        'job_title': 'marketing specialist'
    }]


def is_developer(employee):
    return employee['job_title'] == 'developer'


def is_not_developer(employee):
    return employee['job_title'] != 'developer'


def get_developers():
    developers = list(filter(is_developer, employees))
    return developers


def get_non_developers():
    non_developers = list(filter(is_not_developer, employees))
    return non_developers


def get_salary(employee):
    return employee['salary']


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


def make_upper(word):
    return word.upper()


def make_lower(word):
    return word.lower()


def reverse_word(word):
    return word[::-1]


def count_letters(letter, sentence):
    counter = 0

    for letter_ in sentence:
        if letter in letter_:
            counter += 1

    return counter


def calculate_speed(distance, time):
    return distance / time


def calculate_salary(amount, working_hours):
    return amount * working_hours


def meters_to_feet(meters):
    return meters * 3.28084


def km_to_miles(km):
    return km * 0.621371192


def find_array_item(array, item):
    result = None
    for element in array:
        if array.index(element) == item:
            result = element

    return result


def generate_full_name(first_name, last_name):
    full_name = first_name.capitalize() + ' ' + last_name.capitalize()
    return full_name


def count_capital_letters(string):
    counter = 0
    for char in string:
        if char.isupper():
            counter += 1
    return counter


def pascal_to_hpa(pascals):
    return pascals / 100


def pascal_to_bar(pascals):
    return pascals * math.pow(10, -5)


def pascal_to_newton_on_sq_mm(pascals):
    return pascals * math.pow(10, -6)


def pascal_to_kg_on_sq_m(pascals):
    return round(pascals/ 9.80665, 2)


def pascal_to_at(pascals):
    return round(pascals / 98066.5, 2)


def pascal_to_atm(pascals):
    return pascals / 101325


def pascal_to_tr(pascals):
    return round(pascals / 133.322, 2)


def pascal_to_psi(pascals):
    return round(pascals / 6894.76, 2)


def joul_to_kj(jouls):
    return jouls / 1000


def joul_to_kgm(jouls):
    return round(jouls / 9.80665, 2)


def joul_to_wh(jouls):
    return round(jouls / 3600, 2)


def joul_to_kwh(jouls):
    return jouls / 3600000


def joul_to_cal(jouls):
    return jouls / 4.1268


def joul_to_kcal(jouls):
    return jouls / 4186.8


def is_item_in_array(array, item):
    if item in array:
        return f'{item} found in array'
    else:
        return f'{item} not found'


def dollar_to_euro(dollar_value):
    return dollar_value * 0.89


def euro_to_yen(euro_value):
    return euro_value * 124.15


def random_int_in_range(a, b):
    return random.randrange(a, b)


def random_choice_from_array(array):
    return random.choice(array)


def shuffle_array(array):
    return random.shuffle(array)


def random_from_0_to_1():
    return random.random()


def get_random_float_from_range(a, b):
    return random.uniform(a, b)


def get_random_float_from_range_with_param(a, b, c):
    return random.triangular(a, b, c)


def generate_random_numbers_list(start, end, length):
    return [random.randint(start, end) for _ in range(length)]


def generate_random_string_list(length):
    return [random.choice(string.ascii_letters) for _ in range(length)]


def seconds_to_minutes(sec):
    return sec / 60


def seconds_to_hours(sec):
    return sec / 3600


def seconds_to_days(sec):
    return sec / 86400


def seconds_to_weeks(sec):
    return sec / 604800


def seconds_to_months(sec):
    return sec / 2628000


def seconds_to_years(sec):
    return sec / 31536000


def hours_to_seconds(hours):
    return hours * 3600


def hours_to_minutes(hours):
    return hours * 60


def hours_to_microseconds(hours):
    return hours * 3600000000


def days_to_seconds(days):
    return days * 86400


def days_to_minutes(days):
    return days * 1440


def days_to_hours(days):
    return days * 24


def days_to_microseconds(days):
    return days * 86400000000


def get_center_string(text, param):
    return text.center(param)


def is_ends_with_dot(text):
    return text.endswith('.')


def join_array_by_param(array, param):
    return param.join(array)


def strip_string(text):
    return text.strip()


def replace_fruit(fruit):
    text = 'i like bananas'
    return text.replace('bananas', fruit)


def feet_to_milimeter(value):
    return value * 304.8


def feet_to_micrometer(value):
    return value * 304800


def feet_to_meter(value):
    return value * 0.30


def feet_to_mile(value):
    return value * 0.00018


def feet_to_kilometer(value):
    return value * 0.00030


def feet_to_yard(value):
    return value * 0.33


def feet_to_inch(value):
    return value * 12


def feet_to_centimeter(value):
    return value * 30.48


def mile_to_milimeter(value):
    return value * 1609344


def mile_to_micrometer(value):
    return value * 1609344000


def mile_to_nanometer(value):
    return value * 1609344000000


def mile_to_meter(value):
    return value * 1609.344


def mile_to_feet(value):
    return value * 5280


def mile_to_kilometer(value):
    return value * 1.609344


def mile_to_yard(value):
    return value * 1760


def mile_to_inch(value):
    return value * 63360


def print_truth():
    print('mam już dość!')


def m_to_km(meters):
    return round(meters / 1000, 2)


def min_to_h(minutes):
    return round(minutes / 60, 2)


def convert_f_to_c(temperature):
    return round((temperature - 32) * 0.5556, 2)


def convert_c_to_f(temperature):
    return round((temperature * 1.8) + 32, 2)


def convert_c_to_k(temperature):
    return temperature + 273.15


def count_letters_in_word(word):
    counter = 0

    for _ in word:
        counter += 1

    return counter


def count_digits_in_number(number):
    counter = 0

    while number > 0:
        counter += 1
        number = number // 10

    return counter


def count_elements_in_list(my_list):
    counter = 0
    for _ in my_list:
        counter += 1

    return counter


def check_alphanumeric(text):
    return text.isalnum()


def check_ascii(text):
    return text.isascii()


def check_decimal(text):
    return text.isdecimal()


def check_digit(text):
    return text.isdigit()


def check_identifier(text):
    return text.isidentifier()


def check_lower(text):
    return text.islower()


def check_printable(text):
    return text.isprintable()


def check_space(text):
    return text.isspace()


def check_if_title(text):
    return text.istitle()


def check_if_upper(text):
    return text.isupper()


def mean(x):
    return statistics.mean(x)


def fmean(x):
    return statistics.fmean(x)


def geometric_mean(data):
    return statistics.geometric_mean(data)


def median(data):
    return statistics.median(data)


def median_low(data):
    return statistics.median_low(data)


def median_high(data):
    return statistics.median_high(data)


def median_grouped(data):
    return statistics.median_grouped(data)


def mode(data):
    return statistics.mode(data)


def multi_mode(data):
    return statistics.multimode(data)


def standard_deviation(data):
    return statistics.pstdev(data)


def variance(data):
    return statistics.pvariance(data)


def standard_deviation2(data):
    return statistics.stdev(data)


def variance2(data):
    return statistics.variance(data)


def quantiles(data):
    return statistics.quantiles(data)


def covariance(x, y):
    return statistics.covariance(x, y)


def correlation(x, y):
    return statistics.correlation(x, y)


def linear_regression(x, y):
    return statistics.linear_regression(x, y)


def make_negative_number(number):
    if number > 0:
        return number * -1
    else:
        return number


def reverse_list(l):
    return l[::-1]


def reverse_text(text):
    return text[::-1]


def is_plural(n):
    if n == 1:
        return False
    else:
        return True


def auto_factory(brand, max_speed):
    return {
        'brand': brand,
        'speed': 0,
        'max_speed': max_speed,
        'engine': False
    }


def start_engine(car):
    if not car['engine']:
        car['engine'] = True
        print('Engine started')
    else:
        print('Engine already started')


def stop_engine(car):
    car['engine'] = False
    print('Engine stopped')


def accelerate(car, speed):
    if car['engine']:
        car['speed'] = min(car['speed'] + speed, car['max_speed'])
        print('Speed: {}'.format(car['speed']))
    else:
        print('Engine is not started')


# todo
def sort_todo(fn):
    def inner(*args, **kwargs):
        return sorted(fn(*args, **kwargs), key=lambda item: item['status'], reverse=True)
    return inner


def todo_app():
    tasks_list = []

    @sort_todo
    def todo_instance_(fn=None, **kwargs):
        return fn(tasks_list, **kwargs) if fn is not None else tasks_list

    return todo_instance_


def get_task(tasks_list, task_name, task_day):
    task = None
    for task in tasks_list:
        if task['title'] == task_name.lower() and task['day'] == task_day.lower():
            task = task
            break
    return task


def add_task(task_list, task):
    task_lowercase = dict((k.lower(), v.lower()) for k, v in task.items())
    task_list.append(task_lowercase)
    return task_list


def delete_task(task_list, task_name, task_day):
    task = get_task(task_list, task_name, task_day)

    if task is None:
        raise ValueError(f'can not find and delete task: {task_name}, try again!')

    task_list.remove(task)
    return task_list


def update_task(task_list, task_name, task_day, updates):
    task = get_task(task_list, task_name, task_day)

    if task is None:
        raise ValueError(f'can not find and update task: {task_name}, try again!')

    updates_lower = dict((k.lower(), v.lower()) for k, v in updates.items())

    task.update(updates_lower)
    return task_list


def search_task(task_list, title=''):
    return [task for task in task_list if title.lower() in task['title'].lower()]


def filter_by_status(task_list, status):
    task_list_by_status = []

    for task in task_list:
        if task['status'] == status:
            task_list_by_status.append(task)

    return task_list_by_status


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


product_data = {
    "name": "apple",
    "founder": "jabłko_polskie",
    "type": "fruit",
    "price": 1.88,
    "unit": 'kg',
    "country": "poland",
}


def get_product_price(product):
    return product.get('price')


def get_product_price2(product):
    return product['price']


def change_product_price(product, price):
    product['price'] = price
    return product['price']


def update_product(product, key, value):
    product.update({key: value})
    return product


def update_product2(product, key, value):
    product[key] = value


def get_today_date_time():
    date_ = datetime.today()
    return date_.strftime("%m/%d/%Y, %H:%M:%S")


def calculate_past_date(number_of_days):
    date_ = datetime.today() - timedelta(days=number_of_days)
    return date_.strftime("%m/%d/%Y")


def calculate_future_date(number_of_days):
    date_ = datetime.today() + timedelta(days=number_of_days)
    return date_.strftime("%m/%d/%Y")


def get_day_name_for_date(year, month, day):
    date_ = date(year, month, day)
    return date_.strftime('%A')


def get_current_time2():
    return datetime.now().strftime('%H:%M:%S')


def dollars_to_cents(amount):
    return f'{amount} dollars is: {amount * 100} cents'


def pln_to_eur(pln_amount):
    eur_amount = pln_amount / 4.72
    return f'{pln_amount} PLN is: {round(eur_amount, 2)} EUR'


def pln_to_usd(pln_amount):
    usd_amount = pln_amount / 4.76
    return f'{pln_amount} PLN is: {round(usd_amount, 2)} USD'


def pln_to_gpb(pln_amount):
    gpb_amount = round(pln_amount / 5.48, 2)

    return f'{pln_amount} PLN is: {gpb_amount} GPB'


def pln_to_chf(pln_amount):
    chf_amount = round(pln_amount / 4.8, 2)

    return f'{pln_amount} PLN is: {chf_amount} CHF'


def pln_to_aud(pln_amount):
    aud_amount = round(pln_amount / 3.06, 2)

    return f'{pln_amount} PLN is: {aud_amount} AUD'


def pln_to_bgn(pln_amount):
    bgn_amount = round(pln_amount / 2.39, 2)

    return f'{pln_amount} PLN is: {bgn_amount} BGN'


def pln_to_cad(pln_amount):
    cad_amount = round(pln_amount / 3.5, 2)

    return f'{pln_amount} PLN is: {cad_amount} CAD'


def pln_to_czk(pln_amount):
    czk_amount = round(pln_amount / 0.19, 2)

    return f'{pln_amount} PLN is: {czk_amount} CZK'


def pln_to_dkk(pln_amount):
    dkk_amount = round(pln_amount / 0.63, 2)

    return f'{pln_amount} PLN is: {dkk_amount} DKK'


def pln_to_hkd(pln_amount):
    hkd_amount = round(pln_amount / 0.6, 2)

    return f'{pln_amount} PLN is: {hkd_amount} HKD'


def pln_to_hrk(pln_amount):
    hrk_amount = round(pln_amount / 0.63, 2)

    return f'{pln_amount} PLN is: {hrk_amount} HRK'


def joule_to_ev(joul_amount):
    return joul_amount * 6.241509 * math.pow(10, 18)


def joul_to_ry(joul_amount):
    return joul_amount * 4.5874 * math.pow(10, 17)


def celsius_to_rankine(celsius):
    return (celsius + 273.15) * 1.8


def celsius_to_reaumur(celsius):
    return (celsius * 4) / 5


def celsius_to_romer(celsius):
    return celsius * 21 / 40 + 7.5


def celsius_to_delisle(celsius):
    return (100 - celsius) * 3 / 2


def celsius_to_newton(celsius):
    return celsius * 33 / 100


def rankine_to_celsius(rankine):
    return (rankine / 1.8) - 273.15


def reaumur_to_celsius(reaumur):
    return 1.25 * reaumur


def romer_to_celsius(romer):
    return (romer - 7.5) * 40 / 21


def delisle_to_celsius(delisle):
    return 100 - delisle * 2 / 3


def newton_to_celsius(newton):
    return newton * 100 / 33


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5 / 9


def fahrenheit_to_rankine(fahrenheit):
    return fahrenheit + 459.67


def fahrenheit_to_reaumur(fahrenheit):
    return (fahrenheit - 32) * 4 / 9


def fahrenheit_to_romer(fahrenheit):
    return (fahrenheit - 32) * 7 / 24 + 7.5


def fahrenheit_to_delisle(fahrenheit):
    return (212 - fahrenheit) * 5 / 6


def fahrenheit_to_newton(fahrenheit):
    return (fahrenheit - 32) * 11 / 60


def degree_to_arcminute(degree):
    return degree * 60


def degree_to_arcsecond(degree):
    return degree * 3600


def radian_to_degree(radian):
    return radian * 57.295779513082


def radian_to_gradian(radian):
    return radian * 63.661977236758


def radian_to_arcminute(radian):
    return radian * 3437.7467707849


def radian_to_arcsecond(radian):
    return radian * 206264.8062471


def radian_to_cycle(radian):
    return radian * 0.1592


def arcminute_to_radians(arcminute):
    return arcminute * (2 * math.pi) / 21600


def arcminute_to_degree(arcminute):
    return arcminute / 60


def arcminute_to_gradian(arcminute):
    return arcminute * 4 / 216


def arcminute_to_cycle(arcminute):
    return arcminute / 21600


def arcsecond_to_degree(arcsecond):
    return arcsecond / 3600


def arcsecond_to_arcminute(arcsecond):
    return arcsecond / 60


def arcsecond_to_gradian(arcsecond):
    return arcsecond * 4 / 12960


def arcsecond_to_cycle(arcsecond):
    return arcsecond / 1296000


def get_number():
    while True:
        try:
            result = int(input("Guess the number: "))
            break
        except ValueError:
            print("It's not a number")

    return result


def guess_the_number():
    secret_number = random.randint(1, 100)
    given_number = get_number()
    while given_number != secret_number:
        if given_number < secret_number:
            print("Too small!")
        else:
            print("Too big!")
        given_number = get_number()
    print("You Win!")


def get_numbers():
    result = set()
    while len(result) < 6:
        number = get_number()
        if 0 < number <= 49:
            result.add(number)

    return result


def print_numbers(numbers):
    print(", ".join(str(number) for number in sorted(numbers)))


def drawing_numbers():
    numbers = list(range(1, 50))
    random.shuffle(numbers)
    return set(numbers[:6])


def lotto():
    user_numbers = get_numbers()
    print("Your numbers:")
    print_numbers(user_numbers)

    random_numbers = drawing_numbers()
    print("Lotto numbers:")
    print_numbers(random_numbers)

    hits = 6 - len(random_numbers - user_numbers)

    print(f"You hit {hits} {'number' if hits == 1 else 'numbers'}!")


DICE_PATTERN = re.compile(r"^(\d*)D(\d+)([+-]\d+)?$")


POSSIBLE_DICES = (
    "100",
    "20",
    "12",
    "10",
    "8",
    "6",
    "4",
    "3"
)


def roll_the_dice(dice_code):
    match = DICE_PATTERN.search(dice_code)
    if not match:
        return "Wrong Input"

    multiply2, dice, modifier = match.groups()
    if dice not in POSSIBLE_DICES:
        return "Wrong Input"

    multiply2 = int(multiply2) if multiply else 1
    dice = int(dice)
    modifier = int(modifier) if modifier else 0

    return sum([random.randint(1, dice) for _ in range(multiply2)]) + modifier


def shorten(text):
    return ''.join(word[0] for word in text.split()).upper()


def name_sorter(names):
    result = {
        'female': [],
        'male': []
    }

    for name in names:
        if name[-1] == 'a':
            result['female'].append(name)
        else:
            result['male'].append(name)
    return result


def check_palindrome(text):
    text = text.lower().replace(' ', '')
    return text == text[::-1]


def div(start, end):
    return [i for i in range(start, end + 1) if i % 2 == 0 and i % 3 != 0]


def roll(dices, dice_type=6, modifier=0):
    if dice_type not in (3, 4, 6, 8, 10, 12, 100):
        raise Exception("No such dice!")
    return sum(random.randint(1, dice_type) for _ in range(dices)) + modifier


def herz_to_kiloherz(herz):
    return herz / 1000


def herz_to_hektorez(herz):
    return herz / 100


def herz_to_dekaherz(herz):
    return herz / 10


def herz_to_decyherz(herz):
    return herz * 10


def herz_to_centyherz(herz):
    return herz * 100


def herz_to_miliherz(herz):
    return herz * 1000


def herz_to_microherz(herz):
    return herz * 1000000


def herz_to_nanoherz(herz):
    return herz * 1000000000


def herz_to_picoherz(herz):
    return herz * 1000000000000


def herz_to_femtoherz(herz):
    return herz * math.pow(10, 15)


def cm3_to_dm3(cm3):
    return cm3 / 1000


def cm3_to_ft3(cm3):
    return cm3 / 28.31685


def cm3_to_in3(cm3):
    return cm3 / 16.39


def cm3_to_m3(cm3):
    return cm3 / math.pow(10, 6)


def cm3_to_yd3(cm3):
    return cm3 / 764.55486


def cm3_to_deciliters(cm3):
    return cm3 / 100


def cm3_to_drops(cm3):
    return cm3 * 20


def cm3_to_medical_drops(cm3):
    return cm3 * 12


def cm3_to_metric_cups(cm3):
    return cm3 * 0.004


def m3_to_km3(m3):
    return m3 * math.pow(10, -9)


def m3_to_dc3(m3):
    return m3 * 10 * math.pow(10, 2)


def m3_to_cm3(m3):
    return m3 * 10 * math.pow(10, 5)


def m3_to_mm3(m3):
    return m3 * 10 * math.pow(10, 8)


def m3_to_microm3(m3):
    return m3 * math.pow(10, 18)


def m3_to_nanom3(m3):
    return m3 * 10 * math.pow(10, 26)


def m3_to_liter(m3):
    return m3 * 10 * math.pow(10, 2)


def m3_to_cu_in(m3):
    return m3 * 6.102374 * math.pow(10, 4)


def m3_to_cu_ft(m3):
    return m3 * 3.531467 * math.pow(10, 1)


def m3_to_cu_yd(m3):
    return m3 * 1.307951


def liter_to_km3(liter):
    return liter * math.pow(10, -12)


def liter_to_m3(liter):
    return liter * math.pow(10, -3)


def liter_to_dm3(liter):
    return liter * 10 * math.pow(10, -1)


def liter_to_cm3(liter):
    return liter * 10 * math.pow(10, 2)


def liter_to_mm3(liter):
    return liter * math.pow(10, 6)


def liter_to_microm3(liter):
    return liter * math.pow(10, 15)


def liter_to_nm3(liter):
    return liter * 10 * math.pow(10, 23)


def kilojoules_to_megawatt(kilojoules):
    return kilojoules / 3599712.02


def kilojoules_to_btu(kilojoules):
    return kilojoules / 1.055


def kilojoules_to_kilo_btu(kilojoules):
    return kilojoules / 1055.05


def kilojoules_to_joules(kilojoules):
    return kilojoules * 1000


def kilojoules_to_megajoules(kilojoules):
    return kilojoules / 1000


def kilojoules_to_gigajoules(kilojoules):
    return kilojoules / 1000000


def megajoules_to_watt(megajoules):
    return megajoules * 277.77


def megajoules_to_kilowatt(megajoules):
    return megajoules / 3.60


def megajoules_to_megawatt(megajoules):
    return megajoules / 3600


def megajoules_to_btu(megajoules):
    return megajoules * 947.81


def megajoules_to_kilo_btu(megajoules):
    return megajoules / 1.055


def megajoules_to_joules(megajoules):
    return megajoules * 1000000


def megajoules_to_kilojoules(megajoules):
    return megajoules * 1000


def megajoules_to_gigajoules(megajoules):
    return megajoules / 1000


def gigajoules_to_watt(gigajoules):
    return gigajoules * 277777.77


def gigajoules_to_kilowatt(gigajoules):
    return gigajoules * 277.77


def gigajoules_to_megawatt(gigajoules):
    return gigajoules / 3.60


def gigajoules_to_btu(gigajoules):
    return gigajoules * 947817.12


def gigajoules_to_joules(gigajoules):
    return gigajoules * 1000000000


def gigajoules_to_kilojoules(gigajoules):
    return gigajoules * 1000000


def gigajoules_to_megajoules(gigajoules):
    return gigajoules * 1000


def string_title(text):
    return text.title()


def string_upper_case(text):
    return text.upper()


def string_lower_case(text):
    return text.lower()


def split_string(text):
    return text.split()


def swap_string_case(text):
    return text.swapcase()


def capitalize_string(text):
    return text.capitalize()


def string_ends_with(text):
    return text.endswith('a')


def string_starts_with(text):
    return text.startswith('v')


def string_is_alnum(text):
    return text.isalnum()


def string_is_alpha(text):
    return text.isalpha()


def string_is_decimal(text):
    return text.isdecimal()


def string_is_digit(text):
    return text.isdigit()


def string_is_identifier(text):
    return text.isidentifier()

def string_is_lower(text):
    return text.islower()


def string_is_numeric(text):
    return text.isnumeric()


def string_is_printable(text):
    return text.isprintable()


def is_space_in_string(text):
    return text.isspace()


def string_is_title(text):
    return text.istitle()


def string_is_upper(text):
    return text.isupper()


def appending_to_list(x):
    temp = []
    temp.append(x)
    return temp


def removing_from_list(x):
    temp1 = ['dom', 'dupa']
    temp1.remove(x)
    return temp1


def popping_list():
    temp = ['dom', 'auto']
    temp.pop()
    return temp


def clear_list():
    temp1 = ['komp', 'dupa']
    temp1.clear()
    return temp1


def counting_in_list(x):
    temp = ['komp', 'dupa']
    y = temp.count(x)
    return y


def reversing_list():
    temp = ['komp', 'dupa']
    temp.reverse()
    return temp


print(coin_toss())
print(random_color())
print(random_color2())
print(boolean_to_string([]))
print(is_even_odd(5))
print(celsius_to_fahrenheit(20))
print(fahrenheit_to_celsius(67))
print(celsius_to_kelvin(30))
print(fahrenheit_to_celsius(45))
print(get_bmi(99, 200))
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
print(h_to_min(2))
print(calculate_rectangle_area(4, 5))
print(calculate_parallelogram_area(4, 5))
print(calculate_triangle_area(4, 5))
print(calculate_trapezoid_area(4, 5, 5))
print(calculate_ellipse_area(4, 5))
print(circular_sector_area(15, 25))
print(regular_hexagon_area(4.5))
print(deltoid_area(15, 25))
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
print(is_fibonacci(8))
print(calculation_two_numbers(5, 10))
print(total_list_value([1, 2, 3]))
print(is_longer_then_5([3, 4, 5, 5]))
print(reverse_string('kot'))
print(mirror_string('ahmed'))
print(remove_letter('d', 'dom'))
print(is_number_in_range(5, 2, 10))
print(unique_list([1, 1, 2, 3, 3]))
print(is_palindrome('kajak'))
print(same_initial('apple', 'orange'))
print(in_both('pear', 'apple'))
print(odd_or_even(-2))
print(count_vowels("Hi my name is Ryan"))
print(is_bounded(5, 10, 15))
print(count_even((5, 10, 15)))
print(max_or_min(14, 24, 'min'))
print(get_current_date())
print(get_current_time())
# print(is_developer('Albert'))
# print(is_not_developer('Dennis'))
# print(get_salary('Bill'))
# print(get_developers())
# print(get_non_developers())
print(get_average(15, 23))
print(check_anagrams('kajak', 'kajak'))
print(capitalize_sentences(['ala ma kota', 'Litwo ojczyzno moja']))
print(fibonacci(10))
print(cuboid_surface_area(10, 15, 20))
print(make_upper('ala'))
print(make_lower('ALA'))
print(reverse_word('janusz'))
print(count_letters('a', 'bartek'))
print(calculate_speed(1000, 100))
print(calculate_salary(23, 166))
print(meters_to_feet(1999))
print(km_to_miles(3456))
print(find_array_item([1, 2, 'trzy', 4, 'pięć'], 4))
print(generate_full_name('adam', 'małysz'))
print(count_capital_letters('Ala Ma Kota'))
print(pascal_to_hpa(1500))
print(pascal_to_bar(1500))
print(pascal_to_newton_on_sq_mm(1500))
print(pascal_to_kg_on_sq_m(1500))
print(pascal_to_at(1500))
print(pascal_to_atm(1500))
print(pascal_to_tr(1500))
print(pascal_to_psi(1500))
print(joul_to_kj(1500))
print(joul_to_kgm(1500))
print(joul_to_wh(1500))
print(joul_to_kwh(1500))
print(joul_to_cal(1500))
print(joul_to_kcal(1500))
print(is_item_in_array([1, 2, 'trzy', 4, 'pięć'], 4))
print(dollar_to_euro(100))
print(euro_to_yen(100))
print(random_int_in_range(1, 10))
print(random_choice_from_array(["apple", "banana", "cherry"]))
print(shuffle_array(["apple", "banana", "cherry"]))
print(random_from_0_to_1())
print(get_random_float_from_range(20, 60))
print(get_random_float_from_range_with_param(20, 40, 60))
print(generate_random_numbers_list(2, 5, 15))
print(generate_random_string_list(15))
print(seconds_to_minutes(100))
print(seconds_to_hours(100))
print(seconds_to_days(100))
print(seconds_to_weeks(100))
print(seconds_to_months(1000000))
print(seconds_to_years(1000000))
print(hours_to_seconds(15))
print(hours_to_minutes(15))
print(hours_to_microseconds(15))
print(days_to_seconds(10))
print(days_to_minutes(10))
print(days_to_hours(10))
print(days_to_microseconds(10))
print(get_center_string('ala', 20))
print(is_ends_with_dot('ala ma kota.'))
print(join_array_by_param(["John", "Peter", "Vicky"], '-'))
print(strip_string('    banana     '))
print(replace_fruit('apple'))
print(feet_to_milimeter(150))
print(feet_to_micrometer(150))
print(feet_to_micrometer(150))
print(feet_to_meter(150))
print(feet_to_mile(150))
print(feet_to_mile(150))
print(feet_to_kilometer(150))
print(feet_to_yard(150))
print(feet_to_inch(150))
print(feet_to_centimeter(150))
print(mile_to_milimeter(200))
print(mile_to_micrometer(200))
print(mile_to_nanometer(200))
print(mile_to_meter(200))
print(mile_to_feet(200))
print(mile_to_kilometer(200))
print(mile_to_yard(200))
print(mile_to_inch(200))
print_truth()
print(m_to_km(456))
print(min_to_h(360))
print(convert_f_to_c(78))
print(convert_c_to_f(78))
print(convert_c_to_k(100))
print(count_letters_in_word('ala ma kota'))
print(count_digits_in_number(1500))
print(count_elements_in_list([1, 2, 3, 4, 5, 6]))
print(check_alphanumeric('janusz'))
print(check_ascii('janusz'))
print(check_decimal('123'))
print(check_digit('123'))
print(check_identifier('janusz'))
print(check_lower('janusz'))
print(check_printable('janusz'))
print(check_space('ala ma kota'))
print(check_if_title('Janusz'))
print(check_if_upper('Janusz'))
print(mean([1, 2, 3]))
print(fmean([1, 2, 3]))
print(geometric_mean([1, 2, 3]))
print(median([1, 2, 3]))
print(median_low([1, 2, 3]))
print(median_high([1, 2, 3]))
print(median_grouped([1, 2, 3]))
print(mode([1, 2, 3]))
print(multi_mode([1, 2, 3]))
print(standard_deviation([1, 2, 3]))
print(variance([1, 2, 3]))
print(standard_deviation2([1, 2, 3]))
print(variance2([1, 2, 3]))
print(quantiles([1, 2, 3]))
print(covariance([1, 2, 3], [1, 2, 3]))
print(correlation([1, 2, 3], [1, 2, 3]))
print(linear_regression([1, 2, 3], [1, 2, 3]))
print(make_negative_number(55))
print(reverse_list([1, 2, 3]))
print(reverse_text('ala ma kota'))
print(is_plural(5))
print(auto_factory('audi', str(100)))
# print(start_engine('audi'))
# print(stop_engine(auto_factory('audi', str(100))))
# print(accelerate('audi', '100'))
# # todo
# sort_todo()
# todo_app()
# get_task()
# add_task()
# delete_task()
# update_task()
# search_task()
# filter_by_status()
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
print(get_product_price(product_data))
print(get_product_price2(product_data))
print(change_product_price(product_data, 2.00))
print(update_product(product_data, 'seller', 'Aldi'))
print(update_product(product_data, 'tax', '23%'))
print(get_today_date_time())
print(calculate_future_date(20))
print(calculate_past_date(20))
print(get_day_name_for_date(1992, 3, 20))
print(get_current_time2())
print(dollars_to_cents(2))
print(pln_to_eur(150))
print(pln_to_usd(150))
print(pln_to_gpb(150))
print(pln_to_chf(150))
print(pln_to_aud(150))
print(pln_to_bgn(150))
print(pln_to_cad(150))
print(pln_to_czk(150))
print(pln_to_dkk(150))
print(pln_to_hkd(150))
print(pln_to_hrk(150))
print(joule_to_ev(1500))
print(joul_to_ry(1000))
print(celsius_to_rankine(25))
print(celsius_to_reaumur(25))
print(celsius_to_romer(25))
print(celsius_to_delisle(25))
print(celsius_to_newton(25))
print(rankine_to_celsius(536.15))
print(reaumur_to_celsius(20))
print(romer_to_celsius(20.63))
print(delisle_to_celsius(112.5))
print(newton_to_celsius(8.25))
print(fahrenheit_to_kelvin(77))
print(fahrenheit_to_rankine(77))
print(fahrenheit_to_reaumur(77))
print(fahrenheit_to_romer(77))
print(fahrenheit_to_delisle(77))
print(degree_to_arcminute(90))
print(degree_to_arcsecond(90))
print(radian_to_degree(3))
print(radian_to_gradian(2))
print(radian_to_arcminute(3))
print(radian_to_arcsecond(3))
print(radian_to_gradian(2))
print(arcminute_to_radians(8349))
print(arcminute_to_radians(3))
print(arcminute_to_gradian(345))
print(arcminute_to_cycle(1))
print(arcsecond_to_degree(1))
print(arcsecond_to_arcminute(1))
print(arcsecond_to_gradian(1))
print(arcsecond_to_cycle(1))
# print(get_number())
# print(guess_the_number())
# print(get_numbers())
# print_numbers()
# print(drawing_numbers())
# lotto()
# roll_the_dice()
print(shorten('ala'))
print(['ala', 'ola', 'tomek', 'adam'])
print(check_palindrome('kajak'))
print(div(10, 15))
# print(roll())
print(herz_to_kiloherz(10))
print(herz_to_hektorez(10))
print(herz_to_dekaherz(10))
print(herz_to_decyherz(10))
print(herz_to_centyherz(10))
print(herz_to_miliherz(10))
print(herz_to_microherz(10))
print(herz_to_nanoherz(10))
print(herz_to_femtoherz(10))
print(cm3_to_dm3(30))
print(cm3_to_ft3(10))
print(cm3_to_in3(10))
print(cm3_to_m3(10))
print(cm3_to_yd3(10))
print(cm3_to_deciliters(10))
print(cm3_to_drops(20))
print(cm3_to_medical_drops(40))
print(m3_to_km3(1))
print(m3_to_dc3(1))
print(m3_to_cm3(1))
print(m3_to_mm3(1))
print(m3_to_microm3(1))
print(m3_to_nanom3(1))
print(m3_to_liter(1))
print(m3_to_cu_in(1))
print(m3_to_cu_ft(1))
print(m3_to_cu_yd(1))
print(liter_to_km3(1))
print(liter_to_m3(1))
print(liter_to_dm3(1))
print(liter_to_cm3(1))
print(liter_to_mm3(1))
print(liter_to_microm3(1))
print(kilojoules_to_megawatt(10))
print(kilojoules_to_btu(10))
print(kilojoules_to_kilo_btu(10))
print(kilojoules_to_joules(10))
print(kilojoules_to_megajoules(10))
print(kilojoules_to_gigajoules(10))
print(megajoules_to_watt(10))
print(megajoules_to_kilowatt(10))
print(megajoules_to_megawatt(10))
print(megajoules_to_btu(10))
print(megajoules_to_kilo_btu(10))
print(megajoules_to_joules(10))
print(megajoules_to_kilojoules(10))
print(megajoules_to_gigajoules(10))
print(gigajoules_to_watt(10))
print(gigajoules_to_kilowatt(10))
print(gigajoules_to_megawatt(10))
print(gigajoules_to_btu(10))
print(gigajoules_to_joules(10))
print(gigajoules_to_kilojoules(10))
print(gigajoules_to_megajoules(10))
print(string_title('ala'))
print(string_upper_case('ola i przedszkole'))
print(string_lower_case('ABCDE'))
print(split_string('ala'))
print(swap_string_case('wszy'))
print(capitalize_string('ala ma kota'))
print(string_ends_with('ala'))
print(string_starts_with('hel'))
print(string_is_alnum('python.py'))
print(string_is_alpha('domek'))
print(string_is_decimal('562632'))
print(string_is_digit('ala'))
print(string_is_identifier('ala'))
print(string_is_lower('ALA'))
print(string_is_numeric('jaroslaw'))
print(string_is_printable('dominik'))
print(is_space_in_string('     AWS'))
print(string_is_title('Tadeusz'))
print(string_is_upper('AMADEUSZ'))
print(appending_to_list('kasztan'))
print(removing_from_list('kot'))
print(popping_list())
print(clear_list())
print(counting_in_list('pies'))
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
print(get_product_price(product_data))
print(get_product_price2(product_data))
print(change_product_price(product_data, 2.00))
print(update_product(product_data, 'seller', 'Aldi'))
print(update_product(product_data, 'tax', '23%'))
print(get_today_date_time())
print(calculate_future_date(20))
print(calculate_past_date(20))
print(get_day_name_for_date(1992, 3, 20))
print(get_current_time2())