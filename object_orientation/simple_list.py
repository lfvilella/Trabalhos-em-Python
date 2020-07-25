class SimpleList():

    def __init__(self, items):
        self._items = list(items)

    def __getitem__(self, index):
        return self._items[index]

    def add(self, item):
        self._items.append(item)

    def sort(self):
        self._items.sort()

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return f"{type(self).__name__}({self._items!r})"


class SortedList(SimpleList):

    def __init__(self, items=()):
        super().__init__(items)
        self.sort()

    def add(self, item):
        self._items.append(item)
        self.sort()


class IntList(SimpleList):

    def __init__(self, items=()):
        for x in items: self._validate(x)
        super().__init__()

    def _validate(self, x):
        if not isinstance(x, int):
            raise TypeError("IntList only supports integers values.")

    def add(self, item):
        self._validate(item)
        super().add(item)


class SortedIntList(IntList, SortedList):
    """ Quick Explanation

        When created a instance of this class the __init__ starts
        on IntList class (MRO), so there the method super() goes
        to call SortedList.__init__
    """
    pass


if __name__ == '__main__':
    _list = SimpleList([5, 2, 1, 10, 0])
    sorted_list = SortedList([5, 2, 1, 10, 0])
    print(_list, sorted_list)

    _list.sort()
    sorted_list.add(22)
    print(_list)
    print(sorted_list.__len__())

    print(SortedIntList.__bases__)
    print(SortedIntList.__mro__)
    sorted_int_list = SortedIntList()
    sorted_int_list.add(22)
    sorted_int_list.add(1)
    print(sorted_int_list)

    # Uncomment below to get an error:
    # sorted_int_list.add('1')
