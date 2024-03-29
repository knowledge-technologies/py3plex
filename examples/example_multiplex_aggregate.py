# aggregate a multiplex network

import networkx as nx
from py3plex.core import random_generators

# initiate an instance of a random graph
ER_multilayer = random_generators.random_multiplex_ER(500,
                                                      8,
                                                      0.0005,
                                                      directed=False)
ER_multilayer.basic_stats()


separate_layers = []
layers_to_be_extracted = [1,2,3,4]
for separate_layer in layers_to_be_extracted:
    subnetwork_layer = ER_multilayer.subnetwork(input_list=[separate_layer], subset_by="layers")
    separate_layers.append(subnetwork_layer)
print("Extracted:", len(separate_layers), "separate layers")    

# simple networkx object
aggregated_network1 = ER_multilayer.aggregate_edges(metric="count",
                                                    normalize_by="degree")
print(nx.info(aggregated_network1))

# unnormalized counts for edge weights
aggregated_network2 = ER_multilayer.aggregate_edges(metric="count",
                                                    normalize_by="raw")
print(nx.info(aggregated_network2))

# The two networks have the same number of links (all)
# However, the weights differ!
for e in aggregated_network2.edges(data=True):
    print(e)

for e in aggregated_network1.edges(data=True):
    print(e)
