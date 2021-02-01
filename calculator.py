import graphics
logo = graphics.logo

#Calculator functions
def add(n1,n2):
    """addition """
    return n1+n2

def substract(n1,n2):
    """substraction"""
    return n1-n2

def multiply(n1,n2):
    """multiplication"""
    return n1 * n2

def divide(n1,n2):
    """divison"""
    return n1/n2
#Dict with he calculator functions
calc_functions =  {
    "+" : add,
    "-" : substract,
    "/" : divide,
    "*" : multiply
}

def calculator():
    print(logo)
    num1 =float(input("What is the first number? :> ")) 
    for i in calc_functions.keys():
        print(i)

    should_continue = True
    while should_continue:
        operation_symbol = str(input("Pick an operation symbol:> "))
        num2 =float(input("What is the next number? :> "))
        function = calc_functions[operation_symbol]
        answer = function(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}" )

        if input(f"Type 'y' to continue calcualting with {answer} or  type 'n' to start new calculation") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()


