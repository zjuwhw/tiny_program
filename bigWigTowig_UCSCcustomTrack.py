USAGE='''bigWigTowig_UCSCcustomTrack.py --- convert the bigWig to wig, add the browser lines and track lines and upload to UCSC genome browser

USAGE:
    python %s [--ylim=##] [--output=##] chr str end bigWigfile(one or more)

Default:
--output: stdout

NOTES:
the UCSC bigWigTowig utility must be installed
'''

header = '''browser position %s:%s-%s
browser full refGene
track type=wiggle_0 name="%s" description=" " visibility=full color=0,0,128 altColor=128,128,128 priority=16 autoScale=off alwaysZero=off gridDefault=off maxHeightPixels=128:64:11 graphType=bar viewLimits=0:%s yLineMark=0 yLineOnOff=off
'''

import os, sys, getopt

def cmd_bigWigToWig(nchr, nstr, nend, inputbigWig, outputWig):
    cmd = "bigWigToWig % s %s -chrom=%s -start=%s -end=%s" % (inputbigWig, outputWig, nchr, nstr, nend)
    os.system(cmd)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print USAGE % sys.argv[0]
        sys.exit(1)
    
    # defaults
    output = sys.stdout
    ylim = "25"
    
    opts,args=getopt.getopt(sys.argv[1:],"",["output="])
    for o,a in opts:
        if o=='--output':
            output = open(a, "w")
        elif o=='--ylim':
            ylim = a
            
    nchr = args[0]
    nstr = args[1]
    nend = args[2]
    bigWigfiles = args[3:]
    
    for i in range(len(bigWigfiles)):
        cmd_bigWigToWig(nchr, nstr, nend, bigWigfiles[i], "tmp.wig")
        print >> output, header % (nchr, nstr, nend, bigWigfiles[i].replace(".bigWig",""), ylim)
        tmpfp = open("tmp.wig")
        for line in tmpfp:
            print >> output, line.rstrip()
        tmpfp.close()
        os.remove("tmp.wig")
    output.close()
    