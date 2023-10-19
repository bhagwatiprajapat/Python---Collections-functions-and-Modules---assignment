
# moduL=2
#1. Check if a number is positive, negative, or zero:

num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")



#2. Get the factorial of a given number:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))
print("Factorial:", factorial(num))



#3. Get the Fibonacci series of a given range:


def fibonacci(n):
    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

range_limit = int(input("Enter the range: "))
print("Fibonacci Series:", fibonacci(range_limit))


#4. Memory management in Python:

print("Python uses automatic memory management with a built-in garbage collector that reclaims memory from objects no longer in use.")



#5. Purpose of the continue statement in Python:

print("The continue statement is used to skip the current iteration of a loop and move to the next one.")



#6. Swap two numbers with and without a temp variable:

# With a temp variable
a = 5
b = 10
temp = a
a = b
b = temp
print("a =", a)
print("b =", b)

# Without a temp variable
a = 5
b = 10
a, b = b, a
print("a =", a)
print("b =", b)




#7. Check if a number is even or odd and print an appropriate message:

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")



#8. Test whether a passed letter is a vowel or not:


letter = input("Enter a letter: ")
vowels = "AEIOUaeiou"
if letter in vowels:
    print("It's a vowel.")
else:
    print("It's not a vowel.")




#9. Sum three given integers, but if two values are equal, the sum will be zero:


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 == num2 or num2 == num3 or num1 == num3:
    result = 0
else:
    result = num1 + num2 + num3

print("Sum:", result)




#10. Return True if two given integer values are equal or their sum or difference is 5:


def check_values(a, b):
    return a == b or abs(a - b) == 5 or a + b == 5

value1 = int(input("Enter the first value: "))
value2 = int(input("Enter the second value: "))

if check_values(value1, value2):
    print("True")
else:
    print("False")





#11. Sum of the first n positive integers:


n = int(input("Enter a positive integer: "))
sum_of_n = (n * (n + 1)) // 2
print("Sum of the first", n, "positive integers:", sum_of_n)




#12. Calculate the length of a string:

text = input("Enter a string: ")
length = len(text)
print("Length of the string:", length)


#13. Count the number of characters (character frequency) in a string:

text = input("Enter a string: ")
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

for char, count in char_count.items():
    print(f"'{char}' occurs {count} times.")

    


#14. Negative indexes in Python:

print("Negative indexes in Python are used to access elements from the end of a sequence (e.g., a string or a list). -1 represents the last element, -2 the second-to-last, and so on. They are used for convenience when you need to access elements from the end of the sequence.")



#15. Count occurrences of a substring in a string:

text = input("Enter a string: ")
substring = input("Enter a substring to count: ")
count = text.count(substring)
print(f"'{substring}' occurs {count} times in the string.")



#16. Count occurrences of each word in a given sentence:

sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for word, count in word_count.items():
    print(f"'{word}' occurs {count} times in the sentence.")


#17.Python program to get a single string from two given strings:

def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(chars_mix_up('abc', 'klm'))


#18. Python program to add 'ing' at the end:
def add_string(str1):
  length = len(str1)

  if length > 2:
    if str1[-3:] == 'ing':
      str1 += 'ly'
    else:
      str1 += 'ing'

  return str1
print(add_string('ab'))
print(add_string('abc'))
print(add_string('string'))



#19. first appearance of the substring 'not' and 'poor' from a given string:
def not_poor(str1):
  snot = str1.find('not')
  spoor = str1.find('poor')
  

  if spoor > snot and snot>0 and spoor>0:
    str1 = str1.replace(str1[snot:(spoor+4)], 'good')
    return str1
  else:
    return str1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))


#20. length of the longest one:

def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["PHP", "bhagwati", "Backend"])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])



#21. Reverse a string if it's length is a multiple of 4:

def reverse_string(str1):
    if len(str1) % 4 == 0:
       return ''.join(reversed(str1))
    return str1

print(reverse_string("abcd"))
print(reverse_string("python"))



#22.  string made of the first 2 and the last 2 chars from a given a string:
def string_both_ends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

print(string_both_ends("w3resource"))
print(string_both_ends("w3"))
print(string_both_ends("w"))



#23.  Insert a string in the middle of a string

def insert_sting_middle(str, word):
	return str[:2] + word + str[2:]

print(insert_sting_middle("[[]]", "bhagwati"))
print(insert_sting_middle("{{}}", "prajapat"))
print(insert_sting_middle("<<>>", "parariya"))








#Module=3
#1. list and Reversing a List in Python"
print("Lists are used to store multiple items in a single variable.")

