#!/usr/bin/env python3.11

import tkinter as tk

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

def main():
    # hitomezashi([1,0,1,0,0,1,0,1]*10, [1,0,0]*20)
    hitomezashi_ints(4, 150)

if __name__ == "__main__":
    main()
