import Voter


class Constituency(object):

    def __init__(self, name, lastwinner,numofseats):
        self.name = name
        self.lastwinner = lastwinner
        self.numofseats = numofseats

    def populate(self):
        population = []