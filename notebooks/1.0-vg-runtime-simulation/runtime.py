#!/usr/bin/env python

# graph.py
# Created by Vivek Gopalakrishnan on 2018-11-13.
# Email: vgopala4@jhu.edu
# Copyright (c) 2018. All rights reserved.

import timeit

from src.features.summary import Stats
from src.random.bernoulli import RandomGraph


def measure_runtime(n, p, number=5):


    """
    Calculates the runtime for a given graph.
    Does not time the functions: 'khop_locality', 'scan_statistic'
    """

    # Initialize graph and stats class
    A = RandomGraph(int(n), p)
    s = Stats(A)

    public_method_names = [method for method in dir(s) if callable(
        getattr(s, method)) if not method.startswith('_')]
    for method in ['return_stats', 'khop_locality', 'scan_statistic']:
        public_method_names.remove(method)

    # Dictionary for holding results
    results = [n, p]

    # Runtime
    for method in public_method_names:
        results += [timeit.timeit(lambda: getattr(s, method)(), number=number)]

    return results
