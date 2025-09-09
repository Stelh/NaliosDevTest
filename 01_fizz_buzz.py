def parse_dict(d):
    parsed_dict = []
    for k, v in d.items():
        if '/' in k:
            n1, n2 = map(int, k.split('/'))
            if n1 > n2:
                n1, n2 = n2, n1
            parsed_dict.append(((n1, n2), v, True))
        else:
            parsed_dict.append((int(k), v, False))
    return parsed_dict

def get_n1(v):
    if v[2]:
        print("TEST",v[2])
        return v[0][0]
def get_n2(v):
    if v[2]:
        return v[0][0]

def sort_list(parsed_dict):
    for c in range(len(parsed_dict)):
        for i, v in enumerate(parsed_dict):
            #n1 = get_n1(v)
            #print("n1",n1)
            #n2 = get_n2(v)
            if v[2]:
                n1, n2 = v[0]
                print("ATM TRUE:", v,"|", n1, n2)
            else:
                n1 = v[0]
                print("ATM FALSE:", v,"|", n1)
            
            if i+1 < len(parsed_dict):
                if parsed_dict[i+1][2]:
                    n3, n4 = parsed_dict[i+1][0]
                    print("NEXT TRUE:",parsed_dict[i+1][0], n3, n4)
                else:
                    n3 = parsed_dict[i+1][0]
                    print("NEXT FALSE:", parsed_dict[i+1],"|", n3)
                # for cc in range(len(parsed_dict)):
                #     if n3 > n1:
                #         b = True
                #     else:
                #         b = False
                #         continue
            else:
                print("END OF LIST")
                print("sorted_list:",parsed_dict)
                break
            if n3 < n1:
                print("swap")
                parsed_dict[i], parsed_dict[i+1] = parsed_dict[i+1], parsed_dict[i]
    return parsed_dict

def fizz_buzz(d):
    print("dict:",d)
    print("_____________________________________")
    parsed_dict = parse_dict(d)
    print("parsed_dict:",parsed_dict)
    sort_list(parsed_dict)
    for i in range(1, 2):
        b = False # Si true, alors on a pas trouvé de multiple, donc print le nombre à la fin de la boucle.
        c = 0 # Compteur qui permet de savoir si on est à la fin de la boucle, et de print si b = True.
        for j in parsed_dict:
            c += 1
            if j[2]: # Si true, alors divisible par 2 nombres.
                n1, n2 = j[0]
                if i % n1 == 0 and i % n2 == 0:
                    print(str(j[1]))
                    break # Faut break sinon on peut print à la fin de la boucle un nombre multiple.
                b = True
            else: # Sinon, divisible par 1 nombre.
                n1 = j[0]
                if i % n1 == 0:
                    print(str(j[1]))
                    break
                b = True
            if c == len(parsed_dict) and b: # On est à la fin de la boucle, si on a pas trouvé de multiple on print le nombre.
                print(i)

fizz_buzz({
    '26/13':'FizzBuzz',
    '7':'Buzzy',
    '5/3':'Fizz',
    '5':'Buzz'
})