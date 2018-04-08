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

def primarykey(db, table, key):
	arr = db[table]
	out = {}
	for obj in arr:
		out[obj[key]] = obj
	db[table] = out

def trip_of(db, table, key):
	for trip_id in db['trips'].keys():
		trip = db["trips"][trip_id]
		obj_id = trip[key]
		obj = db[table][obj_id]
		obj.setdefault("trips", [])
		obj["trips"].append(trip_id)


db = {}
for datafile in glob.glob(os.path.join(data, '*.txt')):
	file = open(datafile, "r")
	fileLines = file.readlines()
	table = datafile.replace(data,'')[:-4]
	db[table] = parse(fileLines)
#	json.dumps(db, sort_keys=True, indent=4)

primarykey(db, "trips", "trip_id")
primarykey(db, "shapes", "shape_id")
primarykey(db, "routes", "route_id")

trip_of(db, "shapes", "shape_id")
trip_of(db, "routes", "route_id")

print(json.dumps(db['routes'], sort_keys=True, indent=4))



