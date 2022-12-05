separators = [';',',',' ',"'", '(', ')', '=', ':', '-', '{', '}']

def is_separator(separator):
    if separator in separators:
        return True
    return False
