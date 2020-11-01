import sys

def func1(number):
    num = int(number)
    if num < 0: # or (not num.isnumeric()):
        print("No.")
    elif num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return (func1(num-1) + func1(num-2))


for line in sys.stdin:
    print("Input was: " + str(line))
    print("Fibonacci output: " + str(func1(line)))