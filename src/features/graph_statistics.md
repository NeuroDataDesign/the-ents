# summary_stats.py Explained

### Consult this table for a brief explanation of the graph statistics calculated by the GraphStats class.

### Call each statistic on a GraphStats object (gs) using gs.*(), where the * is replaced by the corresponding abbreviation.

| Statistic | Abbreviation | Explanation | O(n) Complexity |
|:------:|:------:|:------:|:------:|
Avg Degree | avg_degree | Returns the average number of edges connected to each node. | O(n) |
Max Degree | max_degree | Returns the maximum number of edges connected to each node for the whole graph. | O(n) |
Avg Neighbor Degree | avg_neighbor_degree | Returns the average degree of the neighborhood of each node. | O(n) |
Max Neighbor Degree | max_neighbor_degree | Returns the max degree of the neighborhood of each node for the whole graph.| O(n) |
Avg Degree Connectivity | avg_deg_connectivity | Returns the average nearest neighbor degree of nodes with degree k.  | O(n<sup>2</sup>) |
Max Degree Connectivity | max_deg_connectivity | Returns the maximum nearest neighbor degree of nodes with degree k for the whole graph. | O(n<sup>2</sup>) |
Avg Clustering Coeff | avg_clust_coeff | Returns the clustering coefficient for nodes (For unweighted graphs, the clustering of a node n is the fraction of possible triangles through that node that exist. For weighted graphs, the clustering is defined as the geometric average of the subgraph edge weights). | [O(n<sup>2</sup>), O(n<sup>3</sup>)] |
Max Clust Coeff | max_clust_coeff | Returns the max clustering coefficient for nodes across the whole graph (For unweighted graphs, the clustering of a node n is the fraction of possible triangles through that node that exist. For weighted graphs, the clustering is defined as the geometric average of the subgraph edge weights). | [O(n<sup>2</sup>), O(n<sup>3</sup>)] |
Avg Betweenness Centrality | avg_between_cent | Returns the average sum of the fraction of all-pairs shortest paths that pass through for each node | [O(n<sup>2</sup>), O(n<sup>3</sup>)] |
Max Betweenness Centrality | max_between_cent | Returns the largest sum of the fraction of all-pairs shortest paths that pass through for each node | [O(n<sup>2</sup>), O(n<sup>3</sup>)] |
Avg Closeness Centrality | avg_close_cent | Returns the average reciprocal of the sum of the shortest path distances from a node to each other nodes. | O(n<sup>3</sup>) |
Max Closeness Centrality | max_close_cent | Returns the maximum reciprocal of the sum of the shortest path distances from a node to each other nodes. | O(n<sup>3</sup>) |
Avg Eigenvector Centrality | avg_eig_cent | Returns the average measure of influence each node has over the whole graph based on centrality caluclated using the eigenvectors of the graph's adjacency matrix. | O(n<sup>3</sup>) |
Max Eigenvector Centrality | max_eig_cent | Returns the maximum measure of influence each node has over the whole graph based on centrality caluclated using the eigenvectors of the graph's adjacency matrix. | O(n<sup>3</sup>) |
Estrada Index | estrada_index | Originally used to measure protein folding, this returns the sum of the subgraph centralities for all nodes, measuring "compactness" | O(n<sup>3</sup>) |
Dispersion | dispersion | Returns the total "dispersion score" across any two nodes in the graph. | O(n<sup>2</sup>) |
Avg Num Cliques | avg_num_cliques | Returns the average number of maximal cliques for each node. | O(3<sup>n/3</sup>) |
Max Num Cliques | max_num_cliques | Returns the largest number of maximal cliques for each node. | O(3<sup>n/3</sup>)  |
Radius | radius | Returns the minimum eccentricity (smallest maximum distance between any two nodes) of the graph. | O(n<sup>2</sup>) |
Avg Eccentricity | avg_ecc | Returns the average eccentricity for each node (maximum distance to any other node) for the whole graph. | O(n<sup>2</sup>) |
Diameter | diameter | Returns the maximum eccentricity (largest maximum distance between any two nodes) of the graph. | O(n<sup>2</sup>) |
Num Isolates | num_isolates | Returns the number of nodes in the graph without any neighbors. | O(n) |
Avg Shortest Path | avg_shortest_path | Returns the average shortest path length between all nodes of the graph. | O(n<sup>3</sup>) |
