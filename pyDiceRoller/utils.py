
WELCOME_MESSAGE = 'Welcome to pyDiceRoller, a simple python script to easily' + \
        'roll dice and roll the ability scores for your next DnD character!\n' + \
        '\nThis software is pretty smart, but it won\'t save you from ' + \
        'doing stupid things.'
MOD_SELECT_MESSAGE = 'What do you want to do?\n[0] to roll your ability scores' + \
        '\n[1] to roll a dice\n[2] to re-roll one or more of your ability ' + \
        'scores\n[3] to exit\n'
DICE_SELECT_MESSAGE = 'Remember: all dice are possible, but why would you ' + \
        'need a d1?\nWhich die will you roll? d'
DICE_NUMBER_MESSAGE = 'how many dice? '
SCORE_DICE_NUMBER_MESSAGE = 'how many abilities went to shit? '
FAREWELL_MESSAGE = 'Good Game!'

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
 
