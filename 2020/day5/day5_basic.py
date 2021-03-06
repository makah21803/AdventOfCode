import os
import re

dirname = os.path.dirname(__file__)
file = open(dirname+"/input_data.txt", "r")

list = file.readlines()

class main():

    ROWS = [i for i in range(128)]
    COLS = [i for i in range(8)]

    def __init__(self, list):
        all_ids = []
        for line in list:
            row_list = self.ROWS
            col_list = self.COLS
            for letter in line:
                if letter in ('F', 'B'):
                    row_list = self.halving_list(letter, row_list)
                elif letter in ('L', 'R'):
                    col_list = self.halving_list(letter, col_list)
                elif letter in ('', '\n'):
                    continue
                else:
                    print('Wrong input: {}'.format(letter))
            row = row_list[0]
            col = col_list[0]
            id = row*8 + col
            print('{}: row {}, column {}, seat ID {}.'.format(line, row, col, id))

            all_ids.append(id)

        maximum = max(all_ids)
        print('Finished: the highest id is {}'.format(maximum))

    def halving_list(self, letter, list):
        middle = len(list)/2
        if letter in ('F', 'L'):
            return [n for i, n in enumerate(list) if i < middle]
        else:
            return [n for i, n in enumerate(list) if i >= middle]


main(list)
