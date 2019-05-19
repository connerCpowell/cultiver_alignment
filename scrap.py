from scipy.spatial import distance_matrix
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt
from collections import OrderedDict

def distance(lista, listb):
    return sum((b - a) ** 2 for a,b in zip(lista, listb)) ** .5

def get_data(line, num):
    try:
        return float(line.split('\t')[num].strip())
    except:
        return 0

with open('/home/juicebox/Desktop/Acinis/CDFdata/sw2_csv/p125_s100_p3_p10_area.csv', 'r') as f:
    i = 0
    species_dict = OrderedDict()
    list_o_species = []
    for line in f:
        if i != 0:
            count = 0
            for j in range(0, 21):          #rasp
            #for j in range(0, 14)
            #for j in range(0, 38):
            #for j in range(0, 94):         #all
                #y =  get_data(line, j+2)
                #print('y='+str(y)+'\n')
                #count += 1
                #print('c='+str(count))
                species_dict[list_o_species[j]].append(get_data(line, j+2))
        else:
            for j in range(2, 23):          #rasp
            #for j in range(0, 16)
            #for j in range(2, 40):
            #for j in range(2, 96):         #all
                species_dict[line.split('\t')[j].strip()] = []
                u = line.split('\t')[j].strip()
                print('u='+str(u)+'\n')
                list_o_species.append(line.split('\t')[j].strip())
            print(len(list_o_species))
        i = 1
    print( species_dict)


# for species1 in species_dict:
#     for species2 in species_dict:
#         d = distance(species_dict[species1], species_dict[species2])
#         print('The distance between ' + species1 + ' and ' + species2 + ' is: ' + str(d))
#     print('\n')

dm_list =[]
names = []
name2 = []

for l in species_dict:
    #print l, species_dict[l]
    dm_list.append(species_dict[l])
    names.append(l)
    #print(l)
    # if l.endswith('1.cdf'):
    #     print('yes')
    # else:
    #     print('no')

for n in names:
    if n.endswith('1.cdf'):
        print('yes')
        m = n.strip('-')
        #print('m='+m)
        na = m[3:-4]
        #print('na='+na)
    name2.append(na)

print(name2)

d = distance_matrix(dm_list, dm_list)
#print d

linked = linkage(d, 'average')

labelList = range(1, 25)

plt.figure(figsize=(10,10))
dendrogram(linked,
            orientation='top',
            labels=name2,
            distance_sort='descending',
            show_leaf_counts=True)

plt.savefig('straw_p125_s100_p3_p10.png')
plt.show()