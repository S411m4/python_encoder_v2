#Todo:
#Ans button (to save previous answer)

def sum(no1, no2):
    return float(no1) + float(no2)

def subtract(no1, no2):
    return float(no1) - float(no2)

def multiply(no1, no2):
    return float(no1) * float(no2)

def divide(num, den):
    if float(den) == 0:
        return 'error division by zero'

    else:
        return float(num) / float(den)


if __name__ == '__main__':
    print("enter no1, no2: ")
    no1 = input()
    no2 = input()

    print("sum = " + str(sum(no1, no2)))
    print("difference = " + str(subtract(no1, no2)))

    print("multiply = " + str(multiply(no1, no2)))
    print("division = " + str(divide(no1, no2)))

