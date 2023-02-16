num = int(input("Введите число операций: "))
first = float(input("Введите число: "))
i = 0
while i != num:
    a = True
    second = float(input("Введите число: "))
    oper = int(input("Выберите операцию \n1-'+'\n2-'-'\n3-'*'\n4-'/'\n5-'**'\n6-'%'\n"))
    match oper:
        case 1: first += second
        case 2: first -= second
        case 3: first *= second
        case 4:
            if second == 0:
                print("На 0 делить нельзя!")
                a = False
            else:
                first /= second
        case 5: first ** second
        case 6: 
            if second == 0:
                print("На 0 делить нельзя!")
                a = False
            else:
                first % second
    if a:
        print(first)
        i += 1