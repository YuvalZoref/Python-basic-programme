extra = '啊'

answer = input('Enter a word: ')

while len(answer) > 0 and answer.isalpha():
    word = answer.lower()
    first_letter = word[0]
    new_word = word + first_letter + extra
    final_word = new_word[1:len(new_word)]
    print(final_word)
    answer = input('Enter another word or press the enter button to exit: \n')
else:
    print('Welcome to the next question! \n')

    num_answer1 = int(input("Enter any number you like: \n"))
    num_answer2 = int(input("Enter another number: \n"))
    calculate = input('What would you like to do? Please enter one of the following:  +  -  *  %  : ')

while calculate != '':
    if calculate == '*':
        print(num_answer1 * num_answer2)
    elif calculate == '+':
        print(num_answer1 + num_answer2)
    elif calculate == '%':
        print(num_answer1 % num_answer2)
    elif calculate == '-':
        print(num_answer1 - num_answer2)
    calculate = input('Thanks for playing my boring game, press the enter button to exit! \n')
else:
    print('See you later!')
