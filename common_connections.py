import sys
from collections import defaultdict
import operator
from multiprocessing import Pool, Manager
import math

with open('sample.csv') as f:
        header = f.readline()
        connections = defaultdict(set)
        for line in f:
                record = line.strip().split(',')
                connections[int(record[0])].add(int(record[1]))
        print('connections data completed')

# deg_2s = defaultdict(set)
# for member in connections.keys():
#         deg_2s[member] = reduce(lambda x,y: x.union(y), [connections[neighbor] for neighbor in connections[member] if neighbor != member])
# print('neighbors of neighbors found')

def common_count(connections_sub):
        common_counts = {}
        # common_counts, connections_sub = args
        cur_max = 0
        for member in connections_sub:
                for member_2 in connections:
                        if member != member_2 and (member, member_2) not in common_counts and (member_2, member) not in common_counts:
                                common = len(connections[member].intersection(connections[member_2]))
                                if common > cur_max:
                                        common_counts[(member,member_2)] = common
                                        common_counts[(member_2, member)] = common
                                        cur_max = common
                print('member %d processed') % (member)
        print max(common_counts.items(), key = lambda x: common_counts[x[0]])

if __name__=='__main__':
                num_workers = 8
                pool = Pool(processes=num_workers)
                common_counts = Manager().dict()
                nodes = connections.keys()
                pool.map(common_count, [nodes[x:x+int(math.floor(len(nodes)/num_workers))] for x in range(0, len(nodes), int(math.floor(len(nodes)/num_workers)))])
                pool.close()
                pool.join()
                