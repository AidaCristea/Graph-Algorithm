
class Graph:
    def __init__(self, nr_vertices, nr_edges):
        self._nr_vertices = nr_vertices
        self._nr_edges = nr_edges
        self._dIn = {}
        self._dOut = {}
        self._dCost = {}
        for i in range(nr_vertices):
            self._dIn[i] = []
            self._dOut[i] = []


    @property
    def dIn(self):
        return self._dIn

    @property
    def dOut(self):
        return self._dOut

    @property
    def dCost(self):
        return self._dCost

    @property
    def nr_vertices(self):
        return self._nr_vertices

    @nr_vertices.setter
    def nr_vertices(self, new_nrv):
        self._nr_vertices = new_nrv

    @property
    def nr_edges(self):
        return self._nr_edges

    @nr_edges.setter
    def nr_edges(self, new_nre):
        self._nr_edges = new_nre

    def get_value(self, d, pos):
        return d[pos]

    def set_value(self, d, pos, val):
        d[pos] = val

    def get_length(self, d, pos):
        return len(d[pos])

    def get_dCost_value(self, d, i, j):
        return d[(i, j)]

    def set_dCost_value(self, d, i, j, value):
        d[(i, j)] = value

    def set_din_val(self, pos, val):
        self.dIn[pos] = val

    def set_dout_val(self, pos, val):
        self.dOut[pos] = val

    def set_dcost_val(self, i, j, val):
        self.dCost[(i, j)] = val


    def add(self, file_name, vertex_x, vertex_y, cost):

        self._nr_edges += 1
        self._dIn[vertex_y].append(vertex_x)
        self.dOut[vertex_x].append(vertex_y)

        self.set_dCost_value(self._dCost, vertex_x, vertex_y, cost)
        f = open(file_name, "a")
        f.write("\n")
        f.write(str(vertex_x) + " " + str(vertex_y) + " " + str(cost))
        f.close()



