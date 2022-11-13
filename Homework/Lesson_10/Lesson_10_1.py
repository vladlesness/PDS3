import sys


def get_month_name(month_number: int):
    month_tuple = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                   'September', 'October', 'November', 'December')
    try:
        return month_tuple[month_number - 1]
    except TypeError as ex:
        print(f'You got {ex}. Please enter an integer 1 to 12', file=sys.stderr)
    except IndexError as ex:
        print(f'You got {ex}. Please enter an integer 1 to 12', file=sys.stderr)
    except Exception as ex:
        print(f'You got {ex}. Please enter an integer 1 to 12', file=sys.stderr)
    finally:
        return -1
