import data_info as data
import check

'''
#Show differents games in futures updates. 
def choice_game():
    #v1: list of games to choice
    while True:
      try:
          choice = int(input('Choice the game: '))
      except ValueError:
          print("Enter number")
          continue
      if choice != 1:
          print('Choice game')
          continue
      else:
          run_game()
          break
'''

#Start game
def run_game():
    #Call question function
    ask_questions()


#Create questions
def ask_questions():
    #v1 - Future updates: more questions
    print('Which of these countries has the largest population?')
    list_options = data.select_data()
    #print(list_options)
    max_pop = data.evaluate(list_options)
    #print(max_pop)

    #Extract keys to show options to player
    countrieslist = list(list_options.keys())
    #Show options to player
    for i in countrieslist:
        print(f"{countrieslist.index(i)+ 1} - {i}")

    #Save player selection
    user_select = countrieslist[(int(input('> '))) -1 ]
    
    #Call function that check answer
    check.check_answer(list_options, max_pop, user_select)
    




