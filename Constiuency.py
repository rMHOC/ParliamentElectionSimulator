from enum import Enum
import Voter

class Constituency(object):

    def __init__(self, name, lastwinner,numofseats):
        self.name = name
        self.lastwinner = []
        self.numofseats = []

    def populate(self):
        population = []
        for i in range(0,1000):
            population.append(Voter(i))


class VoterPop(object):

    def __init__(self, id, voteGroup):
        self.id = id
        #TODO: Map the Enum to the Voter


