import sys
from collections import defaultdict
import operator
from multiprocessing import Pool
import math
import numpy as np

with open('common_connection_200k.csv') as f:
	header = f.readline()
	# G = nx.Graph()

	connections = defaultdict(set)
	connections_inv = defaultdict(set)
	for line in f:
		record = line.strip().split(',')
		connections[int(record[0])].add(int(record[1]))
		connections_inv[int(record[1])].add(int(record[0]))

# common_counts = defaultdict(int)
common_counts = np.zeros([max(connections.keys()), max(connections.keys())])
for member in connections:
	if len(connections[member]) > 100:
		for connection in connections[member]:
			for degree_2 in connections_inv[connection]:
				if degree_2 != member:
					common_counts[member-1, degree_2-1] += 1
		print 'member %d complete' % (member)
print 'all complete'
cur_max = 0
index = None
it = np.nditer(common_counts, flags=['multi_index'])
while not it.finished:
	tmp = it[0]
	if tmp > cur_max:
		cur_max = tmp
		index = it.multi_index
	it.iternext()
print index, cur_max



# common_counts = {}
# def common_count(connections_sub):
# 	for member in connections_sub:
# 		# degree_2 = reduce(lambda x,y: x.union(y), [connections[neighbor] for neighbor in connections[member]])
# 		for member_2 in connections:
# 			if member != member_2 and (member, member_2) not in common_counts:
# 				common_count = len(connections[member].intersection(connections[member_2]))
# 				common_counts[(member,member_2)] = common_count
# 				common_counts[(member_2,member)] = common_count
# 		print 'one member completed'
# 	print 'thread complete'
# 	print max(common_counts.iteritems(), key = lambda x: common_counts[x[0]])

	

# if __name__=='__main__':

# 		# 	G.add_nodes_from(record)
# 		# 	G.add_edge(record[0], record[1])

# 		# nx.draw(G)

# 		num_workers = 8
# 		pool = Pool(processes=num_workers)
# 		nodes = [k for k,v in connections.items() if v > 100]
# 		pool.map(common_count, [nodes[x:x+int(math.floor(len(nodes)/num_workers))] for x in range(0, len(nodes), int(math.floor(len(nodes)/num_workers)))])