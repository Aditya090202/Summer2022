import math
from typing import List


equation = (10 ** 1) * 110 / 10 + 0.25 - 10 
print(equation)
# What is the value of the expression 4 * (6 + 5) : 44
# What is the value of the expression 4 * 6 + 5 : 29
# What is the value of the expression 4 + 6 * 5 : 34
#What is the type of the result of the expression 3 + 1.5 + 4?: Float
#What would you use to find a number’s square root, as well as its square? exponentiation; raise to the 1/2 power for square root and 2nd power for square
#Strings:
s = "hello"
#Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:
aVar = s[1]
#print(aVar)
aVar2 = s[:-1]
#Reverse the string 'hello' using slicing:
aVar = s[::-1]
print(aVar)
#Given the string hello, give two methods of producing the letter 'o' using indexing
#Method 1:
var2 = s[4]
#Method 2:
var3 = s[-1]
print(var2)
print(var3)
#Lists:
#Build this list [0,0,0] two separate ways
#M1
a = [0,0,0]
#M2
b = list()
b.append(0)
b.append(0)
b.append(0)
#Reassign 'hello' in this nested list to say 'goodbye' instead:
list3 = [1,2,[3,4,'hello']]
list3[2][2] = "goodbye"
#Sort the list below:
list4 = [5,3,4,6,1]
sorted = list4.sort() # has no type and prints "none"
#Dictionaries:
#Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
print(d['simple_key'])
d = {'k1':{'k2':'hello'}}
print(d["k1"]["k2"])
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d["k1"][0]["nest_key"][1][0])
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d["k1"][2]["k2"][1]["tough"][2][0])
# Can you sort a dictionary? Why or why not?
# You cannot sort a dicitonary as it is unordered and doesn't need to be sorted(that's why we use a list instead to sort elements that need to be sorted)
#Tuples:
#What is the major difference between tuples and lists?:
#Lists are mutable data structures and tuples are immutable meaning they elements within a tuple can't be changed
#How do you make tuples?
a = (1,3,4)
def number_to_string(num):
    changeType = str(num)
    return type(changeType)
#print(number_to_string(12))
def solution(string):
    brokenString = ""
    for x in range(len(string) - 1, -1, -1):
        brokenString = brokenString + string[x]
    return brokenString
s = "Rikke"
var = "R" in s
print(var)
#Statements Assesment
st = 'Print only the words that start with s in this sentence'
split = st.split(" ")
# for letter in split:
#     if "s" in letter:
#         print(letter)
#     else:
#        print("This word does not have an s.")
# for x in range(0, 11):
#     if x%2==0:
#         print(x)
#     else:
#         "Not an even number."
list_comprehension = [x for x in range(0, 51) if x%3==0]
st2 = 'Print every word in this sentence that has an even number of letters'
split2 = st2.split(" ")
# for word in split2:
#     if len(letter) % 2 == 0:
#         print("even!")
#     else:
#         print("odd!")
# for number in range(0, 101):
#     if number % 3 == 0 and number % 5 == 0:
#          print("FizzBuzz") 
#     elif number % 5 == 0:
#         print("Buzz is for the number {}".format(number))
#     elif number % 3 == 0:
#         print("Fizz is for the number {}".format(number))
#     else:
#         print("NO idea.")
st3 = 'Create a list of the first letters of every word in this string'
split3 = st3.split(" ")
list4 = [letter[0] for letter in split3]
print(list4)
def myfunc(*args):
    
    


