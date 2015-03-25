#usage: python sequences2consensus.py inputfile(mang DNA sequences with the same length)
#example: input AGCT"\n"CGCT; output: [A/C]GCT and MGCT

import os, sys
inputfile = sys.argv[1]
f1 = open(inputfile)
IUPAC = {"A":"A", "C":"C", "G":"G", "T":"T ", "AG":"R", "CT":"Y", "CG":"S", "AT":"W", "GT":"K", "AC":"M", "CGT":"B", "AGT":"D", "ACT":"H", "ACG":"V", "ACGT":"N"}
consensus_container = {}
consensus_string = ""
consensus_IUPAC = ""
switch = True
for line in f1:
    sequence = line.rstrip()
    if switch:
        switch = False
        for index in range(len(sequence)):
            consensus_container[index] = set()
    for index in range(len(sequence)):
        consensus_container[index].add(sequence[index])

for index in consensus_container.keys():
    #print "".join(consensus_container[index])
    a = list(consensus_container[index])
    a.sort()
    a = "".join(a)
    consensus_string += "[" + "/".join(a) + "]"
    consensus_IUPAC += IUPAC[a]
    #consensus_IUPAC += IUPAC[consensus_container[index]]
print consensus_string
print consensus_IUPAC

f1.close()