#!/usr/bin/python

with open("database.py", "w") as f:
    f.write(u"\"\"\"2 Gis converted database of addresses\"\"\"\n")
    f.write(u"DATABASE = [\n")
    for address in open("2Gis.csv").readlines():
        f.write(u"    {},\n".format(repr(address.strip())))
    f.write(u"]\n")

