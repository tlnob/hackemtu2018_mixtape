from graph_tool.all import *

def parseVertexInfo(stop_filename):

	stops = open(stop_filename)
	d = {}

	for line in stops:
		split = line.split(',')
	
		print(split[3])
		
		stop_id = split[0].strip('"')
		stop_id = stop_id.strip('\0\n\t')

		stop_lat = split[2]

		stop_lon = split[3]


		d[stop_id] = (stop_lat, stop_lon)

	return d

#
def parseEdgeInfo(trips_filename,stop_times_filename):

	trips_file = open(trips_filename, 'r')
	stop_times_file = open(stop_times_filename, 'r')

	shape_id_list = []
	shape_dist_list = []
	
	d = {}
	stops_list = []

	trip_id_antigo = ""
	trip_id = ""
	first = True
	for line in stop_times_file:

		if (trip_id_antigo != trip_id):
			
			if(first):
				trip_id_antigo = trip_id
				first = False

			d[trip_id_antigo] = {}
			d[trip_id_antigo]["stop_id_list"] = stops_list
			
			trip_id_antigo = trip_id
			stops_list = []

		split = line.split(',')
	
		trip_id = split[0].strip('"')
		stop_id = split[3].strip('"')
		trip_id = trip_id.strip('\0\n\t')
		stop_id = stop_id.strip('\0\n\t')
		
		stops_list.append(stop_id)

	trip_id_antigo = ""
	trip_id = ""
	first = True
	for line in trips_file:
		if (trip_id_antigo != trip_id):
			if(first):
				trip_id_antigo = trip_id
				first = False
			d[trip_id_antigo] = {}
			d[trip_id_antigo]["shape_id"] = shape_id
			trip_id_antigo = trip_id

		split = line.split(',')
	
		trip_id = split[2].strip('"')
		shape_id = split[5].strip('"')

		trip_id = trip_id.strip('\0\n\t')
		shape_id = shape_id.strip('\0\n\t')

	return d






def createVertex(vertex_id, lat, lon, g):
	v = g.add_vertex()
	
	v_id = g.new_vertex_property("string")
	v_lat = g.new_vertex_property("float")
	v_lon = g.new_vertex_property("float")

	v_id[v] = vertex_id
	v_lat[v] = lat 
	v_lon[v] = lon


def createEdge():
	pass 

# stop eh um hash contendo id, lat, lon
stop_list = []

# shape_id_list eh pre requisito para criacao de
# trip_list
e = parseEdgeInfo("./datasets/gtfs_emtu/trips.txt","./datasets/gtfs_emtu/stop_times.txt")
v = parseVertexInfo("./datasets/gtfs_emtu/stops.txt")
# trip eh um hash contendo direcao, custo,
# horario de chegada, horario de partida e distancia

