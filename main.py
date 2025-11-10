# # def string1(str1):
# #     str2=str1.upper()
# #     print(str2)
# # string1 = "my name is danyal"
# # string1(tuple1)
# #//////////////////////////////////////////////
# # def describe_types(*args):
# #     for i in args:
# #         print(type(i))
# # describe_types(10, [1,2], {'a':1}, (4,5), {9,10})
# #
# # #//////////////////////////////////////////////
# # def both1(*x,**args):
# #     print(type(x),type(args))
# #     print(args)
# # list1 = [1,2,3,4,5]
# # list2 = {"ali":5}
# # both1(list1,list2)
# # #///////////////////
# # def mixed_func(*args, **kwargs):
# #     print("args:", args)
# #     print("kwargs:", kwargs)
# #
# # mixed_func(1, 2, a=3, b=4, ali=3)
# # #//////////////////////////////////////////////
# # def smart_printer(*args, **kwargs):
# #     print(sum(args))
# #     print(kwargs)
# # smart_printer(1,3,4,5,6,s=9,m=0)
#
# #///////////
# # def configure(*, mode="dark", verbose=False):
# #     print(mode, verbose)
# # configure(mode="light",verbose=True)
#
# #/////////////////////
# # def modify_set(s):
# #     s.add("new")
# #     print("Inside:", s)
# #
# # myset = {"a", "b"}
# # modify_set(myset)
# # print(myset)
# #/////////////////////////
# # /
# # print(operate(operate1))
# # ////
# # def summarize_list(lst):
# #     sum(lst)
# #     pass
# #
# # # Try:
# # nums = [10, 20, 30]
# # print(summarize_list(nums))
#
# #
# # def multiply_all(*args):
# #     result = 1
# #     for a in args:
# #         result *= a
# #     return result
# #
# # # Try both:
# # print(multiply_all(1,2,3))
# # print(multiply_all(*[1,2,3,4]))
#
# # def describe(a,b,c):
# #     print(a,b,c)
# #
# # values = (1,2,3)
# # describe(*values)
#
# # /////////////
# def settings(mode, /, *, debug):
#     print(mode, debug)
#
# settings("dark", debug=True)
# # , debug=True)  # ❌ positional-only
#
#
def greet(name, message="Assalam o Alaikum"):
    print(message, name)

greet("Kashif")
greet("Qasim", "Hello!")
