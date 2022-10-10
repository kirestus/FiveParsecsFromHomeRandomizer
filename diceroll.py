import random


def d100Roll(x, table_id):
    for i in range(x):
        result = random.randint(1, 100)
        print('you roll', result, 'out of 100 on the ', table_id, 'table...')
        return result


def d10Roll(x, table_id):
    for i in range(x):
        result = random.randint(1, 10)
        print('you roll', result, 'out of 10 on the ', table_id, 'table...')
        return result
