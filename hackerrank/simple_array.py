n = int(input())

arr = list(map(int, input().rstrip().split()))

for idx in arr[::-1]:
    print(f'{idx} ', end="")