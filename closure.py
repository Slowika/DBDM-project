#!/usr/bin/env python

import os
import sys
import time
import random
import matplotlib.pyplot as plt

REPOSITORY_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)))
EXAMPLES_DIR = os.path.join(REPOSITORY_DIR, "examples")

"""
Helping functions
"""
def fds_to_dict(fds):
    fds_dict = dict()

    for line in fds.split('\n'):
        if line != "" and line[0].isalnum():
            line = line.split('->')
            keys = line[0].split(' ')
            values = line[1].strip()
            values = line[1].split(' ')

            keys = (frozenset(filter(lambda x: x.isalnum()==True, keys)))
            values = (frozenset(filter(lambda x: x.isalnum()==True, values)))
            fds_dict[keys] = values
    return fds_dict

"""def timing(f):
    def wrap(*args):
        file = open('results.csv', 'a')
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print ('%s function took %0.3f ms' % (f.__name__, (time2-time1)*1000.0))
        file.write('%s function took %0.3f ms\n' % (f.__name__, (time2-time1)*1000.0))
        return ret
    return wrap
"""
"""
Main functions
"""

#@timing
def Closure(fds, atts):
    if len(fds) == 0:
        return atts
    Cl = atts
    done = False
    while (not done):
        done = True
        for key, value in fds.items():
            if key.issubset(Cl) and not value.issubset(Cl):
                Cl = Cl.union(value)
                done = False
    return Cl

def construct_indices(fds):
    if len(fds) == 0:
        return ({},{})
    count = {}
    lista = {}
    for w, z in fds.items():
        count[(w,z)] = len(w)
        for A in w:
            if len(lista) == 0 or A not in lista:
                lista[A] = []
            lista[A].append(tuple([w,z]))
    return (count, lista)

#@timing
def Closure_improved(fds, atts):
    if len(fds) == 0:
        return atts

    count = construct_indices(fds)[0]
    lista = construct_indices(fds)[1]

    closure = atts
    update = atts
    while len(update) != 0:
        for A in update:
            update = update.difference(A)
            if A in lista:

                for (w, z) in lista[A]:
                    count[(w,z)] = count[(w,z)] - 1
                    if count[(w,z)] == 0:
                        update = update.union(z.difference(closure))
                        closure = closure.union(z)
    return closure

def generate(n):
    fds_dict = {}
    keys = [i for i in range(0, int(n))]
    for key in keys:
        fds_dict[frozenset([key])] = frozenset([key+1])
    return fds_dict

def check(G1, x, y):
    closureX = Closure_improved(G1, x)
    return y.issubset(closureX)

def minimize(fds):
    G = {}
    for x, y in fds.items():
        G[x] = Closure_improved(fds, x)
    for x, y in G.items():
        G1 = G.copy()
        del G1[x]
        if (check(G1, x, y) == True):
            del(G[x])
    return G

def reduce(fds):
    min = fds.copy()
    for x, y in min.items():
        w = y.copy()
        del min[x]
        for a in y:
            min1 = min.copy()
            min1.update({x: w.difference(a)})
            if (check(min1, x, y) == True):
                w = w.difference(a)
        min.update({x: w})
    return min

def schema(fds):
    atts = set()
    for x, y in fds.items():
        atts = atts.union(x).union(y)
    return atts

def isKeyOfSchema(fds, atts):
    return schema(fds).issubset(Closure_improved(fds, atts))

""" either x -> y is a trivial fd (y belongs to x) either x is a key for schema """
def isBCNF(fds, atts):
    for x, y in fds.items():
        if not(x.issubset(y)): 
            if not(isKeyOfSchema(fds, atts)):
                return False
    return True

def frozensetInAttrs(frset):
    resultat=''
    for i in frset:
        resultat+=str(i)+', '
    return(resultat[:-2])

"""
Main program
"""

if __name__ == "__main__":
    option = sys.argv[1][1:]
    #print ("The chosen option: " + option)
   
    if option == 'generate':
        n = sys.argv[2]
        #print ("Generate a particular set of FDs for the integer: " + n)
        fds = generate(n)
        keys = fds.keys()
        random.shuffle(keys)
        for key in keys:
            print (frozensetInAttrs(key) +" -> " +frozensetInAttrs(fds[key]))

    else:
        input = sys.argv[2]

        if input == "-":
            file = sys.stdin.read()
            fds = fds_to_dict(file)
     
        elif input[-4:] == ".txt":
            #print ("Reading FDs from the file: " + input)
            file = open(EXAMPLES_DIR + "/" +input, "r")
            fds = fds_to_dict(file.read())
            print (fds)
            
        atts = set()
        if len(sys.argv) > 3:
            for att in sys.argv[3:]:
                if att.isalnum():
                    atts.add(att)
            #print ("Set of attributes: " + str(atts))

        if option == "naive":
            print ("Naive closure: " + str(Closure(fds, atts)))
        elif option == "improved":
            print ("Improved closure: " + str(Closure_improved(fds, atts)))
        elif option == "normalize":
            fds=reduce(minimize(fds))
            for key in fds.keys():
                print (frozensetInAttrs(key) +" -> " +frozensetInAttrs(fds[key]))

            
        elif option == "compare":
            file = open('results.csv', 'w')
            atts = set()
            x = [i for i in range(9)]
            for i in x:
                atts.add(str(i))
                Closure(fds, atts)
                Closure_improved(fds, atts)
            #sample results
            closure = [0.035, 0.042, 0.018, 0.031, 0.028, 0.015, 0.026, 0.012, 0.011]
            closure_improved = [0.143, 0.121, 0.147, 0.141, 0.137, 0.134, 0.102, 0.136, 0.121]
            plt.plot(x, closure, 'r')
            plt.plot(x, closure_improved, 'b')
            plt.show()

    try:
        sys.stdout.close()
    except:
        pass
    try:
        sys.stderr.close()
    except:
        pass
