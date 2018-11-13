#!/usr/bin/env python

# graph.py
# Created by Vivek Gopalakrishnan on 2018-10-27.
# Email:
# Copyright (c) 2018. All rights reserved.

"""
Create random graphs for testing graph statistics on.
"""

import numpy as np
import networkx as nx


def RandomGraph(n, p, binary=True):
    """
    A function for simulating a random graph.
    Paramaters
    ----------
        n: int
            the number of vertices in the graph.
        P: float, bounded between [0,1]
            the probability of connection between any two nodes.
        binary: boolean
            whether to make a binary graph.
    """

    # Generate random adjacency matrix
    s = (n, n)
    A = np.zeros(s)

    for i, j in zip(np.triu_indices(n)[0], np.triu_indices(n)[1]):
        A[i, j] = np.random.binomial(1, p)

    A += A.T
    A[np.diag_indices_from(A)] /= 2

    # Convert adjacency to nx object
    G = nx.from_numpy_array(A)

    return G
