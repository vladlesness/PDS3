import sys


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as ex:
        print(f'{ex}', file=sys.stderr)
        return 0


print(divide(1, 1))
print(divide(1, 0))