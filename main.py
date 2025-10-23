


mem={}

code="SxahelN SxbloN Sxc_woN Sxdrld   PxaN PxbN PxcN Pxd".replace(" ","")

def set_mem(addr,value):
    mem[addr]=value



#opc = {
#    "Q":query_mem,
#    "S":set_mem,
#    "P":print
#}


for line in code.split("N"):
    for c in range(0,len(line)-1):
        if line[c] == "Q":
            line=line.replace(line[c:c+3],mem[line[c+1:c+3]])
        elif line[c] == "S":
            mem[line[c+1:c+3]]=line[c+3:c+6]
        elif line[c] == "P":
            print(mem[line[c+1:c+3]],end="")
