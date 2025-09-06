def fizz_buzz(d):
    parsed_dict = [] # On parse le dictionnaire pour ne pas le parcourir à chaque fois.
    #print("parsed_init:",parsed_dict)
    for k, v in d.items():
        if '/' in k:
            n1, n2 = map(int, k.split('/'))
            #print(n1," ",n2)
            parsed_dict.append(((n1, n2), v, True)) # True = Divisible par 2 nombres(3/5,2/6,etc...)
            #print("parsed_dict:",parsed_dict)
        else:
            parsed_dict.append((int(k), v, False)) # False = Divisible par 1 nombre(3,5,etc...)
            #print("else:",parsed_dict)
    #print(parsed_dict)
    #print("len:",len(parsed_dict))
    
    for i in range(1, 101):
        b = False # Si true, alors on a pas trouvé de multiple, donc print le nombre à la fin de la boucle.
        c = 0 # Compteur qui permet de savoir si on est à la fin de la boucle, et de print si b = True.
        for j in parsed_dict:
            c += 1
            #print("j:",j)
            if j[2]: # Si true, alors divisible par 2 nombres.
                n1, n2 = j[0]
                #print("N1:",n1, "N2:",n2)
                if i % n1 == 0 and i % n2 == 0:
                    print(str(j[1]))
                    break # Faut break sinon on peut print à la fin de la boucle un nombre multiple.
                b = True
            else: # Sinon, divisible par 1 nombre.
                n1 = j[0]
                #print("N1:",n1)
                if i % n1 == 0:
                    print(str(j[1]))
                    break
                b = True
            #print("c:",c, "len:",len(parsed_dict), "j:",j)
            if c == len(parsed_dict) and b: # On est à la fin de la boucle, si on a pas trouvé de multiple,on print le nombre.
                print(i)
fizz_buzz({
    '3/5':'Fizz',
    '5':'Buzz',
    '7':'Buzzy',
    '13/26':'FizzBuzz'
})