#author: zjuwhw
#date: 2015-04-07
USAGE='''melted.data.to.matrix.py --- transform a melted data file into a matrix file
USAGE:
    python %s inputfile

Note:
The inputfile consists three elements each line. And the string "first element + second element" should exist only once!
'''

import os, sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print USAGE % sys.argv[0]
        sys.exit(1)
    inputfile = sys.argv[1]
    f = open(inputfile)
    xcontainer = []
    ycontainer = []
    container = {}
    for line in f:
        linelist = line.rstrip().split()
        xycoordinate = linelist[0] + ":" + linelist[1]
        if xycoordinate in container.keys():
            print "the string: first element + second element should exist only once"
            sys.exit(1)
        else:
            container[xycoordinate] = linelist[2]
        if linelist[0] not in xcontainer:
            xcontainer.append(linelist[0])
        if linelist[1] not in ycontainer:
            ycontainer.append(linelist[1])
    
    
    print " \t" + "\t".join(ycontainer)
    for x in xcontainer:
        yline = []
        for y in ycontainer:
            if x+":"+y in container.keys():
                yline.append(container[x+":"+y])
            else:
                yline.append("none")
        print x + "\t" + "\t".join(yline)
        
    f.close()