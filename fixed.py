import pandas

ab = pandas.read_fwf('fixed.txt', skiprows=35, skipfooter=5)

print(ab)