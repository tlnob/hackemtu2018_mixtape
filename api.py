import glob, os, re, json



data = '/home/thais/Desktop/HackatonEMTU/gtfs_emtu/'

def unquote(str):
	if str[0] == '"' and str[-1] == '"':
		return str[1:-1]
	else:
		return str

def parse(fileLines):
	first = True
	attr = []
	arr = []
	for lines in fileLines:
		if first:
			attr = [unquote(x) for x in lines.strip().split(',')]
			first = False
		else:
			lines = [unquote(x) for x in lines.strip().split(',')]
			obj = {}
			for i in range(len(attr)):
				obj[attr[i]] = lines[i]
			arr.append(obj)
	return arr

db = {}
for datafile in glob.glob(os.path.join(data, '*.txt')):
	file = open(datafile, "r")
	fileLines = file.readlines()
	table = datafile.replace(data,'')[:-4]
	db[table] = parse(fileLines)

print(json.dumps(db, sort_keys=True, indent=4))


