from enum import Enum


class Constituency(object):

    def __init__(self, name, lastwinner,numofseats):
        self.name = name
        self.lastwinner = []
        self.numofseats = []

    def populate(self):
        population = []
        for i in range(0,1000):
            population.append(Voter(i))


class Voter(object):

    def __init__(self, id, voteGroup):
        self.id = id
        #TODO: Map the Enum to the Voter


class VoterGroup(Enum):
    capitalist = {"socialView": 0, "economicView": 0, "interventionism":0}
    communter = {"socialView": 0, "economicView": 0, "interventionism":0}
    environmentalist = {"socialView": 0, "economicView": 0, "interventionism":0}
    ethnic_minority = {"socialView": 0, "economicView": 0, "interventionism":0}
    farmer = {"socialView": 0, "economicView": 0, "interventionism":0}
    liberal = {"socialView": 0, "economicView": 0, "interventionism":0}
    middle_class = {"socialView": 0, "economicView": 0, "interventionism":0}
    motorist = {"socialView": 0, "economicView": 0, "interventionism":0}
    patriot = {"socialView": 0, "economicView": 0, "interventionism":0}
    poor = {"socialView": 0, "economicView": 0, "interventionism":0}
    religious = {"socialView": 0, "economicView": 0, "interventionism":0}
    retired = {"socialView": 0, "economicView": 0, "interventionism":0}
    self_employed = {"socialView": 0, "economicView": 0, "interventionism":0}
    socialist = {"socialView": 0, "economicView": 0, "interventionism":0}
    state_employee = {"socialView": 0, "economicView": 0, "interventionism":0}
    trade_unionist = {"socialView": 0, "economicView": 0, "interventionism":0}
    wealthy = {"socialView": 0, "economicView": 0, "interventionism":0}
    youth = {"socialView": 0, "economicView": 0, "interventionism":0}
