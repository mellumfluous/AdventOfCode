import re

def day3_2():
    with open("day3 - input.txt") as input:
    # with open("day3 - input1.txt") as input:
    # with open("day3 - input2.txt") as input:
        wires = [num.strip() for num in input.read().split()]
    wire_0 = wires[0].split(",")
    wire_1 = wires[1].split(",")
    wire_0_hor = []
    wire_0_ver = []
    wire_1_hor = []
    wire_1_ver = []
    intersections = []

    # Go through the wire and add both the old and new xy coordinates along with
    # the total previous magnitude to its respective horizontal and vertical move lists
    def rldu(wire, wire_hor, wire_ver, pairx, pairy, total_mag):
        for each in wire:
            path = re.search(r'(\w)(.*)', each)
            direction = path.group(1)
            magnitude = int(path.group(2))
            oldx = pairx
            oldy = pairy
            if direction == "R":
                pairx += magnitude
                wire_hor.append([(oldx, oldy), (pairx, oldy), total_mag])
            elif direction == "L":
                pairx -= magnitude
                wire_hor.append([(oldx, oldy), (pairx, oldy), total_mag])
            elif direction == "U":
                pairy += magnitude
                wire_ver.append([(oldx, oldy), (oldx, pairy), total_mag])
            elif direction == "D":
                pairy -= magnitude
                wire_ver.append([(oldx, oldy), (oldx, pairy), total_mag])
            total_mag +=magnitude

    # Go through wire 0's horizontal list to find the wire 1's horizontal intersections
    # Append the intersection coordinate and the total magnitude to get there
    def find_intersections( wire_x_hor, wire_y_ver, intersections):
        for hor in wire_x_hor:
            minx = min(hor[0][0], hor[1][0])
            maxx = max(hor[0][0], hor[1][0])
            for ver in wire_y_ver:
                miny = min(ver[0][1], ver[1][1])
                maxy = max(ver[0][1], ver[1][1])
                x = ver[0][0]
                y = hor[0][1]
                if minx <= x and x <= maxx and miny <= y and y <= maxy:
                    w0_mag = hor[2]+abs(hor[0][0]-x)
                    w1_mag = ver[2]+abs(ver[0][1]-y)
                    tm = w0_mag + w1_mag
                    intersections.append((ver[0][0], hor[0][1], tm))

    rldu(wire_0, wire_0_hor, wire_0_ver, 0, 0, 0)
    rldu(wire_1, wire_1_hor, wire_1_ver, 0, 0, 0)
    find_intersections(wire_0_hor, wire_1_ver, intersections)
    find_intersections(wire_1_hor, wire_0_ver, intersections)

    # The first intersection is (0, 0), which isn't what we want
    intersections.pop(0)
    min_steps = intersections[0][2]
    for each in intersections:
        if each[2] < min_steps:
            min_steps = each[2]
    print("min amount of steps is: {}".format(min_steps))
day3_2()

# Really cool implementation by redditor jadenPete

# !/usr/bin/env python3

# with open("day3.txt", "r") as file:
# 	def crawl_wire():
# 		loc = [0, 0]
# 		steps = 0

# 		for move in file.readline().split(","):
# 			delta = {"L": (0, -1), "R": (0, 1), "U": (1, 1), "D": (1, -1)}[move[0]]

# 			for _ in range(int(move[1:])):
# 				loc[delta[0]] += delta[1]
# 				steps += 1

# 				yield tuple(loc), steps

# 	visited = {}

# 	for loc, steps in crawl_wire():
# 		if loc not in visited:
# 			visited[loc] = steps

# 	print(min(steps + visited[loc] for loc, steps in crawl_wire() if loc in visited))