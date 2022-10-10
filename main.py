#Five Parsecs from home crew generator by Ryan Fry.

import race
import diceroll
import bgandclass


class PlayerCharacter:

    def __init__(self, classid):
        # setting some variables with default values to change later
        self.classid = classid
        self.bgid = classid

    def setRace(self, raceid):
        self.raceid = raceid

    def setBG(self, bgid):
        self.bgid=bgid

    def getBG(self):
        return self.bgid

    def getRace(self):
        return self.raceid

    def printRace(self):
        list=self.getRace()
        racestring = f"""
/////////////////////////////////////////////////////////////////  
Character ID: {self.classid+1}
Character Class: {list[0]} 
STATS Reactions: [{list[1]}],Speed: [{list[2]}"], Combat Skills: [+{list[3]}], Toughness: [{list[4]}], Savvy: [{list[5]}]
Race Info: {list[6]}
//////////////////////////////////////////////////////////////////  
"""
        print(racestring)


def Main():
    #Main loop of the program, will run on init

    partySize = 4
    party = list()
    for member in range(partySize):
        party.append(PlayerCharacter(member))
        party[member].setRace((race.randomRace(diceroll.d100Roll(1,"race"))))
        party[member].setBG(bgandclass.getbackground())

    (party[0].printRace())
    print(party[0].bgid)

    (party[1].printRace())
    print(party[1].bgid)

    (party[2].printRace())
    print(party[2].bgid)

    (party[3].printRace())
    print(party[3].bgid)




Main()