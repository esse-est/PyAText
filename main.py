letter_lookup = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","r","u","v","w","x","y","z"]


data="MAMbN SADxxHello_world!N PRIQEMxx".replace(" ","").split("N")

MEM = {
}

MEM_ADDR_MAX = 0
for line in data:
    #memory opc
    if line[:3] == "MAM":
        #mam of 2 is 676 possible addresses, 3 in 17576
        MEM_ADDR_MAX = letter_lookup.index(line[3])+1
    elif line[:3] == "SAD":
        MEM[line[3:(3+MEM_ADDR_MAX)]]=line[3+MEM_ADDR_MAX:]
    
    #qem swap
    for qem in range(0,line.count("QEM")):
        idval=line.find("QEM")
        line=f"{line[:idval]}{MEM[line[1+idval+MEM_ADDR_MAX:]]}"
    
    #non mathamatical functions
    if line[:3] == "PRI":
        print(line[3:])
    
