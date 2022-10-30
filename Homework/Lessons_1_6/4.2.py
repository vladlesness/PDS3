def concat_dicts(*args):
    assembled_dict = {}

    for i in args:
        assembled_dict.update(i)

    return assembled_dict
