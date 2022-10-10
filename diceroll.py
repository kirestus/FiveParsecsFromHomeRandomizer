import random


def d100Roll(x, table_id):

    for i in range(x):
        result = random.randint(1, 100)
        print('you roll', result, 'out of 100 on the ', table_id, 'table...')
        return result
