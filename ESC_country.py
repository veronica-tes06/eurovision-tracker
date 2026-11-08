

class CountryInputError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class Country:

    def __init__(self, name, contestant, wins, placement, parts, quals, autoqual, semifinal):
        self.__name = name
        self.__contestant = contestant
        self.__wins = wins
        self.__placement = placement
        self.__parts = parts
        self.__quals = quals
        self.__autoqual = autoqual
        self.__semifinal = semifinal

    def resetAll(self):
        self.__points = 0
        self.__played = 0
        self.__wins = 0
        self.__goals = 0

    def getContestant(self):
        return self.__contestant

    def getName(self):
        return self.__name

    def getPlacement(self):
        return self.__placement

    def getParticipations(self):
        return self.__parts

    def getQualifications(self):
        return self.__quals

    def getWins(self):
        return self.__wins

    def getAutomaticQualification(self):
        return self.__autoqual

    def getSemifinal(self):
        return self.__semifinal

    def getPercentQuals(self):
        if (self.__quals)==0:
            return 0
        else:
            return int(100 * (self.__quals / self.__parts))

    def addWin(self):
        self.__wins += 1

    def addQual(self):
        self.__quals += 1

class RatedCountry(Country):
    def __init__(self, name, contestant, points):
        Country.__init__(self, name, contestant, 0, "", 0, 0, False, 1)
        self.__points = points

    def getPoints(self):
        return self.__points

    def setPoints(self, new_points):
        self.__points = new_points