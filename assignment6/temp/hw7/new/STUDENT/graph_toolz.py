import os
from queue import *

class Graph(object):
    # Initializing empty graph
    def __init__(self):
        self.adj_list = dict()    # Initial adjacency list is empty dictionary
        self.vertices = set()    # Vertices are stored in a set
        self.degrees = dict()    # Degrees stored as dictionary
        
        self.pred =  dict()
        self.visited = set()
        self.dist = dict()
        self.max_level = 0

    # Checks if (node1, node2) is edge of graph. Output is 1 (yes) or 0 (no).
    def isEdge(self,node1,node2):
        if node1 in self.vertices:        # Check if node1 is vertex
            if node2 in self.adj_list[node1]:    # Then check if node2 is neighbor of node1
                return 1            # Edge is present!

        if node2 in self.vertices:        # Check if node2 is vertex
            if node1 in self.adj_list[node2]:    # Then check if node1 is neighbor of node2
                return 1            # Edge is present!

        return 0                # Edge not present!

    # Add undirected, simple edge (node1, node2)
    def addEdge(self,node1,node2):

        # print('Called')
        if node1 == node2:            # Self loop, so do nothing
            # print('self loop')
            return
        if node1 in self.vertices:        # Check if node1 is vertex
            nbrs = self.adj_list[node1]        # nbrs is neighbor list of node1
            if node2 not in nbrs:         # Check if node2 already neighbor of node1
                nbrs.add(node2)            # Add node2 to this list
                self.degrees[node1] = self.degrees[node1]+1    # Increment degree of node1

        else:                    # So node1 is not vertex
            self.vertices.add(node1)        # Add node1 to vertices
            self.adj_list[node1] = {node2}    # Initialize node1's list to have node2
            self.degrees[node1] = 1         # Set degree of node1 to be 1

        if node2 in self.vertices:        # Check if node2 is vertex
            nbrs = self.adj_list[node2]        # nbrs is neighbor list of node2
            if node1 not in nbrs:         # Check if node1 already neighbor of node2
                nbrs.add(node1)            # Add node1 to this list
                self.degrees[node2] = self.degrees[node2]+1    # Increment degree of node2

        else:                    # So node2 is not vertex
            self.vertices.add(node2)        # Add node2 to vertices
            self.adj_list[node2] = {node1}    # Initialize node2's list to have node1
            self.degrees[node2] = 1         # Set degree of node2 to be 1

    # Give the size of the graph. Outputs [vertices edges wedges]
    #
    def size(self):
        n = len(self.vertices)            # Number of vertices

        m = 0                    # Initialize edges/wedges = 0
        wedge = 0
        for node in self.vertices:        # Loop over nodes
            deg = self.degrees[node]      # Get degree of node
            m = m + deg             # Add degree to current edge count
            wedge = wedge+deg*(deg-1)/2        # Add wedges centered at node to wedge count
        return [n, m, wedge]            # Return size info

    # Print the graph
    def output(self,fname,dirname):
        os.chdir(dirname)
        f_output = open(fname,'w')

        for node1 in list(self.adj_list.keys()):
            f_output.write(str(node1)+': ')
            for node2 in (self.adj_list)[node1]:
                f_output.write(str(node2)+' ')
            f_output.write('\n')
        f_output.write('------------------\n')
        f_output.close()

    def path(self, src, dest):
        """ implement your shortest path function here """
        #Run BFS for the first time using the source
        if (len(self.visited) == 0):
            self.bfs(src)
        #Create a new graph that start with a new src to handle new path
        graph = Graph()
        graph.vertices = self.vertices
        graph.adj_list = self.adj_list
        graph.pred = self.pred
        graph.bfs(src)
        #self.levels(src)
        #print("___________________________________")

        #print ("__________________________________")
        #print ("BFS is done")
        shortest_path = []
        #self.bfs(src)
        #The method to find the path is through theorm discussed in class
        #The idea is that the pred[dst] is going back a level toward src
        #If src have path to dst, then by iterating through the pred of dst, it will hit src
        #print ("Dest's pred is ", self.pred[dest])
        #Check if there is a pred for destination
        while(dest in self.pred):
            #print ("pred of dest inside while", self.pred[dest])
            if(src == self.pred[dest]):
                #Record the hop, FIX this later
                shortest_path.append(dest)
                shortest_path.append(self.pred[dest])
                #After adding the last point, return this
                shortest_path.reverse()
                #print ("Path found", shortest_path)
                return shortest_path
            else:
                #Change the pointer
                shortest_path.append(dest)
                dest = self.pred[dest]
                #print (shortest_path)
        #If the while loop hits none, then there is no shortest path
        #return empty array
        #shortest_path = []
        print ("No shortest path")
        # Your code comes here
        return shortest_path



    def levels(self, src):
        """ implement your level set code here """
        level_sizes = []
        # Your code comes in here
        #Using BFS to go through all of the graph and the distance should be save
      
        graph = Graph()
        graph.adj_list = self.adj_list
        graph.dist = self.dist
        graph.bfs(src)
        
        #Fill in the 0
        for i in range(0,graph.max_level+1):
            level_sizes.append(0)

        for key in graph.dist:
            if graph.dist[key] > graph.max_level:
                print ("bug")
            else:
                level_sizes[graph.dist[key]] +=1

        #print (level_sizes)
        return level_sizes



    def debug(self,src):
        for v in self.adj_list[src]:
            print (v)
        return
    
    def bfs(self,src):
        #print ("Running once only")
        #make it simple to set if the vertice has been visiteduyt
        q = Queue()
        #visited = set()
        #Make it into a dictionary, so it is better to look up key
        #src.dist = dict()
        #src.pred = dict()
        #Src is visited in the becomming and added into the Q
        #Q.add(src)
        self.dist[src] = 0
        #Put src into the Queue and iterate its neighbor
        q.put(src)
        self.visited.add(src)
        #Need to process everything in the queue first
        while not (q.empty()):
            u = q.get()
            #print(u,"is being dequeue")
            #Mark the head of the Queue as visited 
            #if u not in self.visited:
                #self.visited.add(u)
                #Iterate through all neighbor of v, i+1 level
            for v in self.adj_list[u]:
                #print ("neighbor of v", self.adj_list[u])
                    #If the node is not visited, then add to the queue
                if v not in self.visited:
                        #Update the node that have been visited
                    self.visited.add(v)
                    self.pred[v] = u
                    self.dist[v] = self.dist[u] + 1
                    if((self.dist[v] > self.max_level)):
                        self.max_level = self.dist[v]
                    q.put(v)
                    #print (v, "is being added into the queue")