#Python list intermediate level exercises


#list comprehension that returns a list of squares of even numbers

square = [x**2 for x in range(20) if x % 2 == 0]
print(square)

#modify the list without changing the original list

nums = [3,1,4,1,5,9]

sorted_nums = sorted(nums)
print("Original list:", nums)
print("Sorted list:", sorted_nums)

#remove duplicates from a list while preserving the order

nums = [3,1,4,1,5,9,3,4]
unique_nums = []
for n in nums:
    if n not in unique_nums:
        unique_nums.append(n)
print("Original list:", nums)
print("List without duplicates:", unique_nums)

#flatten a nested list using list comprehension

nested = [[1, 2, 3], [4, 5], [6, 7, 8]]
flat = [item for sublist in nested for item in sublist]
print(flat)

#sort name alphabetically but ignore case

names = ["Alice", "bob", "Charlie", "dave"]
sorted_names = sorted(names, key=str.lower)
print(sorted_names)

#replace items from index in a list using slicing

numbers = [10, 20, 30, 40, 50 , 60]
numbers[2:5] = [100, 200]
print(numbers)

#find all indices of a specific value in a list

numbers = [1, 2, 3, 2, 4, 2, 5]

indices = [index for index, value in enumerate(numbers) if value == 2]
print(indices)

#number in list only appears once

numbers = [1, 2, 3, 2, 4, 2, 5]
unique_numbers = [x for x in numbers if numbers.count(x) == 1]
print(unique_numbers)

#rotate a list to the right by one positions

list1 = [1, 2, 3, 4, 5]
rotated_list = [list1[-1]] + list1[:-1]
print(rotated_list)

#split a list into two list diffrence by odd and even numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = [x for x in numbers if x % 2 == 0]
odd_numbers = [x for x in numbers if x % 2 != 0]
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

#Python tuple intermediate level exercises


#convert a list into a tuple and name them with a variable

numbers_list = [1, 2, 3, 4, 5]
t = tuple(numbers_list)
a, b, c, d, e = t
print(a, b, c, d, e)

#pick up second element
tu = ((a,1), (b,2), (c,3), (d,4), (e,5))
second_element = [x[1] for x in tu]
print(second_element)

#write a function that returns multiple values

def calculate(numbers):
    return sum(numbers), max(numbers), min(numbers)

numbers = [10, 20, 30, 40, 50]
total, maximum, minimum = calculate(numbers)
print("Total:", total)
print("Maximum:", maximum)
print("Minimum:", minimum)

#combine two tuples by adding

t1 = (1, 2, 3)
t2 = (4, 5, 6)

combined_tuple = t1 + t2
list_c = list(combined_tuple)
print(list_c)

#find the number with the highest frequency

t = [1,2,2,3,3,3,4,2]
highest = None
max_count = 0

for item in set(t):
    if t.count(item) > max_count:
        max_count = t.count(item)
        highest = item

print(highest)

#check if two tuple contains same elements

t1 = (1, 2, 3)
t2 = (3, 2, 1)
if sorted(t1) == sorted(t2):
    print("The tuples contain the same elements.")
else:
    print("The tuples do not contain the same elements.")

#extract last three elements from a tuple

t = (10,20,30,40,50,60)
last_three = t[-3:]
print(last_three)

#multiply all elements in a tuple

t = (1, 2, 3, 4, 5)
result = t*3
print(result)

#convert a nested tuple

t = ((1, 2), (3, 4), (5, 6))
flat = tuple(item for subtuple in t for item in subtuple)

print(flat)

#store coordinates in tuple and calculate the manhattan distance

point1 = (2, 3)
point2 = (5, 7)

distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
print(distance)


#Python set intermediate level exercises


#find elements that are in one set but not in another

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
difference = set1 - set2
print(difference)

#find common items in 3 sets

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {4, 5, 6, 7}

common_items = set1 & set2 & set3
print(common_items)

#give senetce in lowercase and return unique words in a set

sentence = "This is a sample sentence with some sample words"
words = set(sentence.lower().split())

print(words)

#convert a list with duplicates into a set

numbers = [1, 2, 3, 2, 4, 5, 1]
result = sorted(set(numbers))
print(result)

#check if one set is a subset of another

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

if set1 < set2:
    print("set1 is a subset of set2")
else:
    print("set1 is not a subset of set2")

#using set comprehension to collect all squares of numbers

squares = {x * x for x in range(1 , 16) if x % 3 == 0}

print(squares)

#count how many duplicates are in a list using set

numbers = [1, 2, 3, 2, 4, 5, 1]
duplicates = len(numbers) - len(set(numbers))

print(duplicates)

#write a program to remove all vowels from a string using set

text = "This is a sample sentence with some vowels"
vowels = {'a', 'e', 'i', 'o', 'u' , 'A', 'E', 'I', 'O', 'U'}

result = ''.join([char for char in text if char not in vowels])

print(result)

#find symmetric difference between two sets

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

symmetric_difference = set1 ^ set2
print(symmetric_difference)

#check if two sets are anagrams using set comprehension (unique letters)

set1 = {1, 2, 3}
set2 = {3, 2, 1}

if set(set1) == set(set2):
    print("The sets are anagrams.")
else:
    print("The sets are not anagrams.")



#python dictionary intermediate level exercises



#count word frequency in a sentence and store the result in a dictionary

sentence = "This is a sample sentence with some sample words"

words = sentence.split()
word_freq = {}

for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

print(word_freq)

#invert a dictionary where all values are unique

original_dict = {'a': 1, 'b': 2, 'c': 3}

inverted_dict = {}

for key, value in original_dict.items():
    inverted_dict[value] = key

print(inverted_dict)

#merge two dictionaries where second dictionary overwrites the first one

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged_dict = {**dict1, **dict2}

print(merged_dict)

#group words by their first letter using a dictionary

words = ["apple", "banana", "cherry", "avocado", "blueberry"]
groups = {}

for word in words:
    groups.setdefault(word[0], []).append(word)

print(groups)

#filter a dictionary to only include items with values greater than a certain threshold

scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 90}

result = {key: value for key, value in scores.items() if value > 80}

print(result)

#given a nested dictionary , safely access a deeply nested key

data = {"student":{"address":{"city":"New York"}}}

city = data.get("student", {}).get("address", {}).get("city")

print(city)

#write a dictionary comprehension that maps numbers to their cubes

cubes = {x: x**3 for x in range(1, 11)}

print(cubes)

#find the key with the maximum value in a dictionary

scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 90}

max_key = max(scores, key=scores.get)

print(max_key)

#combine two lists into a dictionary

keys = ['a', 'b', 'c']
values = [1, 2, 3]

result = dict(zip(keys, values))

print(result)

#remove all keys from dictionary with none values

data = {
'a': 1,
'b': None,
'c': 3,
'd': None
}

result = {key: value for key, value in data.items() if value is not None}

print(result)


#End of intermediate level exercises for list, tuple, set and dictionary in python