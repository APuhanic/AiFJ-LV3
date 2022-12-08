import re
from operators import is_operator
from keywords import is_keyword
from separators import is_separator
from comment import is_comment
from constant import is_constant
from pathlib import Path
from collections import Counter

def analyze_keyword(word):
    print("('",word,"', ključna riječ)")
    #Ako je var ili fun postavlja zastavicu last_word na True da bi se sljedeca rijec mogla spremiti kao identifikator
    if word == "var" or word == "fun" or word == "const":
        return True
    return False

filepath = Path(__file__).parent / "Code.txt"
file = open(filepath, "r")

lines=file.readlines()

identifiers = []
operators = []
separators = []
comments = []
constants = []

if len(lines) <= 0:
    print ("File is empty")
    quit(0)

line_number = 1

for line in lines:
    print("---Linija: ", line_number)
    line_number += 1
    last_word = False
    last_word_const = False
    #Regex koristen da bi se separatori i operatori odvojili razmacima
    words = re.sub(r"(\(|\)|;|\+|\-|\=|\#)", r' \1 ', str(line))
    #Regex funkcija koja razdvaja sve između razmaka i stavlja u objekt, tj. niz
    words = words.split()

    if is_comment(words[0]):
        comments.append(words[0])
        print("('",words[0],"', komentar), (",' '.join(words[1:]),")")
        continue

    #Prođi kroz svaku "rijec" i analiziaj
    for word in words:
        #Analizira je li riječ vec definiran keyword
        if is_keyword(word):
            last_word = analyze_keyword(word)
            continue #Continue nije dobro riješenje za ovo

        if is_operator(word):
            operators.append(word)
            print("('",word,"', operator)")
            continue

        if is_separator(word):
            separators.append(word)
            print("('",word,"', separator)")
            continue
            
        if is_constant(word):
            print("('",word,"', ključna riječ)")
            last_word_const = True
            continue

        if last_word_const:
            constants.append(word)
            print("('",word,"', konstanta)")
            last_word_const = False
            continue

        if last_word:
            #Dodaje trenutnu rijec u listu identifikatora ako je zadnja bila var ili fun
            identifiers.append(word)
            print("('",word,"', identifikator)")
            last_word = False
            continue

        if word in identifiers:
            print("('",word,"', identifikator)")
            continue

        if not is_keyword(word) or not is_operator(word) or not is_separator(word):
            print("('",word,"', vrijednost)")

print("Identifikatori: ", len(identifiers), str(Counter(identifiers))[8:-1])

print("Separatori: ", len(separators), str(Counter(separators))[8:-1])

print("Operatori: ", len(operators), str(Counter(operators))[8:-1])

print("Komentari: ", len(comments), str(Counter(comments))[8:-1])

print("Konstante: ", len(constants), str(Counter(constants))[8:-1])