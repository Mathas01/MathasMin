'''prepro'''
def main():
    '''wewe'''
    num1 = int(input())
    num3 = ''
    sum = 0
    if num1 == 0:
        print("No Tape Measure")
    else:
        while True:
            num2 = input()
            if num3 == 'No more!':
                break
            num2 = int(num2)
            sum += num2
        if int(num2) < num1:
            print("Not Found Number")
        else:
            print("Sum of Found Number = %d" %sum)
main()
    