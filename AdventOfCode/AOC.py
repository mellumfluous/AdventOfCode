import itertools
import copy
import re
from collections import Counter

# 3331523
def day1_1():
    sum = 0
    with open("day1 - input.txt") as input:
        modules = input.read().split()
    # Modules is a list of strings
    for module in modules:
        sum += (int(module) // 3) - 2
    print(str(sum))
# day1_1()
#======================================

# 4994396
def day1_2():
    sum = 0
    with open("day1 - input.txt") as input:
        modules = input.read().split()
    # Modules is a list of strings
    for module in modules:
        sum +=day1_2_rec(int(module)//3-2)
    print(str(sum))

def day1_2_rec(num):
    if ((num // 3) - 2) <= 0:
        return num
    else:
        return num + day1_2_rec(num // 3 - 2) 
# day1_2()

#==============================================================================

# 5305097
def day2_1():
    with open("day2 - input.txt") as input:
        states = [num.strip() for num in input.read().split(',')]
    states = list(map(int, states))
    states[1] = 12
    states[2] = 2
    # states = [1,0,0,0,99]
    # states = [2,3,0,3,99]
    # states = [2,4,4,5,99,0]
    # states = [1,1,1,4,99,5,6,0,99]
    i = 0
    while True:
        if states[i] == 1:
            states[states[i+3]] = states[states[i+1]] + states[states[i+2]]
            i += 4
        elif states[i] == 2:
            states[states[i+3]] = states[states[i+1]] * states[states[i+2]]
            i += 4
        elif states[i] == 99:
            break
        else:
            i += 1
    # print("finished state: {}".format(states))
    print("output: " + str(states[0]))
# day2_1()

#======================================

# Noun: 49, Verb: 25
# Answer: 4925
def day2_2():
    with open("day2 - input.txt") as input:
        states = [num.strip() for num in input.read().split(',')]
    states = list(map(int, states))
    states[1] = 12
    states[2] = 2

    for x,y in itertools.product(range(100), range(100)):
        codes = copy.copy(states)
        codes[1] = x
        codes[2] = y
    
        i = 0
        while codes[i] != 99:
            if codes[i] == 1:
                codes[codes[i+3]] = codes[codes[i+1]] + codes[codes[i+2]]
            elif codes[i] == 2:
                codes[codes[i+3]] = codes[codes[i+1]] * codes[codes[i+2]]
            i += 4

        if codes[0] == 19690720:
            print("noun: {}, verb: {}".format(x,y))
            print("answer: {}".format((100*x)+y))
            break
# day2_2()

#==============================================================================

#529
def day3_1():
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
    manhatten_distance = []

    pairx = 0
    pairy = 0
    for each in wire_0:
        path = re.search(r'(\w)(.*)', each)
        direction = path.group(1)
        magnitude = path.group(2)
        oldx = pairx
        oldy = pairy
        if direction == "R":
            pairx += int(magnitude)
            wire_0_hor.append([(oldx, oldy), (pairx, oldy)])
        elif direction == "L":
            pairx -= int(magnitude)
            wire_0_hor.append([(oldx, oldy), (pairx, oldy)])
        elif direction == "U":
            pairy += int(magnitude)
            wire_0_ver.append([(oldx, oldy), (oldx, pairy)])
        elif direction == "D":
            pairy -= int(magnitude)
            wire_0_ver.append([(oldx, oldy), (oldx, pairy)])
    pairx = 0
    pairy = 0
    for each in wire_1:
        path = re.search(r'(\w)(.*)', each)
        direction = path.group(1)
        magnitude = path.group(2)
        oldx = pairx
        oldy = pairy
        if direction == "R":
            pairx += int(magnitude)
            wire_1_hor.append([(oldx, oldy), (pairx, oldy)])
        elif direction == "L":
            pairx -= int(magnitude)
            wire_1_hor.append([(oldx, oldy), (pairx, oldy)])
        elif direction == "U":
            pairy += int(magnitude)
            wire_1_ver.append([(oldx, oldy), (oldx, pairy)])
        elif direction == "D":
            pairy -= int(magnitude)
            wire_1_ver.append([(oldx, oldy), (oldx, pairy)])

    for hor in wire_0_hor:
        minx = min(hor[0][0], hor[1][0])
        maxx = max(hor[0][0], hor[1][0])
        for ver in wire_1_ver:
            miny = min(ver[0][1], ver[1][1])
            maxy = max(ver[0][1], ver[1][1])
            x = ver[0][0]
            y = hor[0][1]
            if minx <= x and x <= maxx and miny <= y and y <= maxy:
                intersections.append((ver[0][0], hor[0][1]))
                manhatten_distance.append(abs(ver[0][0])+abs(hor[0][1]))
    for ver in wire_0_ver:
        miny = min(ver[0][1], ver[1][1])
        maxy = max(ver[0][1], ver[1][1])
        for hor in wire_1_hor:
            minx = min(hor[0][0], hor[1][0])
            maxx = max(hor[0][0], hor[1][0])
            x = ver[0][0]
            y = hor[0][1]
            if minx <= x and x <= maxx and miny <= y and y <= maxy:
                intersections.append((ver[0][0], hor[0][1]))
                manhatten_distance.append(abs(ver[0][0])+abs(hor[0][1]))
    intersections.pop(0)
    manhatten_distance.pop(0)
    print("answer is: "+str(min(manhatten_distance)))
# day3_1()

#======================================

# 20386
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

    pairx = 0
    pairy = 0
    total_mag = 0
    # Go through wire 0 and add both the old and new xy coordinates along with
    # the total previous magnitude to its respective horizontal and vertical move lists
    for each in wire_0:
        path = re.search(r'(\w)(.*)', each)
        direction = path.group(1)
        magnitude = int(path.group(2))
        oldx = pairx
        oldy = pairy
        if direction == "R":
            pairx += magnitude
            wire_0_hor.append([(oldx, oldy), (pairx, oldy), total_mag])
        elif direction == "L":
            pairx -= magnitude
            wire_0_hor.append([(oldx, oldy), (pairx, oldy), total_mag])
        elif direction == "U":
            pairy += magnitude
            wire_0_ver.append([(oldx, oldy), (oldx, pairy), total_mag])
        elif direction == "D":
            pairy -= magnitude
            wire_0_ver.append([(oldx, oldy), (oldx, pairy), total_mag])
        total_mag +=magnitude
    pairx = 0
    pairy = 0
    total_mag = 0

    # Go through wire 0 and add both the old and new xy coordinates along with
    # the total previous magnitude to its respective horizontal and vertical move lists
    for each in wire_1:
        path = re.search(r'(\w)(.*)', each)
        direction = path.group(1)
        magnitude = int(path.group(2))
        oldx = pairx
        oldy = pairy
        if direction == "R":
            pairx += magnitude
            wire_1_hor.append([(oldx, oldy), (pairx, oldy), total_mag])
        elif direction == "L":
            pairx -= magnitude
            wire_1_hor.append([(oldx, oldy), (pairx, oldy), total_mag])
        elif direction == "U":
            pairy += magnitude
            wire_1_ver.append([(oldx, oldy), (oldx, pairy), total_mag])
        elif direction == "D":
            pairy -= magnitude
            wire_1_ver.append([(oldx, oldy), (oldx, pairy), total_mag])
        total_mag +=magnitude

    # Go through wire 0's horizontal list to find the wire 1's horizontal intersections
    # Append the intersection coordinate and the total magnitude to get there
    for hor in wire_0_hor:
        minx = min(hor[0][0], hor[1][0])
        maxx = max(hor[0][0], hor[1][0])
        for ver in wire_1_ver:
            miny = min(ver[0][1], ver[1][1])
            maxy = max(ver[0][1], ver[1][1])
            x = ver[0][0]
            y = hor[0][1]
            if minx <= x and x <= maxx and miny <= y and y <= maxy:
                w0_mag = hor[2]+abs(hor[0][0]-x)
                w1_mag = ver[2]+abs(ver[0][1]-y)
                tm = w0_mag + w1_mag
                intersections.append((ver[0][0], hor[0][1], tm))

    # Go through wire 0's vertical list to find the wire 1's horizontal intersections
    # Append the intersection coordinate and the total magnitude to get there
    for ver in wire_0_ver:
        miny = min(ver[0][1], ver[1][1])
        maxy = max(ver[0][1], ver[1][1])
        for hor in wire_1_hor:
            minx = min(hor[0][0], hor[1][0])
            maxx = max(hor[0][0], hor[1][0])
            x = ver[0][0]
            y = hor[0][1]
            if minx <= x and x <= maxx and miny <= y and y <= maxy:
                w0_mag = hor[2]+abs(hor[0][0]-x)
                w1_mag = ver[2]+abs(ver[0][1]-y)
                tm = w0_mag + w1_mag
                intersections.append((ver[0][0], hor[0][1], tm))

    intersections.pop(0)
    min_steps = intersections[0][2]
    for each in intersections:
        if each[2] < min_steps:
            min_steps = each[2]
    print("min amount of steps is: {}".format(min_steps))
# day3_2()

#==============================================================================

# guess 546 is too high
# guess 334 is too low
# guess 494 is too low
# 544

def day4_1():

    def viable(password):
        prev_digit = password[0]
        for digit in password:
            if digit < prev_digit:
                return False
            prev_digit = digit

        match = re.search(r'(\d)\1', password)
        # The commented out line didn't work as I thought it would. 
        # If search found nothing, it returns a None. type(match) returns NoneType
        # if type(match) == None:
        if match == None:
            return False
        return True


    count = 0
    for num in range(356261, 846303):
        if viable(str(num)):
            count += 1
    print(count)

# day4_1()

def reddit_day_4_sanjithpk():
    low = 356261
    high = 846303
    a1 = []
    a2 = []

    t = low
    while True:
        d = list(str(t))
        
        for i in range(5):
            if d[i] > d[i+1]:
                d[i + 1:6] = d[i] * (5-i)
                t = int("".join(d))
                d = list(str(t))
                break
        
        if t > high:
            break
        if(collections.Counter(str(t)).most_common(1)[0][1] > 1):
            a1.append(t)
            
        if(2 in collections.Counter(str(t)).values()):
            a2.append(t)
        t += 1
        
    print(len(a1), len(a2))
# reddit_day_4_sanjithpk()

def reddit_day_4_dvrzero():
    potentials = []
    for i in range(356666, 800000):

    # dvrzero's numbers
        potentials.append(str(i))

    passedfirst = []
    for item in potentials:
        if list(item) == sorted(item):
            passedfirst.append(item)
                    
    passedsecond = []
    for number in passedfirst:
        
        for digit in number:
                count = number.count(digit)
                # if count >= 2: #change this to '==' for part 2 (srsly)
                if count == 2: #change this to '==' for part 2 (srsly)
                    passedsecond.append(number)               
                    break  

    print(len(passedsecond))
# reddit_day_4_dvrzero()

# 964 is too high
# def in_order(num_as_str):
#     if list(num_as_str) == sorted(num_as_str):
#         return True

def day4_2():
    sum = 0
    for num in range(356261, 846303):
        str_num = str(num)
        # if str_num == "".join(sorted(str_num)) and 2 in Counter(str_num).values():
            # sum += 1

        if str_num == "".join(sorted(str_num)):
            for digit in str_num:
                if str_num.count(digit) == 2:
                    sum += 1
                    break
    print(sum)
# day4_2()

def day5_1():