import math
import os
import glob
from pprint import pprint as pp


# List
def get_len_words(words):
    len_words = [len(word) for word in words]
    return len_words


# Set
def get_len_factorial(number):
    len_factorial = {len(str(math.factorial(idx))) for idx in range(number)}
    return len_factorial


# Dict
class ComprehensiosWithDict():
    def get_currenty_pyfiles(self):
        file_sizes = {os.path.realpath(p): os.stat(p).st_size
                      for p in glob.glob('*.py')}
        return file_sizes

    def exchange_key_value(self, dictionary):
        new_dict = {value: key for key, value in dictionary.items()}
        return new_dict


class FilterComprehensios():
    def is_prime(self, x):
        if x < 2:
            return False
        for idx in range(2, int(math.sqrt(x)) + 1):
            if x % idx == 0:
                return False
        return True

    def show_filter(self):
        _list = [number for number in range(101) if self.is_prime(number)]
        print(_list)

        prime_square_divisors = {num*num: (1, num, num*num)
                                 for num in range(20) if self.is_prime(num)}
        pp(prime_square_divisors)


def show():
    print(get_len_words('Hello Python3'.split()))
    print(get_len_factorial(20))

    dict_class = ComprehensiosWithDict()
    pp(dict_class.get_currenty_pyfiles())
    dictionary = {idx: str(idx) for idx in range(50)}
    pp(dict_class.exchange_key_value(dictionary))


if __name__ == '__main__':
    show()
