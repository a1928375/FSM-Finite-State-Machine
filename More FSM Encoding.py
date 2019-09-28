edges = {(1,"a"):2, (1,"b"):2, (2,"c"):3, (2,"d"):3}

accepting = [2,3]

def fsmsim(string, current, edges, accepting):
    
    if string == "":
        
        return current in accepting
        
    else:
        
        letter = string[0]
        
        if (current, letter) in edges:
            
            destination = edges[(current, letter)]
            remaining_string = string[1:]
            
            return fsmsim(remaining_string, destination, edges, accepting)
            
        else:
            
            return False

print (fsmsim("a",1,edges,accepting))
print (fsmsim("b",1,edges,accepting))
print (fsmsim("ad",1,edges,accepting))
print (fsmsim("e",1,edges,accepting))
