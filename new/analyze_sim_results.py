import h5py

with h5py.File('sim_results.h5') as hf:
    statistics = hf['statistics'][:]
    time_results = hf['time_results'][:]
