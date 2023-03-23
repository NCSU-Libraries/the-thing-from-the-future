import csv
import json, glob, os

datadir = 'src/data/'
deckdata = {}
for csvfile in glob.glob(os.path.join(datadir, '*.csv')):
	csvReader = csv.DictReader(open(csvfile))
	items = [row for row in csvReader]
	deckdata[os.path.basename(csvfile).replace('.csv', '')] = items

jsonFilePath = os.path.join(datadir, 'all_decks.json')
with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
	jsonf.write(json.dumps(deckdata, indent=4))
