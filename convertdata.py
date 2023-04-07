import csv
import json, glob, os

datadir = 'src/data/'
deckdata = {}
for csvfile in glob.glob(os.path.join(datadir, '*.csv')):
	csvReader = csv.DictReader(open(csvfile))
	items = [row for row in csvReader]
	pageinfo = os.path.basename(csvfile).replace('.csv', '')
	deckdata[pageinfo] = items

jsonFilePath = os.path.join(datadir, 'all_decks.json')
with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
	jsonf.write(json.dumps(deckdata, indent=4))

course_info_path = os.path.join(datadir, 'course_info.json')
course_info = json.load(open(course_info_path))

for slug in deckdata.keys():
	print(course_info.keys())
	if slug not in course_info.keys():
		course_info[slug] = {"course_name": "",
    	"courses": "", "form_link": ""}

with open(course_info_path, 'w') as f:
	f.write(json.dumps(course_info, indent=4))
