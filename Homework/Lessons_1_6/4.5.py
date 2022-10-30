from string import ascii_lowercase


def max_repeated_letter(line: str):
    # lowercase the string
    lower_cased_line = line.lower()
    # create an empty dict to add keys and values
    count_dict = {}

    # loop over the unique/set values of the string
    for l in set(lower_cased_line):
        # check if a value is a Latin letter
        if l in ascii_lowercase:
            # update the dict with a key as a number of letter occurrences and value as a letter
            count_dict.update({lower_cased_line.count(l): l})
        else:
            continue

    # find the max of letter occurrences from dict.keys
    max_value = max(count_dict.keys())
    return count_dict[max_value]
