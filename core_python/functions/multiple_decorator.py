def escape_unicode(f):
    def wrapper(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrapper


class Trace:
    def __init__(self):
        self.enable = True

    def __call__(self, f):
        def wrapper(*args, **kwargs):
            if self.enable:
                print(f"Calling {f}")
            return f(*args, **kwargs)

        return wrapper


@Trace()
@escape_unicode
def my_function(word):
    return word + 'øß'


# Decorating Methods
class Maker:

    def __init__(self, sufix):
        self.sufix = sufix

    @Trace()
    def make_something(self, word):
        return word + self.sufix


if __name__ == "__main__":
    print(my_function("Python2"))
    print(my_function("Python3"))

    maker = Maker(' SUFIX')
    print(maker.make_something('SOME WORD'))
    print(maker.make_something('Python'))
