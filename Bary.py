import itertools
import fnmatch
import os

from pyms.Experiment.IO import load_expr
from pyms.Peak.List.DPA.Class import PairwiseAlignment, Alignment
from pyms.Peak.List.DPA.Function import align_with_tree, exprl2alignment


def glob(glob_pattern, directoryname):
    '''
    Walks through a directory and its subdirectories looking for files matching
    the glob_pattern and returns a list=[].

    :param directoryname: Any accessible folder name on the filesystem.
    :param glob_pattern: A string like "*.txt", which would find all text files.
    :return: A list=[] of absolute filepaths matching the glob pattern.
    '''
    matches = []
    names = []
    for root, dirnames, filenames in os.walk(directoryname):
        for filename in fnmatch.filter(filenames, glob_pattern):
            absolute_filepath = os.path.join(root, filename)
            matches.append(absolute_filepath)

            name = absolute_filepath.rsplit('/CDF/expr')[-1]
            names.append(name)

    return matches, names




def lil_dictor(cdfs):

    breed_dict = {}
    name_dict = {}


    for i in cdfs:
        a = i.split('-')
        print a
        b = list(a)
        #print a
        print b[1]

        if b[1] in breed_dict:
            expr = load_expr(i)
            name_dict[b[1]].append(i)
            breed_dict[b[1]].append(expr)
        else:
            expr = load_expr(i)
            name_dict[b[1]] = [i]
            breed_dict[b[1]] = [expr]

    #print breed_dict
    return breed_dict, name_dict

def dictor(breed, cdfs):


    breed_dict = {}
    name_dict = {}
    b_list = []

    for i in cdfs:
        if str(breed) in str(i):

            b_list.append(i)



    for ber in b_list:
        a = ber.split('-')
        print a
        b = list(a)
        #print a
        print b[1]

        if b[1] in breed_dict:
            expr = load_expr(ber)
            name_dict[b[1]].append(ber)
            breed_dict[b[1]].append(expr)
        else:
            expr = load_expr(ber)
            name_dict[b[1]] = [ber]
            breed_dict[b[1]] = [expr]

    #print breed_dict
    return breed_dict, name_dict

def aligner(exprs, bers, names):

    mod = 2.5
    gp = 0.30

    mA = 10.0

    # print exprs
    # print names


    for dict, n, b in zip(exprs, names, bers):
        print dict
        print '\n'
        print b
        print n
        print '\n'


        #for item, na in zip(dict.items(), n.items()):
        for item, v in dict.items():
            print item
            # print v
            F1 = exprl2alignment(v)
            T1 = PairwiseAlignment(F1, mod, gp)
            A1 = align_with_tree(T1, min_peaks=2)

            A1.write_csv('/home/juicebox/Desktop/Acinis/CDFdata/CDF/output/'+item+'rt.csv', '/home/juicebox/Desktop/Acinis/CDFdata/CDF/output/'+item+'area.csv')

            # for typ, rep in item:
            #     print 'k=' + typ + '\n'
            #     print 'v=' + rep + '\n'

        # for key, values in dict:
        #     print 'k='+key+'\n'
        #     print 'v='+values+'\n'




            # for expr, berry in zip(item, na):
            #     print "expr"+str(expr)
            #     print "berry"+str(berry)



            # F1 = exprl2alignment(item)
            # T1 = PairwiseAlignment(F1, mod, gp)
            # A1 = align_with_tree(T1, min_peaks=2)
            #
            #
            # A1.write_csv('/home/juicebox/Desktop/Acinis/CDFdata/CDF/output/', '/home/juicebox/Desktop/Acinis/CDFdata/CDF/output/clean_p110_s30_%2_n3area.csv')

def align2(exprs, names, bers):
    min = 1.5
    mod = 2.5

    gp = 0.30

    #mA = 10.0

    print()

    for dict, n, b in zip(exprs, names, bers):
        #print ('dict='+dict)
        #print '\n'
        #print ('b='+str(b))
        print ('b='+str(b))
        print '\n'
        T2 = []


        #for item, na in zip(dict.items(), n.items()):
        for item, v in dict.items():
            print ('item='+str(item))
            # print v
            F1 = exprl2alignment(v)
            T1 = PairwiseAlignment(F1, min, gp)
            A1 = align_with_tree(T1, min_peaks=2)
            T2.append(A1)

        T3 = PairwiseAlignment(T2, mod, gp)
        A2 = align_with_tree(T3, min_peaks=2)

        # print'b='+str(b)
        # print'n=' + str(n)

        A2.write_csv('/home/juicebox/Desktop/Acinis/CDFdata/CDF/output2/'+str(b)+'_7035rt.csv', '/home/juicebox/Desktop/Acinis/CDFdata/CDF/output2/'+str(b)+'_7035area.csv')





def alignAll(exprs, bers, names):
    mod = 2.5
    gp = 0.30

    mA = 10.0

    bG = []
    Tall = []

    for dict, n, b in zip(exprs, names, bers):
        print dict
        print '\n'
        #print b
        print n
        print '\n'

        T2 = []
        # for item, na in zip(dict.items(), n.items()):
        for item, v in dict.items():
            print item
            # print v
            F1 = exprl2alignment(v)
            T1 = PairwiseAlignment(F1, mod, gp)
            A1 = align_with_tree(T1, min_peaks=3)
            T2.append(A1)

        T3 = PairwiseAlignment(T2, mod, gp)
        A2 = align_with_tree(T3, min_peaks=4)
        Tall.append(A2)

    T4 = PairwiseAlignment(Tall, mA, gp)
    A3 = align_with_tree(T4, min_peaks=5)
    #

        # print'b='+str(b)
        # print'n=' + str(n)

    #A3.write_csv('/home/juicebox/Desktop/Acinis/CDFdata/CDF/output2/All51_rt.csv', '/home/juicebox/Desktop/Acinis/CDFdata/CDF/output2/All51_area.csv')








def main():

    berrs = ['bk', 'be', 'rp', 'sw']

    folder_with_cdffiles = '/home/juicebox/Desktop/Acinis/CDFdata/CDF/expr7035'

    cdfs, names = glob(glob_pattern="*1.cdf7035", directoryname= folder_with_cdffiles)

    print cdfs

    thictionary = []
    naNames = []


    for i in berrs:
        b, n = dictor(i, cdfs)
        thictionary.append(b)
        naNames.append(n)

    # b, n = lil_dictor(cdfs)
    # print('b='+str(b))
    # print('n='+str(n)+'\n')
    # align2(b, n)


       # print 'n='+str(n)
       #
       #  print '\n'
       #  for k,v in b.items():
       #      print k, v

    print naNames
    # print len(naNames)
    # print '\n'
    # print thictionary
    # print len(thictionary)
    # print '\n'


    #aligner(thictionary, naNames, berrs)
    align2(thictionary, naNames, berrs)
    #alignAll(thictionary, naNames, berrs)

    # for i in thictionary:
    #     print '\n'+str(i)

if __name__ == "__main__":
    main()