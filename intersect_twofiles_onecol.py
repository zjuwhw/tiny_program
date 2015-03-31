#python intersect_twofiles_onecol.py inputfile1_onecol.txt inputfile2_onecol.txt
import sys, os
inputfile1=sys.argv[1]
inputfile2=sys.argv[2]

def fun_rstrip(alist):
    return alist.rstrip()

line1 = open(inputfile1).readlines()
line1 = set(map(fun_rstrip, line1))
line2 = open(inputfile2).readlines()
line2 = set(map(fun_rstrip, line2))

print "A-B:\t%d" % (len(line1 - line2))
print "A&B:\t%d" % (len(line1 & line2))
print "B-A:\t%d" % (len(line2 - line1))
print "A|B:\t%d" % (len(line1 | line2))