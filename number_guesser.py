from random import randint
restart = True
print("Guess Number Between 1-50")

while restart == True:
    randomly_selected_number = randint(1,50)
    try:
        for value in range(6):
            if value-5 == 0:
                print('You lose!')
                x = input('Try Again?(y/n): ')
                if x.lower() == 'n':
                    restart = False
                    break
                else:
                    continue
            guessed_number = int(input("Insert Guessed Number: "))
            if guessed_number == randomly_selected_number:
                print('"You Win!"')
                x = input('Try Again?(y/n): ')
                if x.lower() == 'n':
                    restart = False
                    break
                break
            elif guessed_number < randomly_selected_number:
                print(f'Correct answer is bigger. [**{4-value} Chances left**]')
            elif guessed_number > randomly_selected_number:
                print(f'Correct answer is smaller.[**{4-value} Chances left**]')
            else:
                print('Something Went wrong.')
    except ValueError:
        print("You've inserted latter. Please Insert only numbers")