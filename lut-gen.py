#!/usr/bin/env python3

import pickle


def move_table():
    moves = [0] * (1 << 20)  # 2^20 = 1,048,576

    for i in range(1 << 20):
        # Decode the 20-bit number into 4 tiles (each 5 bits)
        line = [
            (i >> 0) & 0x1F,
            (i >> 5) & 0x1F,
            (i >> 10) & 0x1F,
            (i >> 15) & 0x1F,
        ]

        # Simulate move left logic
        result = [0, 0, 0, 0]
        idx = 0

        for j in range(4):
            if line[j] == 0:
                continue

            if result[idx] == 0:
                result[idx] = line[j]
            elif result[idx] == line[j]:
                result[idx] += 1  # Merge tiles
                idx += 1
            else:
                idx += 1
                result[idx] = line[j]

        # Encode the result back into 20-bit format
        code = 0
        for j in range(4):
            code |= result[j] << (j * 5)

        moves[i] = code

    return moves


pickle.dump(move_table(), open("lut.bin", "w+b"))
