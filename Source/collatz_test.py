# P56 3.11.1 Test

try:
    myNumber = int(input('input a number'))
except ValueError:
    print('please input an int number')


def collatz(number):
    if number % 2 == 0:  # 偶数
        newNumber = number // 2
    elif number % 2 == 1:  # 奇数
        newNumber = number * 3 + 1
    print(newNumber)
    return newNumber


while True:
    myNumber = collatz(myNumber)
    if myNumber == 1:
        break
