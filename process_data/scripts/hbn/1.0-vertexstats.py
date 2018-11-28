# 1.0-vertexstats.py
# Created by Vivek Gopalakrishnan on 2018-11-27.
# Email:
# Copyright (c) 2018. All rights reserved.

import os
import pandas as pd
import networkx as nx

from src.data.edgelist_io import read_edgelist
from src.features.vertex_statistics import Stats


# Find files
FILEPATH = '../../../data/raw/hbn/JHU/'
files = os.listdir(FILEPATH)

# Find median node size
def cutoff():
    tmp = np.array(())
    for file in files:
        G = read_edgelist(FILEPATH + file)
        try:
            tmp = np.append(tmp, nx.number_of_nodes(G))
        except:
            continue
    return np.median(tmp)

med = cutoff()

# Process graphs
data = np.array(())
for file in files:

    subject_id = file.split('_')[0].split('-')[1]
    G = read_edgelist(FILEPATH + file)

    try:
        stat = Stats(G)
    except ValueError:
        print('skip')
        continue

    main = stat.main()
    if len(main) == med*6:
        data = np.append(data, subject_id)
        data = np.append(data, main)

data = data.reshape(int(len(data)/(med*6+1)), int(med*6+1))

# Make primary df
df = pd.DataFrame.from_records(data)
df.columns = ['EID'] + list(range(int(med*6)))

# Read phenotypic
phenotypic = pd.read_csv(
        '../../../data/raw/HBN-phenotypic.csv').loc[:, ['EID', 'Sex', 'Age']]

# Make single df
df = pd.merge(phenotypic, df, how='inner', on=['EID'])
df.columns = ['id', 'sex', 'age'] + list(range(int(med*6)))
df['sex'] = df['sex'].map({'F': 1, 'M': 0})

# Save
df.to_csv('../../../data/processed/hbn_vertexstats.csv', index=False)
