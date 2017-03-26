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

                keys = (frozenset(filter(lambda x: x.isalnum()==True, keys)))
                values = (frozenset(filter(lambda x: x.isalnum()==True, values)))
                fds_dict[keys] = values
    return fds_dict

"""
Main functions
"""

def Closure(fds, atts):
    Cl = atts
    done = False
    while (not done):
        done = True
        for key, value in fds.items():
            if key.issubset(Cl) and not value.issubset(Cl):
                Cl = Cl.union(value)
                done = False
    return Cl

def Closure_improved(fds, atts):
    count = {}
    lista = {}
    for w, z in fds.items():
        count[(w,z)] = len(w)
        for A in w:
            if len(lista) == 0 or A not in lista:
                lista[A] = []
            lista[A].append(tuple([w,z]))
    closure = atts
    update = atts
    while len(update) != 0:
        for A in update:
            update = update.difference(A)
            for (w, z) in lista[A]:
                count[(w,z)] = count[(w,z)] - 1
                if count[(w,z)] == 0:
                    update = update.union(z.difference(closure))
                    closure = closure.union(z)
    return closure

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
            fds = fds_to_dict(file)
            print (fds)

        if len(sys.argv) > 3:
            atts = set()
            for att in sys.argv[3:]:
                if att.isalnum():
                    atts.add(att)
            print ("Set of attributes: " + str(atts))

        if option == "naive":
            print ("Naive closure: " + str(Closure(fds, atts)))
        elif option == "improved":
            print ("Improved closure: " + str(Closure_improved(fds, atts)))

