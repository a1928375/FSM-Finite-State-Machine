edges = { (1, 'a') : [2, 3],
          (2, 'a') : [2],
          (3, 'b') : [2, 4],
          (4, 'c') : [5] }

accepting = [5] 

edges2 = { (1, 'a') : [1],
           (2, 'a') : [2] }

accepting2 = [2] 

visited = []

def nfsmaccepts(current, edges, accepting, visited): 
    
    if current in visited:
        
        return None
        
    elif current in accepting:
        
        return ""
    
    else:
        
        newvisited = visited + [current]
        
        for edge in edges:
            
            if edge[0] == current:
                
                for newstate in edges[edge]:
                    
                    foo = nfsmaccepts(newstate, edges,accepting, newvisited)
                    
                    if foo != None:
                        
                        return edge[1] + foo
                        
        return None


print ("Test 1: " + str(nfsmaccepts(1, edges, accepting, []) == "abc"))
print ("Test 2: " + str(nfsmaccepts(1, edges, [4], []) == "ab"))
print ("Test 3: " + str(nfsmaccepts(1, edges2, accepting2, []) == None))
print ("Test 4: " + str(nfsmaccepts(1, edges2, [1], []) == ""))
