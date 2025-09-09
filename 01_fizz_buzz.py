# useless functions
def get_n3(v):
    return v[0]
def get_n3_n4(v):
    return v[0][0], v[0][1]
def get_n1(v):
    return v[0]
def get_n1_n2(v):
    return v[0][0], v[0][1]
#############################################
def sort_list(parsed_dict, parsed_dict_copy):
    c = 0
    for _ in range(len(parsed_dict)-1):
        for i, v in enumerate(parsed_dict):
            if v[2]:
                n1, n2 = get_n1_n2(parsed_dict[i])
                #print("ATM TRUE:", v,"|", n1, n2)
            else:
                n1 = get_n1(v)
                #print("ATM FALSE:", v,"|", n1)
            if i < len(parsed_dict)-1:
                if parsed_dict[i+1][2]:
                    n3, n4 = get_n3_n4(parsed_dict[i+1])
                    #print("NEXT TRUE:",parsed_dict[i+1][0], n3, n4)
                else:
                    n3 = get_n3(parsed_dict[i+1])
                    #print("NEXT FALSE:", parsed_dict[i+1],"|", n3)
            else:
                #print("End of ",_," sort")
                #print("sorted_list:",parsed_dict)
                break
            ############# HEEEEEEEEEEEEEEEEERE
            if n3 < n1:
                parsed_dict[i], parsed_dict[i+1] = parsed_dict[i+1], parsed_dict[i]
                print("sort:",parsed_dict)
            else:
                c += 1
            if c == len(parsed_dict)-1: # YEAH BOY
                print("sorted in ",_," iteration")
                break
    return parsed_dict

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

def fizz_buzz(d):
    print("dict:",d)
    print("_____________________________________")
    parsed_dict = parse_dict(d)
    parsed_dict_copy = [row[:] for row in parsed_dict] # just for log
    print("parsed_dict:",parsed_dict)
    print("_____________________________________")
    sort_list(parsed_dict, parsed_dict_copy)
    for i in range(1, 2):
        b = False
        c = 0
        for j in parsed_dict:
            c += 1
            if j[2]:
                n1, n2 = j[0]
                if i % n1 == 0 and i % n2 == 0:
                    print(str(j[1]))
                    break
                b = True
            else:
                n1 = j[0]
                if i % n1 == 0:
                    print(str(j[1]))
                    break
                b = True
            if c == len(parsed_dict) and b:
                print(i)

fizz_buzz({
    '26/13':'FizzBuzz',
    '7':'Buzzy',
    '5/3':'Fizz',
    '5':'Buzz'
})