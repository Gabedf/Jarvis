from Data import options as op
from Data import jokes as j
from Data import curiosities as c
import random as r

# OPÇÕES
def firstOptions():
    for i in range(len(op.start)):
        print(op.start[i])
    print('\n')

def talkOptions():
    for i in range(len(op.talk)):
        print(op.talk[i])

def jokesOptions():
    randomJoke = r.choice(j.jokes)
    return randomJoke

def curiositiesOptions():
    randomCuriosity = r.choice(c.curiosities)
    return randomCuriosity