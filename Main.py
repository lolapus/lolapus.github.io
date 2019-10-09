# Nomative
NM1 = {"-a", "-us"}
NM1A = {"-us", "-is"}
NM2 = {"-ae", "-i", "-es", "-us"}
NM2A = {"-i", "-es"}
NF1 = {"-a", "-es", "-us"}
NF1A = {"-a", "-is"}
NF2 = {"-ae", "-es", "-us"}
NF2A = {"-ae", "-es"}
NN1 = {"-um", "-u"}
NN1A = {"-um", "-e"}
NN2 = {"-i", "-a", "-ia", "-ua"}
NN2A = {"-a", "-ia"}
# Genitive
GM1 = {"-ae", "-i", "-is", "-us"}
GM1A = {"-i", "-is"}
GM2 = {"-arum", "-orum", "-um", "-ium", "-uum"}
GM2A = {"-ōrum", "-ium"}
GF1 = {"-ae", "-is", "-us", "-ei"}
FF1A = {"-ae", "-is"}
GF2 = {"-arum", "-um", "-ium", "-uum", "-erum"}
GF2A = {"-arum", "-ium"}
GN1 = {"-i", "-is", "-us"}
GN1A = {"-i", "-is"}
GN2 = {"-orum", "-um", "-us", "-uum"}
GN2A = {"-orum", "-ium"}
# Dative
DM1 = {"-ae", "-o", "-i", "-ui"}
DM1A = {"-o", "-i"}
DM2 = {"-is", "-ibus"}
DM2A = {"-is", "-ibus"}
DF1 = {"-ae", "-i", "-ui", "-ei"}
DF1A = {"-a", "-i"}
DF2 = {"-is", "-ibus", "-erum"}
DF2A = {"-is", "-ibus"}
DN1 = {"-o", "-i", "-u"}
DN1A = {"-o", "-i"}
DN2 = {"-is", "-ibus"}
DN2A = {"-is", "-ibus"}
# Accusative
AM1 = {"-am", "-um", "-em"}
AM1A = {"-um", "-em"}
AM2 = {"-as", "-os", "-es"}
AM2A = {"-os", "-es"}
AF1 = {"-am", "-um", "-em"}
AF1A = {"-am", "-em"}
AF2 = {"-as", "-es", "-us"}
AF2A = {"-as", "-es"}
AN1 = {"-as", "-u"}
AN1A = {"-um", "-e"}
AN2 = {"-a", "-ia", "-ua"}
AN2A = {"-a", "-ia"}
# Ablative
A1M1 = {"-a", "-o", "-e", "-u"}
A1M1A = {"-o", "-i"}
A1M2 = {"-is", "-ibus"}
A1M2A = {"-is", "-ibus"}
A1F1 = {"-a", "-e", "-u"}
A1F1A = {"-a", "-i"}
A1F2 = {"-is", "-ibus", "-ebus"}
A1F2A = {"-is", "-ibus"}
A1N1 = {"-o", "-e", "-i", "-u"}
A1N1A = {"-o", "-i"}
A1N2 = {"-is", "-ibus"}
A1N2A = {"-is", "-ibus"}

nounEnd = input("Noun Ending")
nounColumn = input("Noun Column m,f,n")
adjEnd = input("Adjective Ending")

answer = 0

if nounColumn == "m":
    if nounEnd in NM1:
        if adjEnd in NM1A:
            answer = 1
    elif nounEnd in NM2:
        if adjEnd in NM2A:
            answer = 1
    elif nounEnd in GM1:
        if adjEnd in GM1A:
            answer = 1
    elif nounEnd in GM2:
        if adjEnd in GM2A:
            answer = 1
    elif nounEnd in DM1:
        if adjEnd in DM1A:
            answer = 1
    elif nounEnd in DM2:
        if adjEnd in DM2A:
            answer = 1
    elif nounEnd in AM1:
        if adjEnd in AM1A:
            answer = 1
    elif nounEnd in AM2:
        if adjEnd in AM2A:
            answer = 1
    elif nounEnd in A1M1:
        if adjEnd in A1M1A:
            answer = 1
    elif nounEnd in A1M2:
        if adjEnd in A1M2A:
            answer = 1
elif nounColumn == "f":
    if nounEnd in NF1:
        if adjEnd in NF1A:
            answer = 1
    elif nounEnd in NF2:
        if adjEnd in NF2A:
            answer = 1
    elif nounEnd in GF1:
        if adjEnd in GM1A:
            answer = 1
    elif nounEnd in GF2:
        if adjEnd in GF2A:
            answer = 1
    elif nounEnd in DF1:
        if adjEnd in DF1A:
            answer = 1
    elif nounEnd in DF2:
        if adjEnd in DF2A:
            answer = 1
    elif nounEnd in AF1:
        if adjEnd in AF1A:
            answer = 1
    elif nounEnd in AF2:
        if adjEnd in AF2A:
            answer = 1
    elif nounEnd in A1F1:
        if adjEnd in A1F1A:
            answer = 1
    elif nounEnd in A1F2:
        if adjEnd in A1F2A:
            answer = 1
elif nounColumn == "n":
    if nounEnd in NN1:
        if adjEnd in NN1A:
            answer = 1
    elif nounEnd in NN2:
        if adjEnd in NN2A:
            answer = 1
    elif nounEnd in GN1:
        if adjEnd in GN1A:
            answer = 1
    elif nounEnd in GN2:
        if adjEnd in GN2A:
            answer = 1
    elif nounEnd in DN1:
        if adjEnd in DN1A:
            answer = 1
    elif nounEnd in DN2:
        if adjEnd in DN2A:
            answer = 1
    elif nounEnd in AN1:
        if adjEnd in AN1A:
            answer = 1
    elif nounEnd in AN2:
        if adjEnd in AN2A:
            answer = 1
    elif nounEnd in A1N1:
        if adjEnd in A1N1A:
            answer = 1
    elif nounEnd in A1N2:
        if adjEnd in A1N2A:
            answer = 1
if nounEnd == adjEnd:
    answer = 1

if answer == 0:
    print("No")
else:
    print("Yes")

end = input("Press Enter to continue...")
