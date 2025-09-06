# if voisin <= 1: cell  0
# if voisin >= 4: cell = 0
# if voisin >=2 and voisin <= 3: cell = 1
# if cell = 0 and voisin = 3: cell = 1

def game_of_life(m):
    print("= m:",m)
    print("= len(m):",len(m))
    print("= len(m[0]):",len(m[0]))
    print("= m[0][0]:",m[0][0])
    
    for i, r in enumerate(m):
        print("-i:",i,"| -r:",r)
        for j, c in enumerate(r):
            print("-j:",j,"| -c:",c)
            print(r[j-1])
game_of_life(
    [
        [0,1],
        [1],
        [2]
    ]
)