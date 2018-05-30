from collections import deque
vertices = [0,1,2,3,4]

adj_list = [[1],[2,4],[3],[1],[0]]

visited = [None,None,None,None,None]

stack = deque()

s = int(raw_input("enter source"))

stack.append(s)

while (len(stack)!= 0):
    vertex_check = stack.pop()

    if visited[vertex_check] == None: #if node has not been visited
        print vertex_check #printing the top vertex on the stack

        visited[vertex_check] = 0 #marking as visited
        
    #iterate through the adjacency list of the vertex being checked
    #if the vertices have not been visited mark them so 
    #push on the stack
    for i in adj_list[vertex_check][::-1]:
        if visited[i] == None:
            stack.append(i)
