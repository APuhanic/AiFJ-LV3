import re
from operators import is_operator
from keywords import is_keyword
from separators import is_separator

file = open("code.txt", "r")

lines=file.readlines()

identifiers = []

if len(lines) <= 0:
    print ("File is empty")
    quit(0)

line_number = 0

for line in lines:
    words = line.split()
    print("Linija: ", line_number)
    for word in words:
        if is_keyword(word):
            print("Keyword: ", word)
            if word == "var" or word == "fun":
                last_word = True
            continue
        if is_operator(word):
            print("Operator: ", word)
            continue
        if is_separator(word):
            print("Separator: ", word)
            continue
        if last_word:
            identifiers.append(word)
            print("Identifier: ", word)
            last_word = False
            continue
        print("Value: ", word)
        line_number += 1

        


