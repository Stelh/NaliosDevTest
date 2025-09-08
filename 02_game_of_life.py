# if voisin <= 1: cell  0
# if voisin >= 4: cell = 0
# if voisin = 2 or voisin = 3: cell = 1
# if cell = 0 and voisin = 3: cell = 1

#####################################################

def i0_j0_c0_check_neightbors(m, i, j, m_copy):
    c = 0
    if m[i][j+1]:
        c += 1
    if m[i+1][j]:
        c += 1
    if m[i+1][j+1]:
        c += 1
    m_copy[i][j] = 1
    print("____________")
    for ii in m_copy:
        print(ii)

def i0_j0_c1_check_neightbors(m, i, j, m_copy):
    c = 0
    if m[i][j+1]:
        c += 1
    if m[i+1][j]:
        c += 1
    if m[i+1][j+1]:
        c += 1
    
    if c <= 1:
        m_copy[i][j] = 0
    elif c == 2 or c == 3:
        m_copy[i][j] = 1
    elif c >= 4:
        m_copy[i][j] = 0
    
    for ii in m_copy:
        print(ii)

#####################################################

# def check_neighbors(alive_positions,m_copy):
#     i = 2
#     for (x,y) in alive_positions:   
#         for nx in [-1,0,1]:
#             if nx == 0:
#                 continue
#             m_copy[x+nx][y+nx] = i
#             i += 1
#     for i in m_copy:
#         print(i)
            
#             # for ny in [-1,0,1]:
#             #     print("ny:",ny)

def check_neighbors(alive_positions,m_copy):
    for (x,y) in alive_positions:   
        for nx in [-1,0,1]:
            for ny in [-1,0,1]:
                if nx == 0 and ny == 0:
                    continue
                if m_copy[x+nx][y+ny] == 1:
                    print("voisin found:",x+nx,y+ny)
                    m_copy[x+nx][y+ny] = 2
    for i in m_copy:
        print(i)
            
            # for ny in [-1,0,1]:
            #     print("ny:",ny)

def alive_cells(m_copy,alive_positions):
    for i, r in enumerate(m_copy):
        for j, c in enumerate(r):
            if c == 1:
                alive_positions.append((i,j))
    return alive_positions

def infinite_grid(m, m_copy):
    for i in range(1):
        # m_copy.insert(0, new_r)
        # m_copy.append(new_r)
        m_copy.insert(0, [0] * len(m[0]))
        m_copy.append([0] * len(m[0]))
        for r in m_copy:
            r.insert(0,0)
            r.append(0)
    return m_copy

def game_of_life(m):
    #new_r = [0] * len(m[0])
    m_copy = [row[:] for row in m]
    alive_positions = []
    
    # for r in m:
    #     print(r)
    # print("Start:m_________________________")
    
    infinite_grid(m, m_copy)
    
    # for r in m_copy:
    #     print(r)
    # print("m_copy_________________________")
    
    alive_cells(m_copy,alive_positions)
    
    print("alive_cells:",alive_positions)
    
    check_neighbors(alive_positions,m_copy)
    


    # for i, r in enumerate(m):
    #     for j, c in enumerate(r):
    #         if i == 0 and j == 0 and c == 0:
    #             i0_j0_c0_check_neightbors(m, i, j, m_copy)
    #         if i == 0 and j == 0 and c == 1:
    #             i0_j0_c1_check_neightbors(m, i, j, m_copy)
    #         # if i == 0 and j != 0 and j < len(r)-1
    
game_of_life(
    [
        [1,1,1],
        [0,0,0],
        [1,0,0],
        [0,1,0],
        [0,0,0],
        [0,1,0],
        [0,0,0],
        [0,1,0],
        [0,1,0]
    ]
)