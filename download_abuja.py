import osmnx as ox
import matplotlib.pyplot as plt

def main():
    center_point = (9.0765, 7.3986)
    dist_meters = 15000
    print(f"Downloading street network for Abuja around {center_point} with a radius of {dist_meters}m...")
    
    # Download the street network for driving
    G = ox.graph_from_point(center_point, dist=dist_meters, network_type="drive")
    
    print(f"Successfully downloaded network with {len(G.nodes)} nodes and {len(G.edges)} edges.")
    
    # Save network to disk as GraphML format
    out_file = "abuja_network.graphml"
    ox.save_graphml(G, filepath=out_file)
    print(f"Saved network data to {out_file}.")
    
    # Plot and save a rendering of the network
    fig, ax = ox.plot_graph(G, show=False, close=True, node_size=0, edge_linewidth=0.5, bgcolor="#111111", edge_color="#ffffff")
    img_file = "abuja_network.png"
    fig.savefig(img_file, dpi=300, bbox_inches='tight')
    print(f"Saved network plot to {img_file}.")

if __name__ == "__main__":
    main()
