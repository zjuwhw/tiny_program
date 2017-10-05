#!/usr/bin/env python

import argparse
import sys
import os

def get_list(onelist, index):
    if len(onelist) >= index+1:
        return onelist[index]
    else:
        return "NA"
    

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Intersect two columns in two files')
    parser.add_argument('--file1','-f1', required=True, help='the path of file1')
    parser.add_argument('--file2','-f2', required=True, help='the path of file2')
    parser.add_argument('--column1', '-c1', type=int, default=1, help='the column number(1-based) of file1')
    parser.add_argument('--column2', '-c2', type=int, default=1, help='the column number(1-based) of file2')
    parser.add_argument('--sep', default=None, help="the separator of columns")
    args = parser.parse_args()
    opts = vars(args)

    col1_list = [ line.rstrip().split(args.sep)[args.column1-1] for line in open(args.file1)]
    col2_list = [ line.rstrip().split(args.sep)[args.column2-1] for line in open(args.file2)]
    col1 = set(col1_list)
    col2 = set(col2_list)
    col1and2 = col1 & col2
    col1min2 = col1 - col2
    col1or2 = col1 | col2
    col2min1 = col2 - col1

    print "Intersect between column %d of file %s and column %d of file %s" % (args.column1, args.file1, args.column2, args.file2)
    print "\n"
    print "Options:"
    for opt in opts:
        print "   --" + opt + ": " + str(opts[opt])
    print "\n"
    print "Stats:"
    print "   f1: " +  str(len(col1)) + " (e.g. "+ get_list(col1_list,0), ")"
    print "   f2: " + str(len(col2)) + " (e.g. "+ get_list(col2_list,0), ")"
    print "   f1&f2: " + str(len(col1and2)) + " (e.g. "+ get_list(list(col1and2),0), ")"
    print "   f1|f2: " + str(len(col1or2)) + " (e.g. "+ get_list(list(col1or2),0), ")"
    print "   f1-f2: " + str(len(col1min2)) + " (e.g. "+ get_list(list(col1min2),0), ")"
    print "   f2-f1: " + str(len(col2min1)) + " (e.g. "+ get_list(list(col2min1),0), ")"
