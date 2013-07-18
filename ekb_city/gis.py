# ~*~ coding: utf-8 ~*~
__author__ = 'Messiah'


class Finder(object):
    def __init__(self):
        self.database = self.DB()
        self.streets = self.Streets()
        self.houses = self.Houses()

    def DB(self):
        """Load 2Gis.csv file"""
        database = []
        try:
            database = open("2Gis.csv").readlines()
            database = map(lambda z: (u"{}, {}".format(z[1].strip(),
                                                       z[0].strip()),
                                      z[2].strip()),
                           map(lambda y: y.split(";"),
                           map(lambda x: x.decode("utf-8"), database)))
        except IOError:
            print("[ERROR]: File 2Gis.csv not found")
        return database

    def Streets(self):
        """Aggregate addresses into dictionary by streets"""
        streets = dict()
        for street, house in self.database:
            if street in streets:
                streets[street].append(house)
            else:
                streets[street] = [house, ]
        return streets

    def Houses(self):
        """Aggregate addresses into dictionary by houses"""
        houses = dict()
        for street, house in self.database:
            if house in houses:
                houses[house].append(street)
            else:
                houses[house] = [street, ]
        return houses

    def match(self, address):
        matches = []
        try:
            matches.extend(self.matchStreet(address))
        except:
            pass

        try:
            matches.extend(self.matchHouse(address))
        except:
            pass

        return filter(lambda x: len(x) > 0, matches)

    def matchHouse(self, address):
        """Return all matches by house number"""
        matches = []
        try:
            matches.extend(self.houses[address])
        except KeyError:
            for house in self.houses:
                if address in house:
                    matches.extend(self.houses[house])
        return matches

    def matchStreet(self, address):
        """Return all matches by street name"""
        matches = []
        try:
            matches.extend(self.streets[address])
        except KeyError:
            for street in self.streets:
                if address in street:
                    matches.extend(self.streets[street])
        return matches

    #TODO: What if Street and House are known together?