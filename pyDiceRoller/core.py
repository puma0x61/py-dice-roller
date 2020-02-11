import sys
from random import randint

def score_roll(rolls = 6):
    dice = 6
    number = 4
    score_list = []
    for roll in range(0, rolls):
        score_result_tmp = []
        score_result_tmp.append(dice_roll(dice, number))
        score_result = remove_minimum(score_result_tmp)
        score_list.append(score_result)
    return score_list

def score_roll_replace(rolls):
    return score_roll(rolls)


def dice_roll(dice, number):
    result_list = []
    for i in range(0, number):
        result_list.append(randint(1, dice))
    return result_list

def remove_minimum(input_list):
    output_list = []
    for sub_list in input_list:
        minimum_index = 0
        new_sub_list = []
        for i, n in enumerate(sub_list):
            if n < sub_list[minimum_index]: minimum_index = i
        for i, n in enumerate(sub_list):
            if i == minimum_index:
                continue
            else:
                new_sub_list.append(n)
        output_list.append(new_sub_list)
    return output_list

