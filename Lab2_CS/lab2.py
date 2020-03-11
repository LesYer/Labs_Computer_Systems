def multiple():
    num1 = list(input('Write first binary number: '))
    num2 = list(input('Write second binary number: '))

    count = 0
    q = list('0' * len(num1))
    mult = list('0' * len(num1))
    control = list(num1)
    for i in reversed(range(len(num2))):
        if num2[i] == '1':
            control = list(num1)
        else:
            control = q
        print('Add', ''.join(control))
        for j in reversed(range(len(num1))):
            if control[j] == '1':
                if mult[j] == '0' and count == 0:
                    mult[j] = '1'
                    count = 0
                elif mult[j] == '0' and count == 1:
                    mult[j] = '0'
                    count = 1
                elif mult[j] == '1' and count == 0:
                    mult[j] = '0'
                    count = 1
                elif mult[j] == '1' and count == 1:
                    mult[j] = '1'
                    count = 1
                    print('pizda')
            elif control[j] == '0':
                if mult[j] == '1' and count == 1:
                    mult[j] = '0'
                    count = 1
                elif mult[j] == '0' and count == 1:
                    mult[j] = '1'
                    count = 0
                elif mult[j] == '0' and count == 0:
                    mult[j] = '0'
                    count = 0
        print('Result after iteration', ''.join(mult))

        res = ''.join(mult)
        mult.insert(0, '0')
    if count == 1:
        mult.insert(0, '1')
        res = ''.join(mult)
    return res

def dec_to_bin(x):
    return list(str(int(bin(x)[2:])))

def divisor():
    num1 = dec_to_bin(int(input('Write first number: ')))
    num2 = dec_to_bin(int(input('Write second number: ')))
    quotier = 0
    while True:
        num1_10 = int(''.join(num1), 2)
        num2_10 = int(''.join(num2), 2)
        tab = len(num1) - len(num2)
        if len(num1) <= 64:
            num1.insert(0,'0'*(64-len(num1)))
        else:
            print('Bad format!')
        if len(num2) <= 64:
            num2.insert(0,'0'*(64-len(num2)))
        else:
            print('Bad format!')

        if (num1_10 < num2_10):
            print('Quotient: ', ''.join(dec_to_bin(quotier)))
            print('Remainder: ', ''.join(dec_to_bin(int(''.join(num1), 2))))
            break
        elif (num1_10 == num2_10):
            print('Quotient: 1')
            print('Remainder: 0')
            break
        else:
            print(' '*tab + ''.join(num1))
            print(''.join(num2))
            print('-'*70)
            quotier += 1
            num1_10 -= num2_10
            num1 = dec_to_bin(num1_10)
            num2 = dec_to_bin(num2_10)

def floating_point():
    num1 = list(input('Write first binary number: '))
    num2 = list(input('Write second binary number: '))
    s1 = num1[0]
    s2 = num2[0]
    e1 = num1[1:9]
    e2 = num2[1:9]
    end1 = num1[9:]
    end2 = num2[9:]
    e1_10 = int(''.join(e1), 2) - 127
    e2_10 = int(''.join(e2), 2) - 127
    print('s1 = ', s1)
    print('s2 = ', s2)
    print('e1 = ', ''.join(e1))
    print(e1_10)
    print('e2 = ', ''.join(e2))
    print(e2_10)
    print('end1 = ', ''.join(end1))
    print('end2 = ', ''.join(end2))
    num = e1
    if (e1_10 > e2_10):
        d = e1_10 - e2_10
        end2 = ['1'] + end2
        end2 = ['0']*(d-1) + end2
        end2 = end2[:23]
        print('-'*40)
        print('end1 = ', ''.join(end1))
        print('end2 = ', ''.join(end2))
    elif (e1_10 < e2_10):
        num = e2
        d = e2_10 - e1_10
        end1 = ['1'] + end1
        end1 = ['0']*(d-1) + end1
        end1 = end1[:23]
        print('-'*40)
        print('end1 = ', ''.join(end1))
        print('end2 = ', ''.join(end2))
    if (s1 == '0' and s2 == '0'):
        end = dec_to_bin(int(''.join(end1), 2) + int(''.join(end2), 2))
    elif (s1 == '0' and s2 == '1'):
        end = dec_to_bin(int(''.join(end1), 2) - int(''.join(end2), 2))
    elif (s1 == '1' and s2 == '1'):
        end = dec_to_bin(- int(''.join(end1), 2) - int(''.join(end2), 2))
    elif (s1 == '1' and s2 == '0'):
        end = dec_to_bin(int(''.join(end2), 2) - int(''.join(end1), 2))
    print('-'*40)
    print('end = ', ''.join(end))
    res = ''.join(list(s1)+num+end)
    print(s1, ''.join(num), ''.join(end))
    print(res)


multiple()
divisor()
floating_point()