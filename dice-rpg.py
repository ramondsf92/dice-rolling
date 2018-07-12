from random import randint
from time import sleep

class Dice():
    def __init__(self, side=6):
        self.side = side
        self.result = 0
    def getResult(self):
        return self.result
    def roll(self):
        print('Rolando o dado de {} lados...'.format(self.side))
        sleep(0.5)
        self.result = randint(1,self.side)
        print('Resultado: {}'.format(self.result))

roll = input('Role o dado: ')
roll_result = 0
mod_value = 0
if 'd' in roll:
    pos = roll.find('d')
    dice_qtd = int(roll[:pos])
    if 'mod' in roll:
        mod_pos = roll.find('mod')
        dice_face = int(roll[pos+1:mod_pos])
        mod_value = int(roll[mod_pos+3:])
    else:
        dice_face = int(roll[pos+1:])
    dice = Dice(dice_face)
    for c in range(dice_qtd):
        dice.roll()
        roll_result+=dice.getResult()
    roll_final = roll_result + mod_value
    print(f'Resultado: {roll_result} + {mod_value} = {roll_final}')
