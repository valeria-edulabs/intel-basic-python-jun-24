# from israel_id import calc_control_digit, my_foo
# from israel_id import *
from israel_id import my_foo as external_foo
from utilities.str_utils import get_word_len

import math
math.ceil(4.11)
# from math import *
# ceil()


# digits = input("Insert 8 digits:")
# calc_control_digit(digits)
def my_foo():
    print("Here is my foo")

my_foo()
external_foo()

print(get_word_len("ryertyrty"))