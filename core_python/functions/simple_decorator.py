def escape_unicode(f):
    def wrapper(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrapper


@escape_unicode
def my_function():
    return "Hello Look at: åß∫åß"


def check_non_negative(index):
    def validator(f):
        def wrapper(*args):
            if args[index] < 0:
                raise ValueError("We can't accepity negative numbers.")
            return f(*args)

        return wrapper
    return validator


@check_non_negative(1)
def create_list(value, size):
    return [value] * size


if __name__ == "__main__":
    print(my_function())
    print(create_list('abc', 3))

    # Get a error:
    # print(create_list('abc', -3))
