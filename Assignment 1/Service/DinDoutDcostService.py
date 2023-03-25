import queue

from Domain.GraphDom import Graph
import random
import copy

class Services:
    def __init__(self):
        self._graph = Graph(0, 0)

    def read_file(self, file_name):
        """
        Reads the graph from the file
        :param file_name:
        :return:
        """
        try:
            f = open(file_name, "r")
            line = f.readline().strip()
            vertices, edges = line.split(" ", 1)
            if self.if_graph_possible(int(vertices), int(edges)) == 1:
                self._graph = Graph(int(vertices), int(edges))
                line = f.readline().strip()
                while line != "":
                    tok = line.split(" ")
                    self._graph._dOut[int(tok[0])].append(int(tok[1]))
                    self._graph.dIn[int(tok[1])].append(int(tok[0]))
                    self._graph.dCost[(int(tok[0]), int(tok[1]))] = int(tok[2])
                    line = f.readline().strip()
                f.close()
            else:
                raise ValueError("Too many edges for this number of vertices")
        except IOError:
            raise ValueError("Something went wrong!")
        # print(self._graph.dIn.values())

    def _save_file(self, file_name):
        """
        Save the graph in a file with the given name
        :param file_name:
        :return:
        """
        # verificare varf izolat
        f = open(file_name, "wt")
        f.write(str(self._graph.nr_vertices) + " " + str(self._graph.nr_edges) + "\n")
        for i in range(self._graph.nr_vertices):
            if i in self._graph.dIn.keys() and i in self._graph.dOut.keys():
                if self._graph.dIn[i] == [] and self._graph.dOut[i] == []:
                    f.write(str(i) + " ")

        f.write("\n")

        for i in range(self._graph.nr_vertices):
            if i in self._graph.dIn.keys() and i in self._graph.dOut.keys():
                for j in range(self._graph.nr_vertices):
                    if self.find_if_edge(i, j) is not None:
                        f.write(str(i) + " " + str(j) + " " + str(self.find_if_edge(i, j)) + "\n")


    def if_graph_possible(self, nr_vert, nr_edge):
        """
        Checks if the graph can be created
        :param nr_vert:
        :param nr_edge:
        :return:0 if not possible, 1 otherwise
        """
        if nr_edge > nr_vert*(nr_vert-1):
            return 0
        return 1

    def random_graph(self, nr_vert, nr_edg):
        """
        Creates a random graph with nr_vert vertices and nr_edg edges
        :param nr_vert:
        :param nr_edg:
        :return:
        """
        self._graph = Graph(nr_vert, nr_edg)
        self._graph.nr_vertices = nr_vert
        self._graph.nr_edges = nr_edg

        i = 0
        while i < nr_edg:
            nr = 0
            x = random.randint(0, nr_vert-1)
            y = random.randint(0, nr_vert-1)
            cost = random.randint(-10, 20)

            if not self._graph.dIn[y]:
                self._graph.dIn[y].append(x)
                nr += 1
            else:
                a = self._graph.get_value(self._graph.dIn, y)
                if x not in a:
                    self._graph.dIn[y].append(x)
                    nr += 1

            if not self._graph.dOut[x]:
                self._graph.dOut[x].append(y)
                nr += 1
            else:
                b = self._graph.get_value(self._graph.dOut, x)
                if y not in b:
                    self._graph.dOut[x].append(y)
                    nr += 1

            if nr == 2:
                self._graph.dCost[(x, y)] = cost
                i += 1



    def get_nr_vertices(self):
        """
        Returns the number of vertices
        :return:
        """
        return self._graph.nr_vertices


    def parse_set_edges(self):
        """
        Parse the edges, return the list that contains all the edges
        :return:
        """
        a = list()
        for i in range(self._graph.nr_vertices):
            for j in range(self._graph.nr_vertices):
                if self.find_if_edge(i, j) is not None:
                    a.append([i, j])

        return a





    def parse_set_vertices(self):
        """
        Parses the vertices, returns the list that contains all the vertices
        :return:
        """
        a = list()
        for i in range(self._graph.nr_vertices):
            a.append(i)
        return a

    def find_if_edge(self, vertex_x, vertex_y):
        """
        Returns the cost of the edge with endpoints vertex_x and vertex_y. If the edge doesn't exist, return None. If the vertices doesn't exist, return -1
        :param vertex_x:
        :param vertex_y:
        :return:
        """
        if vertex_x >= self._graph.nr_vertices:
            return -1

        if vertex_y >= self._graph.nr_vertices:
            return -1

        a = self._graph.get_value(self._graph.dOut, vertex_x)
        if vertex_y in a:
            return self._graph.get_dCost_value(self._graph.dCost, vertex_x, vertex_y)


    def in_degree(self, vertex):
        """
        Return the indegree of the given vertex
        :param vertex:
        :return:
        """
        return self._graph.get_length(self._graph.dIn, vertex)


    def out_degree(self, vertex):
        """
        Return the outdegree of the given vertex
        :param vertex:
        :return:
        """
        return self._graph.get_length(self._graph.dOut, vertex)


    def parse_out_outbound(self, vertex):
        """
        Parse the outbound of the given vertex, and returns the list
        :param vertex:
        :return:
        """
        a = self._graph.get_value(self._graph.dOut, vertex)
        b = list()
        for i in a:
            b.append(i)

        return b

    def parse_in_inbound(self, vertex):
        """
        Parse the inbound of the given vertex, and return the list
        :param vertex:
        :return:
        """
        a = self._graph.get_value(self._graph.dIn, vertex)
        b = list()
        for i in a:
            b.append(i)

        return b

    def remove_cost(self, vertex_x, vertex_y):
        """
        Removes the cost of an edge
        :param vertex_x:
        :param vertex_y:
        :return:
        """
        self._graph.set_dCost_value(self._graph.dCost, vertex_x, vertex_y, "")

    def update_cost(self, vertex_x, vertex_y, val):
        """
        Updates the cost of an edge
        :param vertex_x:
        :param vertex_y:
        :param val:
        :return:
        """
        self._graph.set_dCost_value(self._graph.dCost, vertex_x, vertex_y, val)


    def add_edge(self, file_name, v_x, v_y, cost):
        """
        Adds an edge
        :param file_name:
        :param v_x:
        :param v_y:
        :param cost:
        :return: 0 if the edge already exist, 1 if the edge was added
        """
        if self.find_if_edge(v_x, v_y) is not None:
            return 0
        else:
            self._graph.add(file_name, v_x, v_y, cost)
            return 1


    def remove_edge(self, v_x, v_y):
        """
        Removes the edge that has the first vertex v_x and the target vertex v_y
        :param v_x:
        :param v_y:
        :return:
        """
        self._graph.nr_edges -= 1
        del self._graph.dCost[(v_x, v_y)]

        a = self._graph.get_value(self._graph.dOut, v_x)
        for i in range(len(a)):
            if a[i] == v_y:
                del a[i]
                break

        b = self._graph.get_value(self._graph.dIn, v_y)
        for j in range(len(b)):
            if b[j] == v_x:
                del b[j]
                break

    def add_vertex(self, vertex):
        """
        Add the vertex
        :param vertex:
        :return: -1 if the vertex is greater than the number of vertices so it cannot be added, 0 otherwise
        """
        if vertex >= self._graph.nr_vertices:
            return -1
        #print(self._graph.dIn.keys())
        if vertex in self._graph.dIn.keys():
            return -1
        if vertex in self._graph.dOut.keys():
            return -1
        else:
            self._graph.nr_vertices += 1
            self._graph.dIn[vertex] = []
            self._graph.dOut[vertex] = []
        return 0



    def remove_vertex(self, vertex):
        """
        Removes a vertex
        :param vertex:
        :return:
        """

        if vertex not in self._graph.dIn.keys() and vertex not in self._graph.dOut.keys():
            return -1


        for i in range(self._graph.nr_vertices):
            a = self._graph.get_value(self._graph.dIn, i)
            b = self._graph.get_value(self._graph.dOut, i)
            for j in range(len(a)):
                if a[j] == vertex:
                    a.pop(j)
                    break
            for z in range(len(b)):
                if b[z] == vertex:
                    b.pop(z)
                    self._graph.nr_edges -= 1
                    break

        for i in self._graph.dIn.keys():
            if i == vertex:
                del i

        for i in self._graph.dOut.keys():
            if i == vertex:
                del i

        del self._graph.dIn[vertex]
        del self._graph.dOut[vertex]
        # self._graph.nr_vertices -= 1
        return 0



    def copy_grapf(self, file_name):
        """
        Copies the graph and saves it in the file with the given name
        :param file_name:
        :return:
        """
        new_graph = Graph(0, 0)
        new_graph.nr_edges = self._graph.nr_edges
        new_graph.nr_vertices = self._graph.nr_vertices

        for i in range(self._graph.nr_vertices):
            a = self._graph.get_value(self._graph.dIn, i)
            for j in range(len(a)):
                new_graph.set_din_val(i, a[j])

            b = self._graph.get_value(self._graph.dOut, i)
            for z in range(len(b)):
                new_graph.set_dout_val(i, b[z])
                val = self._graph.get_dCost_value(self._graph.dCost, i, b[z])
                new_graph.set_dcost_val(i, z, val)
        self._save_file(file_name)



    def shortest_path(self, s, t):
        """
        Finds the shortest path from s to t in the graph
        :param s: start
        :param t: end
        :return: the path as a list of vertices starting with s and ending with t.
        """
        dist, next = self.bfs(s, t)

        if s not in dist.keys():
            return None

        path = []
        y = s
        while y != t:
            path.append(y)
            y = next[y]

        path.append(t)
        #path.reverse()
        len = dist[s]
        return path, len


    def bfs(self, s, t):
        """
        Does a BFS from vertex s in the graph. It stops if vertex t is reached(if not None)
        :param s:
        :param t:
        :return: a pair (dist, prev) of dictionaries where the keys are the vertices and the values are the corresponding distances and the previous vertex on the optimal path
        """
        q = queue.Queue()

        q.put(t)

        dist = {}
        dist[t] = 0
        next = {}
        next[t] = None

        while not q.empty():
            x = q.get()

            for y in self.parse_in_inbound(x):
                if y not in dist.keys():
                    dist[y] = dist[x]+1
                    next[y] = x
                    q.put(y)

        return dist, next



    def lowest_cost_Ford(self, V, E, s, t):
        """
        Return the dist and prev dictionaries
        :param V: set of vertices
        :param E: the set of edges cost
        :param s: first vertex
        :param t: second vertex
        :return:
        """
        dist = {}
        prev = {}
        for x in V:
            dist[x] = 10000000

        dist[s] = 0
        changed = True
        nr = self._graph.nr_vertices
        i=0
        while changed and i<nr:
            i+=1
            changed = False
            for (x, y) in E:
                if dist[y] > dist[x] + self._graph.dCost[x, y]:
                    dist[y] = dist[x] + self._graph.dCost[x, y]
                    prev[y] = x
                    changed = True

        #negative cycles
        ok = 0
        for (x, y) in E:
            if dist[y] > dist[x] + self._graph.dCost[x, y]:
                ok = 1

        return dist, prev, ok



    def PredecessorCountingAlgTopoSort(self):
        """
        Return a list of vertices in topological sorting order, or null if the graph has cycles
        :return:
        """

        sorted = []
        queue = []
        count = dict()
        for x in self.parse_set_vertices():
            count[x] = self.in_degree(x)
            if count[x] == 0:
                queue.append(x)

        visited_vertices = 0

        while queue:
            vertex = queue.pop(0)
            sorted.append(vertex)
            for neighbour in self.parse_out_outbound(vertex):
                count[neighbour] -= 1
                if count[neighbour] == 0:
                    queue.append(neighbour)
            visited_vertices+=1

        if visited_vertices != len(self.parse_set_vertices()):
            sorted = None


        return sorted


    def get_costs(self):
        return self._graph.dCost.values()


    def printVertexCover(self):
        visited =[False] * (self._graph.nr_vertices)

        for u in range(self._graph.nr_vertices):
            if not visited[u]:
                for v in self.parse_out_outbound(u):
                    if not visited[v]:
                        visited[v]=True
                        visited[u]=True
                        break

                for v in self.parse_in_inbound(u):
                    if not visited[v]:
                        visited[v]=True
                        visited[u]=True
                        break

        for j in range(self._graph.nr_vertices):
            if visited[j]:
                print(j, end=' ')
        print()









