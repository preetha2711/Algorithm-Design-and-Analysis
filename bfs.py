
#indexed from 0 for easy reading
from collections import deque  #allows me to use lists as queues

vertices = [0,1,2,3,4]

adj_list = [[1,2],[2,3], [3,4],[4,0], [0,1]] #2D array consisting of the edges to which the vertices are going

visited  = [None,None,None,None,None] #this is an array that will indicate whether the nodes have been visited or not. 

#using multiple arrays in place of structures

#since the visited array is null all vertices are marked as not visited in the graph right now

s = int(raw_input("enter source vertex"))

visited[s] = 0 #marked the source as visited in the array

queue = deque()

queue.append(s)

while (len(queue)!=0):
    vertex_check = queue.popleft() #deque the element being checked 
    print vertex_check 

    for i in adj_list[vertex_check]:
        if visited[i] == None: #if vertex has not been visited yet
            visited[i] = 0 #marked as visited
            queue.append(i)

flag = False #variable to check whether the graph is disconnected

for i in visited:
    if visited[i] == None:
        flag = True

if flag == True:
    print "Graph is disconnected"

else:
    print "all nodes of the graph have been traversed"


##BFS can also be used to track cycles in an undirected graph##

##following is a function that will do the same##
parent = [None,None,None,None,None]
visited = [None,None,None,None,None] #reinitialising visited array for this purpose

def cycle_BFS(array, s ,parent):
    parent[s] = None #marked the source as visited in the array
    visited[s] = 0

    queue = deque()

    queue.append(s)

    while (len(queue)!=0):
        vertex_check = queue.popleft() #deque the element being checked 

        for i in array[vertex_check]:
            
            if parent[i] != None: #if vertex already has a parent then it can be reached from another node
                #This implies that a cycle exists
                print "Cycle exists"
                break
            else:
                visited[i] = 0 #marked as visited
                parent[i] = vertex_check
                queue.append(i)


cycle_BFS(adj_list,2,parent)