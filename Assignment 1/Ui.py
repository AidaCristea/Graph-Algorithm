from Service.DinDoutDcostService import Services

class UI:
    def __init__(self):
        self._serv = Services()

    def start(self):

        ok = 0
        while ok == 0:
            print("1. Get the number of vertices\n")
            print("2. Parse the set of vertices\n")
            print("3. Given two vertices, find out whether there is an edge from the first one to the second one\n")
            print("4. Get the degree and the out degree of a specified vertex\n")
            print("5. Parse the set of outbound edges of a specified vertex\n")
            print("6. Parse the set of inbound edges of a specified vertex\n")
            print("7. Remove edge cost\n")
            print("8. Update edge cost\n")
            print("9. Copy graph\n")
            print("10. Read graph from text file\n")
            print("11. Write the graph from a text file\n")
            print("12. Create random graph with specified number of vertices and of edges\n")
            print("13. Add an edge\n")
            print("14. Remove an edge\n")
            print("15. Add a vertex\n")
            print("16. Remove a vertex\n")
            print("17. Exit\n")
            print("18. Print graph\n")
            print("19. Display the minimum length path between two vertices and the corresponding length.\n")
            print("20. Display the lowest cost walk between the given vertices\n")
            print("21. verify if the corresponding graph is a DAG and performs a topological sorting of the activities using the algorithm based on predecessor counters\n")
            print("22. Given an undirected graph, find a vertex cover of minimum size\n")


            option = int(input("Enter your option: "))

            if option == 1:
                # Get the number of vertices
                print(self._serv.get_nr_vertices())
                #self._serv._save_file(self._out_file_name)
            elif option == 2:
                # Parse the set of vertices
                rez = self._serv.parse_set_vertices()
                print(rez)

            elif option == 3:
                # Given two vertices, find out whether there is an edge from the first one to the second one
                first_vertex = int(input("Enter first vertex: "))
                second_vertex = int(input("Enter second vertex: "))
                rez = self._serv.find_if_edge(first_vertex, second_vertex)
                if rez == -1:
                    print("The vertices doesn't exist")
                else:
                    print("the vertex from vertex " + str(first_vertex) + " to vertex " + str(second_vertex) + " has the cost " + str(rez))

            elif option == 4:
                # Get the in degree and the out degree of a specified vertex
                vertex = int(input("Enter vertex: "))
                in_degree = self._serv.in_degree(vertex)
                out_degree = self._serv.out_degree(vertex)
                print("The in degree is " + str(in_degree) + " and the out degree is " + str(out_degree))
            elif option == 5:
                # Parse the set of outbound edges of a specified vertex
                vertex = int(input("Enter vertex: "))
                rez = self._serv.parse_out_outbound(vertex)
                print(rez)

            elif option == 6:
                # Parse the set of inbound edges of a specified vertex
                vertex = int(input("Enter vertex: "))
                rez = self._serv.parse_in_inbound(vertex)
                print(rez)

            elif option == 7:
                # Remove edge cost
                first_vertex = int(input("Enter the first vertex of the wanted edge: "))
                second_vertex = int(input("Enter the second vertex of the wanted edge: "))
                self._serv.remove_cost(first_vertex, second_vertex)
                #self._serv._save_file(self._out_file_name)

            elif option == 8:
                # Update edge cost
                first_vertex = int(input("Enter the first vertex of the wanted edge: "))
                second_vertex = int(input("Enter the second vertex of the wanted edge: "))
                val = int(input("Enter the new cost: "))
                self._serv.update_cost(first_vertex, second_vertex, val)
                #self._serv._save_file(self._out_file_name)

            elif option == 9:
                # Copy graph; citire si numele fisierului din care vreau sa citesc
                file_name = input("Enter the name of the file where you want to save the copy of the graph: ")
                self._serv.copy_grapf(file_name)
            elif option == 10:
                # Read graph from text file
                file_name = input("Enter the name of the file from which you want to load the graph: ")
                self._serv.read_file(file_name)

            elif option == 11:
                # Write the graph from a text file
                file_name = input("Enter the name of the file in which you want to save the graph: ")
                self._serv._save_file(file_name)
            elif option == 12:
                # Create random graph with specified number of vertices and of edges
                nr_vertices = int(input("Enter number of vertices: "))
                nr_edges = int(input("Enter number of edges: "))
                if self._serv.if_graph_possible(nr_vertices, nr_edges) == 0:
                    print("Please enter other numbers; too many edges for this number of vertices")
                else:
                    self._serv.random_graph(nr_vertices, nr_edges)

            elif option == 13:
                # Add an edge
                first_vertex = int(input("Enter the first vertex of the edge: "))
                second_vertex = int(input("Enter the second vertex of the edge: "))
                cost = int(input("Enter the cost of the new edge: "))
                file_name = input("Enter the file in which you want to add an edge: ")
                rez = self._serv.add_edge(file_name, first_vertex, second_vertex, cost)
                if rez == 0:
                    print("Edge already exists, enter something else")
                #self._serv._save_file(self._out_file_name)
            elif option == 14:
                # Remove an edge
                first_vertex = int(input("Enter the first vertex of the edge you want to remove: "))
                second_vertex = int(input("Enter the second vertex of the edge you want to remove: "))
                self._serv.remove_edge(first_vertex, second_vertex)
                # self._serv._save_file(self._out_file_name)
            elif option == 15:
                # Add a vertex
                vertex = int(input("Enter the vertex you want to add: "))
                if self._serv.add_vertex(vertex) == -1:
                    print("Vertex cannot be added")
                else:
                    print("Vertex added")


            elif option == 16:
                # Remove a vertex
                vertex = int(input("Enter the vertex you want to remove: "))
                rez = self._serv.remove_vertex(vertex)
                if rez == -1:
                    print("Cannot remove a vertex that doesn't exist")
                else:
                    print("Success")
            elif option == 17:
                # Exit
                ok = 1
            elif option == 18:
                print(str(self._serv._graph.nr_vertices) + " " + str(self._serv._graph.nr_edges))
                for i in range(self._serv._graph.nr_vertices):
                    if i in self._serv._graph.dIn.keys() and i in self._serv._graph.dOut.keys():
                        if self._serv._graph.dIn[i] == [] and self._serv._graph.dOut[i] == []:
                            print(str(i))

                for i in range(self._serv._graph.nr_vertices):
                    if i in self._serv._graph.dIn.keys() and i in self._serv._graph.dOut.keys():
                        for j in range(self._serv._graph.nr_vertices):
                            if self._serv.find_if_edge(i, j) is not None:
                                print(str(i) + " " + str(j) + " " + str(self._serv.find_if_edge(i, j)))

            elif option == 19:
                # display the minimum length path between two vertices and the corresponding length.
                first = int(input("Enter the vertex you want to start from: "))
                second = int(input("Enter the vertex you want to end: "))
                if self._serv.shortest_path(first, second) is None:
                    print("There is no path")
                else:
                    path, len = self._serv.shortest_path(first, second)
                    print(path)
                    print("Length = " + str(len))

            elif option == 20:
                # display the lowest cost walk between the given vertices
                first = int(input("Enter the first vertex you want to start from: "))
                second = int(input("Enter the second vertex you want to end: "))
                set_vertex = self._serv.parse_set_vertices()
                set_edges= self._serv.parse_set_edges()

                dist, prev, okk = self._serv.lowest_cost_Ford(set_vertex, set_edges, first, second)
                print("cost ", dist[second])
                #print(prev)

                if okk == 1:
                    print("Negative cycle")

                if prev == {}:
                    print("No path")

                if second not in prev.keys():
                    print("No path")

                else:
                    nr=0
                    for i in prev:
                        nr += 1

                    keys = [i for i in prev.keys()]
                    rez=[]
                    nrr=0

                    i=0
                    while keys[i] != second:
                        i += 1

                    rez.append(second)
                    nrr += 1
                    i=prev[second]

                    #keys=prev.keys()
                    #i=keys[nr-1]

                    while i != first:
                        rez.append(i)
                        nrr += 1
                        i = prev[i]


                    rez.append(i)
                    nrr += 1
                    v=nrr-1
                    while v>=0:
                        print(rez[v])
                        v -= 1

            elif option==21:

                #call the topo function
                sorted = self._serv.PredecessorCountingAlgTopoSort()
                print(sorted)

                if(sorted!=None):
                    nr=0
                    for i in sorted:
                        nr+=1
                    early_start=dict()
                    early_finish=dict()
                    late_start=dict()
                    late_finish=dict()

                    cost = list(self._serv.get_costs())
                    # print(cost)

                    early_start[0] = 0
                    """
                    i=0
                    for i in range(self._serv.get_nr_vertices()):
                        if self._serv.find_if_edge(0, i):
                            break
                    """
                    early_finish[0] = cost[0]

                    i=1
                    while i < nr:

                        durations=[]
                        for ditem in self._serv.parse_in_inbound(i):
                            durations.append(ditem)

                        if durations !=[]:


                            early_start[i] = max(durations)


                            """
                            if early_finish[i] > early_finish[i-1]:
        
                                early_start[i] = early_finish[i]
                            else:
                                early_start[i]=early_finish[i-1]
                            """
                            early_finish[i]=early_start[i] + cost[i]
                        i+=1


                    late_finish[nr-1]=early_finish[nr-1]
                    late_start[nr-1] = early_finish[nr-1] - cost[nr-1]
                    i=nr - 1
                    while i>=0:
                        durations = []
                        for ditem in self._serv.parse_out_outbound(i):
                            durations.append(ditem)
                        """
                        if(late_finish[i] < late_finish[i+1] ):
                            late_start[i+1]=late_finish[i]
                        else:
                            late_start[i+1] = late_finish[i+1]
                        """
                        if durations != []:

                            late_finish[i] = min(durations)
                            late_start[i] = late_finish[i] - cost[i]
                        i-=1

                    print("Early start: ")
                    print(early_start)
                    print("Late start: ")
                    print(late_start)
                    print("Early finish: ")
                    print(early_finish)
                    print("Total time: ")
                    print(early_finish[self._serv.get_nr_vertices() -1])

                    print("Late finish: ")
                    print(late_finish)

                    ok=0
                    print("Critical activity: ")
                    for i in range(nr):
                        if(early_start[i] == early_finish[i] and late_start[i] == late_finish[i]):
                            ok=1
                            print(i)
                    if(ok==1):
                        print("No critical activities")

            elif option == 22:
                #Given an undirected graph, find a vertex cover of minimum size
                self._serv.printVertexCover()










