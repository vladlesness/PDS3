from sys import stderr
from EmptyIterableException import EmptyIterableError


def check_unique_values(iterable):
    count = 1
    try:
        if not iterable:
            raise EmptyIterableError('Your iterable is empty')
        for n in iterable:
            if iterable.count(n) > count:
                count = iterable.count(n)
                max_count = n
        if count == 1:
            return 'Your iterable has unique values'
        return f'Your iterable does not have unique values. {max_count} has {count} occurrences.'
    except TypeError as ex:
        print(f'{ex}, your argument must be an iterable', file=stderr)
    except EmptyIterableError as ex:
        print(ex, file=stderr)
    except Exception as ex:
        print(ex, file=stderr)


# print(check_unique_values([]))