import score

#Function that checks the answer
def check_answer(lista, max_popu, answer):
    if answer == max_popu:
        answer_score = True
        print(f"Correct! \nYou added {score.correctAnswer} points. \n")

        score.score_count(answer_score)

    else:
        answer_score = False
        print(f"Incorrect. \nThe correct answer was {max_popu}. \n{score.wrongAnswer} points are substracted.")

        score.score_count(answer_score)
