#!/usr/bin/env python
# coding: utf-8

import sys
from enum import Enum

filename = sys.argv[1].strip()

labels = {}


class Instructions_A(Enum):
    cv = "01110"
    ce = "01111"
    gv = "10000"
    ge = "10001"

    andve = "00000"
    andvv = "00001"
    orve = "00010"
    orvv = "00011"
    xore = "00100"
    xorv = "00101"

    cdv = "00110"
    civ = "00111"
    rd = "01000"
    ri = "01001"

    sv = "01010"
    sve = "01011"
    rv = "01100"
    rve = "01101"

    stp = "11111"


class Instructions_B(Enum):
    cde = "10011"
    cie = "10100"
    si = "10101"


def normalize_whitespace(string):
    return " ".join(string.strip().lower().split())


def parse_instruction(data, counter):

    if (data[0] in Instructions_A.__members__):
        return parse_a_instruction(data)

    elif (data[0] == "ci"):
        print("Instrucción CI")
        opcode = "10110"
        imm = '{:08b}'.format(int(data[1]))
        reg = convert_register(data[2])

        return opcode + reg + imm

    if (data[0] in Instructions_B.__members__):
        return parse_b_instruction(data)

    elif (data[0][0] == "_"):
        labels[data[0][1:]] = instruction_counter
        return

    elif (data[0] == "j"):
        opcode = "000010"
        addr = labels.get(data[1])
        addr = '{:026b}'.format(int(addr))

        return opcode + addr

    elif (data[0] == "bne"):
        opcode = "000101"
        addr = labels.get(data[3])
        addr = '{:016b}'.format(int(addr))

        return opcode + convert_register(data[1]) + convert_register(data[2]) + addr


def convert_register(register) -> str:
    registers = {
        "r0": "000",
        "r1": "001",
        "r2": "010",
        "r3": "011",
        "r4": "100",
        "r5": "101",
        "r6": "110",
        "r7": "111",
        "v0": "000",
        "v1": "001",
        "v2": "010",
        "v3": "011",
        "v4": "100",
        "v5": "101",
        "v6": "110",
        "v7": "111",
    }

    return registers.get(register)


def parse_a_instruction(data):
    print("Instrucción A")
    print(data)

    opcode = Instructions_A[data[0]].value

    # Stop, ningun parametro
    if len(data) == 1:
        return opcode + "00000000000"

    p1 = convert_register(data[1])
    p2 = convert_register(data[2])

    # Instrucciones de 2 parametros
    if len(data) < 4:
        if data[0] == "gv" or data[0] == "ge":
            return opcode + "000" + p1 + p2 + "00"

        else:
            return opcode + p1 + p2 + "00000"

    p3 = convert_register(data[3])

    return opcode + p1 + p2 + p3 + "00"


def parse_b_instruction(data):
    print("Instrucción B")
    print(data)

    opcode = Instructions_B[data[0]].value

    rd = convert_register(data[1])
    imm = '{:05b}'.format(int(data[2]))
    rs = convert_register(data[3])

    return opcode + rd + imm + rs


with open('instrucciones.mif', 'w+') as out_file:
    with open(filename, 'r') as input_file:
        print("Procesando " + filename)

        lines = [line for line in input_file.readlines() if line.strip()]

        instruction_counter = 0
        for line in lines:
            line = normalize_whitespace(line)
            data = line.split(" ")
            code = parse_instruction(data, instruction_counter)
            print(code)
            if code:
                out_file.write(format(int(code, 2), "x") + "\n")
                instruction_counter += 1
