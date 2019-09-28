def cfginfinite(grammar): 
    
      for Q in [rule[0] for rule in grammar]:
          
            # See if Q can rewritten to x Q y, where |x + y| > 0
            def helper(current, visited, sizexy):
                
                  if current in visited:
                      
                        return sizexy > 0
                        
                  else:
                      
                        new_visited = visited + [current]
                        
                        for rhs in [rule[1] for rule in grammar if rule[0] == current]:
                            
                              for symbol in rhs:
                                  
                                    if helper(symbol, new_visited, sizexy + len(rhs) - 1):
                                        
                                          return True
                                          
                        return False

            if helper(Q, [], 0):
                
                  return True
                  
      return False

grammar1 = [ 
      ("S", [ "S", "a" ]), # S -> S a
      ("S", [ "b", ]) , # S -> b 
      ] 
print (cfginfinite(grammar1) == True)

grammar2 = [ 
      ("S", [ "S", ]), # S -> S 
      ("S", [ "b", ]) , # S -> b 
      ] 

print (cfginfinite(grammar2) == False)

grammar3 = [ 
      ("S", [ "Q", ]), # S -> Q
      ("Q", [ "b", ]) , # Q -> b
      ("Q", [ "R", "a" ]), # Q -> R a 
      ("R", [ "Q"]), # R -> Q
      ] 

print (cfginfinite(grammar3) == True)

grammar4 = [  # Nobel Peace Prizes, 1990-1993
      ("S", [ "Q", ]),
      ("Q", [ "Mikhail Gorbachev", ]) ,
      ("Q", [ "P", "Aung San Suu Kyi" ]),
      ("R", [ "Q"]),
      ("R", [ "Rigoberta Tum"]),
      ("P", [ "Mandela and de Klerk"]),
      ] 

print (cfginfinite(grammar4) == False)
