import operator
import copy
import sys
def day5_2():
    with open("day5 - input.txt") as input:
        states = [num.strip() for num in input.read().split(',')]
    states = list(map(int, states))

    # states = [3,9,8,9,10,9,4,9,99,-1,8]
    # states = [3,9,7,9,10,9,4,9,99,-1,8]
    # states = [3,3,1108,-1,8,3,4,3,99]
    # states = [3,3,1107,-1,8,3,4,3,99]
    
    # states = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
    # states = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]

    # states = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

    ops = {
        "1": operator.add,
        "2": operator.mul,
        "7": operator.lt,
        "8": operator.eq
    }
    next_instr = [0, 4, 4, 2, 2, 0, 0, 4, 4]

    opcode_add = "1"
    opcode_mul = "2"
    opcode_save = "3"
    opcode_out = "4"
    opcode_jump_true = "5"
    opcode_jump_false = "6"
    opcode_less_than = "7"
    opcode_equals = "8"
    opcode_halt = 99
    code_input = 5

    codes = copy.copy(states)

    i = 0
    while codes[i] != opcode_halt:
        instr = f"{codes[i]:05}"
        op = instr[-1]

        try:
            parameter_1 = codes[codes[i+1]] if instr[-3] == "0" else codes[i+1]
            parameter_2 = codes[codes[i+2]] if instr[-4] == "0" else codes[i+2]
        except IndexError: pass
        if op == opcode_add or op == opcode_mul:
            op_func = ops[op]
            codes[codes[i+3]] = op_func(parameter_1, parameter_2)
        elif op == opcode_save:
            codes[codes[i+1]] = code_input
        elif op == opcode_out:
            address = i if instr[-3] == "1" else codes[i+1]
            print("value at address {}: {}".format(address, parameter_1))
        elif instr[4] == opcode_jump_true or op == opcode_jump_false:
            jump = True if op == opcode_jump_true else False
            i = parameter_2 if bool(parameter_1) == jump else i+3
        elif instr[4] == opcode_less_than or op == opcode_equals:
            op_func = ops[op]
            codes[codes[i+3]] = 1 if op_func(parameter_1, parameter_2) else 0
        else:
            print("something went wrong :(")
            sys.exit()
        i += next_instr[int(op)]
day5_2()