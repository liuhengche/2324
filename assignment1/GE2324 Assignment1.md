### GE2324 Assignment1
LIU Hengche 57854329



#### Q1:
- The network contains **12** vertices
- The network contains **19** edges
- The degree distribution:
	![pic](degree_distribution.png)


#### Q2:
- Degrees of nodes: [3, 4, 5, 3, 3, 4, 3, 2, 2, 3, 4, 2]
- Maximum degree (D_max): 5
- Number of nodes (N): 12
- Centralization numerator (∑(D_max - D_i)): 22
- Freeman's Degree Centralization (C_D) = 22 / (11 * 10) = **0.2**


#### Q3:
- B:
	- A -> F: 0.5, A -> E: 0.5, C -> D: 0.5, C -> E: 0.5, D -> F: 0.5 
	- From D to [G, H, I, J, K, L]: 0.5
	- From E to [G, H, I, J, K, L]: 0.5
	- The answer is (0.5 * 17) / (11 * 10 / 2) =**0.1545**
- D:
  - From A to [H, I, J, K, L]: 1
  - From B to [H, I, J, K, L]: 1
  - From C to [H, I, J, K, L]: 1
  - From D to [H, I, J, K, L]: 1
  - From E to [H, I, J, K, L]: 1
  - From F to [H, I, J, K, L]: 1
  - H -> I, H -> K, I -> K: 0.5
  - The answer is (6 * 5 + 0.5 * 3) / (11 * 10 / 2) = **0.5727**

#### Q4:
- B:

	- Shortest Distances: [1, 0, 1, 1, 1, 1, 2, 3,  3, 4, 3, 4]
	- 11/24 = **0.4583**
- D:

	- Shortest Distances: [2, 2, 1, 3, 3, 2, 0, 1, 1, 2 ,1, 2]
	- 11/20 = **0.55**

#### Q5:
- (i) Betweenness of G:

	- Change: **No change**
	- Reason: Adding an edge between F and G does not reduce the number of shortest paths passing through G. G remains a critical bridge connecting the two main subgraphs (F’s subgraph and G’s subgraph), as the new edge F-G does not bypass G for most paths between these subgraphs.

- (ii) Closeness of G:

	- Change: **Larger**
	- Reason: Closeness centrality improves when a node’s average distance to others decreases. The new edge F-G shortens G’s distance to nodes in F’s subgraph (e.g., A, B, C, D, E), reducing G’s overall average distance and increasing its closeness.
- (iii) Freeman's Centralization Value

	- Change: **Smaller**
	- Reason: Freeman’s centralization measures how unevenly centrality is distributed. Adding F-G makes the network more connected and decentralized. Nodes like B and G lose some dominance as the network becomes more balanced, lowering the centralization value.

#### Q6:
- (i) Betweenness of G:

	- Change: **Smaller**
	- Reason: Before adding the edge, the shortest path between H and I was H-G-I. After adding H-I, the shortest path becomes direct (H-I), bypassing G. This reduces the number of shortest paths passing through G, lowering its betweenness centrality.

- (ii) Closeness of G:

	- Change: **No change**
	- Reason: Closeness centrality depends on the average distance from G to all other nodes. The edge H-I does not affect G’s distance to other nodes (e.g., G to H is still 1, G to I is still 1, and other paths remain unchanged). Thus, G’s average distance remains the same, leaving its closeness centrality unchanged.

- (iii) Freeman's Centralization Value

	- Change: **Smaller**
	- Reason: Freeman’s centralization measures how unevenly centrality is distributed. Adding H-I makes the network more connected and decentralized:
G’s betweenness decreases (as explained in (i)). H and I become more connected (degree increases), reducing the dominance of nodes like B or G. This leads to a more balanced centrality distribution, lowering the overall centralization value.


#### Q7:
- Maximal Cliques:

	- Maximal Cliques: **[['K', 'L', 'J'], ['K', 'G'], ['G', 'C'], ['G', 'I'], ['G', 'H'], ['H', 'J'], ['J', 'I'], ['B', 'C', 'F'], ['B', 'C', 'A'], ['B', 'E', 'F'], ['B', 'E', 'D'], ['B', 'D', 'A']]**

- For the sub - graph {A,B,C,D,E,F}

	- A: 3, B: 5, C: 3, D: 3, E: 3, F: 3.The minimum degree is 3, so **k = 3**

- For the sub - graph {G, H, I, J, K, L}

	- G: 3, H: 2, I: 2, J: 4, K: 3, L: 2. The minimum degree is 2, so **k = 2**.

