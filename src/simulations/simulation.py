import numpy as np
import time
import h5py

from ..features.summary_stats import stats
from graph import random_graph


if __name__ == '__main__':

    statistics = []
    time_results = []

    for n in np.linspace(5, 100, 20):
        for p in np.linspace(0.1, 0.8, 20):

            A = random_graph(int(n), p)
            s = stats(A)

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
