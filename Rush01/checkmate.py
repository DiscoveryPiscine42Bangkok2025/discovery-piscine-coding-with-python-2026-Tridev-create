def check():
    map = """\
..K...
.....B
.Q....
......\
    """

    list_map = map.splitlines()
    x, y = 0, 0
    piece = []
    all_pieces = ['P', 'B', 'R', 'Q']

    for i in list_map:
        for j in i:
            if j in all_pieces:
                print(x, y)
                piece.append([y,x, j])
            # print('x', x)
            x += 1
        # print('y', y)
        x = 0
        y += 1

    # print(piece)
    row = len(list_map)
    column = len(list_map[0])

    for i in piece:
        if i[2] == 'B' and 0 <= i[0] < row and 0 < i[1] <= column:
            print(list_map[i[0]+1][i[1]])
            if list_map[i[0]-1][i[1]-1] == 'K' or list_map[i[0]-1][i[1]+1] == 'K':
                return 'good'
            else:
                continue
        else:
            continue
            

ans = check()
print(ans)