import csv
from datetime import date
from datetime import datetime


conditionDict = {}
conditionInd = 1
measureIDDict = {}
measureIDInd = 1
footnoteDict = {}
footnoteInd = 1
idDict = {}
idInd = 1


def getMeasureID(measureid):
	global measureIDInd, measureIDDict
	if(measureIDDict.has_key(measureid)):
		return measureIDDict[measureid]
	else:
		measureIDDict[measureid] = measureIDInd
		measureIDInd+=1
		return measureIDDict[measureid]

def getCondition(condition):
	global conditionInd, conditionDict
	if(conditionDict.has_key(condition)):
		return conditionDict[condition]
	else:
		conditionDict[condition] = conditionInd
		conditionInd+=1
		return conditionDict[condition]

def getFootnote(footnote):
	global footnoteDict, footnoteInd
	if(footnoteDict.has_key(footnote)):
		return footnoteDict[footnote]
	else:
		footnoteDict[footnote] = footnoteInd
		footnoteInd += 1
		return footnoteDict[footnote]


def getTime(date):
	date = date.split('/')
	return datetime(int(date[2]), int(date[0]), int(date[1])).toordinal()


def measureTime(date1, date2):
	date1 = date1.split('/')
	date2 = date2.split('/')
	d1 = date(int(date1[2]), int(date1[0]), int(date1[1]))
	d2 = date(int(date2[2]), int(date2[0]), int(date2[1]))
	return (d2-d1).days

def getScore(score):
	if(score == 'Not Available'):
		return 0
	else:
		return float(score)

def getFootnote(footnote):
	if not footnote == '':
		return int(footnote.lstrip().split()[0])
	else:
		return 0

def getID(id):
	global idInd, idDict
	if idDict.has_key(id):
		return idDict[id]
	else:
		idDict[id] = idInd
		idInd += 1
		return idDict[id]

def getZip(zip):
	return int(zip)

def main():
	csvfile = open('Timely_and_Effective_Care_-_Hospital.csv', 'rb')
	reader = csv.reader(csvfile, delimiter = ',')
	reader.next()
	data = []
	for row in reader:
		datarow = []
		datarow.append(getID(row[0]))
		datarow.append(getZip(row[5]))
		datarow.append(getCondition(row[8]))
		datarow.append(getMeasureID(row[9]))
		datarow.append(getFootnote(row[13]))
		datarow.append(getTime(row[14]))
		datarow.append(getTime(row[15]))
		datarow.append(measureTime(row[14], row[15]))
		data.append(datarow)

	return data

if __name__ == '__main__':
	print(main())