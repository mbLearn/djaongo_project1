import unittest
import time
import sys

# 2 >> 4 >> 16 >> 37 >> 58 >> 74 >>

#7 >> 49 >> 97 >> 130 >> 10 >> 1 >> happy
#2 >> 4 >> 16 >> 37 >> 58 >> 89 >> 145 >> 42 >> 20 >> 4 >> Not happy


#1. Check for the digit size
#2. If single digit then multiply the number by itself
#3. Update new_num = the product of step 2
#4. Again check size of the digits
#5. if digits size > 1 : then split the numbers and for each number multiply by itself and sum it all
#6. update new_num with the new sum
#7. if new_sum == 1 print "happy" and stop
#8.

# def helper(num_list):
#     collect = 0
#     for x in num_list:
#         collect += x*x
#     return collect

# def helper2(num_list):
#     collect = 0
#     for x in num_list:
#         collect += x*x
#     return collect
#
# def happy_number(num):
#
#     num_list = map(int,str(num))
#     a = helper2(num_list)
#
#     if a == 1:
#         print "happy"
#         return True
#     elif a == 4:
#         print "Not happy"
#         return False
#     else:
#         answer = happy_number(a)
#         return answer
#
# def isHappy(n):
#     seen = set()
#     while n not in seen:
#         seen.add(n)
#         # print seen
#
#         n = sum([int(x) ** 2 for x in str(n)])
#         print n
#     return n == 1



## Question 2: Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#Example:
#Given nums = [2, 7, 11, 15], target = 9,
#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].
# def indices_of_numbers_adding_upto_target(list_numbers, target):
#     """ so you take each element in the list and add to the rest of the elements.
#     Now you verify if the result of their addition equals the target if true, return their indices.
#     If false move on to the next number.
#     Do not use the same element twice."""
#     new_list = []
#     for x in list_numbers:
#         print x
#         interim_list=[]
#         for y in list_numbers:
#             a = x+y
#             if a == target:
#                 print "you are here... "
#                 o= [list_numbers.index(x), list_numbers.index(y)]
#                 return o
#             else:
#                 pass
#             interim_list.append(a)
#         new_list.append(interim_list)
#
#
# print (indices_of_numbers_adding_upto_target([1,2,3,6, 0, 8, 5], 4))


def indices_of_numbers_adding_upto_target(lista, target):

    # create an empty dictionary to track look_ups
    look_up_dict = {}

    # iterate thru the list
    for i, item in enumerate(lista):
        new_value = target - item

        # check if the new_value exists in look_up_dict
        # if it does then return its value (which is the index)
        # along with i (index of current item)
        # if not in look_up_dict
        # then add it to dict
        if new_value in look_up_dict:
            return [look_up_dict[new_value], i]
        else:
            look_up_dict[item] = i

print indices_of_numbers_adding_upto_target([1,2,3,6,0,8,5], 11)



# def indices_of_numbers_adding_upto_target(lista, target):
#
#     for x in lista:
#         look_up = target - x
#         if look_up in lista:
#             return [lista.index(x), lista.index(look_up)]
#         else:
#             pass
#
# print (indices_of_numbers_adding_upto_target([1,2,3,6, 0, 8, 5], 4))
# print (indices_of_numbers_adding_upto_target([2, 7, 11, 15], 17))

## Question 3: You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit.
# # Add the two numbers and return it as a linked list. You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8





## Question 4: Given a string, find the length of the longest substring without repeating characters.
# Examples:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3.
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.




# class MyTest(unittest.TestCase):
#
#     # def test_1_unhappy(self):
    #     self.assertEqual(happy_number(1), True)
    #
    # def test_4_unhappy(self):
    #     self.assertEqual(happy_number(4), False)
    #
    # def test_15_happy(self):
    #     self.assertEqual(happy_number(42), False)
    #
    # def test_7_unhappy(self):
    #     self.assertEqual(happy_number(7), True)
    #
    # def test_38_unhappy(self):
    #     self.assertEqual(happy_number(38), False)
    #
    # def test_133_unhappy(self):
    #     self.assertEqual(happy_number(133), True)
    #
    # def test_3_unhappy(self):
    #     self.assertEqual(happy_number(3), False)

    # def test_1(self):
    #     self.assertEqual(indices_of_numbers_adding_upto_target([1,2,3,6, 0, 8, 5], 4), [0,2])
    #
    # def test_2(self):
    #     self.assertEqual(indices_of_numbers_adding_upto_target([2, 7, 11, 15], 17), [0,3])




