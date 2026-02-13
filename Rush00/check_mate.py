def checkmate(board):

    # แปลงเป็น Array
    map = board.splitlines()
    
    # print('Map', map)
    if not map:
        print("Fail")
        return
    
    #เช็คว่า map บั๊กอ่ะเปล่า
    for i in range(len(map)):
        if len(map) != len(map[i]):
            print('Fail')
            return
        # return False    

    # หาตำแหน่ง K นะจั๊ฟฟ
    k_row, k_col = -1, -1
    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c] == 'K':
                k_row = r
                k_col = c
                # print('kk_roww', k_row)
                # print(k_col)
                break
        if k_row != -1: 
            break

    if k_row == -1:
        print("Fail")
        return

    #เช็คทิศทาง แต่ละเคส เช่น Q ไปยังไง
    def check_piecess(dy, dx, enemy):
        r, c = k_row + dy, k_col + dx
        
        # while 0 >= r > len(map) and 0 >= c > len(map[r]):
        while 0 <= r < len(map) and 0 <= c < len(map[r]):
            piece = map[r][c]


            if piece in enemy:
                return True

            #ถ้าซ้อนกันนะจั๊ฟฟหรือว่าง
            elif piece != '.': 
                return False

            r += dy
            # print('r', r)
            c += dx
            # print('cc', c)
        return False

    #ทิศทางของ R, Q
    directionss = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dy, dx in directionss:
        # print('dy, dx', dy, dx)
        if check_piecess(dy, dx, ['R', 'Q']):
            print("Success")
            return

    #ทิศทางเหมือนข้างบน เป็น B, Q
    directionss_2 = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dy, dx in directionss_2:
        # print('dy, dx', dy, dx)
        if check_piecess(dy, dx, ['B', 'Q']):
            print("Success")
            return
    # ของ P
    pawn_directionss = [(1, 1), (1, -1)]
    for dy, dx in pawn_directionss:
        r, c = k_row + dy, k_col + dx
        # print('Moo')
        # print('c', c)
        if 0 <= r < len(map) and 0 <= c < len(map[r]):
            # print('ee', map[r][c])
            # print(r, c)
            if map[r][c] == 'P':
                print("Success")
                return

    print("Fail")