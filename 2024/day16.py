import deengi.renderables
import aocutils.utils as aoc

import deengi

vis = deengi.Engine()

maze = aoc.input_as_nested_list("2024/i16")



for i, row in enumerate(maze):
    for j, t in enumerate(row):
        if t =="#":
            tile = deengi.renderables.Tile((i,j), size=(1,1), color="darkblue")
            vis.add_to_layer("main", tile)
        elif t == "S":
            start = deengi.renderables.Tile((i,j), size=(1,1), color="green")
            vis.add_to_layer("main", start) 
        elif t == "E":
            end = deengi.renderables.Tile((i,j), size=(1,1), color="red")
            vis.add_to_layer("main", end) 

l = len(maze)
vis.setup_camera(pos=(l//2,l//2), zoom=(0.09,0.09), rotation=90)

vis.run()
