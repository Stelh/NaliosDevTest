# if voisin <= 1: cell  0
# if voisin >= 4: cell = 0
# if voisin = 2 or voisin = 3: cell = 1
# if cell = 0 and voisin = 3: cell = 1

#####################################################
def alive_cells(m):
    alive_positions = []
    for i, r in enumerate(m):
        for j, c in enumerate(r):
            if c == 1:
                alive_positions.append((i,j))
    return alive_positions

def check_neighbors(alive_positions):
    for (x,y) in alive_positions:
        print("alive_cell_position:x",x,"y",y)

        for nx in [-1,0,1]:
            print("nx:",nx)

            for ny in [-1,0,1]:
                print("ny:",ny)

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

def game_of_life(m):
    m_copy = [row[:] for row in m]
    new_r = [0] * len(m[0])
    generation = 1
    
    for r in m:
        print(r)
    print("m_________________________")

    for i in range(generation+1):
        # m_copy.insert(0, new_r)
        # m_copy.append(new_r)
        m_copy.insert(0, [0] * len(m[0]))
        m_copy.append([0] * len(m[0]))
    
    for r in m_copy:
        print(r)
    print("m_copy_________________________")
    
    for i in range(generation+1):
        for r in m_copy:
            r.insert(0,0)
            r.append(0)
    
    for r in m_copy:
        print(r)
    print("last_m_copy_________________________")
    for r in m:
        print(r)
    print("last_m_________________________")
    print("copy:",m_copy)
    print("m:",m)
    
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
        [1,1,1],
        [1,1,1]
    ]
)