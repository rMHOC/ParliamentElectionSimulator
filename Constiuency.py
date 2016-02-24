


class Constituency(object):

    def __init__(self, name, lastwinner,numofseats):
        self.name = name
        self.lastwinner = lastwinner
        self.numofseats = numofseats

    def populate(self):
        population = []
        for i in range(0,1000):
            population.append(Voter(i))


class Voter(object):

    def __init__(self, id):
        self.id = id


