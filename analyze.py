import re
from operators import is_operator
from keywords import is_keyword

file = open("code.txt", "r")

lines=file.readlines()

if len(lines) <= 0:
    print ("File is empty")
    quit(0)

for line in lines:
    words = line.split()
    for word in words:
        if(is_keyword(word)):
            print("Keyword: ", word)
