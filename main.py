from module import Sum
import os
import sys

try:
    # creating an object
    ab: Sum = Sum(6,14)
    # calling calculate instance method to find sum of integers
    print(ab.calculate())
    # calling class method change the class or static variable
    Sum.change()
    print(ab.calculate())
    # calling instance method to change instance variable
    ab.update()
    print(ab.calculate())
except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(e, exc_type, 'in file name ', file_name, 'and at line number', exc_tb.tb_lineno)
