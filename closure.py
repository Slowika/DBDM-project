import os
import sys

REPOSITORY_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)))
EXAMPLES_DIR = os.path.join(REPOSITORY_DIR, "examples")

"""
Helping functions
"""
def fds_to_dict(fds):
    fds_dict = dict()

    if type(fds) == "<class 'list'>":
        print ("TODO: FDs read from the standard input")
    else:
        for line in fds:
            if line != "" and line[0].isalnum():
                line = line.split('->')
                keys = line[0].split(' ')

                if len(line[1])>1 and line[1][-1].isalnum() == False:
                    values = line[1][:-1].split(' ')
                else:
                    values = line[1].split(' ')

                keys = (tuple(filter(lambda x: x.isalnum()==True, keys)))
                values = (set(filter(lambda x: x.isalnum()==True, values)))
                fds_dict[keys] = values
    return fds_dict

"""
Main functions
"""
"""
def Closure(fds, atts):
    Cl = atts
    done = False
    while (not done):
        done = True
        for key in fds:
            #key is a tuple and to use issubset you need two sets!!!!
            keys = set()
            for a in range (len(key)): #how to "parcourir" all elt in a tuple??
                keys.add(a)
            #keys is a set and key is a tuple with the same element. we can use keys now to know if it's a subset of Cl and Z
            if (keys.issubset(Cl.intersection(fds[key])) and not ((Cl.intersection(fds[key])).issubset(Cl))):
                Cl = Cl.union(fds[key])
                done = False
    return Cl
"""


"""
Main program
"""

if __name__ == "__main__":
    option = sys.argv[1][1:]
    print ("The chosen option: " + option)
    if option == 'generate':
        n = sys.argv[2]
        print ("Generate a particular set of FDs for the integer: " + n)
    else:
        input = sys.argv[2]

    if input == "~":
        #TODO
        fds_list = []
        for fd in sys.argv[3:]:
            fds_list.append(fd)

    elif input[-4:] == ".txt":
        print ("Reading FDs from the file: " + input)
        file = open(EXAMPLES_DIR + "/" +input, "r")
        print (fds_to_dict(file))

    if len(sys.argv) > 3:
        atts = set()
        for att in sys.argv[3:]:
            if att.isalnum():
                atts.add(att)
        print ("Set of attributes: " + str(atts))