# if __name__ == '__main__':
#     from timeit import Timer
#     t = Timer("indices_of_numbers_adding_upto_target([1,2,3,6, 0, 8, 5], 4)", "from __main__ import indices_of_numbers_adding_upto_target")
#     t1 = Timer("indices_of_numbers_adding_upto_target([2, 7, 11, 15], 12)", "from __main__ import indices_of_numbers_adding_upto_target")
#     print t.timeit()
#     print t1.timeit()
#     unittest.main()



# x = 0
# li1 = [1,2,3,4]
# for m in li1:
#     print x
#     for n in li1:
#         print x
#         for o in li1:
#             x += 1
# print x

## so if the length of the list is '4' then for each loop x is 4*4
# so the runtime for iterating over each loop is n times n.
# where n is the length of the loop.


# Question: Our goal is to write a boolean function that will take two strings and return whether they are anagrams.
def find_anagrams(str1, str2):

    # create an empty dictionary to track the count of each char.
    dict1 = {}

    # convert all the characters to lower case.
    s1 = str1.lower()
    s2 = str2.lower()

    if len(s1) != len(s2):
        return False

    # now iterate thru first directory and
    # and keep track of each char
    # example string : "boba"
    # example: a:1, b:2, o:1
    for i in s1:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1

    # Now iterate thru 2nd string
    # lookup if the char in dict1
    # if not exit
    # if exists then reduce the count by 1
    for i in s2:
        if i not in dict1:
            return False
        else:
            dict1[i] -= 1

    # now if the value for any key is 0,
    # delete that key
    # for i in dict1.keys():
    #     if dict1.get(i) == 0:
    #         del dict1[i]

    for i in dict1.values():
        if i != 0:
            return False
    return True


    # now check the length of the dictionary
    # if 0, return True
    # else False
    # if len(dict1) == 0:
    #     return True
    # else:
    #     return False


print find_anagrams("stttttreaaam", "treamsttttttaaa")
print find_anagrams("abbc", "bbca")
print find_anagrams("AAAAAAbAAAAAAABB", "BBAAAAAAAbAAAAAA")
print find_anagrams("AAABBAbAAAAAAABB", "BBAAAAAAAbAAAAAA")
print find_anagrams("AAABBAbAAAAAAAB", "BBAAAAAAAbAAAAAA")


c = 'AAAAAAbAAAAAAABB'
d = c[::-1]

print d

# Option 2 : This is a bad answer in terms of efficiency
# we are unnecessarily creating 2nd dictionary.
def count_characters(input):
    collect_char = {}
    for char in input:
        if char not in collect_char:
            collect_char[char] = 1
        else:
            collect_char[char] += 1

    return collect_char

def is_it_anagram(str1,str2):
    str1_lower = str1.lower()
    str2_lower = str2.lower()

    return count_characters(str1_lower) == count_characters(str2_lower)

print is_it_anagram("stttttreaaam", "treamsttttttaaa")
print is_it_anagram("abbc", "bbca")
print is_it_anagram("AAAAAAbAAAAAAABB", "BBAAAAAAAbAAAAAA")
print is_it_anagram("AAABBAbAAAAAAABB", "BBAAAAAAAbAAAAAA")
print is_it_anagram("AAABBAbAAAAAAAB", "BBAAAAAAAbAAAAAA")
print is_it_anagram("stream", "stre")


# Question: List has duplicates except for 1
# find that non-duplicate number
a = [1,2,3,4,1,2,3,5,5,6,7,6,4]
b = [1,2,3,4,1,2,3,4]

def find_non_duplicate(lista):
    seen = {}
    for e in lista:
        if e not in seen:
            seen[e] = 1
        else:
            seen[e] += 1

    for key,val in seen.items():
        if val != 2:
            return key
    return True

## alternative answer
def find_nondup(values):
    seen = {}
    for v in values:
        if v in seen:
            del seen[v]
        else:
            seen[v] = 1

    return seen.keys()[0]

print find_non_duplicate(a)
print find_non_duplicate(b)


def findSmallestInt(arr):
    """ Return min in the array """
    smallest = arr[0]
    for x in arr:
        if x < smallest:
            smallest = x
    return smallest


def find_smallest(arr):
    return min(arr)

print find_smallest([78,56,232,12,11,43])

print find_smallest([78,56,-2,12,8,-33])
print find_smallest([0, -1-sys.maxint,sys.maxint])


def find_short(s):
    lista = s.split()
    l = len(lista[0])
    for x in lista:
        if len(x) < l:
            l = len(x)
    return l

def make_negative( number ):
    """ Return a negative number.
    input: Any intger could be 0, positive or negative.
    output: If 0 return 0 else return negative of that number."""
    if number > 0:
        return -1 * number
    else:
        return number

def multiply(a, b):
    if isinstance(a,int) and isinstance(b,int):
      return (a * b)
    else:
        return None

def find_len_of_short_substring(s):
    l = min([len(x) for x in s.split()])
    return l

