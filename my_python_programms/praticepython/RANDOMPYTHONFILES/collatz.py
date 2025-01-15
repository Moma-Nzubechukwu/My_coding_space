


def collatz(number):
    if number % 2 == 0:
        result = number // 2
        print(result)
    elif number % 2 != 0:
        result = 3 * number + 1
    return result
try:
    num = int(input("enter a number "))

    while num != 1:
        num = collatz(num)
    print(num)
except ValueError:
    print("not an intger")
