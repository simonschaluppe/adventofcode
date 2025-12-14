
from operator import mul
import random
from time import sleep
import deengi
import deengi.renderables

class Robot:
    def __init__(self, pos, vel, space=(103,101), color=None, size=(1,1)):
        self.pos = pos
        self.vel = vel
        self.speed = sum(vel)
        self.space = space
        self.color = color or (random.randint(0,40), random.randint(120,180),random.randint(0,30))
        self.visual = deengi.renderables.Tile(self.pos, size=size, color=self.color)
    
    def move(self):
        x,y = self.pos
        maxx, maxy = self.space
        dx, dy = self.vel
        self.pos = ((x+dx)%maxx, (y+dy)%maxy)
        self.visual.pos = self.pos
        
    def __repr__(self):
        return f"🤖@{self.pos} {self.vel}"
        
        
if __name__ =="__main__":
    robots = []
    moves =0
    inc = 1
    delay = 0
    def move():
        global moves
        global delay
        global inc
        for robot in robots:
            robot.move()
            
        moves+=inc
        sleep(delay)
            
    def nmoves(n=100, s =0):
        for i in range(n):
            move()
            sleep(s)
            
    def reverse():
        for r in robots:
            vx,vy = r.vel
            r.vel = -vx,-vy
        global inc
        inc = -inc
        
    vis = deengi.Engine(screen_size=(1000,1000), debug=True)

    import re
    with open("2024/i14") as f:
        for line in f.readlines():
            posy,posx,vy,vx = list(map(int,re.findall("(-*\d+)", line)))
            robot = Robot((posx,posy), (vx,vy))
            vis.add_tooltip(robot.visual, repr(robot))
            vis.add_to_layer("main", robot.visual)
            robots.append(robot)
    nmoves(100)
    quadrants = {"TL":0,"TR":0,"BL":0,"BR":0}
    for robot in robots:
        px,py = robot.pos
        print(px,py, robot)
        if px < 51: t = "T"
        elif px>51: t="B"
        else: continue
        if py <50: l = "L"
        elif py >50: l= "R"
        else: continue
        quadrants[t+l] += 1
        
    safety_rating = 1
    for n in quadrants.values():
        safety_rating *= n
        
    print(safety_rating)

    nmoves(8170)
    vis.paused = True

    vis.show_debug(lambda: repr(moves))
    vis.show_debug(lambda: repr(quadrants))
    vis.show_debug(lambda: repr(safety_rating))
    vis.bind_key("m", move)
    vis.bind_key("h", nmoves)
    vis.bind_key("r", reverse)
    vis.setup_camera(pos=(50,50), zoom=(0.09,0.09), rotation=90)
    vis.show_background((10,20,50))
    vis.show_grid((103,101), (0,0), color=("red", "blue"), labels=10)
    vis.update_callbacks.append(move)
    vis.run()

    import itertools