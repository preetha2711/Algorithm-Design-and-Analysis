vertices = [0,1,2,3,4]

adj_list = [[1,2],[2,3], [3,4],[4,0], [0,1]] #2D array consisting of the edges to which the vertices are going

visited  = [None,None,None,None,None] #this is an array that will indicate whether the nodes have been visited or not. 

#using multiple arrays in place of structures

s  = vertices[0] #say we take first index as source 

visited[s] = 0 #mark as visited

stack = []


def DFS(array,node, visited):

    for i in array[node]:
        if visited[i] == None:
            visited[i] = 0
            print i
            DFS(array,i,visited)



DFS(adj_list,s,visited)
