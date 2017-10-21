#!/usr/bin/env python

import argparse
import sys
import os
import time

def print_masthead():
    masthead = "===================================\n"
    masthead += "Extract the lines of file1 \nwhoses column1 element is contained \nin the column2 of file2\n"
    masthead += "==================================\n"
    print masthead

def print_options(args):
    opts = vars(args)
    print "Options:"
    for opt in opts:
        print "   --" + opt + ": " + str(opts[opt])
    print ""

def hour_min_sec(seconds):
    # seconds is a duration in seconds
    h = int(seconds)/3600
    m = int(seconds%3600/60)
    s = int(seconds%3600%60)
    return "%d:%d:%d" % (h,m,s)

def read_column(filepath, column, sep, ignore):
    collist = []
    n = 0
    with open(filepath) as f:
        for line in f:
            n += 1
            if n > ignore:
                collist.append(line.rstrip().split(sep)[column])
    return(collist)

def argument_parser():
    parser = argparse.ArgumentParser(description='Extract the lines of file1 whoses column1 element is contained in the column2 of file2')
    parser.add_argument('--file1','-f1', required=True, help='the path of file1')
    parser.add_argument('--file2','-f2', required=True, help='the path of file2')
    parser.add_argument('--column1', '-c1', type=int, default=1, help='the column number(1-based) of file1')
    parser.add_argument('--column2', '-c2', type=int, default=1, help='the column number(1-based) of file2')
    parser.add_argument('--sep1', '-s1', default=None, help="the separator of columns for file1")
    parser.add_argument('--sep2', '-s2', default=None, help="the separator of columns for file2")
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--skip1', '-sk1', default=0, type=int, help="the number of lines of file1 skipped and those lines will output.")
    group.add_argument('--ignore1', '-i1', default=0, type=int, help="the number of lines of file1 ignored and those lines will not output")
    parser.add_argument('--ignore2', '-i2', default=0, type=int, help="the number of lines of file2 ignored")
    parser.add_argument('--out', default = "extracted.txt", help="the filename of output, default: extracted.txt")
    return parser.parse_args()

if __name__ == "__main__":
    start_time = time.time()
    args = argument_parser()
    print_masthead()
    print_options(args)

    collist2 = read_column(args.file2, args.column2-1, args.sep2, args.ignore2)
    print "Read the %dth column of file2 %s, %d lines out of %d lines have been readed." % (args.column2, args.file2,len(collist2), len(collist2)+args.ignore2)
    with open(args.out, "w") as fout:
        with open(args.file1) as f1:
            n = 0
            nout = 0
            for line in f1:
                n += 1
                if n <= args.skip1:
                    nout += 1
                    fout.write(line)
                elif n > args.ignore1 and line.rstrip().split(args.sep1)[args.column1-1] in collist2:
                    nout += 1
                    fout.write(line)
    print "Write lines in file1 %s into file %s, %d lines out of %d lines written." % (args.file1, args.out, nout, n) 
    end_time = time.time()
    print "Analysis time: %s" % hour_min_sec(end_time - start_time)


    
