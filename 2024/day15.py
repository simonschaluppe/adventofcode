from collections import deque
from functools import partial

import deengi
from aocutils.utils import *
from day14 import Robot

warehouse = input_as_nested_list("2024/i15a")
robot_moves = deque("".join([line.strip() for line in open("2024/i15b").readlines()]))


show(warehouse, use_emojis=False)
print(len(robot_moves), len(warehouse), len(warehouse[0]))

dirs = {"^":(-1,0),">":(0,1),"v":(1,0),"<":(0,-1)}

class Wall(Robot):
    pass

class PushyObject(Robot):
    
    
    def move(self, warehouse, direction):
        if direction == (0,0): return direction
        dx,dy = direction
        x,y = self.pos
        target = warehouse[x+dx][y+dy]
        if target == self: return (0,0)
        elif isinstance(target, Wall):
            return (0,0)
        elif isinstance(target, PushyObject):
            direction = target.move(warehouse, direction)
            self.vel= dx,dy = direction
            super().move()
            self.vel=(0,0)
            warehouse[x][y]=" "
            warehouse[x+dx][y+dy]=self
            return direction
        elif target in [None, " ","."]:
            self.vel = direction
            super().move()
            self.vel=(0,0)
            warehouse[x][y]=" "
            warehouse[x+dx][y+dy]=self
            return direction
        
        else:
            raise ValueError(target)
            
def gps(warehouse):
    gpssum = 0
    for x, row in enumerate(warehouse):
        for y, item in enumerate(row):
            if isinstance(item, PushyObject) and item != robot:
                gpssum += x*100+y
    print(gpssum)
    return gpssum

if __name__ == "__main__":
        
    vis = deengi.Engine()
    vis.show_grid(50, (0,0), labels=10)
    vis.setup_camera(zoom=0.1, pos=(25,25))
    vis.paused = True
        
    for x, row in enumerate(warehouse):
        for y, item in enumerate(row):
            if item == "O":
                box = PushyObject((x,y*2), (0,0), color=(130,80,60))
                warehouse[x][y] = box
                vis.add_to_layer("main", box.visual)
            if item == "#":
                wall = Wall((x,y),(0,0), color=(40,95,150))
                warehouse[x][y] = wall
                vis.add_to_layer("main", wall.visual)
            if item == "@":
                robot = PushyObject((x,y), (0,0), color=(150,200,255))
                warehouse[x][y] = robot
                vis.add_to_layer("main", robot.visual)
            if item == ".":
                warehouse[x][y] == " "
                
    def update(vis):
        if len(robot_moves)==0:
            vis.paused = True
            print(gps(warehouse))
            vis.show_debug(partial(gps, warehouse))
            return
        instruction = robot_moves.popleft()
        try:
        
            robot.move(warehouse, dirs[instruction])
        except:
            show(warehouse, use_emojis=True, legend={robot:"@"})
            print(instruction)
            vis.paused = True
            return

    vis.update_callbacks.append(partial(update, vis))
    # vis.show_debug(lambda: f"Next move {dirs[robot_moves[0]]}")
    # vis.show_debug(lambda: f"MOves left {len(robot_moves)}")
    vis.run()