print find_short("Lets all go on holiday somewhere very cold")


print "*" * 100
#Calculate how many times a number can be divided by a given number.
def divide_number(num, divider):
    i = 0
    while num // divider != 0:
        num //= divider
        i += 1
    return i

print divide_number(100,2)
print divide_number(6,2)
print divide_number(600,2)
print divide_number(2450,5)


print '*' * 40
## Linear search
def linear_search_algo_1(arr, item):
    pos = None
    counter = 1
    for x in range(len(arr)):
        if arr[x] == item:
            pos = x
            return pos, counter
        elif arr[x] != item:
            counter += 1
    if pos == None:
        arr.append(item)
    return arr

print linear_search_algo_1([1,2,3,4,5,6], 4)
print linear_search_algo_1([1,2,3,4,5,6], 0)


def linear_search_2(arr, item):
    pos = 0
    found = False
    while pos < len(arr) and not found:
        if arr[pos] == item:
            found = True
            return pos
        pos += 1
    if pos == None:
        arr.append(item)
        return arr


print linear_search_2([1,2,3,4,5,6], 4)
print linear_search_2([1,2,3,4,5,6], 0)


## Who likes it?
def likes(names):
    # make a dictionary d of all the possible answers. Keys are the respective number
    # of people who liked it.

    # {} indicate placeholders. They do not need any numbers but are simply replaced/formatted
    # in the order the arguments in names are given to format
    # {others} can be replaced by its name; below the argument "others = length - 2"
    # is passed to str.format()
    d = {
        0: "no one likes this",
        1: "{} likes this",
        2: "{} and {} like this",
        3: "{}, {} and {} like this",
        4: "{}, {} and {others} others like this"
    }
    length = len(names)
    # d[min(4, length)] insures that the appropriate string is called from the dictionary
    # and subsequently returned. Min is necessary as len(names) may be > 4

    # The * in *names ensures that the list names is blown up and that format is called
    # as if each item in names was passed to format individually, i. e.
    # format(names[0], names[1], .... , names[n], others = length - 2
    return d[min(4, length)].format(*names, others=length - 2)

print likes([])
print likes(['Peter'])
print likes(['Jacob', 'Alex'])
print likes(['Max', 'John', 'Mark'])
print likes(['Alex', 'Jacob', 'Mark', 'Max'])


print '*' * 20
names = ['acv' ,'abc', 'aff', 'utut', 'dfdf']
length = len(names)
d = {
    0: "no one likes this",
    1: "{} likes this",
    2: "{} and {} like this",
    3: "{}, {} and {} like this",
    4: "{}, {} and {others} others like this"
}

print d[min(4, length)].format(*names, others=length - 2)


def sort_array(source_array):
    if len(source_array) == 0:
        return source_array
    else:
        new_arr = source_array[:]
        smallest = None

        for x in range(0, 1):
            if source_array[x] % 2 == 0:
                pass
            else:
                smallest = source_array[x]

        for x in range(len(source_array)):
            if source_array[x] % 2 == 0 or source_array[x] == 0:
                new_arr[x] = source_array[x]
            elif source_array[x] % 2 != 0 and source_array[x] < smallest:

                new_arr.insert(new_arr.index(smallest), source_array[x])
                smallest = source_array[x]
                del new_arr[x + 1]
            else:
                pass
        return new_arr


print sort_array([5, 3, 2, 8, 1, 4])



def sort_array(source_array):
    if len(source_array) == 0:
        return source_array
    else:
        new_arr = source_array[:]
        smallest = None

        for x in range(0, 1):
            if source_array[x] % 2 == 0:
                pass
            else:
                smallest = source_array[x]

        for x in range(len(source_array)):
            if source_array[x] % 2 == 0 or source_array[x] == 0:
                new_arr[x] = source_array[x]
            elif source_array[x] % 2 != 0 and source_array[x] < smallest:

                new_arr.insert(new_arr.index(smallest), source_array[x])
                smallest = source_array[x]
                del new_arr[x + 1]
            else:
                pass
        return new_arr


print sort_array([5, 3, 2, 8, 1, 4])



def sort_array(source_array):
    if len(source_array) == 0:
        return source_array
    else:
        new_arr = source_array[:]
        smallest = None

        for x in range(0, 1):
            if source_array[x] % 2 == 0:
                pass
            else:
                smallest = source_array[x]

        for x in range(len(source_array)):
            if source_array[x] % 2 == 0 or source_array[x] == 0:
                new_arr[x] = source_array[x]
            elif source_array[x] % 2 != 0 and source_array[x] < smallest:

                a, b = new_arr.index(smallest), new_arr.index(source_array[x])
                new_arr[b], new_arr[a] = new_arr[a], new_arr[b]
                new_arr
        return new_arr


