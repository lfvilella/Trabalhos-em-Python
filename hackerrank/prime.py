import math

def check_prime(number):
    if number == 2:
        return True
    if number < 2:
        return False
    if number % 2 == 0:
        return False
    stop = math.sqrt(number)
    i = 3
    while i <= stop:
        if number % i == 0:
            return False
        i += 2
    return True


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        num = int(input())
        if check_prime(num):
            print('Prime')

        else:
            print('Not prime')
