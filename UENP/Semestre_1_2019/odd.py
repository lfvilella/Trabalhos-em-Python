from datetime import datetime
import random
import time

odds = [ 1, 3, 5 , 7, 9, 11, 13, 15, 17,19, 
        21,23,25,27,29,31,33,35,37,39,41,43,
        45,47,49,51,53,55,57,59]

for x in range(5):
    right_this_minutes = datetime.today().minute
    
    if right_this_minutes in odds:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")

    # Random number
    random_second = random.randint(1,60)
    # Pausa e Execuçao
    time.sleep(random_second)
    print(random_second)




# for contador in range(5):
#         print(contador, "X 5 = ", contador*5)

# for num in range(8):
#         if num % 2 ==0:
#                 print(num, "é par.")
#         else:
#                 print(num, "é impar.")

# sum_ = 0
# for num in range(11):
#         sum_ += num
# print(sum_)

# string = "HELLO WORLD !"
# for char in string:
#         print(char)

# for x in range(100):
#         print(x)