
#################################################################
## Home Assignment - 4 ##
## Name: Brock Gion
## Due Date: May 4 (Wednesday), 11.59 in Blackboard
## Type your answers in this python file and submit in blackboard.
#################################################################

###############
# ## Problem 1 ## - COMPLETE
# ###############

# # Given the string:
# s = 'django'

# # Use indexing to print out the following:
# # 'd'
# print(s[0])

# # 'o'
# print(s[5])

# # 'djan' 
# print(s[:4]) #slice from start

# # 'jan'
# print(s[1:4])

# # 'go'
# print(s[4:]) #slice to the end

# # Bonus: Use indexing to reverse the string
# print(s[::-1]) #start at string length, end at position 0, move with the step -1 (or one step backward)


###############
## Problem 2 ## - COMPLETE
###############

# # Given this nested list:
# l = [3, 7, [1, 4, 'hello']]
# # Reassign "hello" to be "goodbye"
# l[2][2] = 'goodbye' #list items are indexed, so here you can manually replace. Another approach could be looping through list
# print(l)

###############
## Problem 3 ## - COMPLETE
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

# d1 = {'simple_key': 'hello'}
# print(d1['simple_key'])

# d2 = {'k1': {'k2': 'hello'}}
# print(d2['k1']['k2'])

# d3 = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
# print(d3['k1'][0]['nest_key'][1][0])


###############
## Problem 4 ## - COMPLETE
###############

# Use a set to find the unique values of the list below:
# mylist = [1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
# myset = set(mylist)
# for uniquevalue in myset:
#     print(uniquevalue)


# ###############
# ## Problem 5 ## - COMPLETE
# ###############

# # You are given two variables:
# age = 4
# name = "Sammy"

# # Use print formatting to print the following string:
# #"Hello my dog's name is Sammy and he is 4 years old"

# print(f"Hello my dog's name is {name} and he is {age} years old")


# Complete the tasks below by writing functions! 

#####################
## -- PROBLEM 6 -- ## - COMPLETE
#####################

# Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.

# def arrayCheck(nums):
#     # CODE GOES HERE
#     return str([1, 2, 3])[1:-1] in str(nums) #explicity typecasting both to strings, so comparing the sequence of '1,2,3' to the list '1,1,2,3,1', then returns T/F boolean

# For example:
# print(arrayCheck([1, 1, 2, 3, 1])) # → True
# print(arrayCheck([1, 1, 2, 4, 1])) # → False
# print(arrayCheck([1, 1, 2, 1, 2, 3])) # → True


    #####################
    ## -- PROBLEM 7 -- ## - COMPLETE
    #####################

    # Given a string, return a new string made of every other character starting
    # with the first, so "Hello" yields "Hlo".


# def stringBits(str):
#   # CODE GOES HERE
#   slice notation in python has the syntax [<start>:<stop>:<step>] 
#   [::2] takes in the full string printing every other character
#   return print(str[::2]) 

# # For example:
# stringBits('Hello') #→ 'Hlo'
# stringBits('Hi') #→ 'H'
# stringBits('Heeololeo') #→ 'Hello'

    #####################
    ## -- PROBLEM 8 -- ## - COMPLETE
    #####################

    # Given two strings, return True if either of the strings appears at the very end
    # of the other string, ignoring upper/lower case differences (in other words, the
    # computation should not be "case sensitive").
    #
    # Note: s.lower() returns the lowercase version of a string.
    #

# def end_other(a, b):

#     a1 = a.lower()
#     b1 = b.lower()
 
#     if a1.endswith(b1) or b1.endswith(a1):
#         return True
#     else:
#         return False

# # Examples:
# print(end_other('Hiabc', 'abc')) #→ True
# print(end_other('AbC', 'HiaBc')) #→ True
# print(end_other('abc', 'abXabc')) #→ True


    #####################
    ## -- PROBLEM 9 -- ## - COMPLETE
    #####################

    # Given a string, return a string where for every char in the original,
    # there are two chars.

    # doubleChar('The') → 'TThhee'
    # doubleChar('AAbb') → 'AAAAbbbb'
    # doubleChar('Hi-There') → 'HHii--TThheerree'
    
# def doubleChar(str):
#   newStr = ''
#   for x in str:
#     newStr += x + x
#   return newStr
  
# print(doubleChar("brock"))


    #####################
    ## -- PROBLEM 10 -- ## - COMPLETE
    #####################

    # Read this problem statement carefully!

    # Given 3 int values, a b c, return their sum. However, if any of the values is a
    # teen -- in the range 13-19 inclusive -- then that value counts as 0, except 15
    # and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
    # takes in an int value and returns that value fixed for the teen rule.
    #
    # In this way, you avoid repeating the teen code 3 times (i.e. "decomposition").
    # Define the helper below and at the same indent level as the main no_teen_sum().
    # Again, you will have two functions for this problem!
    #
    # Examples:
    #
    # no_teen_sum(1, 2, 3) → 6
    # no_teen_sum(2, 13, 1) → 3
    # no_teen_sum(2, 1, 14) → 3

# def no_teen_sum(a, b, c):
#   # CODE GOES HERE
#   return fix_teen(a) + fix_teen(b) + fix_teen(c)

# def fix_teen(n):
#   # CODE GOES HERE
#   if n == 15 or n == 16:
#     return n
#   return 0

# print(no_teen_sum(15,15,16))



    #####################
    ## -- PROBLEM 11 -- ## - COMPLETE
    #####################

    # Return the number of even integers in the given array.
    #

# def count_evens(nums):
#   # CODE GOES HERE
#   count_even = 0
#   for x in nums:
#     if not x % 2: #even number
#       count_even+=1
#   return count_even

# # Examples:
# #
# print(count_evens([2, 1, 2, 3, 4])) #→ 3
# print(count_evens([2, 2, 0])) #→ 3
# print(count_evens([1, 3, 5])) #→ 0


