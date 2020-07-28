def escape_unicode(f):
    def wrapper(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrapper


@escape_unicode
def my_function():
    return 'Hello Look at: åß∫åß'


if __name__ == "__main__":
    print(my_function())
