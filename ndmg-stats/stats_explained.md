# GraphStats Explained

### Consult this table for a brief explanation of the graph statistics calculated by the GraphStats class.

### Call each statistic on a GraphStats object (gs) using gs.*(), where the * is replaced by the corresponding abbreviation.

| Statistic | Abbreviation | Explanation | O(n) Complexity |
|:------:|:------:|:------:|:------:|
Avg Degree | avg_degree | Returns the average number of edges connected to each node. | O(1) |
Max Degree | max_degree | Returns the maximum number of edges connected to each node for the whole graph. | O(n) |
Avg Neighbor Degree | avg_neighbor_degree | Returns the average degree of the neighborhood of each node. | |
Max Neighbor Degree | max_neighbor_degree | Returns the max degree of the neighborhood of each node for the whole graph.| |
Avg Degree Connectivity | avg_deg_connectivity | Returns the average nearest neighbor degree of nodes with degree k.  | |
Max Degree Connectivity | max_deg_connectivity | Returns the maximum nearest neighbor degree of nodes with degree k for the whole graph. | |
Avg Clustering Coeff | avg_clust_coeff | Returns the clustering coefficient for nodes (For unweighted graphs, the clustering of a node n is the fraction of possible triangles through that node that exist. For weighted graphs, the clustering is defined as the geometric average of the subgraph edge weights). | |
Max Clust Coeff | max_clust_coeff | | |
Avg Betweenness Centrality | avg_between_cent | | |
Max Betweenness Centrality | max_between_cent | | |
Avg Closeness Centrality | avg_close_cent | | |
Max Closeness Centrality | max_close_cent | | |
Avg Eigenvalue Centrality | avg_eig_cent | | |
Max Eigenvalue Centrality | max_eig_cent | | |
Estrada Index | estrada_index | | |
Dispersion | dispersion | | |
Avg Num Cliques | avg_num_cliques | | |
Max Num Cliques | max_num_cliques | | |
Radius | radius | | |
Avg Eccentricity | avg_ecc | | |
Diameter | diameter | | |
Num Isolates | num_isolates | | |
Avg Shortest Path | avg_shortest_path | | |