#string practice

print("length of the string:")
sentence = "It is our choices that show what we truly are, happiness can be found even in the darkest of times, and words are our most inexhaustible source of magic"
print(len(sentence))

some_words = "Life is a journey filled with challenges, lessons, and beautiful moments that shape who we become over time. Every mistake teaches wisdom, every success builds confidence, and every difficult day reminds us to value happiness even more. No matter how slow progress feels, staying patient, focused, and hopeful can turn even the smallest efforts into meaningful achievements and lasting memories."
print(len(some_words))

#upper case and lower case 

print("upper case and lower case:")
print(sentence.upper())
print(sentence.lower())

print(some_words.upper())
print(some_words.lower())

#counting characters

print("counting characters:")
someoncename = "John Doe lives in a small town. John Doe is a kind person who loves to help others. Many people in the town know John Doe and appreciate his generosity."
print(someoncename.count("John"))

#bringing first and last character and printing them

print("first and last character changing:")
str = "Hello, World!"

print("First character:", str[0])
print("Last character:", str[-1])
print("First and Last character:", str[0], str[-1])

if str :
    print("first character:", str[0])
    print("last character:", str[-1])

else:print("The string is empty.")

#substring

print("new line substring:")
bookname = "The Great Gatsby"

print(bookname[4:9])
print(bookname[0:3])
print(bookname[10:15])
print(bookname[0:15])
print(bookname[5:12])

#string slicing

print("string slicing:")
news = "Breaking news: Scientists discover a new species of bird in the Amazon rainforest, showcasing the incredible biodiversity of our planet and highlighting the importance of conservation efforts to protect these unique ecosystems for future generations."

print(news[0:8])
print(news[9:14])
print(news[15:25])
print(news[-20:-15])

#string reversal

print("string reversal:")

print(news[::-1])
print(sentence[::-1])
print(news[::-3])

#string character replacement

print("string character replacement:")

sentence2 = "The quick brown fox jumps over the lazy dog."

print(sentence2.replace("dog", "cat"))
print(sentence2.replace("fox", "rabbit"))
print(sentence2.replace("lazy", "energetic"))

#split and join

print("split and join:")

sentence3 = "Python is a powerful programming language that is widely used for web development, data analysis, artificial intelligence, and more."
print(sentence3.split())
print("-".join(sentence3.split()))

#strip and whitespace removal

print("strip and whitespace removal:")

sentence4 = "   Hello, World!   "

print(sentence4.strip())
print(sentence4.lstrip())
print(sentence4.rstrip())


#counting vowels and consonants

print("counting vowels and consonants:")
sentence5 = "Programming is fun and rewarding, allowing us to create amazing applications and solve complex problems while continuously learning and improving our skills in the ever-evolving world of technology."

for character in sentence5.lower():
    if character in "aeiou":
        print("vowel:" , character)
    elif character.isalpha():
        print("consonant:" , character)

#palindrome check

print("palindrome check:")

sentence6 = ["madam" , "racecar"]
cleaned_sentence = ''.join(character.lower() for character in sentence6 if character.isalnum())
if cleaned_sentence == cleaned_sentence[::-1]:
    print("The sentence is a palindrome.")
else:
    print("The sentence is not a palindrome.")

#conerting string into title without using title function

sentence7 = "tHe qUick bROwn fOX jUMps oVER tHE lAZY dOG"
new_sentence = []
splitted_sentence = sentence7.split()
for word in splitted_sentence:
    new_sentence.append(word[0].upper() + word[1:].lower())
print(" ".join(new_sentence))

#find all indices of a substring in a string

sentence8 = "The rain in Spain stays mainly in the plain."

substring = "ain"

for i in range(len(sentence8)):
    if sentence8[i:i+len(substring)] == substring:
        print("Substring found at index:", i)

#character frequency count

sentence9 = "is this the real life? is this just fantasy? caught in a landslide, no escape from reality."
frequency = {}

for character in sentence9:
    if character in frequency:
        
        frequency[character] += 1
    else:
        frequency[character] = 1

print(frequency)

#anagram check

string1 = "listen"
string2 = "silent,"

cleaned_string1 = "".join(c.lower() for c in string1 if c.isalnum() and c.isalpha())
cleaned_string2 = "".join(c.lower() for c in string2 if c.isalnum() and c.isalpha())

if sorted(cleaned_string1) == sorted(cleaned_string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

#compress repeated characters in a string

text = "aaabbcaaa"

count = 1

for i in range(len(text)-1):
    if text[i] == text[i+1]:
        count += 1
    else:
        print(text[i] , count)
        count = 1
print(text[-1] , count)

#longest word in a string

sentence10 = "The quick brown fox jumps over the lazy dog"

words = sentence10.split()
longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest word:", longest_word)

#removing duplicates from a string

sentence11 = "a quick brown fox jumps over the lazy dog"

seen = set()
result = ""

for character in sentence11:
    if character not in seen:
        seen.add(character)
        result += character

print(result)

#masked username in email

email = "shfuiwie@gmail.com"

parts = email.split("@")
username = parts[0]
domain = parts[1]

masked_username = username[0] + "*" * (len(username) - 2) + username[-1]

print(masked_username + "@" + domain)



