import networkx as nx

def main():
    G = nx.Graph()
    G.add_node(1)
    G.add_nodes_from([2, 3])
    G.add_edge(1,2)
    e = (2, 3)
    G.add_edge(*e)

    print(G.number_of_nodes())
    print(G.number_of_edges())
    print(list(G.nodes))
    print(list(G.edges))
    print(list(G.adj[1]))
    print(G.degree[1])

if __name__ == '__main__':
    main()
