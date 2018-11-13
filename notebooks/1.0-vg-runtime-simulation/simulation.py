#!/usr/bin/env python

# graph.py
# Created by Vivek Gopalakrishnan on 2018-11-13.
# Email: vgopala4@jhu.edu
# Copyright (c) 2018. All rights reserved.

import numpy as np
import timeit
import h5py

from src.features.summary import Stats
from src.random.bernoulli import RandomGraph

def measure_runtime(n, p, n=5):

    # Initialize graph and stats class
    A = RandomGraph(int(n), p)
    s = Stats(A)

    # Dictionary for holding results
    results = {}
    results['parameters'] = (n, p)




if __name__ == '__main__':

    statistics = []
    time_results = []

    for n in np.linspace(5, 100, 20):
        for p in np.linspace(0.1, 0.8, 20):

            A = RandomGraph(int(n), p)
            s = Stats(A)

            public_method_names = [method for method in dir(s) if callable(getattr(s, method)) if not method.startswith('_')]
            public_method_names.remove('return_stats')

            tmp = [n, p]
            times = [n, p]

            print(tmp)

            for method in public_method_names:

                start= time.time()

                if method == 'khop_locality':
                    tmp += [getattr(s, method)(1)]
                elif method == 'scan_statistic':
                    tmp += [getattr(s, method)(1)]
                else:
                    tmp += [float(getattr(s, method)())]

                end= time.time()

                times += [end - start]

            statistics += [tmp]
            time_results += [times]

    with h5py.File('sim_results.h5', 'w') as hf:
        hf.create_dataset('statistics', data=statistics)
        hf.create_dataset('time_results', data=time_results)
