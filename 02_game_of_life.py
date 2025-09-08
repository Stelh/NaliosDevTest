# if voisin <= 1: cell  0
# if voisin = 2 or voisin = 3: cell = 1
# if voisin >= 4: cell = 0

# if cell = 0 and voisin = 3: cell = 1

#####################################################
def print_all(m, m_copy, next_step):
    
    print("initial matrix:")
    for i in m:
        print(i)
    print("_________________________")
    
    print("infinite grid:")
    for i in m_copy:
        print(i)
    print("_________________________")
    
    print("next_step:")
    for i in next_step:
        print(i)
    print("_________________________")

#####################################################
def check_neighbors_alive(alive_positions, next_step, m_copy):
    for (x,y) in alive_positions:
        c = 0
        for nx in [-1,0,1]:
            for ny in [-1,0,1]:
                if nx == 0 and ny == 0:
                    continue
                if m_copy[x+nx][y+ny] == 1:
                    #m_copy[x+nx][y+ny] = 2
                    #print("voisin found:",x+nx,y+ny)
                    c += 1
        if c <= 1:
            next_step[x][y] = 0
        elif c == 2 or c == 3:
            next_step[x][y] = 1
        elif c >= 4:
            next_step[x][y] = 0

def alive_cells(m_copy, alive_positions):
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
    
    infinite_grid(m, m_copy)
    next_step = [row[:] for row in m_copy]
    alive_cells(m_copy,alive_positions)
    check_neighbors_alive(alive_positions,next_step,m_copy)
    
    print_all(m, m_copy, next_step)

    # for i, r in enumerate(m):
    #     for j, c in enumerate(r):
    #         if i == 0 and j == 0 and c == 0:
    #             i0_j0_c0_check_neightbors(m, i, j, m_copy)
    #         if i == 0 and j == 0 and c == 1:
    #             i0_j0_c1_check_neightbors(m, i, j, m_copy)
    #         # if i == 0 and j != 0 and j < len(r)-1
    
game_of_life(
    [
        [1,1,1]
    ]
)