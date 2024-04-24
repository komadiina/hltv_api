import csv
from json import dump

playernames = []

# List will appear outdated, but it's a good starting point for now.
# Credits to:
# https://github.com/DSCKGEC/CS-GO-Professionals/
with open('scraped.csv', newline='') as data:
  reader = csv.reader(data, delimiter=',')
  for row in reader:
    playernames.append(row[0])

with open('playernames.json', 'wt') as f:
  dump(playernames, f, indent=4)