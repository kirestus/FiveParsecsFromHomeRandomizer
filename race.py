import diceroll

# creates and populates an array with the stats and name of a random race depennding on as series of die rolls
# this whole thing is a mess that could have been handled better with a dictionary or spreadsheet but i dont want to redo it
def randomRace(x):
    race = [0,0,0,0,0,0,0]

    if x <= 60: race = ["Basic Human",1,4,0,3,0,"Baseline Human characters are plain, ordinary people. Distributed across thousands of worlds, cultures, and environments, their appearance, customs, and outlook on life can vary tremendously, but ultimately the baseline is Human, through and through."]
    elif x <= 80:
        # Basic alien subroll
        y = diceroll.d100Roll(1, "sub-species")
        #roll 1d100 for the subspecies
        if y <= 20: race = ['Engineer', 1, 4, 0, 2, 1, 'Slim humanoids with a fragile physique. They have an innate talent for interfacing with machinery, making them highly desirable crew companions. ']
        elif y <= 40: race = ['KErin', 1, 4, 0, 4, 0, 'Proud and warlike aliens with a penchant for brutality and a peculiar sense of honor.']
        elif y <= 55: race = ['Soulless', 1,4,0,4,1, 'A species of cybernetic organisms, connected into a combined hive-intelligence.']
        elif y <= 70: race = ['Precursor',1,5,0,2,0, 'Graceful and refined alien humanoids who were traveling the stars when other species were still lingering in caves.']
        elif y <= 90: race = ['Feral', 1,4,0,3,0, 'Humanoid-animal hybrids, typically patterned on Earth predators such as wolves or large cats. Originally engineered for military purposes, they are considered an independent species in Unified Space.']
        else : race = ["Swift",1,5,0,3,0, 'Diminutive, winged, lizard people, the species received the nickname “Swift” due to their erratic, jerky motions.']
    elif x <= 90:
        race = ["Bot",2,4,1,4,2,'Typical Bots are built to a bewildering array of configurations, but the profile given here will fit most combat, security, and multipurpose Bots. They are fitted with emotionsimulation modules, allowing fairly complex “personalities”.']
    elif x <= 100:
        # Strange Character Subroll
        y = diceroll.d100Roll(1,"strange character")
        if y <= 2: race = ['De-Converted',1,4,0,3,0]
        elif y <= 8: race = ['Unity Agent',2,4,0,3,0]
        elif y <= 17: race = ['Mysterious Past',1,4,0,3,0,"A standard human but "]
        elif y <= 22: race = ['Hakshan',1,4,0,3,0,"High-tech aliens traveling the galaxy in search of something. Fairly friendly. "]
        elif y <= 27:race = ['Stalker',1,4,0,3,0,'Blue-skinned Human gene-mods. Rarely seen, on account of their innate teleportation ability, originally the result of a secret military development project']
        elif y <= 34: race = ['Hulker', 1,4,1,5,0, 'Bulging with muscles and rage, these Human gene-mods are perfect for hauling, crushing, and breaking. Or hauling things that need to be crushed or broken.']
        elif y <= 41: race = ['Hopeful Rookie',1,4,0,3,0, 'Wide-eyed and enthusiastic, you almos tfeel bad for this kid, because the universe is going to hit them like a ton of bricks.']
        elif y <= 47: race = ['Genetic Uplift',2,5,1,4,1, 'All manner of genetic adjustments arepossible with the basic Human template. This could, of course, be used to createliteral super-humans, if you have the cash. This one had the cash.']
        elif y <= 53: race = ['Mutant',1,4,0,3,0,'Genetic distorts are common enough sightsaround the galaxy, whether it’s due to black-war weaponry, scientific experiments, cosmic disturbances, or industrial pollution.']
        elif y <= 58: race = ['Assault Bot',2,4,1,4,0, 'Like a typical work Bot, except encased in armor, and programmed with a homicidal demeanor']
        elif y <= 62: race = ['Manipulator', 2,4,0,3,1, 'Bizarre-looking aliens renowned for their talents at communication and large-scale political machinations. Occasionally, they drag their tentacled selves out into the universe alone so they can observe the creatures that inhabit it.']
        elif y <= 67: race = ['Primitive',1,4,0,3,0,'Inhabitants from a technologically regressed world sometimes find it difficult to shed their backwards ways. However, being handy with a blade has its uses.']
        elif y <= 73: race = ['Feeler',1,4,0,3,0, 'Some cultures have extremely strong emotional output.']
        elif y <= 79: race = ['Emo Suppressed',1,4,0,3,0,'Whether requested, imposed as a criminal punishment, or due to cultural customs, this character is unable to feel any emotions beyond those needed for rudimentary existence.']
        elif y <= 85: race = ['Minor Alien',1,4,0,3,0,'One of the many alien species that do not form a major political entity in the Fringe regions (see p.143).']
        elif y <= 87: race = ['Traveler', 3,4,0,4,2, 'An odd person, claiming they are not really from this moment in space and time. They certainly dress in an eccentric manner']
        elif y <= 93: race = ['Empath' ,1,4,0,3,0, 'Minor psionic inclination allowing the easy reading of emotional states. Surprisingly handy during a negotiation process.']
        else: race = ['Bio-upgrade',1,4,0,3,0,'Humans with a heightened tolerance for cybernetic enhancements are often given genetic treatments to let them take full advantage of this fact.']
    else:
        race = "fail"
    return(race)