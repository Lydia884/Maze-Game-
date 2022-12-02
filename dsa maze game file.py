# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 12:48:34 2022

@author: SADHAN
"""

from tkinter import *
from random import randint


cell_size = 12 #pixels
ms = 50 # rows and columns
visited_cells = []
walls = []
revisited_cells = []

# creates a list with 50 x 50 "w" items
map = [['w' for _ in range(ms)] for _ in range(ms)]



def create():
    "Create a rectangle with draw function (below) with random color"
    for row in range(ms):
        for col in range(ms):
            if map[row][col] == 'P':
                color = 'White'
            elif map[row][col] == 'w':
                color = 'black'
            draw(row, col, color)


def draw(row, col, color):
    x1 = col * cell_size
    y1 = row * cell_size
    x2 = x1 + cell_size
    y2 = y1 + cell_size
    ffs.create_rectangle(x1, y1, x2, y2, fill=color)


def check_neighbours(ccr, ccc):
    neighbours = [[
        ccr,
        ccc - 1,
        ccr - 1,
        ccc - 2,
        ccr,
        ccc - 2,
        ccr + 1,
        ccc - 2,
        ccr - 1,
        ccc - 1,
        ccr + 1,
        ccc - 1
    ],

# left
                [ccr, ccc + 1, ccr - 1, ccc + 2, ccr, ccc + 2, ccr + 1, ccc + 2, ccr - 1, ccc + 1, ccr + 1, ccc + 1], #right
                [ccr - 1, ccc, ccr - 2, ccc - 1, ccr - 2, ccc, ccr - 2, ccc + 1, ccr - 1, ccc - 1, ccr - 1, ccc + 1], #top
                [ccr + 1, ccc, ccr + 2, ccc - 1, ccr + 2, ccc, ccr + 2, ccc + 1, ccr + 1, ccc-1, ccr + 1, ccc + 1]] #bottom
    visitable_neighbours = []           
    for i in neighbours:                                                                        #find neighbours to visit
        if i[0] > 0 and i[0] < (ms-1) and i[1] > 0 and i[1] < (ms-1):
            if map[i[2]][i[3]] == 'P' or map[i[4]][i[5]] == 'P' or map[i[6]][i[7]] == 'P' or map[i[8]][i[9]] == 'P' or map[i[10]][i[11]] == 'P':
                walls.append(i[0:2])                                                                                               
            else:
                visitable_neighbours.append(i[0:2])
    return visitable_neighbours

#StartingPoint

# starting color of row
scr = randint(1, ms)
# starting random column
scc = randint(1, ms)
start_color = 'Green'
# memorize row and column of the starting rectangle
# current color row and current color column
ccr, ccc = scr, scc
x1 = ccr * 12
y1 = ccc * 12
print(scr, scc)
print(ccr, ccc)

map[ccr][ccc] = 'P'
loop = 1
while loop:
    visitable_neighbours = check_neighbours(ccr, ccc)
    if len(visitable_neighbours) != 0:
        d = randint(1, len(visitable_neighbours))-1
        ncr, ncc = visitable_neighbours[d]
        map[ncr][ncc] = 'P'
        visited_cells.append([ncr, ncc])
        ccr, ccc = ncr, ncc
    if len(visitable_neighbours) == 0:
        try:
            ccr, ccc = visited_cells.pop()
            revisited_cells.append([ccr, ccc])

        except:
            loop = 0


window = Tk()
window.title('Maze')
canvas_side = ms*cell_size
ffs = Canvas(window, width = canvas_side, height = canvas_side, bg = 'grey')
ffs.pack()


create()
y1 = scr * cell_size 
x1 = scc * cell_size
draw(scr, scc, start_color)
e = randint(1, len(revisited_cells))-1
ecr = revisited_cells[e][0]
ecc = revisited_cells[e][1]
end_color = 'red'
draw(ecr, ecc, end_color)
# print(revisited_cells)


# creating the 
def draw_rect():
    ffs.create_rectangle((x1, y1, x1 + 12, y1 + 12), fill="green")

def del_rect():
    ffs.create_rectangle((x1, y1, x1 + 12, y1 + 12), fill="white")

def move(event):
    global x1, y1
    # print(event.char)
    del_rect()
    col = w = x1//cell_size
    row = h = y1//cell_size
    print("before", map[row][col])
    if event.char == "a":
        if map[row][col - 1] == "P":
            x1 -= cell_size
    elif event.char == "d":
        if map[row][col + 1] == "P":
            x1 += cell_size
    elif event.char == "w":
        if map[row - 1][col] == "P":
            y1 -= cell_size
    elif event.char == "s":
        if map[row + 1][col] == "P":
            y1 += cell_size

    draw_rect()
    col = w = x1//cell_size
    row = h = y1//cell_size
    print(w, h)
    print("after", map[row][col])


window.bind("<Key>", move)

# recording the positions in the output
window.mainloop()
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
