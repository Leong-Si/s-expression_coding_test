import sys

# Find the first valid expression
def firstExpr(args):
    if not args.startswith('('):
        return args.split(maxsplit=1)[0]
    else:
        openParenCount = 1
        closeParenCount = 0
        loopIndex = 1

        while loopIndex < len(args) and openParenCount != closeParenCount:
            arg = args[loopIndex]
            if arg == '(':
                openParenCount = openParenCount + 1
            elif arg == ')':
                closeParenCount = closeParenCount + 1
            loopIndex = loopIndex + 1

        return args[:loopIndex]

# Assuming matching open and close parenthesis, and formatting are all correct
def calc(expr):
    if expr.isdigit():
        return int(expr)
    if expr.startswith('(') and expr.endswith(')'):
        # removes outer parenthesis
        expr = expr[1:-1]

        # separate function name and the rest of the expression
        (funcName, separator, funcArgs) = expr.partition(' ')
        funcName = funcName.lower()

        argsLen = 0
        args = []

        while argsLen < len(funcArgs):
            resultArg = firstExpr(funcArgs[argsLen:])
            args.append(resultArg)
            argsLen = argsLen + len(resultArg) + 1  # +1 for the trailing whitespace

        # optionally check args length

        if funcName == 'add':
            return calc(args[0]) + calc(args[1])
        elif funcName == 'multiply':
            return calc(args[0]) * calc(args[1])

    # If code reaches here, optionally throw an error

def main():
    if len(sys.argv) > 1:
        arg = sys.argv[1].strip()
        if isinstance(arg, int):
            print(arg)
        elif isinstance(arg, str):
            print(calc(arg))

    # Do nothing if there is not enough arguments

if __name__ == '__main__':
    main()
