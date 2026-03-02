import osmnx as ox
import networkx as nx

def main():
    print("Loading Abuja street network from disk...")
    G = ox.load_graphml("abuja_network.graphml")
    
    # Define two approximate coordinates in Abuja
    # Origin: Wuse Market area
    origin_point = (9.0645, 7.4566)
    
    # Destination: Nnamdi Azikiwe International Airport area
    destination_point = (9.0065, 7.2631)
    
    print(f"Finding the shortest path from {origin_point} to {destination_point}...")
    
    # Find the nearest network nodes to these coordinates
    orig_node = ox.distance.nearest_nodes(G, X=origin_point[1], Y=origin_point[0])
    dest_node = ox.distance.nearest_nodes(G, X=destination_point[1], Y=destination_point[0])
    
    # Calculate the shortest path using Dijkstra's algorithm
    route = nx.shortest_path(G, orig_node, dest_node, weight='length')
    
    # Calculate total distance
    distance_meters = nx.shortest_path_length(G, orig_node, dest_node, weight='length')
    distance_km = distance_meters / 1000
    
    print(f"Shortest path found! The route contains {len(route)} nodes.")
    print(f"Total driving distance: {distance_km:.2f} kilometers.")

if __name__ == "__main__":
    main()
