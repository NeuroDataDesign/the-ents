# graph_statistics.sh
# Created by Ganesh Arvapalli on 2018-11-02.
# Email:
# Copyright (c) 2018. All rights reserved.

"""
    Create graph statistics class that can calculate common graph statistics
    Format graph statistics as list (to be inserted into data matrix)
    (https://networkx.github.io/documentation/networkx-1.10/reference/algorithms.html)
"""

import networkx as nx
import numpy as np
from graspy.utils.ptr import pass_to_ranks


class Stats():
    """
    Takes in graph as input and computes relevant graph statistics.
    Call gs.return_stats() to get vector of features
    """

    def __init__(self, g_):
        if len(g_.nodes()) == 0:
            print("Empty graph input detected.")
        else:
            self.graph = g_
            self.num_nodes = self.graph.order()
            self.num_edges = self.graph.size()

    def avg_degree(self):
        # Average degree of nodes
        return 1.0 * self.num_edges / self.num_nodes

    def max_degree(self):
        # Maximum degree of graph
        deg_seq = [d for n, d in self.graph.degree()]
        return max(deg_seq)

    def avg_neighbor_degree(self):
        # Average neightbor degree
        andeg = nx.average_neighbor_degree(self.graph)
        if len(andeg) != 0:
            avg_andeg = sum(andeg.values()) / len(andeg)
        return avg_andeg

    # This seems a little redundant compared to max_degree
    def max_neighbor_degree(self):
        # Maximum neightbor degree
        andeg = nx.average_neighbor_degree(self.graph)
        if len(andeg) != 0:
            max_andeg = max(andeg.values())
        return max_andeg

    def avg_deg_connectivity(self):
        # Average degree connectivity
        adc = nx.average_degree_connectivity(self.graph)
        if len(adc) != 0:
            avg_adc = sum(adc.values()) / len(adc)
        return avg_adc

    def max_deg_connectivity(self):
        # Maximum degree connectivity
        adc = nx.average_degree_connectivity(self.graph)
        if len(adc) != 0:
            max_adc = max(adc.values())
        return max_adc

    def avg_clust_coeff(self):
        # Average clustering coefficient
        ccs = nx.clustering(self.graph)
        if len(ccs) != 0:
            avg_cc = sum(ccs.values()) / len(ccs)
        return avg_cc

    def max_clust_coeff(self):
        # Maximum clustering coefficient
        ccs = nx.clustering(self.graph)
        if len(ccs) != 0:
            max_cc = max(ccs.values())
        return max_cc

    def avg_between_cent(self):
        # Average Betweenness centrality
        bet_cen = nx.betweenness_centrality(self.graph)
        if len(bet_cen) != 0:
            avg_bc = sum(bet_cen.values()) / len(bet_cen)
        return avg_bc

    def max_between_cent(self):
        # Maximum Betweenness centrality
        bet_cen = nx.betweenness_centrality(self.graph)
        if len(bet_cen) != 0:
            max_bc = max(bet_cen.values())
        return max_bc

    def avg_close_cent(self):
        # Average Closeness centrality
        clo_cen = nx.closeness_centrality(self.graph)
        if len(clo_cen) != 0:
            avg_clc = sum(clo_cen.values()) / len(clo_cen)
        return avg_clc

    def max_close_cent(self):
        # Maximum Closeness centrality
        clo_cen = nx.closeness_centrality(self.graph)
        if len(clo_cen) != 0:
            max_clc = max(clo_cen.values())
        return max_clc

    def avg_eig_cent(self):
        # Average Eigenvector centrality
        if len(self.graph.nodes()) != 0:
            eig_cen = nx.eigenvector_centrality(self.graph)
            if len(eig_cen) != 0:
                avg_ec = sum(eig_cen.values()) / len(eig_cen)
        else:
            print("No nodes in graph: Eig Cen(avg)")
            avg_ec = 0
        return avg_ec

    def max_eig_cent(self):
        # Maximum Eigenvector centrality
        if len(self.graph.nodes()) != 0:
            eig_cen = nx.eigenvector_centrality(self.graph)
            if len(eig_cen) != 0:
                max_ec = max(eig_cen.values())
        else:
            print("No nodes in graph: Eig Cen(max)")
            max_ec = 0
        return max_ec

    def estrada_index(self):
        # Estrada Index
        ei = nx.estrada_index(self.graph)
        return ei

    # This one could be worth scrapping
    def dispersion(self):
        # Dispersion
        dis = nx.dispersion(self.graph)
        total = 0
        for i in dis.values():
            if len(i.values()) != 0:
                total += sum(i.values()) / len(i.values())
        return total

    def avg_num_cliques(self):
        # Average number of cliques
        nc = nx.number_of_cliques(self.graph)
        if len(nc) != 0:
            avg_nc = sum(nc.values()) / len(nc)
        return avg_nc

    def max_num_cliques(self):
        # Average number of cliques
        nc = nx.number_of_cliques(self.graph)
        if len(nc) != 0:
            max_nc = max(nc.values())
        return max_nc

    def radius(self):
        # Radius (min ecc)
        if nx.is_connected(self.graph):
            r = nx.radius(self.graph)
        else:
            r = 0
        return r

    def avg_ecc(self):
        # Average Eccentricity
        if nx.is_connected(self.graph):
            e = nx.eccentricity(self.graph)
            if len(e) != 0:
                avg_e = sum(e.values()) / len(e)
        else:
            avg_e = 0
        return avg_e

    def diameter(self):
        # Diameter (max ecc)
        if nx.is_connected(self.graph):
            d = nx.diameter(self.graph)
        else:
            d = 0
        return d

    def num_isolates(self):
        return len(list(nx.isolates(self.graph)))

    def avg_shortest_path(self):
        # Shortest path length:
        if nx.is_connected(self.graph):
            avg_spl = nx.average_shortest_path_length(self.graph)
        else:
            avg_spl = 0
        return avg_spl

    # rad = radius of scan statistic neighborhood
    def scan_statistic(self, rad):
        tmp = np.array(())
        for n in self.graph.nodes():
            sg = nx.ego_graph(self.graph, n, radius=rad)
            tmp = np.append(tmp, np.sum([sg.get_edge_data(e[0], e[1])['weight']
                                         for e in sg.edges()]))
        return np.max(tmp)

    # 1-hop and 2-hop scan statistics
    def khop_locality(self, k, binary=True):

        # PTR graph
        if not binary:
            ptr_G = pass_to_ranks(self.graph, method='zero-boost')
            G = nx.from_numpy_array(ptr_G)
        else:
            G = self.graph
        tmp = []

        for node in G.nodes:

            k_hop = list(nx.single_source_shortest_path_length(
                G, node, cutoff=k).keys())
            induced = nx.get_edge_attributes(G.subgraph(k_hop), 'weight')
            tmp += [sum(induced.values())]

        if len(tmp) == self.num_nodes:
            return max(tmp)

    def main(self):
        stats = [self.avg_degree(),
                 self.max_degree(),
                 self.avg_neighbor_degree(),
                 self.max_neighbor_degree(),
                 self.avg_deg_connectivity(),
                 self.max_deg_connectivity(),
                 self.avg_clust_coeff(),
                 self.max_clust_coeff(),
                 self.avg_between_cent(),
                 self.max_between_cent(),
                 self.avg_close_cent(),
                 self.max_close_cent(),
                 self.avg_eig_cent(),
                 self.max_eig_cent(),
                 self.estrada_index(),
                 self.dispersion(),
                 self.avg_num_cliques(),
                 self.max_num_cliques(),
                 self.radius(),
                 self.avg_ecc(),
                 self.diameter(),
                 self.num_isolates(),
                 self.avg_shortest_path(),
                 self.khop_locality(1),
                 self.khop_locality(2)]

        stats = [float(i) for i in stats]

        return np.array(stats)

    # Extra stats that didn't get implemented cause they seemed to cause issues
    # Communicability
    #   t = time.time()
    #   cmb = nx.communicability(g)
    #   total = 0
    #   for i in cmb.values():
    #     if len(i.values()) != 0:
    #       total += sum(i.values())/len(i.values())
    #   print("Communicability:", total, "took", round(time.time() - t, 3), "seconds")

    # Chordality
    #   if len(list(g.nodes_with_selfloops())) == 0:
    #     if nx.is_chordal(g):
    #       chordal = 1
    #   else:
    #     chordal = 0

    # Closeness vitality
    #   cv = nx.closeness_vitality(g)
    #   if len(cv) != 0:
    #     avg_cv = sum(cv.values())/len(cv)
