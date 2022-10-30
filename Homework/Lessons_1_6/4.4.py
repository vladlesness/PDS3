def sum_of_digits_from_number(number: int):
    total = 0

    for digit in str(number):
        total += int(digit)

    return total
