import sys
from utils import *
import core

def main():
    print(WELCOME_MESSAGE)
    try:
        while True:
            print()
            mod = input(MOD_SELECT_MESSAGE)
            if mod == '0':
                score_list = core.score_roll()
                print_scores(score_list)
            elif mod == '1':
                valid_die = False
                while not valid_die:
                    try:
                        dice = int(input(DICE_SELECT_MESAGE))
                        valid_die = True
                    except ValueError:
                        print('That\'s not a die')
                valid_number = False
                while not valid_number:
                    try:
                        number = int(input(DICE_NUMBER_MESSAGE))
                        valid_number = True
                    except ValueError:
                        print('Are you sure about that?')
                result_list = core.dice_roll(dice, number)
                print_dice(result_list)
            elif mod == '2':
                valid_number = False
                while not valid_number:
                    try:
                        number = int(input(SCORE_DICE_NUMBER_MESSAGE))
                        valid_number = True
                    except ValueError:
                        print('Is that even a number!?')
                score_list = core.score_roll_replace(number)
                print_replace_scores(score_list)
            elif mod == '3':
                print(FAREWELL_MESSAGE)
                exit(0)
            else:
                print('WHY!?')
    except (KeyboardInterrupt, EOFError):
        print()
        exit(0)
    
if __name__ == '__main__':
    main()

