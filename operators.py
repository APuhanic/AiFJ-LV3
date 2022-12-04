operators = ['+','-','/',"!", '*', '<', '>']

def is_operator(operator):
    if operator in operators:
        print("Separator: ",operator)
        return True
    return False
