# # question 1
# my_list = [1, 2]

# for v in range(2):
#     my_list.insert(-1, my_list[v])
#     # my_list[0] = 1 => [1, 1, 2]
#     # my_list[1] = 1 => [1, 1, 1, 2]

# print(my_list)

# #question 5
# def function_1(a):
#     return None


# def function_2(a):
#     return function_1(a) * function_1(a)


# print(function_2(2))
## error

# # question 7
# def func(a, b):
#     return b ** a


# print(func(b=2, 2))
## error

# #question 8
# z = 0
# y = 10
# x = y < z and z > y or y < z and z < y #false

# question 9
# Which of the following variable names are illegal and will cause the SyntaxError exception?
# -print, in, for, In? 
# -in, for

# question 10
# my_list =  [x * x for x in range(5)]


# def fun(lst):
#     del lst[lst[2]]
#     return lst

# print(fun(my_list))
##[0, 1, 4, 9]

#question 11
# x = 1
# y = 2
# x, y, z = x, x, y
# z, y, z = x, y, z

# print(x, y, z)

##1 1 2

# #question 12
# a = 1
# b = 0
# a = a ^ b #1^0 = 1 = a
# b = a ^ b #1^0 = 1 = b
# a = a ^ b #1^1 = 0 = a

# print(a, b) #0 1

# # question 13
# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return 2


# print(fun(fun(2))) #fun(1) = 2

# question 14
# nums = [1, 2, 3]
# vals = nums
# del vals[:]
# print(nums) #[]
# print(vals) #[]

# question 15
# x = int(input()) #3
# y = int(input()) #2
# x = x % y
# x = x % y
# y = y % x
# print(y) #0

# question 16
# y = input() #3
# x = input() #6
# print(x + y) #63

# question 17
# print("a", "b", "c", sep="sep") #asepbsepc

# question 18
# x = 1 // 5 + 1 / 5
# print(x) #0.2

#question 19
# my_tuple[1] = my_tuple[1] + my_tuple[0]
# is illegal

# # question 20
# x = float(input()) #2
# y = float(input()) #4
# print(y ** (1 / x)) #2.0

# question 21
# dct = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dct['three']

# for k in range(len(dct)):
#     v = dct[v]

# print(v) #one

# question 22
# lst = [i for i in range(-1, -2)] #0 elements

# #question 24
# def fun(x, y):
#     if x == y:
#         return x
#     else:
#         return fun(x, y-1)


# print(fun(0, 3)) #0

#question 25
# i = 0
# while i < i + 2 :
#     i += 1
#     print("*")
# else:
#     print("*")

# #infinite loop

# # question 26
# tup = (1, 2, 4, 8)
# tup = tup[-2:-1]
# print(tup) #(4,)
# # print(tup[0]) #4
# tup = tup[-1]
# print(tup) #4

# #question 27
# dd = {"1": "0", "0": "1"}
# for x in dd.vals(): #AttributeError
#     print(x, end="")

# #question 28
# dct = {}
# dct['1'] = (1, 2)
# dct['2'] = (2, 1)

# for x in dct.keys():
#     print(dct[x][1], end="")
# #21

# #question 29
# def fun(inp=2, out=3):
#     return inp * out


# print(fun(out=2)) #4

# #question 30
# lst = [[x for x in range(3)] for y in range(3)]
# #lst = [[0, 1, 2], [0, 1, 2], [0, 1, 2]]

# for r in range(3):
#     for c in range(3):
#         if lst[r][c] % 2 != 0:
#             print("#")
# #prints 3 #

# #question 31
# try:
#     value = input("Enter a value: ")
#     print(int(value)/len(value)) #0.0
# except ValueError:
#     print("Bad input...")
# except ZeroDivisionError:
#     print("Very bad input...")
# except TypeError:
#     print("Very very bad input...")
# except:
#     print("Booo!")

# # question 32
# try:
#     print(5/0)
#     break #SyntaxError "break" can be used only within a loop => stops execution
# except:
#     print("Sorry, something went wrong...")
# except (ValueError, ZeroDivisionError): #SyntaxError A named except clause cannot appear after catch-all except clause
#     print("Too bad...")

# #question 33
# foo = (1, 2, 3)
# foo.index(0) #ValueError

#question 34
# # A:
# except (TypeError, ValueError, ZeroDivisionError):
#     # Some code.

# # B:
# except TypeError, ValueError, ZeroDivisionError:
#     # Some code.

# # C:
# except: (TypeError, ValueError, ZeroDivisionError)
#     # Some code.

# # D:
# except: TypeError, ValueError, ZeroDivisionError
#     # Some code.

# # E:
# except (TypeError, ValueError, ZeroDivisionError)
#     # Some code.

# # F:
# except TypeError, ValueError, ZeroDivisionError
#     # Some code.

#only A is correct

# #question 35
# print(Hello, World!) #SyntaxError

