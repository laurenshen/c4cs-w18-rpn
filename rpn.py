#!/usr/bin/env python3

import operator
from colored import fg, bg, attr


operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    while True:
        result = calculate(input("rpn calc> "))
        if result < 0:
            color = bg('indian_red_1a') + fg('white')
            reset = attr('reset')
            print(color + "Result: " + result + reset)
        elif:
            print("Result: ", result)

if __name__ == '__main__':
    main()