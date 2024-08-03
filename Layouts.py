
# Assumptions:-
# S = Station
# T = Rail + Train
# R = Rail
# . = Empty
# Train moves clockwise
# Train always faces in the early stage, i.e., if we see layouts1, the train is actually facing west instead of north
# Only one train is there

layout1 = [['.','.','.','.','S','S','S','.','.'],
           ['.','.','.','.','S','S','S','.','.'],
           ['.','.','.','R','R','R','R','.','.'],
           ['.','.','.','R','.','.','R','.','.'],
           ['.','.','.','R','.','.','R','.','.'],
           ['.','.','.','R','.','.','R','.','.'],
           ['.','.','.','R','.','.','R','S','S'],
           ['.','.','.','T','.','.','R','S','S'],
           ['.','.','S','S','R','R','R','.','.'],
           ['.','.','S','S','.','.','.','.','.'],
           ['.','.','.','.','.','.','.','.','.'],
           ['.','.','.','.','.','.','.','.','.']]
layout1f = "WEST"