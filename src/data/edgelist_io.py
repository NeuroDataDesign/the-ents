# edgelist_io.py
# Created by Vivek Gopalakrishnan on 2018-11-13.
# Email: vgopala4@jhu.edu
# Copyright (c) 2018. All rights reserved.

import networkx as nx


def read_edgelist(filepath):

    with open(filepath)as f:

        edges = []

        for line in f:

            line = line.split(' ')
            line[2] = line[2][:-1]
            edges += [tuple(int(round(float(x))) for x in line)]

        if edges == []:
            return
        else:
            G = nx.Graph()
            G.add_weighted_edges_from(edges)

    return G
