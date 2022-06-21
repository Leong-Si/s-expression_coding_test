import sys

def calc(expr):
    if isinstance(expr, int):
        return expr
    elif isinstance(expr, str):
        # check if the expr is only digit, therefore an int in string form
        # this can happen when calc() is first called from main()
        if expr.isdigit():
            return expr

        # removes leading and trailing whitespace
        expr = expr.strip()
        if expr.startswith('(') and expr.endswith(')'):
            # removes parenthesis
            expr = expr[1:-1]
            return expr
    #

def main():
    if len(sys.argv) > 1:
        print(calc(sys.argv[1]))

    # Do nothing if there is not enough arguments

if __name__ == '__main__':
    main()
