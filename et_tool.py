from ete3 import Tree, TreeStyle
import pandas
import argparse
import itertools

def add_paranthesis (s):
    """
    The function "add_paranthesis" takes a string "s" and
    add paranthesis, i.e., "(s)"
    """
    return('(' + s + ')')

def str_append_helper (s,l):
    """
    This function take a string (e.g., 'abc') and list (e.g., ['s1', 's2']) and
    append the elements of the list with the string in following format:
    ['(abc)s1', (abc)s2]
    """
    out = []
    for i in l:
        out.append (add_paranthesis(s + i))
    return(out)



def make_tree (sys):
    """
    This function takes the system description in the following format (csv):
            componenet 1, component 2
            ---------------------------
           |  Sensor_1  , Sensor_2     (first row for component names)
  State 1  |   open     ,  misaligned
  State 2  |   short    ,  low_voltage
  State 3  |   stuck    ,  noisy

    and convert this to "Newick Tree" format which can then be visualized in a
    different ways using "ete3" library.
    """
    sys.reverse()
    head, *tail =sys
    s = (tuple(head))
    init_str = add_paranthesis(add_paranthesis (','.join(s)))
    str_iter = [init_str]
    for elements in tail:
        intermediate_str = []
        for st in str_iter:
            intermediate_str = intermediate_str + str_append_helper(st,elements)
            next_iter = add_paranthesis(add_paranthesis (','.join(intermediate_str)))
            str_iter = [next_iter]
    return(str_iter)

# df.head() -- gives full system

def get_system(name):
    data = name
    df = pandas.read_csv(data)
    comp_states = []
    components = df.columns.tolist()
    for i in components:
        comp_states.append(list(df[i]))
    all_paths = list(itertools.product(*comp_states))
    return (df,components,comp_states,all_paths)





parser = argparse.ArgumentParser(description='Event Tree Analysis Tool')

parser.add_argument('-s', action="store", dest="system",
                help='System Description -- components and associated states')
parser.add_argument('-o', action="store", dest="out",
                help='Name of the output analysis file')

args = parser.parse_args()

sys_txt = '''\
*********************************************************************
                                System Description
*********************************************************************
'''

et_txt = '''\
*********************************************************************
                                Event Tree Graph
*********************************************************************
'''

paths_txt = '''\
*********************************************************************
                                All Paths
*********************************************************************
'''

some_space = '''\n \n'''


gsystem = get_system (args.system)
t = make_tree(gsystem[2])
tre = t[0] + 'SYSTEM' + ';'
rtree = Tree(tre, format=1)

outfile = open(args.out, "w+")


outfile.write(sys_txt)
outfile.write(gsystem[0].to_string())

outfile.write(some_space)
outfile.write(et_txt)

outfile.write(rtree.get_ascii(show_internal=True))

outfile.write(some_space)
outfile.write(paths_txt)
outfile.write('\n')


m = 1
for j in gsystem[3]:
    n = 'Path ' + str(m) + ' = '
    outfile.write(n + str(j) + '\n')
    m = m + 1


#print (rtree.get_ascii(show_internal=True))








#    ex = [l1,l2,l3,l4,l5]
#    xx = make_tree (ex)
#    print(xx[0])

#    tre = xx[0] + 'SYSTEM' + ';'

#    rtree = Tree(tre, format=1)

#    print (rtree.get_ascii(show_internal=True))
