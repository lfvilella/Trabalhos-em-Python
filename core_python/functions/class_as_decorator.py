class CallCount:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)


@CallCount
def hello(name):
    print(f"Hello {name} !")


class Trace:
    def __init__(self):
        self.enable = True

    def __call__(self, f):
        def wrapper(*args, **kwargs):
            if self.enable:
                print(f"Calling {f}")
            return f(*args, **kwargs)

        return wrapper


tracer = Trace()


@tracer
def rotate_list(_list):
    return _list[1:] + [_list[0]]


if __name__ == "__main__":
    hello("Person1")
    print(f"Counter: {hello.count}")
    hello("Person2")
    hello("Person3")
    print(f"Counter: {hello.count}")

    _list = [1, 2, 3]
    _list = rotate_list(_list)
    print(_list)
