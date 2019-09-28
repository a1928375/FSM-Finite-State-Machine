edges = { (1,'a') : [2],
          (2,'b') : [3,4],
          (3,'x') : [5],
          (4,'y') : [5],
          (5,'b') : [3,4], 
          (5,'c') : [6],
          } 
accepting = 6

start = 1 

def reverse(edges,accepting,start): 
    
    new_edges = {}
    
    new_accepting = start
    
    new_start = accepting
    
    for k in edges:
        
        start_state = k[0]
        
        letter = k[1]
        
        des_states = edges[k]
        
        for des_state in des_states:
            
            before = []
            
            if (des_state, letter) in new_edges:            # if (des_state, letter) has existed in new_edges
                
                before = new_edges[(des_state, letter)]     # use before to get original value of (des_state, letter)
                
            new_edges[(des_state,letter)] = [start_state] + before     # reverse: (des_state,letter) to (start_state + before)
    
    return (new_edges,new_accepting,new_start) 

print (reverse(edges,accepting,start))
                
def nfsmaccepts(edges,accepting,current,str): 
        if str == "":
                return current == accepting
        letter = str[0]
        rest = str[1:] 
        if (current,letter) in edges:
                for dest in edges[(current,letter)]:
                        if nfsmaccepts(edges,accepting,dest,rest):
                                return True
        return False
        
r_edges, r_accepting, r_start = reverse(edges,accepting,start) 

for s in [ "abxc", "abxbyc", "not", "abxbxbxbxbxc", "" ]: 
        # The original should accept s if-and-only-if the
        # reversed version accepts s_reversed.
        
        print (nfsmaccepts(edges,accepting,start,s) == nfsmaccepts(r_edges,r_accepting,r_start,s[::-1]))

# r"a+b*"
edges2 = { (1,'a') : [2],
          (2,'a') : [2],
          (2,'b') : [2] 
          }

accepting2 = 2

start2 = 1 

r_edges2, r_accepting2, r_start2 = reverse(edges2,accepting2,start2) 

for s in [ "aaaab", "aabbbbb", "ab", "b", "a", "", "ba" ]:
    
        print (nfsmaccepts(edges2,accepting2,start2,s) == nfsmaccepts(r_edges2,r_accepting2,r_start2,s[::-1]))
