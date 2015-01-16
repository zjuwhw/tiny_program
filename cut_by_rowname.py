#author: zjuwhw
#2015-01-16
USAGE = '''cut_by_colname.py --- a tiny program to exact the column accoading the first row
USAGE:
    python %s [--output=#] inputfile the_selected_colnames(one or more)
Default:
--output: stdout
the_selected_colnames: "NullCharacter" means ""
'''

import os, sys, getopt

def list_in(onelist, twolist):
    element_in = []
    element_notin = []
    switch = True
    for element in onelist:
        if element in twolist:
            element_in.append(element)
        else:
            element_notin.append(element)
            switch = False
    if switch:
        return True
    else:
        print "These colnames are in the first line:" + "\t".join(element_in)
        print "However, these colnames are NOT in the first line:" + "\t".join(element_out)
        return False
def list_index(onelist, twolist):
    index_list = []
    for a in onelist:
        index_list.append(twolist.index(a))
    return index_list

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print USAGE % sys.argv[0]
        sys.exit(1)
    
    #default
    f_output = sys.stdout
    
    opts, args = getopt.getopt(sys.argv[1:], "", ["output="])
    f_input = open(args[0])
    select_colnames = args[1:]   
    for o,a in opts:
        if o == "--output":
            f_output = open(a, "w")
    
    switch = True
    for line in f_input:
        linelist = line.rstrip().split("\t")
        if switch:
            if not list_in(select_colnames, linelist):
                sys.exit(1)
            select_index = list_index(select_colnames, linelist)
            print >> f_output, "\t".join(select_colnames)
            switch = False
        else:
            output_container = []
            for m in select_index:
                output_container.append(linelist[m])
            print >> f_output, "\t".join(output_container)
    f_input.close()
    f_output.close()