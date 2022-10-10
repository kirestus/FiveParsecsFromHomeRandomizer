import diceroll
import pandas as pd

bgdata = 'bgTable.csv'
bgdf = pd.read_csv(bgdata)

mvdata = 'motivationTable.csv'
mvdf = pd.read_csv(mvdata)


def getbackground():

    roll = diceroll.d100Roll(1, "background")
    shortlist = (bgdf.loc[bgdf['Roll'] <= roll])
    # show only the closest item to our search
    background = (shortlist.iloc[-1, 1])
    return background


def getMotivation():

    roll = diceroll.d100Roll(1, "motivation")
    shortlist = (mvdf.loc[mvdf['ROLL'] <= roll])
    # show only the closest item to our search
    motivation = (shortlist.iloc[-1, 1])
    return motivation




