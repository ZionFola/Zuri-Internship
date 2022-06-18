# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}



def read_file_content(filename):
    with open("story.txt", "r") as file:
        data = file.read()
    print(data)
read_file_content("story.txt")


from collections import Counter
import re

text = read_file_content("./story.txt")
with open("story.txt", "r") as file:
    data = file.read()
count_words = Counter(re.findall('\w+', data))

print(count_words)
