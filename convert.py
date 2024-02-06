import re
from ete3 import Tree
import argparse

def convert_nexus_to_nwk_label_mut(file,outputfile):
    with open(file) as f:
        for line in f:
            if 'Tree tree1' in line:
                tree=line
                break
    tree=re.sub(r' Tree tree1=','',tree)
    tree=re.sub(r'\[&mutations=\"\"\]','',tree)
    tree=re.sub(r',([A-Z\-]\d+?[\-A-Z])',r'@\1',tree)
    tree=re.sub(r'(\:[0-9\.]+?)\[&mutations=\"(.+?)\"\]',r'@\2\1',tree)
    #tree=re.sub(r'\[&mutations=\"',r'@',tree)
    #tree=re.sub(r'(\:[0-9\.]+?)(@.+?),',r'\2\1,',tree)
    #tree=re.sub(r'["]]','',tree)
    tree=re.sub(r'NODE_0000',r'Node',tree)
    f=open(outputfile,'w')
    f.write(tree)
    f.close()
    return

#use argparse to get the input file and output file
parser = argparse.ArgumentParser(description='convert nexus tree to newick tree with mutation label')
parser.add_argument('inputfile', type=str, help='input file')
parser.add_argument('outputfile', type=str, help='output file')
args = parser.parse_args()
convert_nexus_to_nwk_label_mut(args.inputfile,args.outputfile)
#convert_nexus_to_nwk_label_mut('tree.nexus','tree.nwk')