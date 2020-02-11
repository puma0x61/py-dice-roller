import sys
from utils import *
import core

def main():
    print(welcome_message)
    while True:
        print()
        mod = input(mod_select_message)
        if mod == '0':
            score_list = core.score_roll()
            print_scores(score_list)
        elif mod == '1':
            valid_die = False
            while not valid_die:
                try:
                    dice = int(input(dice_select_message))
                    valid_die = True
                except ValueError:
                    print('That\'s not a die')
            valid_number = False
            while not valid_number:
                try:
                    number = int(input(dice_number_message))
                    valid_number = True
                except ValueError:
                    print('Are you sure about that?')
            result_list = core.dice_roll(dice, number)
            print_dice(result_list)
        elif mod == '2':
            valid_number = False
            while not valid_number:
                try:
                    number = int(input(score_dice_number_message))
                    valid_number = True
                except ValueError:
                    print('Is that even a number!?')
            score_list = core.score_roll_replace(number)
            print_replace_scores(score_list)
        elif mod == '3':
            print(farewell_message)
            exit(0)
        else:
            print('WHY!?')
    
if __name__ == '__main__':
    main()

