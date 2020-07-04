# StopIteration异常的触发

# gen = (i for i in range(2))  # 生成器表达式，返回一个生成器对象
'''
for的工作原理:
    1.调用range(2).__iter__()返回一个迭代器对象
    2.调用 迭代器.__next__()拿到一个返回值，并赋值给i
    3.重复步骤2直到抛出StopIteration异常，for捕捉到异常停止循环
'''
# print(next(gen))  # 拿到第一个值
# print(next(gen))  # 拿到第二个值
# print(next(gen))  # 抛出异常
# try:
#     print(next(gen))
# except StopIteration:
#     print("抛出异常，没有数据可以拿了")

#-----------------------------------------------------------
#自定义异常
# class UserInputError(Exception):
#     def __init__(self, error_info):
#         super().__init__(self, error_info)
#         self.error_info = error_info

#     def __str__(self):
#         return self.error_info


# user_input = 'a'
# try:
#     if not user_input.isdigit():
#         raise UserInputError('用户输入错误')
# except UserInputError as e:
#     print(e)

#-----------------------------------------------------------
#pretty_errors模块的使用，更清晰的发现异常发生的地方
# import pretty_errors
# def a():
#     b()

# def b():
#     c()

# def c():
#     x = 0
#     return 100/x

# a()
'''
没有pretty_errors的异常跟踪
Traceback (most recent call last):
  File "section1.py", line 48, in <module>
    a()
  File "section1.py", line 39, in a
    b()
  File "section1.py", line 42, in b
    c()
  File "section1.py", line 46, in c
    return 100/x
ZeroDivisionError: division by zero
'''

'''
pretty_errors导入后的异常跟踪
section1.py 49 <module>
a()

section1.py 40 a
b()

section1.py 43 b
c()

section1.py 47 c
return 100/x

ZeroDivisionError:
division by zero
'''

