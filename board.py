#!/usr/bin/env python3

from copy import deepcopy
from util import hex_num_to_str
import pickle, os, subprocess, random


def load_lut():
    if os.path.exists("lut.bin"):
        with open("lut.bin", "rb") as f:
            return pickle.load(f)
    else:
        subprocess.run(["python", "lut-gen.py"], check=True)
        with open("lut.bin", "rb") as f:
            return pickle.load(f)


MOVE_TABLE = load_lut()


class Board:
    def __init__(self, tiles):
        self.tiles = tiles  # 4x4 list

    @staticmethod
    def from_tiles(tiles):
        return Board(deepcopy(tiles))

    def move_right(self):
        legal = False
        for x in range(4):
            v = 0
            for y in range(4):
                v = v * 32 + self.tiles[x][y]
            c = MOVE_TABLE[v]
            if c == v:
                continue
            legal = True
            for y in range(3, -1, -1):
                self.tiles[x][y] = c % 32
                c //= 32
        return legal

    def move_left(self):
        legal = False
        for x in range(4):
            v = 0
            for y in range(3, -1, -1):
                v = v * 32 + self.tiles[x][y]
            c = MOVE_TABLE[v]
            if c == v:
                continue
            legal = True
            for y in range(4):
                self.tiles[x][y] = c % 32
                c //= 32
        return legal

    def move_down(self):
        legal = False
        for y in range(4):
            v = 0
            for x in range(4):
                v = v * 32 + self.tiles[x][y]
            c = MOVE_TABLE[v]
            if c == v:
                continue
            legal = True
            for x in range(3, -1, -1):
                self.tiles[x][y] = c % 32
                c //= 32
        return legal

    def move_up(self):
        legal = False
        for y in range(4):
            v = 0
            for x in range(3, -1, -1):
                v = v * 32 + self.tiles[x][y]
            c = MOVE_TABLE[v]
            if c == v:
                continue
            legal = True
            for x in range(4):
                self.tiles[x][y] = c % 32
                c //= 32
        return legal

    def get_random_empty_tile(self):
        empty_tile_positions = []
        for i, row in enumerate(self.tiles):
            for j, val in enumerate(row):
                if val == 0:
                    hex_pos = format(i * 4 + j, "x")  # convert to hex
                    empty_tile_positions.append(hex_pos)
        if not empty_tile_positions:
            return None
        return random.choice(empty_tile_positions)

    def add_random_tile(self):
        square_position = self.get_random_empty_tile()
        if square_position is None:
            return

        tile_value = 1 if random.random() < 0.9 else 2
        dec = int(square_position, 16)
        row = dec // 4
        col = dec % 4
        self.tiles[row][col] = tile_value
        return f"\nadd {square_position} {tile_value}"

    def print_board(self):
        flat_tiles = [cell if cell != 0 else " " for row in self.tiles for cell in row]
        flat_tiles = [
            hex_num_to_str(cell) if isinstance(cell, int) and cell > 9 else cell
            for cell in flat_tiles
        ]

        t = flat_tiles
        print(
            f"""
    ┌───┬───┬───┬───┐
    │ {t[0]} │ {t[1]} │ {t[2]} │ {t[3]} │
    ├───┼───┼───┼───┤
    │ {t[4]} │ {t[5]} │ {t[6]} │ {t[7]} │
    ├───┼───┼───┼───┤
    │ {t[8]} │ {t[9]} │ {t[10]} │ {t[11]} │
    ├───┼───┼───┼───┤
    │ {t[12]} │ {t[13]} │ {t[14]} │ {t[15]} │
    └───┴───┴───┴───┘
        """
        )


def board_from_fen(fen):
    squares = [[0 for _ in range(4)] for _ in range(4)]
    x = 0
    y = 0

    for c in fen:
        if c == "/":
            y += 1
            x = 0
            continue

        if c.isdigit():
            squares[y][x] = int(c)
        elif c in "abcdef":
            squares[y][x] = 10 + ord(c) - ord("a")
        else:
            raise ValueError(f"Invalid character in FEN: {c}")

        x += 1

    return Board(squares)
