import sys


def find_index(lst, index):
    try:
        return lst[index]
    except IndexError as ex:
        print(f'{ex}', file=sys.stderr)
        return -1


print(find_index([1, 2, 3], 3))