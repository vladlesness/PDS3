import os


def write_dict(dictionary, name):
    with open(name, 'w') as file:
        for k, v in dictionary.items():
            # adjust dict keys and values and assign to a variable
            to_write = str(k) + ': ' + str(v) + '\n'
            # write the string to the file in a new line
            file.write(to_write)


def read_file(file_name):
    dictionary = {}
    with open(file_name) as file:
        lines = file.read()
    # split the string into a list by '\n'
    line_list = lines.split('\n')
    # the list has an empty string as the last item, remove it
    line_list.pop()
    # split each element into a list by ': ' to have a nested list
    line_list = [i.split(': ') for i in line_list]
    # loop over the nested list and update the dict with a key and value
    for i in line_list:
        dictionary[i[0]] = float(i[1])

    return dictionary


def get_directory_files():
    directory_file_list = os.listdir()
    for i in directory_file_list:
        # check if an item is a directory
        if os.path.isdir(i):
            # get the index of the item
            index = directory_file_list.index(i)
            # update a dir item with '|'
            directory_file_list[index] += '|'

    print(directory_file_list, 'Number of files and directories: ' + str(len(directory_file_list)), sep='\n')


movie_rating_dict = {
    'Breaking Bad': 9.5,
    'Dexter': 8.7,
    'The Matrix': 8.7,
    'Prison Break': 8.3,
    'Sherlock': 9.1,
    'The Walking Dead': 8.1
}
