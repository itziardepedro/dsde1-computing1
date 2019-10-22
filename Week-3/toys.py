#question 1
# write a function that adds 1
# to the input and prints the result
def addOne(a):
    a += 1
    print(a)

#question 2
# write a function that adds 1
# to the input and returns the result
def add1(a):
    a += 1
    return a

#question 3 
# write a function that adds
# the two input numbers together
# and returns the sum
def sum(a, b): 
    return a+b
 
#question 4
# write a function that takes two
# numbers, adds them together using 
# sum() and then increments the sum
# using inc_return
def sum_inc(a,b):
    return add1(sum(a,b))

#question 5
# write a function that returns a 
# boolean (True or False) for whether 
# the input number is even
def is_even(a):
    a = input('choose a number')
    even = False 
    if a % 2: 
        even = True 
        return even 
    else: 
        return even

#question 6 
# create for loop that takes a string
# and an integer and returns a new string 
# that is the string repeated equal to 
# integer
# e.g. string_repeat('ho', 3) returns
# 'hohoho'
def string_repeat(phrase, repeat):
    for i in range(repeat): 
        print('ho')

    
    # hint: you can add strings together 
    # in order to concatenate them
    return
