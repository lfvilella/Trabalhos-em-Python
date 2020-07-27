def list_generator(_list):
    for item in _list:
        yield item


if __name__ == "__main__":
    _list = [0, 1, 2, 3, 4, 5]
    _list = list_generator(_list)
    print(_list)

    for x in range(6):
        print(next(_list))
