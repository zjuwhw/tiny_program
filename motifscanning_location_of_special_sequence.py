#usage: python fing_location_of_special_sequence.py fastafile motif_sequence(s)
import os, re, sys

def lowerfunction(s):
    return s.lower()
def revcomp(seq):
    rc = {'A':'T', 'G':'C', 'C':'G', 'T':'A', 'N':'N'}
    return ''.join([rc[seq[i]] for i in xrange(len(seq) - 1, -1, -1)])

#directory="E:/task/liyz-2013.4.1-chip-seq/summary-20150304/figure3D-2_boxplot_aggregation_motif_site_ACCACA/"
fastafile = sys.argv[1]
sequences = sys.argv[2:]

for m in map(revcomp, sequences):
    sequences.append(m)
#for n in map(lowerfunction, sequences):
#    sequences.append(n)

f = open(fastafile)
f2 = open(fastafile.replace("fa","motifsite.txt"), "w")
for line in f:
    line = line.rstrip()
    if line.startswith(">"):
        chromosome = line.split(":")[0].lstrip(">")
        start = line.split(":")[1].split("-")[0]
        end = line.split(":")[1].split("-")[1]
    else:
        for sequence in sequences:
            for target in re.finditer("(?=%s)" % sequence, line, flags=re.IGNORECASE):
                print >>f2, "%s\t%s\t%d\t%s\t%s" % (chromosome, int(start)+target.start() , int(start)+target.start()+len(sequence), "%s:%s-%s" % (chromosome,start,end), sequence)
f.close()
f2.close()

cmd = "sort -k1,1 -k2,2n -k3,3n %s > %s" % (fastafile.replace("fa","motifsite.txt"), fastafile.replace("fa","motifsite.sorted.txt"))
os.system(cmd)
os.remove(fastafile.replace("fa","motifsite.txt"))
