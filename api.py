import glob, os, re
from jsonify import convert


data = '/home/thais/Desktop/HackatonEMTU/gtfs_emtu/'

def unquote(str):
	if str[0] == '"' and str[-1] == '"':
		return str[1:-1]
	else:
		return str

#dir = os.listdir('/home/thais/Desktop/HackatonEMTU/gtfs_emtu')
#print(dir)
arr = {}
for datafile in glob.glob(os.path.join(data, '*.txt')):
	file = open(datafile, "r")
	fileLines = file.readlines()
	first = True
	attr = []
	for lines in fileLines:
		if first:
			attr = [unquote(x) for x in lines.strip().split(',')]
			first = False
		else:
			lines = [unquote(x) for x in lines.strip().split(',')]
			for i in range(len(attr)):
				arr[attr[i]] = lines[i]

print(arr)
