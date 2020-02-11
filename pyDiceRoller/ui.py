import sys
from utils import *
import core

def main():
    print(welcome_message)
    mod = int(input(mod_select_message))
    if mod == 0:
        score_list = core.score_roll()
        print_scores(score_list)
    elif mod == 1:
        dice = int(input(dice_select_message))
        number = int(input(dice_number_message))
        result_list = core.dice_roll(dice, number)
        print_dice(result_list)
    elif mod == 2:
        number = int(input(score_dice_number_message))
        score_list = core.score_roll_replace(number)
        print_replace_scores(score_list)
    else:
        print('WHY!?')
    
if __name__ == '__main__':
    main()

