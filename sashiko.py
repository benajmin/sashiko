#!/usr/bin/env python3.11

import tkinter as tk
import functools

STITCH_LENGTH = 10
OFFSET = 10

def stitch(canva, start, num_stitches, coord):
    for i in range(num_stitches):
        if (i % 2) != int(start):
            canva.create_line(*coord(i), *coord(i+1))

def hitomezashi(rows, cols):
    window = tk.Tk()
    canva = tk.Canvas(window, width=STITCH_LENGTH*(len(cols)+2), height=STITCH_LENGTH*(len(rows)+2))

    for i, row in enumerate(rows):
        stitch(canva, row, len(cols), lambda x: (OFFSET + x*STITCH_LENGTH, OFFSET+i*STITCH_LENGTH))

    for i, col in enumerate(cols):
        stitch(canva, col, len(rows), lambda y: (OFFSET + i*STITCH_LENGTH, OFFSET+y*STITCH_LENGTH))

    canva.pack()
    window.mainloop()

def hitomezashi_ints(x, y):
    hitomezashi(f"{x:b}"*10, f"{y:b}"*10)

def hitomezashi_strings(x, y):
    def char_to_binary(c):
        x = ord(c.lower()) - ord('a')
        return f"{x:05b}"

    def string_to_binary(s):
        return ''.join(char_to_binary(c) for c in s)

    hitomezashi(string_to_binary(x), string_to_binary(y))

@functools.cache
def pell(n):
    if n == 0:
        return ""
    if n == 1:
        return "1"

    def bitflip(s):
        return "".join(["1" if x == "0" else "0" for x in s])

    return bitflip(pell(n-1)) + bitflip(pell(n-2))[::-1] + pell(n-1)

def fibonacci_snowflake(n):
    x = pell(n) + pell(n)[::-1]
    hitomezashi(x, x)

def main():
    # hitomezashi([1,0,1,0,0,1,0,1]*10, [1,0,0]*20)
    hitomezashi_ints(4, 150)

if __name__ == "__main__":
    main()
