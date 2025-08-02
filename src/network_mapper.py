# \                     \
# \\\ NETWORK_MAPPER.PY \\\  Skanowanie sieci (nmap)
# \  \                  \  \

import nmap
import networkx as nx
import matplotlib.pyplot as plt

def scan_network(network_range):
    scanner = nmap.PortScanner()

    print(f"[i] Skanowanie sieci: {network_range}...")
    scanner.scan(hosts=network_range, arguments='-sn -PR') # -sn -PR = Ping scan z portami

    devices = []

    for host in scanner.all_hosts():
        if scanner[host].state() == 'up':
            device = {
                'ip': host,
                'mac': scanner[host]['addresses'].get('mac', 'Unknown')
            }
            devices.append(device)
    
    return devices


def print_network(devices):
    print("\n=== Wykryte urządzenia w sieci===")
    for device in devices:
        print(f"{device['ip']} ({device['mac']})")


# To zakłada, że router ma .1 lub .254 końcówkę
def identify_router(devices):
    for device in devices:
        ip = device['ip']
        if ip.endswith('.1') or ip.endswith('.254'):
            return device
        return None


def build_graph(devices):
    G = nx.Graph()

    # Sprawdź, które urządzenie to router
    router_device = identify_router(devices)
    if router_device:
        router_label = f"{router_device['ip']}\n{router_device['mac']}"
    else:
        router_label = 'Router'

    # Dodaj router jako centralny punkt
    G.add_node(router_label)


    for device in devices:
        device_label = f"{device['ip']}\n{device['mac']}"
        G.add_node(device_label)

        if device_label != router_label:
            G.add_edge(router_label, device_label) # Tylko nie łącz routera sam ze sobą

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
