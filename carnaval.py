a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    if b >= c:
        print(c) 
        print(b) 
        print(a) 
    else:
        print(b) 
        print(c) 
        print(a) 

elif b >= a and b >= c:
    if a >= c:
        print(c) 
        print(a) 
        print(b) 
    else:
        print(a) 
        print(c) 
        print(b) 

elif c >= b and c >= a:
    if b >= a:
        print(a) 
        print(b) 
        print(c) 
    else:
        print(b) 
        print(a) 
        print(c) 

else:
    print(a)
    print(b)
    print(c)

# n = 1

# while n >=0:
#     i=1
#     fat = 1
#     n = int (input ())
#     if n == -1:
#         break
#     while i <= n:
#         fat = fat * i
#         i = i + 1
#     print (fat)