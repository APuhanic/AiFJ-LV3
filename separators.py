separators = [';',',',' ',"'", '(', ')', '=', ':', '-']

def is_separator(separator):
    if separator in separators:
        print("Separator: ",separator)
        return True
    return False
