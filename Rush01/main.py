from check_mate import checkmate

def main():

    print("Test 1: ")
    board1 = """\
..K...
......
.Q....
......\
"""

#     board1 = """\
# ..K...
# ......
# ...B..
# ......\
# """
    print(board1)
    checkmate(board1)
    print()

    print("Test 2: ")
    board2 = """\
R...
.K..
..P.
....\
"""
    print(board2)
    checkmate(board2)
    print()

    print("Test 3: ")
    board3 = """\
B...
....
....
...K\
"""

#     board3 = """\
# Q...
# ....
# ....
# ...K\
# """


    print(board3)
    checkmate(board3)
    print()

    print("Test 4: ")
    board4 = """\
K..
.P.
\
"""
    print(board4)
    checkmate(board4)
    print()

    board5 = """\
.R..
....
....
.K..\
"""


    print(board5)
    checkmate(board5)
    print()

if __name__ == "__main__":
    main()