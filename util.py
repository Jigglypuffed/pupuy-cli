#!/usr/bin/env python3

def hex_num_to_str(n):
    return {
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }.get(n, str(n))
