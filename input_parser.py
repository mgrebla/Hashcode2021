from collections import defaultdict

class SimulationMeta:
	def __init__(self, meta_list):
		self.duration, \
		self.no_of_intersections, \
		self.no_of_streets, \
		self.no_of_cars, \
		self.car_bonus = meta_list

	def __str__(self):
		str_to_return = (
			f'self.duration: {self.duration}\n'
			f'self.no_of_intersections: {self.no_of_intersections}\n'
			f'self.no_of_streets: {self.no_of_streets}\n'
			f'self.no_of_cars: {self.no_of_cars}\n'
			f'self.car_bonus: {self.car_bonus}\n'
		)
		return str_to_return


class Street:
	def __init__(self, street_data):
		self.beginning, \
		self.end, \
		self.name, \
		self.passage_time = street_data

	def __str__(self):
		str_to_return = (
			f'self.beginning: {self.beginning}\n'
			f'self.end: {self.end}\n'
			f'self.name: {self.name}\n'
			f'self.passage_time: {self.passage_time}\n'
		)
		return str_to_return


class Car:
	def __init__(self, no_of_streets, streets_list):
		self.no_of_streets = no_of_streets
		self.streets_list = streets_list
		self.init_position = streets_list[0]
		self.position = streets_list[0]

	def __str__(self):
		str_to_return = (
			f'self.no_of_streets: {self.no_of_streets}\n'
			f'self.streets_list[0]: {self.streets_list[0]}\n'
			f'self.streets_list[-1]: {self.streets_list[-1]}\n'
			f'self.init_position: {self.init_position}\n'
			f'self.position: {self.position}\n'
		)
		return str_to_return

class Intersection:
	def __init__(self, name, incoming, outcoming):
		self.name = name
		self.incoming = incoming
		self.outcoming = outcoming

	def __str__(self):
		str_to_return = (
			f'self.name: {self.name}\n'
			f'self.incoming: {self.incoming}\n'
			f'self.outcoming: {self.outcoming}\n'
		)
		return str_to_return


class Graph:
	def __init__(self, connections, no_of_intersections, streets_list):
		self.intersections = self.init_intersections(no_of_intersections, streets_list)
		self.graph = defaultdict(set)
		self.add_connections(connections)

	def init_intersections(self, no_of_intersections, streets_list):
		intersections_dict = {}
		for i in range(no_of_intersections):
			intersections_dict[i] = {
				"name": i,
				"incoming": [],
				"outcoming": [],
			}

		self.create_intersections(intersections_dict, streets_list)

		return intersections_dict

	def create_intersections(self, intersections_dict, streets_list):
		for street in streets_list:
			intersections_dict[int(street.beginning)]["outcoming"].append(street)
			intersections_dict[int(street.end)]["incoming"].append(street)

	def add_connections(self, connections):
		""" Add connections (list of tuple pairs) to graph """

		for node1, node2 in connections:
			self.add(node1, node2)

	def add(self, node1, node2):
		""" Add connection between node1 and node2 """

		self.graph[node1].add(node2)

	def is_connected(self, node1, node2):
		""" Is node1 directly connected to node2 """

		return node1 in self.graph and node2 in self.graph[node1]



with open('hashcode.in', 'r') as file:
	items = list(file.readlines())
	simulation = SimulationMeta(items.pop(0).split())
	streets_data = items[0:int(simulation.no_of_streets)]
	cars_data = items[int(simulation.no_of_streets):]

	streets_list = []
	connections = []
	for street in streets_data:
		streets_list.append(Street(street.split()))
		connections.append((street.split()[0], street.split()[1]))

	cars_list = []
	for car in cars_data:
		no_of_streets = car.split()[0]
		streets = car.split()[1:]
		cars_list.append(Car(no_of_streets, streets))

	graph = Graph(connections, int(simulation.no_of_intersections), streets_list)


	print(simulation)
	print(graph.is_connected("0", "4"))
	print("OUTCOMING")
	for item in graph.intersections[7999]["outcoming"]:
		print(item)

	print(cars_list[0])
