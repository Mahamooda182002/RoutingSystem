import networkx as nx
import requests
import tkinter as tk
from tkinter import messagebox

# Create a graph using NetworkX and add nodes and edges
# ... (same as before)

# Update edge weights based on real-time traffic data
# ... (same as before)

# Dijkstra's shortest path algorithm
# ... (same as before)

# User Interface
class TrafficRoutingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time Traffic Routing System")

        self.source_label = tk.Label(root, text="Source:")
        self.source_label.pack()

        self.source_entry = tk.Entry(root)
        self.source_entry.pack()

        self.dest_label = tk.Label(root, text="Destination:")
        self.dest_label.pack()

        self.dest_entry = tk.Entry(root)
        self.dest_entry.pack()

        self.calculate_button = tk.Button(root, text="Calculate Route", command=self.calculate_route)
        self.calculate_button.pack()

        self.route_label = tk.Label(root, text="Optimal Route:")
        self.route_label.pack()

        self.route_text = tk.Text(root, height=5, width=30)
        self.route_text.pack()

    def calculate_route(self):
        source = self.source_entry.get()
        destination = self.dest_entry.get()

        if source and destination:
            optimal_route = shortest_path(source, destination)
            if optimal_route:
                self.route_text.delete(1.0, tk.END)
                self.route_text.insert(tk.END, " -> ".join(optimal_route))
            else:
                messagebox.showerror("Error", "No route found.")
        else:
            messagebox.showerror("Error", "Please enter both source and destination.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TrafficRoutingApp(root)
    root.mainloop()
