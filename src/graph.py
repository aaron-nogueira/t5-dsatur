import sys
from bag import Bag
class Graph:
    def __init__(self, arg):
        print("DEBUG -> tipo recebido:", type(arg))
        if isinstance(arg, int):
            if arg < 0: raise ValueError("Number of vertices must be non-negative")
            self._V = arg
            self._E = 0
            self._adj = [Bag() for _ in range(self._V)]
        
        elif isinstance(arg, Graph):
            self._V = arg.V()
            self._E = arg.E()
            self._adj = [Bag() for _ in range(self._V)]
            for v in range(arg.V()):
                reverse = []
                for w in arg.adj(v):
                    reverse.append(w)
                for w in reversed(reverse):
                    self._adj[v].add(w)
        
        else:
            try:
                with open(arg, 'r') as f:
                    content = f.read().split()
                if not content: raise ValueError("Empty input")
                
                self._V = int(content[0])
                if self._V < 0: raise ValueError("Number of vertices must be non-negative")
                
                self._adj = [Bag() for _ in range(self._V)]
                self._E = 0
                
                num_edges = int(content[1])
                if num_edges < 0: raise ValueError("Number of edges must be non-negative")
                
                idx = 2
                for _ in range(num_edges):
                    v = int(content[idx])
                    w = int(content[idx+1])
                    self.add_edge(v, w)
                    idx += 2
            except (IndexError, ValueError) as e:
                raise ValueError("Invalid input format") from e

    def V(self):
        return self._V

    def E(self):
        return self._E

    def _validate_vertex(self, v):
        if v < 0 or v >= self._V:
            raise ValueError(f"vertex {v} is not between 0 and {self._V-1}")

    def add_edge(self, v, w):
        self._validate_vertex(v)
        self._validate_vertex(w)
        self._E += 1
        self._adj[v].add(w)
        self._adj[w].add(v)

    def adj(self, v):
        self._validate_vertex(v)
        return self._adj[v]

    def degree(self, v):
        self._validate_vertex(v)
        return self._adj[v].size()

    def __str__(self):
        s = [f"{self._V} vertices, {self._E} arestas"]
        for v in range(self._V):
            line = [f"{v}:"]
            for w in self._adj[v]:
                line.append(str(w))
            s.append(" ".join(line))
        return "\n".join(s)

    def to_dot(self):
        s = ["graph {", "node[shape=circle, style=filled, fixedsize=true, width=0.3, fontsize=\"10pt\"]"]
        self_loops = 0
        for v in range(self._V):
            for w in self._adj[v]:
                if v < w:
                    s.append(f"{v} -- {w}")
                elif v == w:
                    if self_loops % 2 == 0:
                        s.append(f"{v} -- {w}")
                    self_loops += 1
        s.append("}")
        return "\n".join(s)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        graph = Graph(sys.argv[1])
        print(graph)