class GraphColoringDSatur:
    def __init__(self, graph):
        if graph is None:
            raise ValueError("graph nao pode ser nulo")
        self._graph = graph
        self._colors = [-1] * graph.V()
        self._coloring_order = []
        self._saturation_degrees = [0] * graph.V()

    def get_graph(self):
        return self._graph

    def color(self):
        self._colors = [-1] * self._graph.V()
        self._coloring_order = []
        self._saturation_degrees = [0] * self._graph.V()
        
        uncolored = list(range(self._graph.V()))

        while uncolored:
            u = self._select_next_vertex(uncolored)
            uncolored.remove(u)
            
            neighbor_colors = {self._colors[v] for v in self._graph.adj(u) if self._colors[v] != -1}
            
            clr = 0
            while clr in neighbor_colors:
                clr += 1
            
            self._colors[u] = clr
            self._coloring_order.append(u)
            self._update_saturation(u)

    def _select_next_vertex(self, uncolored):
        best_v = uncolored[0]
        max_sat = -1
        max_deg = -1

        for v in uncolored:
            sat = self._saturation_degrees[v]
            deg = self._graph.degree(v)
            
            if sat > max_sat:
                max_sat = sat
                max_deg = deg
                best_v = v
            elif sat == max_sat:
                if deg > max_deg:
                    max_deg = deg
                    best_v = v
        return best_v

    def _update_saturation(self, u):
        for v in self._graph.adj(u):
            if self._colors[v] == -1:
                distinct_colors = {self._colors[n] for n in self._graph.adj(v) if self._colors[n] != -1}
                self._saturation_degrees[v] = len(distinct_colors)

    def get_color(self, vertex):
        return self._colors[vertex]

    def get_color_count(self):
        if not self._colors or max(self._colors) == -1:
            return 0
        return max(self._colors) + 1

    def get_coloring_order(self):
        return self._coloring_order

    def is_valid_coloring(self):
        for v in range(self._graph.V()):
            if self._colors[v] == -1:
                return False
            for w in self._graph.adj(v):
                if self._colors[v] == self._colors[w]:
                    return False
        return True

    def get_label(self, vertex):
        return f"V{vertex}(C:{self._colors[vertex]})"