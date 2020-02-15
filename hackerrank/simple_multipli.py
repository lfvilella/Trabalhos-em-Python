def multiplication_table(number):
    for idx in range(1,11,1):
        print(f'{number} x {idx} = {number*idx}')

if __name__ == '__main__':
    num = 0
    while num < 2 or num > 20:
        num = int(input())
    
    multiplication_table(num)