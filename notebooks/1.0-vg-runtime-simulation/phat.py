#!/usr/bin/env python

# phat.py
# Created by Vivek Gopalakrishnan on 2018-11-13.
# Email: vgopala4@jhu.edu
# Copyright (c) 2018. All rights reserved.

import numpy as np
import networkx as nx
import os

from src.data.edgelist_io import read_edgelist


def estimate_phat(G):

    # Get matrix
    A = nx.to_numpy_matrix(G)
    n = A.shape[0]

    # Count upper triangular elements
    edges = np.count_nonzero(np.triu(A))
    num_upper = n * (n + 1) / 2

    # Estimate phat
    return n, edges / num_upper


def main(filepath='../../data/raw/hbn/'):

    # Results dictionary
    results = {}

    # List the altlases
    atlases = os.listdir(filepath)

    # Iterate through atlases
    for atlas in atlases:

        p_i = []
        filelist = os.listdir(filepath + atlas)
        print(atlas)

        # Iterate through all files in a given atlas
        for file in filelist:
            path = filepath + atlas + '/' + file
            G = read_edgelist(path)
            try:
                n, phat_i = estimate_phat(G)
                p_i += [phat_i]
            except:
                pass

        # Attach to dictionary
        p_hat = np.mean(p_i)
        results[atlas] = [n, p_hat]

    return results
