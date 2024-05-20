#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print('Happy New Year!')
happy_new_year()


def square_integers(int_list):
    squired_ints = [int*int for int in int_list]
    return squired_ints


def fizzbuzz():
    i = 0
    while i < 100:
        i +=1
        if i%3 == 0 and i%5 ==0:
            print('FizzBuzz')
        elif i%3 == 0:
            print('Fizz')
        elif i%5 == 0:
            print('Buzz')
        else:
            print(i)
fizzbuzz()


for i in range(10):
    print("Looping!")
    print(f"i is: {i}")

    
player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]
player_heights = [height * 7920 for height in player_heights]
print(player_heights)