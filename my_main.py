# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True



def find_anagram(word, anagram):
    if sorted(word) == sorted(anagram):
        print(True)
    else:
        print(False)

value1  = input('What is the first word? ')
value2 = input('What is the second word? ')

find_anagram(value1, value2)
