#Задание_1

import re
EMAIL = re.compile(r'([a-z0-9]+)@([a-z0-9]+\.[a-z]+)')
def email_parse(email):
    found_info = EMAIL.findall(email)[0]
    if found_info:
        name, addr = found_info
    else:
        raise ValueError(f'wrong email: {email}')
    print(name, addr)

email_parse('d.smirnovk@bk.ru')
email_parse('d.smirnovk@bk.ru')

#Задание_2

import re
import requests

PAD = re.compile(r'((?:[0-9]{,3}[.]){3}[0-9]{,3}) - - '
                 r'(.[0-9]{,2}/\w+/[0-9]{4}:(?:[0-9]{2}:){2}[0-9]{2} \+[0-9]{4}]) .(\w+) '
                 r'([/\w+]{0,}) (?:[^\"]*)\" ([0-9]+) ([0-9]+)')
url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
content = requests.get(url).text
for arg in PAD.findall(content):
    addr, datetime, r_type, resource, code, size = arg
    #print(addr, datetime, r_type, resource, code, size)

#Задание_3

from functools import wraps
def type_logger(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            print(f'{func.__name__}({arg}: {type(arg)})', end=', ')
        return func(*args)

    return wrapper


@type_logger
def calc_cube(*args):
    return list(map(lambda x: x ** 3, args))


a = calc_cube(5, 3)
print(a)
print(calc_cube.__name__)
print(calc_cube.__doc__)

#Задание_4

from functools import wraps


def val_checker(decorator_check_func):
    def _val_checker(func_calc_cube):
        @wraps(func_calc_cube)  
        def wrapped(x):
            if decorator_check_func(x):
                return func_calc_cube(x)
            else:
                raise ValueError(x)

        return wrapped
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)
print(calc_cube.__name__)
print(calc_cube.__doc__)
