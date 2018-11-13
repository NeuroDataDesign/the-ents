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

    A = nx.to_numpy_matrix(G)
    n = A.shape[0]

    edges = np.count_nonzero(np.triu(A))
    num_upper = n * (n + 1) / 2

    return edges / num_upper


def main(filepath='../../data/raw/hbn/'):

    results = {}

    atlases = os.listdir(filepath)

    for atlas in atlases:

        filelist = os.listdir(filepath + atlases)

        p_i = []

        for file in filelist:
            path = filepath + atlas + file
            G = read_edgelist(path)
            try:
                p_i += [estimate_phat(G)]
            except:
                pass

        p_hat = np.mean(p_i)

        results[atlas] = p_hat

    return results
