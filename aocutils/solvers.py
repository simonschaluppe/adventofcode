from collections import deque
from sys import intern


class Puzzle:
    
    pos = "" # internal representation of the puzzle state
    goal = "" 
    
    def __init__(self, pos=None):
        if pos: self.pos = pos
    
    def isgoal(self):
        """are we at the goal state?
        -> True / False
        needs subclass implementation"""
        return repr(self.pos) == repr(self.goal)
        
    def __iter__(self):
        """needs to be implemented by subclass:
        yield possible moves from self"""
        ...
        
    def solve(pos, depthFirst=False, verbose=False):
        i, c = 0, 0
        queue = deque([pos])
        trail = {intern(pos.canonical()): None} # from here where?
        load = queue.append if depthFirst else queue.appendleft
        
        while not pos.isgoal():
            if verbose and not i%1000: 
                print("_"*10, f"{i=:_},{c=:_} remaining Queue: {len(queue)}")
                if i<100: print(pos)
            for candidate in pos:
                candid_rep = candidate.canonical()
                if candid_rep in trail: 
                    c+=1
                    continue # beacuse weve already visited
                trail[intern(candid_rep)] = pos
                load(candidate)
            pos = queue.pop()
            i+=1
            
            
        solution = deque()
        s=0
        while pos: # starts with goal state
            solution.appendleft(pos)
            pos = trail[pos.canonical()] # reverse through the trail
            s+=1
            print("___",s,pos, sep="\n")
        
        print()
        print("steps:", len(list(solution))) 
        
        return len(list(solution))
        
    def __repr__(self):
        """to be implemented by subclass"""
        ...
        
    def canonical(self):
        """checks of give state is isomorphic, meaning
        equivalent to a different state"""
        return repr(self)