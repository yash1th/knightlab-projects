'''This module simulates a rolling dice between two given numbers'''
import sys
import random


def rolling_dice(min,max):
    '''returns a number on a rolling dice between a minimum and maximum

    Args:
        minimum, maximum
    Returns:
        random number on a dice between minimum and maximum
    '''
    return random.randint(int(min),int(max))

if __name__ == '__main__':
    a = rolling_dice(min=sys.argv[1],max=sys.argv[2])
    print(a)
