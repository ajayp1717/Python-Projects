# #
# #
import math
import os
import random
import re
import sys

n = int(input("Enter any integer n: "))

if n in range(1,101):
    if (n % 2 == 1):
        print("Weird")
    if (n% 2 == 0):
        if n in range(2, 6):
            print("Not Weird")
        if n in range(6, 21):
            print("Weird")
        if n in range(21, 101):
            print("Not Weird")












# #
# #
# #
# #
# #
# #
# #
# def is_leap(year):
#     leap = False
#
# year = int(input(i))
#
# i= (range(1900, (10 ** 5) + 1)
# if (i % 100 == 0):
#     if (i % 400 == 0):
#         print(True)
#     else:
#         print(False)
# elif (i % 4 == 0):
#     print(True)
# else:
#     print(False)
#
#
#
# print(is_leap(year))
import calendar

month=int(input("   "))
date=int(input("   "))
year=int(input('    '))
calendar.weekday(year,month,day)


print(weekday(day))