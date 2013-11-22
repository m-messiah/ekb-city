# ~*~ coding: utf-8 ~*~
__author__ = 'Messiah'
from urllib import urlencode


class Finder(object):
    def __init__(self):
        self.database = self.load_database()
        self.streets = self.streets()
        self.houses = self.houses()

    @staticmethod
    def load_database():
        """Load 2Gis database"""
        try:
            from database import DATABASE
        except ImportError:
            print("[ERROR]: Can't import database")
            return []
        else:
            db = map(lambda z: (u"{}, {}".format(z[1].strip(),
                                                 z[0].strip()),
                                z[2].strip()),
                     map(lambda y: y.split(";"),
                         map(lambda x: x.decode("utf-8").lower(),
                             DATABASE)))
            return db

    def streets(self):
        """Aggregate addresses into dictionary by streets"""
        streets = dict()
        for street, house in self.database:
            if street in streets:
                streets[street].append(house)
            else:
                streets[street] = [house, ]
        return streets

    def houses(self):
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
        address = address.lower()
        if len(address.split()) > 1:
            street, house = address.split()[:2]
            houses = self.match_street(street)
            for h in houses:
                if house in h:
                    matches.append(u"{}".format(h))
        else:
            matches.extend(self.match_street(address))
            matches.extend(self.match_house(address))

        matches = filter(lambda x: len(x) > 0, matches)
        return map(lambda x:
                   u'''<a href="http://maps.yandex.ru/?{}"
                   target="_blank">{}</a>'''
                   .format(urlencode({'text': x.encode("utf-8"),
                                      'x': 15,
                                      'l': 'map'}),
                           x),
                   matches)

    def match_house(self, address):
        """Return all matches by house number"""
        matches = []
        try:
            matches.extend(map(lambda x: u"{} {}".format(x, address),
                               self.houses[address]))
        except KeyError:
            for house in self.houses:
                if address in house:
                    houses = map(lambda x: u"{} {}".format(x, house),
                                 self.houses[house])
                    matches.extend(houses)
        return matches

    def match_street(self, address):
        """Return all matches by street name"""
        matches = []
        try:
            matches.extend(self.streets[address])
        except KeyError:
            for street in self.streets:
                if address in street:
                    streets = map(lambda x: u"{} {}".format(street, x),
                                  self.streets[street])
                    matches.extend(streets)
        return matches
