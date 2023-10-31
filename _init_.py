from operaciones import add, subtraction, multiply, division, potencia

def game():
    score = 0
    while True:
        print('======== Menu ========'
              '\n1. Add'
              '\n2. Subtraction'
              '\n3. Multiplication'
              '\n4. Division'
              '\n5. Exponentiation'
              '\n0. Exit')
        option = int(input('\nChoose an option: '))
        if option == 0:
            break
        num_1 = float(input('Enter the first number: '))
        num_2 = float(input('Enter the second number: '))
        answer = float(input('Enter your answer: '))

        if option == 1:
            result = add(num_1, num_2)
        elif option == 2:
            result = subtraction(num_1, num_2)
        elif option == 3:
            result = multiply(num_1, num_2)
        elif option == 4:
            result = division(num_1, num_2)
        elif option == 5:
            result = potencia(num_1, num_2)
        else:
            print('Invalid option')
            continue

        if result == answer:
            score += 1
            print('Correct!')
        else:
            print('Incorrect')

    print('======== Game Over ========'
          f'\nYour score is {score}'
          '\nKeep going!')

game()