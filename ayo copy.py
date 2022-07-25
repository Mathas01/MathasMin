'''sdsdf'''
def main():
    '''blahblah'''
    money = int(input())
    water = int(input())
    snack1 = int(input())
    snack2 = int(input())
    snack3 = int(input())
    balance1 = money - water
    if balance1 % 3 == 0:
        snack1 = (snack1*10)
        balance1 = balance1 - snack1
    elif balance1 % 3 == 1:
        snack1 = (snack1*15)
        balance1 = balance1 - snack1
    elif balance1 % 3 == 2:
        snack1 = (snack1*20)
        balance1 = balance1 - snack1

    if balance1 % 3 == 0:
        snack2 = (snack2*12)
        balance1 = balance1 - snack2
    elif balance1 % 3 == 1:
        snack2 = (snack2*15)
        balance1 = balance1 - snack2
    elif balance1 % 3 == 2:
        snack2 = (snack2*18)
        balance1 = balance1 - snack2

    if balance1 % 3 == 0:
        snack3 = (snack3*5)
        balance1 = balance1 - snack3
    elif balance1 % 3 == 1:
        snack3 = (snack3*7)
        balance1 = balance1 - snack3
    elif balance1 % 3 == 2:
        snack3 = (snack3*9)
        balance1 = balance1 - snack3

    if balance1 <= 0:
        print("Now you have %d left." %money)
        print("You don't have enough money!")
    elif balance1 >= 0:
        print("Now you have %d left." %balance1)
        print("Here's your order!")
        print("Water %d baht" %water)
        print("Snack number 1: %d baht" %snack1)
        print("Snack number 2: %d baht" %snack2)
        print("Snack number 3: %d baht" %snack3)
main()
