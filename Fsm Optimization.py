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
				    
					foo = nfsmaccepts(newstate, edges, accepting, newvisited)
					
					if foo != None:
					    
						return edge[1] + foo
						
		return None


def nfsmtrim(edges, accepting):
    
	# Step 1, find live states gather up all of the states (maybe duplicated)
	states = []
	
	for e in edges:
	    
		states.append(e[0])
		states.extend(edges[e])
		
	# a state is live if there is some way to accept starting from it
	live = []
	
	for s in states:
	    
		if nfsmaccepts(s, edges, accepting, []) != None:
		    
			live.append(s)        
			
	# Step 2, create new FSM
	new_edges = {}
	
	for e in edges:
	    
		if e[0] in live:
		    
			new_destinations = []
			
			for dest in edges[e]:
			    
				if dest in live:
				    
					new_destinations.append(dest)
					
			if new_destinations != []:
			    
				new_edges[e] = new_destinations
				
	new_accepting = []
	
	for s in accepting:
	    
		if s in live:
		    
			new_accepting.append(s)
	
	return (new_edges, new_accepting)
    

edges1 = { (1,'a') : [1] ,
           (1,'b') : [2] ,
           (2,'b') : [3] ,
           (3,'b') : [4] ,
           (8,'z') : [9] , } 
           
accepting1 = [ 1 ] 

(new_edges1, new_accepting1) = nfsmtrim(edges1,accepting1) 

print (new_edges1)
print (new_edges1 == {(1, 'a'): [1]})
print (new_accepting1 == [1]) 

(new_edges2, new_accepting2) = nfsmtrim(edges1,[]) 

print (new_edges2 == {})
print (new_accepting2 == []) 

(new_edges3, new_accepting3) = nfsmtrim(edges1,[3,6]) 

print (new_edges3 == {(1, 'a'): [1], (1, 'b'): [2], (2, 'b'): [3]})
print (new_accepting3 == [3])

edges4 = { (1,'a') : [1] ,
           (1,'b') : [2,5] ,
           (2,'b') : [3] ,
           (3,'b') : [4] ,
           (3,'c') : [2,1,4] } 
           
accepting4 = [ 2 ] 

(new_edges4, new_accepting4) = nfsmtrim(edges4, accepting4) 

print (new_edges4 == { 
  (1, 'a'): [1],
  (1, 'b'): [2], 
  (2, 'b'): [3], 
  (3, 'c'): [2, 1], 
})
print (new_accepting4 == [2])
