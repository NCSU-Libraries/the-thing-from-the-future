import csv
import json, glob, os

datadir = 'src/data/'
deckdata = {}
for csvfile in glob.glob(os.path.join(datadir, '*.csv')):
	csvReader = csv.DictReader(open(csvfile))
	items = [row for row in csvReader]
	print(os.path.basename(csvfile).replace('.csv', '').split('_'))
	slugpagename = os.path.basename(csvfile).replace('.csv', '').split('_')
	pagename = slugpagename[1] if len(slugpagename) == 2 else ''
	deckdata[slugpagename[0]] = {'rows': items, 'title': pagename}

jsonFilePath = os.path.join(datadir, 'all_decks.json')
with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
	jsonf.write(json.dumps(deckdata, indent=4))
