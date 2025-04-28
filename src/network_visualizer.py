# \                         \
# \\\ NETWORK_VISUALIZER.PY \\\  Wizualizacja sieci (tekst/graf)
# \  \                      \  \

import networkx as nx
import matplotlib.pyplot as plt

def build_graph(devices):
    G = nx.Graph()

    # Dodaj router jako centralny punkt
    G.add_node('Router')


    for device in devices:
        device_label = f"{device[ip]}\n{device['mac']}"
        G.add_node(device_label)
        G.add_edge('Router', device_label) # Łączymy każde urządzenie z routerem

    # Rysujemy graf
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue')
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos, font_size=8)

    plt.title('Mapa sieci')
    plt.axis('off')
    plt.tight_layout()
    plt.show()