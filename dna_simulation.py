####script to simulate evolution of a single DNA_sequence###
#         code by Alexander Kehr, 2015                     #
###         GNU General Public License                   ###
import random 
import time
DNA_sequence = raw_input("DNA_sequence>")
ticks = raw_input("Ticks>")
N = len(DNA_sequence)
N = int(N)
change_IDs = []
counter = int(0)
def dna_changeH(N):
    return(random.randrange(1, N))           
def dnaID (N):
   erfolg = "false"
   while (erfolg == "false"):
    ID = random.randrange(1, N)
    if ID in change_IDs:)
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
for i in range(int(ticks)):
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
        DNA_part1 = DNA_sequence[0:ch_ID1]
        DNA_part2 = DNA_sequence[ch_ID:99999]
        DNA_sequence = DNA_part1 + changeInto() + DNA_part2
    print("")
    print("##new DNA: " + DNA_sequence + "##")
    print("")
    change_IDs = []
    time.sleep(3)
print("end of script.")
