# 'b' est un booléen de controle qui permet de print une seul fois un nombre. Dans ma logique de code, for k, v peut print plusieurs fois un nombre si on ne met pas b = False. C'est la seul logique que j'ai trouvé pour pouvoir print un nombre une seul fois.

# 'c' est un compteur pour len(d) pour vérifier si on a parcouru toutes les clés du dictionnaire et print une seule fois à la fin du parcours notre nombre si il doit être print. En corélation avec b.

#Donc ma logique : 

# Je parcours en premier la liste des nombre pour, puis je parcour le dictionnaire et test 1 par 1 chaque élément. 

# Je test en premier si ça contient un "/", puis je vérifie le modulo. Si modulo, alors print et on break. Sinon, B = True, cela signifie qu'on a le droit de le print à la fin car il n'est pas modulo. 

# Si ça contient pas de "/", alors ça fait le modulo comme plus haut, puis ça break. Sinon, comme plus haut, on passe B à true. Puis à la fin on vérifie si on est à la dernière occurence du for k, v avec len(d) et si B alors on print le last number

def fizz_buzz(d):
    for i in range(1, 101):
        #print("For:",i)
        b = False
        c = 0
        for k, v in d.items():
            c += 1
            #print("leng:",len(d))
            #print("c:",c)
            #print("K:",k,"V:",v)
            if "/" in k:
                n1, n2 = map(int, k.split('/'))
                w = str(v)
                #print("-If \"/\" N1:",n1," N2:",n2," W:",w)
                if i % n1 == 0 and i % n2 == 0:
                    b = False
                    #print("-i % n1 and i % n2 == 0: ",w)
                    print(w)
                    break
                else:
                    if not b:
                        b = True
                        #print("B1 is True")
            else:
                n1 = int(k)
                w = str(v)
                if i % n1 == 0:
                    b = False
                    #print("_i % n1 == 0: ",w)
                    print("w:",w)
                    break
                else:
                    if not b:
                        b = True
                        #print("B2 is True")
            if c == len(d) and b:
                print("i:",i)

fizz_buzz({
    '3/5':'Fizz',
    '5':'Buzz',
    '7':'Buzzy',
    '2/10':'FizzBuzz'
})