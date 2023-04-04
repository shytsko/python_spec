from typing import Callable


#
#
# def pow_(p: int) -> Callable[[int], int]:
#     def fun2(num: int) -> int:
#         return num ** p
#
#     return fun2
#
#
# pow2 = pow_(2)
# pow3 = pow_(3)
#
# print(pow2(2))
# print(pow3(2))


# def main(x: int) -> Callable[[int], dict[int, int]]:
#     d = {}
#
#     def loc(y: int) -> dict[int, int]:
#         for i in range(y):
#             d[i] = x ** i
#         return d
#
#     return loc
#
#
# small = main(42)
# big = main(73)
# print(id(small(7)))
# print(id(big(7)))
# print(id(small(3)))

# def counter(start, step):
#     state = start
#
#     def increment():
#         nonlocal state
#         state += step
#         return state
#
#     return increment
#
#
# counter_0_1 = counter(0, 1)
# counter_100_5 = counter(100, 5)
#
# print(counter_0_1())
# print(counter_0_1())
# print(counter_0_1())
# print(counter_100_5())
# print(counter_0_1())
# print(counter_100_5())
# print(counter_0_1())
# print(counter_100_5())
# print(counter_0_1())

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("------------before---------------")
#         res = func(*args, **kwargs)
#         print("------------afret----------------")
#         return res
#
#     return wrapper
#
#
# def my_fun(message):
#     print(f"my_fun: {message}")
#
#
# my_fun_decor = decorator(my_fun)
# my_fun_decor("message")
#
#
# @decorator
# def my_fun2(message):
#     print(f"my_fun2: {message}")
#
#
# my_fun2("message2")
