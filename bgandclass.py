import diceroll
import pandas as pd

bgdata = 'bgTable.csv'
bgdf = pd.read_csv(bgdata)


def getbackground():

    roll = diceroll.d100Roll(1, "background")
    shortlist = (bgdf.loc[bgdf['Roll'] <= roll])
    # show only the closest item to our search
    background = (shortlist.iloc[-1, 1])
    return background


def randomclass():
    return()


