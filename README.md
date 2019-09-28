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

Hint #1: This problem is trickier than it looks. If you do not keep track of where you have been, your procedure may loop forever on the second example. Before you make a recursive call, add the current state to the list of visited states (and be sure to check the list of visited states elsewhere). 

Hint #2: (Base Case) If the current state is accepting, you can return "" as an accepting string.  

Hint #3: (Recursion) If you have an outgoing edge labeled "a" that goes to a state that accepts on the string "bc" (i.e., the recursive call returns "bc"), then you can return "abc". 

Hint #4: You may want to iterate over all of the edges and only consider those relevant to your current state. "for edge in edges" will iterate over all of the keys in the mapping (i.e., over all of the (state,letter) pairs) -- you'll have to write "edges[edge]" to get the destination list. 

(7) Fsm Optimization:  Lexical analyzers are implemented using finite state machines generated from the regular expressions of token definition rules. The performance of a lexical analyzer can depend on the size of the resulting finite state machine. If the finite state machine will be used over and over again (e.g., to analyze every token on every web page you visit!), we would like it to be as small as possible (e.g., so that your webpages load quickly). However, correctness is more important than speed: even an optimized FSM must always produce the right answer. One way to improve the performance of a finite state machine is to make it smaller by removing unreachable states. If such states are removed, the resulting FSM takes up less memory, which may make it load faster or fit better in a storage-constrained mobile device. For this assignment, you will write a procedure nfsmtrim that removes "dead" states from a non-deterministic finite state machine. A state is (transitively) "dead" if it is non-accepting and only non-accepting states are reachable from it. Such states are also called "trap" states: once entered, there is no escape. In this example FSM for r"a*" ...

          edges = { (1,'a') : [1] ,
                   (1,'b') : [2] ,
                   (2,'b') : [3] ,
                   (3,'b') : [4] } 

          accepting = [ 1 ] 

... states 2, 3 and 4 are "dead": although you can transition from 1->2, 2->3 and 3->4 on "b", you are doomed to rejection if you do so. 

You may assume that the starting state is always state 1. Your procedure nfsmtrim(edges,accepting) should return a tuple (new_edges,new_accepting) corresponding to a FSM that accepts exactly the same strings as the input FSM but that has all dead states removed. 

Hint 1: This problem is tricky. Do not get discouraged. 

Hint 2: Think back to the nfsmaccepts() procedure from the "Reading Machine Minds" homework problem in Unit 1. You are welcome to reuse your code (or the solution we went over) to that problem. 

Hint 3: Gather up all of the states in the input machine. Filter down to just those states that are "live". new_edges will then be just like edges, but including only those transitions that involve live states. new_accepting will be just like accepting, but including only those live states.