print sort_array([5, 3, 2, 8, 1, 4])


## ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain
## # anything but exactly 4 digits or exactly 6 digits.
## If the function is passed a valid PIN string, return true, else return false.

print 'M' * 15
def validate_pin(pin):
    new_pin = pin[:]
    smallest = pin[0]
    for x in range(len(pin)):
        if isinstance(pin[x], int) and  pin[x] < smallest:
            new_pin.insert(new_pin.index(smallest), pin[x])
            smallest = pin[x]
            del new_pin[x+1]
        elif not isinstance(pin[x], int):
            return None

    return new_pin



a_ints = [9,4,2,10,11,1,3]
b_ints = [-1,2,3,a]
print validate_pin(a_ints)
print validate_pin(b_ints)


print 'oo' * 15
def validate_pin(pin):
    new_pin = pin[:]
    smallest = pin[0]
    for x in range(len(pin)):
        if isinstance(pin[x], int) and  pin[x] < smallest:
            a, b = new_pin.index(smallest), new_pin.index(pin[x])
            new_pin[b], new_pin[a] = new_pin[a], new_pin[b]
        elif not isinstance(pin[x], int):
            return None

    return new_pin



a_ints = [9,4,2,10,11,1,3]
b_ints = [-1,2,3,a]
print validate_pin(a_ints)
print validate_pin(b_ints)



## Given an array (a list in Python) of integers and an integer n, find all occurrences
## of n in the given array and return another array containing all the index
# positions of n in the given array. If n is not in the given array, return an empty array [].

#Assume that n and all values in the given array will always be integers.
def find_all(array, n):
    trach_index = []
    for ind, e in enumerate(array):
        if e == n:
            pass

# Find binary value of a given int
def find_highest_power_2(num):
    n=0
    while 2**n <= num:
        n += 1
    return n-1

def add_binary(a,b):
    sum = a + b
    number = 0
    while sum != 0:
        place_holder = find_highest_power_2(sum)
        number += 10**place_holder
        sum = sum - 2**place_holder
    return str(number)


#Replace With Alphabet Position
# Welcome. In this kata you are required to, given a string,
# replace every letter with its position in the alphabet.
# If anything in the text isn't a letter,
# ignore it and don't return it. a being 1,
# b being 2, etc. As an example:
import string
def alphabet_position(text):
    alphabet_dict = dict(zip(string.ascii_lowercase, range(1,27)))


# sum_two_smallest_numbers
def sum_two_smallest_numbers(numbers):
    least_a, least_b = numbers[0], numbers[1]
    for v in numbers[2:]:
        print v
        if v < least_a:
            print v
            least_a = v
        elif  least_a < least_b:
            least_b = least_a
    print least_a, least_b
    return least_a + least_b

print "XX00" * 7
print sum_two_smallest_numbers([90,92,93,94,99,9,8,2])



print "90909090" * 5
def sqrt(x):
    ans = 0
    if x >= 0:
        while ans*ans < x:
            ans += 1
        if ans*ans != x:
            print x, 'is not a perfect square'
        else:
            return ans
    else:
        print x, "is a negative number"
        return None
print sqrt(25)
print sqrt(90)


print "****" * 10
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print factorial(12)


def ispalindrome(string1):
    if len(string1) <=1 :
        return True
    else:
        return string1[0] == string1[-1] and ispalindrome(string1[1:-1])

print "$$$" * 15
print ispalindrome("aabbaa")
print ispalindrome("aabba")



class Foo(object):
    """ 
    if type is different in the argument, reset counter to 1.
    Otherwise increament counter by 1. Use start_range as a starting point.
    """

    type_name = "bar"
    counter = 1

    def __init__(self, next_type_name, start_range):
        self.next_type_name = next_type_name
        self.start_range = start_range
        self.reset()


    def reset(self):
        Foo.counter =self.start_range
        print self.next_type_name, Foo.type_name
        if Foo.type_name != self.next_type_name:
            print "here..."
            Foo.counter = self.start_range+1
            Foo.type_name = self.next_type_name
        else:
            Foo.counter += 1
            print Foo.counter





print "-------------------------- bar "
d = Foo("bar", 100)
print d.counter
## result >> 101

print "-------------------------- list "
new_instances = []
for i in range(0, 10):
    new_instances.append(Foo("bar", 100))
    print new_instances[i].counter
## result >> 102, 103, 104, 105, 106, 107, 108, 109, 110, 111


print "-------------------------- test starts here ... "
c = Foo("test", 200)
print c.counter
## result >> 201

print "-------------------------- test "
e = Foo("test", 200)
print e.counter
## result >> 202

print "-------------------------- test "
f = Foo("test", 200)
print f.counter
## result >> 203
