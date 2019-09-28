edges = { (1, 'a') : [2, 3],
          (2, 'a') : [2],
          (3, 'b') : [4, 3],
          (4, 'c') : [5] }

accepting = [2, 5] 

def nfsmsim(string, current, edges, accepting): 
    
    if string == "":
        
        return current in accepting
    
    else:
        
        letter = string[0]
        
        if (current, letter) in edges:
            
            remaining = string[1:]
            
            newstates = edges[(current, letter)]
            
            for newstate in newstates:
                
                if nfsmsim(remaining, newstate, edges, accepting):
                    
                    return True    
        
        return False

print ("Test case 1 passed: " + str(nfsmsim("abc", 1, edges, accepting) == True))
print ("Test case 2 passed: " + str(nfsmsim("aaa", 1, edges, accepting) == True)) 
print ("Test case 3 passed: " + str(nfsmsim("abbbc", 1, edges, accepting) == True)) 
print ("Test case 4 passed: " + str(nfsmsim("aabc", 1, edges, accepting) == False))
print ("Test case 5 passed: " + str(nfsmsim("", 1, edges, accepting) == False)) 
