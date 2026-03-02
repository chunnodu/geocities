import osmnx as ox
import matplotlib.pyplot as plt

def main():
    center_point = (9.0765, 7.3986)
    dist_meters = 30000
    print(f"Downloading street network for Abuja around {center_point} with a radius of {dist_meters}m...")
    
    # Download the street network for driving
    G = ox.graph_from_point(center_point, dist=dist_meters, network_type="drive")
    
    print(f"Successfully downloaded network with {len(G.nodes)} nodes and {len(G.edges)} edges.")
    
    # Save network to disk as GraphML format
    out_file = "abuja_network.graphml"
    ox.save_graphml(G, filepath=out_file)
    print(f"Saved network data to {out_file}.")
    
    # Export for QGIS (GeoPackage)
    pkg_file = "abuja_network.gpkg"
    ox.save_graph_geopackage(G, filepath=pkg_file)
    print(f"Saved GeoPackage for QGIS to {pkg_file}.")
    
    # Export for Kepler.gl (GeoJSON)
    nodes, edges = ox.graph_to_gdfs(G)
    nodes.to_file("abuja_nodes.geojson", driver="GeoJSON")
    edges.to_file("abuja_edges.geojson", driver="GeoJSON")
    print("Saved GeoJSON files for Kepler.gl.")
    
    # Plot and save a rendering of the network
    fig, ax = ox.plot_graph(G, show=False, close=True, node_size=0, edge_linewidth=0.5, bgcolor="#111111", edge_color="#ffffff")
    img_file = "abuja_network.png"
    fig.savefig(img_file, dpi=300, bbox_inches='tight')
    print(f"Saved network plot to {img_file}.")

if __name__ == "__main__":
    main()
