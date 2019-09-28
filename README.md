# FSM-Finite-State-Machines

(1) Fsm Simulator:  Hint: recursion.

(2) Fsm Interpretation:  Define edges and accepting to encode r"q*". Name your start state 1.

(3) More FSM Encoding

(4) Mis Msf:  Provide s1 and s2 that are both accepted, but s1 != s2.

(5) Simulating Nondeterminism:  Each regular expression can be converted to an equivalent finite state machine. This is how regular expressions are implemented in practice. We saw how non-deterministic finite state machines can be converted to deterministic ones (often of a different size). It is also possible to simulate non-deterministic machines directly -- and we'll do that now! In a given state, a non-deterministic machine may have *multiple* outgoing edges labeled with the *same* character. To handle this ambiguity, we say that a non-deterministic finite state machine accepts a string if there exists *any* path through the finite state machine that consumes exactly that string as input and ends in an accepting state. Write a procedure nfsmsim that works just like the fsmsim we covered together, but handles also multiple outgoing edges and ambiguity. Do not consider epsilon transitions. Formally, your procedure takes four arguments: a string, a starting state, the edges (encoded as a dictionary mapping), and a list of accepting states. To encode this ambiguity, we will change "edges" so that each state-input pair maps to a *list* of destination states. For example, the regular expression r"a+|(?:ab+c)" might be encoded like  this:

          edges = { (1, 'a') : [2, 3],
                    (2, 'a') : [2],
                    (3, 'b') : [4, 3],
                    (4, 'c') : [5] }
          
          accepting = [2, 5] 

It accepts both "aaa" (visiting states 1 2 2 and finally 2) and "abbc" (visting states 1 3 3 4 and finally 5). 
 
(6) Reading Machine Minds:  In this homework problem you will determine if a finite state machine is empty or not. If it is not empty, you will prove that by returning a string that it accepts. Formally, you will write a procedure nfsmaccepts() that takes four arguments corresponding to a non-derministic finite state machine:
 
          the start (or current) state
          the edges (encoded as a mapping)
          the list of accepting states
          a list of states already visited (starts empty) 

If the finite state machine accepts any string, your procedure must return one such string (your choice!). Otherwise, if the finite state machine is empty, your procedure must return None (the value None, not the string "None"). For example, this non-deterministic machine ...

          edges = { (1, 'a') : [2, 3],
                    (2, 'a') : [2],
                    (3, 'b') : [2, 4],
                    (4, 'c') : [5] }
          
          accepting = [5] 
          
... accepts exactly one string: "abc". By contrast, this non-deterministic machine: 

          edges2 = { (1, 'a') : [1],
                     (2, 'a') : [2] }
                     
          accepting2 = [2] 
          
