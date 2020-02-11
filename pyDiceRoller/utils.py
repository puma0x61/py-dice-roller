
welcome_message = 'Welcome to pyDiceRoller, a simple python script to easily \
                    roll dice and roll the ability scores for your next DnD \
                    character!'
mod_select_message = 'What do you want to do?\n[0] to roll your ability scores\
                        \n[1] to roll a dice\n[2] to re-roll one or more of your ability scores\
                        \n[3] to exit\n'
dice_select_message = 'Which die will you roll? d'
dice_number_message = 'how many dice? '
score_dice_number_message = 'how many abilities went to shit? '
farewell_message = 'Good Game!'

def print_scores(score_list):
    result = 'Your six ability scores are:'
    for score in score_list:
        total = 0
        for die in score:
            for actual_die in die:
                total = total + actual_die
        result = result + ' ' + str(total)
    print(result)

def print_replace_scores(score_list):
    result = 'Your new scores are:'
    for score in score_list:
        total = 0
        for die in score:
            for actual_die in die:
                total = total + actual_die
        result = result + ' ' + str(total)
    print(result)

def print_dice(dice_list):
        total = 0
        dice = 'The results were:'
        for die in dice_list:
            total = total + die
            dice = dice + ' ' + str(die)
        print(dice)
        print('The total is: ' + str(total))
 
