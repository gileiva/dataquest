import ask
#import check

nameGame = "DataQuest"
nickname = input('Your nickname: ')

score = 200
winScore = 1000
lostScore = 0
correctAnswer = 250
wrongAnswer = 150

#Show rules & call game
def rules():

    rules = f"Hi, {nickname}! Welcome to {nameGame} \nYou have {score} points to start playing. Correct answers add {correctAnswer} and wrong answers subtract {wrongAnswer}. \nYou win the game when you reach {winScore}. \nGood Luck! \n"
    print(rules)

    while True:
        try:
            startGame = int(input('Enter 1 to start > '))
        except ValueError:
            print("Please enter 1 > ")
            continue
        if startGame != 1:
            print('Please enter 1 >')
            continue
        else:
            #Call function to choice game (For futures updates with new games)
            #ask.choice_game()
            ask.run_game()
            break


def score_count(answer_score):
    global score 

    if answer_score:
        score += correctAnswer
        win_or_lost(score)
    else:
        score -= wrongAnswer
        win_or_lost(score)


def win_or_lost(score):

    if score >= winScore:
        print('You win!!\n\n')
    elif score <= 0:
        print('You lost\n\n')
    else:
        print(f"Your current score is {score} \n")
        input('Press enter to next question')
        ask.run_game()