print(" 1.Using the slicing technique --2.Reversing list by swapping present and last numbers at a timezUsing the reversed() and reverse() built-in function-3.Using a two-pointer approach-- 4.Using the insert() function-- 5.Using list comprehension-- 6.Reversing a list using Numpy")




#2. remove the last object from list:
print (" using by pop function from list library ")


#3. l=[2, 33, 222, 14, 25],  list1 [-1]?

l=[2, 33, 222, 14, 25]
print(l[-1])


#4. Differentiate between append () and extend () methods:
print (" in append the single streing is add in the list and in extend new list is add in last of the list")




#5. Python program to find largest:
#create empty list 

mylist = []
number = int(input('How many elements to put in List: '))
for n in range(number):
    element = int(input('Enter element '))
    mylist.append(element)
print("Maximum element in the list is :", max(mylist))
print("Minimum element in the list is :", min(mylist))



#6. compare two lists :
print(" by ,Using list. sort() and == operator")



#7.count the number of strings where the string length is 2 or more: 
def match_words(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr

print(match_words(['abc', 'xyz', 'aba', '1221']))



#8. remove duplicates from a list:

def my_function(x):
  return list(dict.fromkeys(x))

mylist = my_function(["a", "b", "a", "c", "c"])



#9. list is empty or not:
l = []
if not l:
  print("List is empty")



#10. takes two lists and returns true if they have at least one common member:

def common_data(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,2,3,4,5], [6,7,8,9]))




#11. Generate and print a list of first and last 5 elements where the values are square of numbers between two numbers

def printValues():
	l = list()
	for i in range(1,21):
             
		l.append(i**2)
	print(l[:5])
	print(l[-5:])

printValues()


#12. Unique elements from a list:
def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5])) 



#13. Convert a list of characters into a string:

s = ['p', 'y', 't', 'h', 'o', 'n']
str1 = ''.join(s)
print(str1)


#14. select an item randomly from a listL:

import random
color_list = ['Red', 'Blue', 'Green', 'White', 'Black']
print(random.choice(color_list))



#15. find the second smallest number in a list:

def second_smallest(numbers):
  if (len(numbers)<2):
    return
  if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
    return
  dup_items = set()
  uniq_items = []
  for x in numbers:
    if x not in dup_items:
      uniq_items.append(x)
      dup_items.add(x)
  uniq_items.sort()    
  return  uniq_items[1]   

print(second_smallest([1,22,29,65,8]))



#16. unique number:

my_list = [10, 20, 30, 40, 20, 50, 60, 40]
print("Original List : ",my_list)
my_set = set(my_list)
my_new_list = list(my_set)
print("List of unique numbers : ",my_new_list)



#17. tuple, diffrent between tuple and list:
print(" a tuple is one of the four data types that are built into Python. The other three data types are Lists, Sets, and Dictionaries. Every data type has its qualities and presents its unique drawbacks when used")

print("List and Tuple in Python are the classes of Python Data Structures. The list is dynamic, whereas the tuple has static characteristics. This means that lists can be modified whereas tuples cannot be modified, the tuple is faster than the list because of static in nature. Lists are denoted by the square brackets but tuples are denoted as parenthesis.")


#18.Create a tuple with different data types:

tuplex = ("tuple", False, 3.2, 1)
print(tuplex)



#19. create a tuple with numbers:


intTuple=()
n=int(input("enter the total tuple item to store="))
for i in range (1, n+1):
     value=int(input("enter %d tuple item=" %i))
     intTuple+=(value,)

print("tuple item =", intTuple)



#20. convert a tuple to a string

tup = ('B', 'H', 'A', 'G', 'W', 'A', 'T', 'I')
str =  ''.join(tup)
print(str)



#21. Reversing a tuple using slicing technique

def Reverse(tuples):
	new_tup = tuples[::-1]
	return new_tup
tuples = ('B', 'H', 'A', 'G', 'W', 'A', 'T', 'I')
print(Reverse(tuples))




#22. Replace last value of tuples in a list:

l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([t[:-1] + (300,) for t in l])



#23. remove an empty tuple (s) from a list of tuples:
L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
L = [t for t in L if t]
print(L)


#24. convert list into dictionary:


l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
d = {}
for a, b in l:
    d.setdefault(a, []).append(b)
print (d)



#25 script to print a dictionary number between 1 to 15:
d=dict()
for x in range(1,15):
    d[x]=x
print(d) 


#26. Check multiple keys exists in a dictionary:

student = {'name': 'Alex','class': 'V','roll_id': '2'}
print(student.keys() >= {'class', 'name'})
print(student.keys() >= {'name', 'Alex'})
print(student.keys() >= {'roll_id', 'name'})



#27. combine two dictionary adding values for comman keys:

from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d)






















