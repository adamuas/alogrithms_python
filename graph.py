# -*- coding: cp1252 -*-
class Graph:
    """ 
    An adjacency graph implementation 
    """
    def __init__(self):
        """
        Constructs a graph from an adjacency list
        """
        self.vertices = dict();

    def addVertex(self, v):
        """
        Adds a vetex to the graph
        """
        try:    
            #make a new vertex with empty edjes
                    self.vertices[str(v)] = set();
        except:
            raise Exception("hmm..vertex has to be a string");
    
    def removeVertex(self, v):
        """
        removes a vertex from the graph
        """
        #check if key is in the graph
        if v in self.vertices.keys():
                #remove vertex
                del self.vertices[v];
                
                #remove edges point to the vertex - if any
                for vi,E in self.vertices.iteritems():
                        if v in E:
                                self.vertices[vi].remove(v);
        else:
                print "amm...that vertex is not in the graph";


    def addEdge(self, i, j):
        """
        adds an edge from i to j
        
        params:
        i - edge i in the graph
        j - edge j in the graph
        """
        

        #check if both nodes exist
        if i in self.vertices.keys() and j in self.vertices.keys():
            #connect from i to j
            self.vertices[i].add(j);
        else:
            print "hmm..one of the vertices is not in the graph.";


    def removeEdge(self, i,j):
        """
        removes an edge from i to j

        params:
        i - edge i in the graph
        j - edge in the graph
        """

        #check if both nodes exist in the graph
        if i in self.vertices.keys() and j in self.vertices.keys():
            #check if the connection exists
            if j in self.vertices[i]:
                #remove it from the edge set
                self.vertices[i].remove(j);

            else:
                print "hmm..connection doesnt seem to be in graph";

        else:
            print "hmm...one or both of the edges is not in the graph";


    def neighbours(self, v):
        """
        returns the vertices connected to v
        """

        return self.vertices[v];

    def bfs(self, v):
        """
        breadth first search traversal

        params:
        v - vertex to search from

        returns:
        pathTo - path to set which is shortest path to the vertex
        """
        #visited edges
        pathTo = dict();
        #visited edges
        visited = dict()

        #initialize the dictionaries
        for vi in self.vertices.keys():
            pathTo[vi] = None;
            visited[vi] = False;
            
        #recursive bfs
        pathTo = self._bfs(vertex = v, pathTo = pathTo, visited = visited);

        return pathTo;

        
    def dfs(self, v):
        """
        depths first search

        params:
        v - source vertex
        """

        #visited edges
        pathTo = dict();
        #visited edges
        visited = dict()

        #initialize the dictionaries
        for vi in self.vertices.keys():
            pathTo[vi] = None;
            visited[vi] = False;
            
        # dfs
        self._dfs(vertex = v, pathTo = pathTo, visited = visited);

        



    def _dfs(self, vertex, pathTo, visited):
        """
        A helper function for the depth first search

        params:
        vertex - starting vertex (source)
        pathTo - pathTo dictionary that trakcs path to the source vertex
        visited - dictionary 
        """

        #stack
        s = [];

        #put the current state in stack
        s.append(vertex);

        while s != []:

            #pop from stack
            vi = s.pop(-1);
            visited[vi] = True;
            print vi;
            
            #check neighbourds
            for vj in self.neighbours(vi):
                #check if visited
                if not visited[vj]:
                    #push to the stack
                    s.append(vj);
                    #set pathTo
                    pathTo[vj] = vi;
                    #visited vj
                    visited[vj] = True;

        print "pathTo:{0} \nvisited: {1}".format(pathTo, visited);

        return pathTo;
                    
                    

    def shortestPath(self, vi, vj):
        """
        Shortest path from vertex vi to vj
        """

        pathTo = self.bfs(vi);

        path_ij = set();

        vertex = vj;
        while vertex != vi:
            #append to path
            path_ij.add(vertex);
            #get next path to the given vertex
            vertex = pathTo[vertex];

        path_ij.add(vertex);


        print "vertex",path_ij;

        
            
        
            
        
    def _bfs(self, vertex, pathTo, visited):
        """
        A helper function for the breadth first search

        params:
        vertex  - starting vertex (source)
        pathTo - pathTo dictionary that tracks path to the source vertex (i.e. shortest path)
        visited - dictionary that tracks visited

        returns
        pathTo - returns the path to dicationary
        """

        #queue
        q = [];

        #enqueue (FILO)
        q.append(vertex);
        visited[vertex] = True;

        while q != []:

            #pop first item (make-shift dequeue)
            vi = q.pop(0);
            print vi;

            for vj in self.neighbours(vi):
                if not visited[vj]:
                    q.append(vj);
                    visited[vj] = True;
                    pathTo[vj] = vi;



        print "pathTo:{0} \nvisited: {1}".format(pathTo, visited);

        return pathTo;
    
     

    def __repr__(self):
        """
        returns a string representation of the 
        """
        return """
                <GRAPH>
                    <Vertices>
                    {0}
                    </Vertices>
                </GRAPH>
                """.format(self.vertices);



g = Graph();

g.addVertex('A');
g.addVertex('B');
g.addVertex('C');
g.addVertex('D');
g.addVertex('E');
g.addVertex('F');
g.addVertex('G');



g.addEdge('A', 'B');
g.addEdge('A', 'C');
g.addEdge('A', 'D');
g.addEdge('B', 'E');
g.addEdge('B', 'F');
g.addEdge('C', 'G');

print g;

g.bfs('A');
g.dfs('A');

g.shortestPath('A', 'G');
        
