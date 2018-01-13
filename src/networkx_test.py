import networkx as nx
import matplotlib.pyplot as plt

def main():
    G = nx.Graph()
    G.add_node("조준영")
    G.add_node("김영진")
    G.add_edge("조준영","김영진")

    nx.write_yaml(G, "data.yml")

    nx.draw(G)
    plt.show()

if __name__ == '__main__':
    main()
