n = int(input('Hello User, enter your desired fibbo number: '))

if n <=2:
    print('Enter a number from 3')
else:
    a = 0
    b = 1

    print(a)
    print(b)
    for i in range(2, n):

        c = a+b
        a = b
        b = c
        print(c)