... accepts no strings (if you look closely, you'll see that you cannot actually reach state 2 when starting in state 1). 

          Hint #1: This problem is trickier than it looks. If you do not keep track of where you have been, your procedure may loop               forever on the second example. Before you make a recursive call, add the current state to the list of visited states (and be             sure to check the list of visited states elsewhere). 

          Hint #2: (Base Case) If the current state is accepting, you can return "" as an accepting string.  

          Hint #3: (Recursion) If you have an outgoing edge labeled "a" that goes to a state that accepts on the string "bc" (i.e., the           recursive call returns "bc"), then you can return "abc". 

          Hint #4: You may want to iterate over all of the edges and only consider those relevant to your current state. "for edge in             edges" will iterate over all of the keys in the mapping (i.e., over all of the (state,letter) pairs) -- you'll have to write             "edges[edge]" to get the destination list. 

(7) Fsm Optimization:  Lexical analyzers are implemented using finite state machines generated from the regular expressions of token definition rules. The performance of a lexical analyzer can depend on the size of the resulting finite state machine. If the finite state machine will be used over and over again (e.g., to analyze every token on every web page you visit!), we would like it to be as small as possible (e.g., so that your webpages load quickly). However, correctness is more important than speed: even an optimized FSM must always produce the right answer. One way to improve the performance of a finite state machine is to make it smaller by removing unreachable states. If such states are removed, the resulting FSM takes up less memory, which may make it load faster or fit better in a storage-constrained mobile device. For this assignment, you will write a procedure nfsmtrim that removes "dead" states from a non-deterministic finite state machine. A state is (transitively) "dead" if it is non-accepting and only non-accepting states are reachable from it. Such states are also called "trap" states: once entered, there is no escape. In this example FSM for r"a*" ...

          edges = { (1,'a') : [1] ,
                   (1,'b') : [2] ,
                   (2,'b') : [3] ,
                   (3,'b') : [4] } 

          accepting = [ 1 ] 

... states 2, 3 and 4 are "dead": although you can transition from 1->2, 2->3 and 3->4 on "b", you are doomed to rejection if you do so. 

You may assume that the starting state is always state 1. Your procedure nfsmtrim(edges,accepting) should return a tuple (new_edges,new_accepting) corresponding to a FSM that accepts exactly the same strings as the input FSM but that has all dead states removed. 

          Hint 1: This problem is tricky. Do not get discouraged. 

          Hint 2: Think back to the nfsmaccepts() procedure from the "Reading Machine Minds" homework problem in Unit 1. You are welcome           to reuse your code (or the solution we went over) to that problem. 

          Hint 3: Gather up all of the states in the input machine. Filter down to just those states that are "live". new_edges will               then be just like edges, but including only those transitions that involve live states. new_accepting will be just like                 accepting, but including only those live states.

(8) Reading Machine Minds 2:  We say that a finite state machine is "empty" if it accepts no strings. Similarly, we say that a context-free grammar is "empty" if it accepts no strings. In this problem, you will write a Python procedure to determine if a context-free grammar is empty. A context-free grammar is "empty" starting from a non-terminal symbol S if there is no _finite_ sequence of rewrites starting from S that yield a sequence of terminals. For example, the following grammar is empty:

          grammar1 = [ 
          ("S", [ "P", "a" ] ),           # S -> P a
          ("P", [ "S" ]) ,                # P -> S
          ] 
     
Because although you can write S -> P a -> S a -> P a a -> ... that process never stops: there are no finite strings in the language of that grammar. 

By contrast, this grammar is not empty: 

          grammar2 = [
          ("S", ["P", "a" ]),             # S -> P a
          ("S", ["Q", "b" ]),             # S -> Q b
          ("P", ["P"]),                   # P -> P
          ("Q", ["c", "d"]),              # Q -> c d 

And ["c","d","b"] is a witness that demonstrates that it accepts a string. Write a procedure cfgempty(grammar,symbol,visited) that takes as input a grammar (encoded in Python) and a start symbol (a string). If the grammar is empty, it must return None (not the string "None", the value None). If the grammar is not empty, it must return a list of terminals corresponding to a string in the language of the grammar. (There may be many such strings: you can return any one you like.) To avoid infinite loops, you should use the argument 'visited' (a list) to keep track of non-terminals you have already explored. 

          Hint 1: Conceptually, in grammar2 above, starting at S is not-empty with witness [X,"a"] if P is non-empty with witness X and           is non-empty with witness [Y,"b"] if Q is non-empty with witness Y. 
          
          Hint 2: Recursion! A reasonable base case is that if your current symbol is a terminal (i.e., has no rewrite rules in the               grammar), then it is non-empty with itself as a witness. 

          Hint 3: all([True,False,True]) = False any([True,True,False]) = True
 
(9) Infinite Mind Reading:  Just as a context-free grammar may be 'empty', it may also have an infinite language. We say that the language for a grammar is infinite if the grammar accepts an infinite number of different strings (each of which is of finite length). Most interesting (and creative!) languages are infinite. For example, the language of this grammar is infinite:

          grammar1 = [ 
          ("S", [ "S", "a" ] ),        # S -> S a
          ("S", [ "b", ]) ,            # S -> b 
          ] 

Because it accepts the strings b, ba, baa, baaa, baaaa, etc. However, this similar grammar does _not_ have an infinite language: 

grammar2 = [ 
          ("S", [ "S", ]),             # S -> S 
          ("S", [ "b", ]) ,            # S -> b 
          ] 

Because it only accepts one string: b. For this problem you will write a procedure cfginfinite(grammar) that returns True (the value True, not the string "True") if the grammar accepts an infinite number of strings (starting from any symbol). Your procedure should return False otherwise. Consider this example: 
          
          grammar3 = [ 
          ("S", [ "Q", ] ),        # S -> Q
          ("Q", [ "b", ]) ,        # Q -> b
          ("Q", [ "R", "a" ]),     # Q -> R a 
          ("R", [ "Q"]),           # R -> Q
          ] 

The language of this grammar is infinite (b, ba, baa, etc.) because it is possible to "loop" or "travel" from Q back to Q, picking up an "a" each time. Since we can travel around the loop as often as we like, we can generate infinite strings. By contrast, in grammar2 it is possible to travel from S to S, but we do not pick up any symbols by doing so. Important Assumption: For this problem, you may assume that for every non-terminal in the grammar, that non-terminal derives at least one non-empty finite string.  (You could just call cfgempty() from before to determine this, so we'll assume it.)  

          Hint 1: Determine if "Q" can be re-written to "x Q y", where either x or y is non-empty. 

          Hint 2: The "Important Assumption" above is more important than it looks: # it means that any rewrite rule "bigger" than ("P",           ["Q"]) adds at least one token. 
          
          Hint 3: While cfginfinite(grammar) is not recursive, you may want to write a helper procedure (that determines if Q can be re-           written to "x Q y" with |x+y| > 0 ) that _is_ recursive. Watch out for infinite loops: keep track of what you have already 
          visited. 
          
(10) Turning Back Time:  For every regular language, there is another regular language that all of the strings in that language, but reversed. For example, if you have a regular language that accepts "Dracula", "Was" and "Here", there is also another regular language that accepts exactly "alucarD", "saW" and "ereH". We can imagine that this "backwards" language is accepted by a "backwards" finite state machine. In this problem you will construct that "backwards" finite state machine. Given a non-deterministic finite state machine, you will write a procedure reverse() that returns a new non-deterministic finite state machine that accepts all of the strings in the first one, but with their letters in reverse order. We will use same the "edges" encoding from class, but we will make the start and accepting state explicit.  For example, the regular expression r"a(?:bx|by)+c" might be encoded like this:

          edges = { (1,'a') : [2],
                    (2,'b') : [3,4],
                    (3,'x') : [5],
                    (4,'y') : [5],
                    (5,'b') : [3,4], 
                    (5,'c') : [6],
                    }          

          accepting = 6 
          start = 1 

For this problem we will restrict attention to non-deterministic finite state machines that have a single start state and a single accepting state. Similarly, we will not consider epsilon transitions. For the example above, since the original NFSM accepts "abxc", the NFSM you produce must accept "cxba". Similarly, since the original accepts "abxbyc", the NFSM you produce must accept "cybxba", and so on. Your procedure "reverse(edges,accepting,start)" should return a tuple (new_edges,new_accepting,new_start) that defines a new non-deterministic finite state machine that accepts every string in the language of the original ... reversed! Vague Hint: Draw a picture, and then draw all the arrows backwards. 

