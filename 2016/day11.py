from aocutils.solvers import Puzzle
from itertools import chain, combinations, zip_longest

class FloorPuzzle(Puzzle):
    goal = [['**','cG','cM','kG','kM','pG','pM','rG','rM','uG','uM'],[],[],[]]

    pos = [[],['cM','kM','rM','uM'],['cG','kG','rG','uG'],['**','pG','pM']]


    def __repr__(self):
        return "\n".join([f"F{4-i}:"+",".join(sorted([i for i in line])) for i, line in enumerate(self.pos)])
    
    def is_valid(self, floor_items):
        microchips = [item[0] for item in floor_items if item[1:]=="M"]
        generators = set(item[0] for item in floor_items if item[1:]=="G")
        return not generators or all([element in generators for element in microchips]) 
    
    def cfn(self):
        """current floor number"""
        for i, floor in enumerate(self.pos):
            if "**" in floor: return i
            
    def above_below(self, current_floor_id):
        if current_floor_id == 0: return [1]
        elif 1 <= current_floor_id <=2: return [0,1,2,3][current_floor_id+1::-2]
        else: return [2]
           
    def possible_takes(self, items):
        return [*combinations(items, 2), *combinations(items,1)]    
        # interlaced = list(chain.from_iterable(
        #         filter(None, pair)  # Remove `None` values from uneven zipping
        #         for pair in zip_longest(combinations(items, 1), combinations(items, 2))
        #         ))
        # return interlaced
    
    def items_on(self, n):
        return set(self.pos[n]) - {"**"}
    
    def transfer(self, what, from_floorn:str, to_floorn):
        floors = [floor.copy() for floor in self.pos]
        floors[from_floorn]= sorted([item for item in floors[from_floorn] if not item in what])
        floors[to_floorn] = sorted(floors[to_floorn] + list(what))
        return floors
    
    def __iter__(self):

        current_floor = self.items_on(self.cfn())
        for combination in self.possible_takes(current_floor) :
            elevator_content = set([*combination, "**"])
            
            # print("can take", 4-self.cfn(), self.is_valid(current_floor - elevator_content), *elevator_content)
            if not self.is_valid(current_floor - elevator_content): 
                continue
            for new_fn in self.above_below(self.cfn()):
                # print("to", 4-new_fn, end=" ")
                new_floor = self.items_on(new_fn)
                
                # print(self.is_valid(new_floor | elevator_content), *new_floor)
                if not self.is_valid(new_floor | elevator_content): continue
                
                # print("adding", *elevator_content, "to floor", 4-new_fn, ":", *new_floor)
                p=self.transfer(elevator_content, self.cfn(), new_fn)
                # input(f"continue to {p}")
                valid = type(self)(pos=p) # not FloorPuzzle() cause of subclassing
                yield valid

    

class SimplePuzzle(FloorPuzzle):
    pos = [[],["lG"],["hG"],["**","hM","lM"]]
    goal = [["**","hG","hM","lG","lM"],[],[],[]]
    

simple = SimplePuzzle()
print(simple.goal)
simple.solve(verbose=True, depthFirst=False)


class HardPuzzle(FloorPuzzle):
    pos = [[],['cM','kM','rM','uM'],['cG','kG','rG','uG'],['**','dG','dM','eG','eM','pG','pM']]
    goal = [['**','cG','cM','dG','dM','eG','eM','kG','kM','pG','pM','rG','rM','uG','uM'],[],[],[]]

if input("start real solve?"):
    real_one = FloorPuzzle([[],['cM','kM','rM','uM'],['cG','kG','rG','uG'],['**','pG','pM']])#
    real_two = HardPuzzle()
    real_two.solve(verbose=True, depthFirst=False)
