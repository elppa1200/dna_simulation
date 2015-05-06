import random 
import time
dna_sequence = raw_input("DNA_sequence>")
ticks = raw_input("Ticks>")
N = len(dna_sequence)
N = int(N)
change_IDs = []
counter = int(0)
def dna_changeH(N):
    return(random.randrange(1, N))           
def dnaID (N):
   erfolg = "false"
   while (erfolg == "false"):
    ID = random.randrange(1, N)
    if ID in change_IDs:
       nana = 'pointless' #do nothing
    else:
       erfolg = "true"
       change_IDs.append(ID)
def changeInto():
   into = random.randrange(0, 3)
   if into == 0:
       return("A")
   elif into == 1:
       return("G")                              
   elif into == 2:
       return("T")
   else:
       return("H")
def wipevalues():
   change_IDs = []
def checkdna(dna_sequence):
    if 'B' in dna_sequence:
	    return 'err'
    elif 'C' in dna_sequence:
	    return 'err'
    elif 'D' in dna_sequence:
	    return 'err'
    elif 'E' in dna_sequence:
	    return 'err'
    elif 'F' in dna_sequence:
	    return 'err'
    elif 'I' in dna_sequence:
	    return 'err'
    elif 'J' in dna_sequence:
	    return 'err'
    elif 'K' in dna_sequence:
	    return 'err'
    elif 'L' in dna_sequence:
	    return 'err'
    elif 'M' in dna_sequence:
	    return 'err'
    elif 'N' in dna_sequence:
	    return 'err'
    elif 'O' in dna_sequence:
	    return 'err'
    elif 'P' in dna_sequence:
	    return 'err'
    elif 'Q' in dna_sequence:
	    return 'err'
    elif 'R' in dna_sequence:
        return 'err'
    elif 'S' in dna_sequence:
	    return 'err'
    elif 'U' in dna_sequence:
	    return 'err'
    elif 'V' in dna_sequence:
	    return 'err'
    elif 'W' in dna_sequence:
	    return 'err'
    elif 'X' in dna_sequence:
	    return 'err'
    elif 'Y' in dna_sequence:
	    return 'err'
    elif 'Z' in dna_sequence:
	    return 'err'
for i in range(int(ticks)):
    if checkdna(dna_sequence) == 'err':
        print("DNA contains errors: " + dna_sequence)
        break
    counter = counter + 1
    print("[STAGE " + str(counter) + "]")
    haufigkeit = dna_changeH(N)
    print("Haufigkeit:" + str(haufigkeit))
    for i in range(haufigkeit):
        dnaID(N)
    print(change_IDs)
    for i in range(haufigkeit):
        ch_ID = change_IDs.pop()
        int(ch_ID)
        ch_ID1 = ch_ID - 1
        DNA_part1 = dna_sequence[0:ch_ID1]
        DNA_part2 = dna_sequence[ch_ID:99999]
        dna_sequence = DNA_part1 + changeInto() + DNA_part2
    print("")
    print("##new DNA: " + dna_sequence + "##")
    print("")
    change_IDs = []
    time.sleep(3)
print("end of script.")
