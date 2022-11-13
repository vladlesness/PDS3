class EmptyIterableError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'{self.message}'
        else:
            return 'EmptyIterableError'


# raise EmptyIterableError('!')
# err = EmptyIterableError()
# err2 = EmptyIterableError('empty')
# print(err)
# print(err2.message)