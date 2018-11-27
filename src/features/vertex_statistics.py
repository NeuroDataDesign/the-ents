# vertex_statistics.sh
# Created by Vivek Gopalakrishnan on 2018-11-16.
# Email:
# Copyright (c) 2018. All rights reserved.

import networkx as nx
from graspy.utils import import_graph


class Stats():

    '''
    `Stats` class handles the calculation of multiple vertex statistics.
    Individual functions can be called using the class, or the `master` function
    can be run so that all statistics are calculated.

    This class is primarily used for the generation of feature matrices. A
    population of graphs are passed in sequence to the class and a final feature
    vector is generated using the `master` function.
    '''

    def __init__(self, graph):
        if type(graph) is not nx.Graph:
            raise ValueError('Graph must be a NetworkX object.')
        else:
            self.graph = graph

    def khop_locality(self, radius):
        '''
        `k-hop locality` is the cardinality of the edge set of the induced subgraph
        within k hops of vertex u.

        Given a graph and a radius, this function returns a vector of all
        '''

        tmp = np.array(())
        for n in self.graph.nodes():
            subgraph = nx.ego_graph(self.graph, n, radius=radius)
            tmp = np.append(tmp, np.sum([subgraph.get_edge_data(e[0], e[1])['weight']
                                         for e in subgraph.edges()]))
        return tmp

    def degree(self):
        '''
        Return the degree of every node in the graph
        '''

        tmp = np.array(())
        for n in self.graph.nodes():
            tmp = np.append(tmp, nx.degree(G, n))

        return tmp

    def degree_centrality(self):
        '''
        Return the degree centrality of every node in the graph
        '''
        tmp = np.array(())
        tmp = np.append(tmp, list(nx.degree_centrality(self.graph).values()))

        return tmp

    def closeness_centrality(self):

        tmp = np.array(())
        tmp = np.append(
            tmp, list(nx.closeness_centrality(self.graph).values()))

        return tmp

    def eigenvector_centrality(self):
        '''
        Return the eigenvector centrality for every node in the graph
        '''
        tmp = np.array(())
        tmp = np.append(
            tmp, list(nx.eigenvector_centrality(self.graph).values()))

        return tmp

    def triangles(self):
        ''''
        Return the number of triangles each node in the graph is a vertex of
        '''
        tmp = np.array()
        for node in self.graph.nodes():
            tmp = np.append(tmp, nx.triangles(self.graph, node))

        return tmp
