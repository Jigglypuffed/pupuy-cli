#!/usr/bin/env python3

import subprocess
import sys
from board import Board, board_from_fen


if len(sys.argv) != 2:
    print("Missing engine executable")
    exit()

engine = subprocess.Popen(
    sys.argv[1],
    stdout=subprocess.PIPE,
    stdin=subprocess.PIPE,
    universal_newlines=True,
)
assert engine.stdin and engine.stdout is not None

print(engine.stdout.readline())
board = Board([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
engine.stdin.write("position 0000/0000/0000/0000\n")
engine.stdin.flush()
while True:
    cmds = input().strip().split(" ")
    match cmds[0]:
        case "exit":
            exit()

        case "move":
            match cmds[1]:
                case "l":
                    board.move_left()
                case "r":
                    board.move_right()
                case "u":
                    board.move_up()
                case "d":
                    board.move_down()
            engine.stdin.write(cmds[0] + cmds[1] + "\n")
            engine.stdin.flush()

        case "add":
            if cmds[1] == "random":
                command_str = board.add_random_tile()
                if command_str is None:
                    pass
                else:
                    engine.stdin.write(command_str + "\n")
                    engine.stdin.flush()
            else:
                row = int(cmds[1]) // 4
                col = int(cmds[1]) % 4
                board.tiles[row][col] = int(cmds[2], 16)
                engine.stdin.write(cmds[0] + cmds[1] + cmds[2] + "\n")
                engine.stdin.flush()

        case "position":
            board = board_from_fen(cmds[1])

        case "show":
            board.print_board()

        case "go":
            time = int(cmds[2])
            engine.stdin.write("go time %d\n" % time)
            engine.stdin.flush()

            responded = False
            while responded is False:
                tokens = engine.stdout.readline().strip().split(" ")
                if tokens[0] == "bestmove":
                    responded = True
                    print("bestmove %s" % tokens[1])
        case _:
            pass
