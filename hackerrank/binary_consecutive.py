if __name__ == '__main__':
    n = int(input())

    binary = list(bin(n)[2::])
    cnt, consecutive = 0, 0
    for num in binary:
        if num == '1':
            cnt += 1
        else:
            cnt = 0

        consecutive = max(consecutive, cnt)

    print(consecutive)