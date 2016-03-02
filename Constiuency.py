from enum import Enum


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


class VoterGroup(Enum):
    capitalist = []
    communter = []
    environmentalist = []
    ethnic_minority = []
    farmer = []
    liberal = []
    middle_class = []
    motorist = []
    patriot = []
    poor = []
    religious = []
    retired = []
    self_employed = []
    socialist = []
    state_employee = []
    trade_unionist = []
    wealthy = []
    youth = []
