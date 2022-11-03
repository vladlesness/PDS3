def rectangle_area(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('The sides are not int or float')
    elif a <= 0 or b <= 0:
        raise ValueError('The sides are less than 0 or equal to 0')
    return a * b
