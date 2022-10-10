#Five Parsecs from home crew generator by Ryan Fry.

import race
import diceroll
import bgandclass
import sys


class PlayerCharacter:

    def __init__(self, classid):
        # setting some variables with default values to change later
        self.classid = classid
        self.bgid = classid
        self.mvid = classid

# Set and get functions for the PC class
    def setRace(self, raceid): self.raceid = raceid
    def getRace(self):return self.raceid
    def setBG(self, bgid): self.bgid=bgid
    def getBG(self): return self.bgid
    def setMotiv(self, mvid):self.mvid = mvid
    def getMotiv(self,): return self.mvid
    def setClass(self, playerclassid):self.playerclassid = playerclassid
    def getClass(self,): return self.playerclassid


    def printRace(self):
        list=self.getRace()
        racestring = f"""
/////////////////////////////////////////////////////////////////  
//  Character ID: {self.classid+1}
//  Character Class: {list[0]} 
//  STATS Reactions: [{list[1]}],Speed: [{list[2]}"], Combat Skills: [+{list[3]}], Toughness: [{list[4]}], Savvy: [{list[5]}]
//
//  Race Info: {list[6]}
//
//   Background: {self.bgid}
//   Motivation: {self.mvid}
//   Class: {self.getClass()}
//////////////////////////////////////////////////////////////////  
"""
        print(racestring)


def Main():
    # Main loop of the program, will run on init
    charnumber = int(input("How many characters do you want to generate: "))
    partySize = charnumber
    party = list()
    for member in range(partySize):
        party.append(PlayerCharacter(member))
        party[member].setRace((race.randomRace(diceroll.d100Roll(1, "race"))))
        party[member].setBG(bgandclass.getbackground())
        party[member].setMotiv(bgandclass.getMotivation())
        party[member].setClass(bgandclass.getClass())

    #this is used to display all the party members
    for member in range(partySize):
        (party[member].printRace())





Main()