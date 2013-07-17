# ~*~ coding: utf-8 ~*~
__author__ = 'Messiah'


class Finder(object):
    def __init__(self):
        self.database = self.DB()
        self.streets = self.Streets()
        self.houses = self.Houses()

    def DB(self):
        """Load 2Gis.csv file"""
        pass

    def Streets(self):
        """Aggregate addresses into dictionary by streets"""
        streets = dict()
        return streets

    def Houses(self):
        """Aggregate addresses into dictionary by houses"""
        houses = dict()
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

    def matchHouse(self):
        """Return all matches by house number"""
        matches = []
        return matches

    def matchStreet(self):
        """Return all matches by street name"""
        matches = []
        return matches


    #TODO: What if Street and House are known together?