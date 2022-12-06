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

line_number = 1

for line in lines:
    print("---Linija: ", line_number)
    line_number += 1
    last_word = False
    #Regex koristen da bi se separatori i operatori odvojili razmacima
    words = re.sub(r"(\(|\)|;|\+|\-|\=)", r' \1 ', str(line))
    #Regex funkcija koja razdvaja sve između razmaka i stavlja u objekt, tj. niz
    words = words.split()

    #Prođi kroz svaku "rijec" i analiziaj
    for word in words:
        #Analiza je li riječ vec definiran keyword
        if is_keyword(word):
            print("Keyword: ", word)
            #Ako je keyword, onda za var i fun postavlja zastavicu last_word na True da bi se sljedeca rijec mogla spremiti kao identifikator
            if word == "var" or word == "fun":
                last_word = True
            continue #Continue nije dobro riješenje za ovo

        if is_operator(word):
            print("Operator: ", word)
            continue

        if is_separator(word):
            print("Separator: ", word)
            continue
            

        if last_word:
            #Dodaje trenutnu rijec u listu identifikatora ako je zadnja bila var ili fun
            identifiers.append(word)
            print("Identifier: ", word)
            last_word = False
            continue

        if word in identifiers:
            print("Identifier: ", word)
            continue

        if not is_keyword(word) or not is_operator(word) or not is_separator(word):
            print("Value: ", word)
