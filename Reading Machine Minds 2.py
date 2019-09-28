def cfgempty(grammar, symbol, visited):
    
    if symbol in visited:
        
        # no infinite loops!        
        return None
        
    elif not any([ rule[0] == symbol for rule in grammar ]):
        
        # base case: 'symbol' is a terminal        
        return [symbol]
        
    else:
        new_visited = visited + [symbol]
        
            # consider every rewrite rule "Symbol -> RHS"        
        for rhs in [r[1] for r in grammar if r[0] == symbol]: 
            
            # check if every part of RHS is non-empty
            if all([None != cfgempty(grammar, r, new_visited) for r in rhs]):
                
                result = [] # gather up the result
                
                for r in rhs:
                    
                    result = result + cfgempty(grammar, r, new_visited)
                    
                return result
                
        # didn't find any 
        return None

grammar1 = [ 
      ("S", [ "P", "a" ] ),           
      ("P", [ "S" ]) ,               
      ] 
                        
print (cfgempty(grammar1,"S",[]) == None)

grammar2 = [
      ("S", ["P", "a" ]),             
      ("S", ["Q", "b" ]),             
      ("P", ["P"]), 
      ("Q", ["c", "d"]),              
      ] 

print (cfgempty(grammar2,"S",[]) == ['c', 'd', 'b'])


grammar3 = [  # some Spanish provinces
        ("S", [ "Barcelona", "P", "Huelva"]),
        ("S", [ "Q" ]),
        ("Q", [ "S" ]),
        ("P", [ "Las Palmas", "R", "Madrid"]),
        ("P", [ "T" ]),
        ("T", [ "T", "Toledo" ]),
        ("R", [ ]) ,
        ("R", [ "R"]), 
        ]

print (cfgempty(grammar3,"S",[]) == ['Barcelona', 'Las Palmas', 'Madrid', 'Huelva'])
