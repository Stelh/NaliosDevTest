#####################################################
def _print_matrix(m):
    print("initial matrix:")
    for i in m:
        print(i)
    print("_________________________")
def _print_infinite_grid(m_copy):
    print("infinite grid:")
    for i in m_copy:
        print(i)
    print("_________________________")
def _print_next_step(next_step):
    for i in next_step:
        print(i)
    print("_________________________")
def print_alive_positions(alive_positions):
    print("alive positions:")
    for i in alive_positions:
        print(i)
    print("_________________________")
#####################################################

def end_it(m_copy):
    for _, r in enumerate(m_copy):
        for _, c in enumerate(r):
            if c == 1:
                return True
    return False

def check_border(next_step):
    for i, r in enumerate(next_step[0]):
        if r == 1:
            return True
    for i, r in enumerate(next_step[-1]):
        if r == 1:
            return True
    for i in range(len(next_step)):
        if next_step[i][0] == 1:
            return True
    for i in range(len(next_step)):
        if next_step[i][-1] == 1:
            return True
    return False

def check_neighbors_for_dead_cell(dead_positions, m_copy, next_step):
    for (x,y) in dead_positions:
        c = 0
        for nx in [-1,0,1]:
            for ny in [-1,0,1]:
                if nx == 0 and ny == 0:
                    continue
                try:
                    if m_copy[x+nx][y+ny] == 1:
                        c += 1
                except IndexError:
                    continue
        if c == 3:
            next_step[x][y] = 1

def check_neighbors_for_alive_cell(alive_positions, m_copy, next_step):
    for (x,y) in alive_positions:
        c = 0
        for nx in [-1,0,1]:
            for ny in [-1,0,1]:
                if nx == 0 and ny == 0:
                    continue
                if m_copy[x+nx][y+ny] == 1:
                    c += 1
        if c <= 1:
            next_step[x][y] = 0
        elif c == 2 or c == 3:
            next_step[x][y] = 1
        elif c >= 4:
            next_step[x][y] = 0

def dead_cells(m_copy):
    dead_positions = []
    for i, r in enumerate(m_copy):
        for j, c in enumerate(r):
            if c == 0:
                dead_positions.append((i,j))
    return dead_positions

def alive_cells(m_copy):
    alive_positions = []
    for i, r in enumerate(m_copy):
        for j, c in enumerate(r):
            if c == 1:
                alive_positions.append((i,j))
    return alive_positions

def infinite_grid(m, m_copy):
    m_copy.insert(0, [0] * len(m[0]))
    m_copy.append([0] * len(m[0]))
    for r in m_copy:
        r.insert(0,0)
        r.append(0)
    return m_copy

def game_of_life(m):
    _print_matrix(m)
    m_copy = [row[:] for row in m]
    infinite_grid(m, m_copy)
    _print_infinite_grid(m_copy)
    for i in range(5):
        next_step = [row[:] for row in m_copy]
        alive_positions = alive_cells(m_copy)
        dead_positions = dead_cells(m_copy)
        check_neighbors_for_alive_cell(alive_positions,m_copy,next_step)
        check_neighbors_for_dead_cell(dead_positions,m_copy,next_step)
        print("iteration:",i+1)
        if check_border(next_step):
            infinite_grid(next_step, next_step)
        _print_next_step(next_step)
        m_copy = [row[:] for row in next_step]
        if not end_it(m_copy):
            print("end")
            break

game_of_life(
    [
        [1,1,1],
        [1,0,1],
    ]
)