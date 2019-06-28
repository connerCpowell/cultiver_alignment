from scipy.spatial import distance_matrix
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import pdist, squareform
from matplotlib import pyplot as plt
from collections import OrderedDict

def get_data(line, num):
    try:
        return float(line.split('\t')[num].strip())
    except:
        return 0

with open('/home/juicebox/Desktop/Acinis/CDFdata/be2_csv/blue_p120s30pe10n3_p23_area.csv', 'r') as f:
    i = 0
    species_dict = OrderedDict()
    list_o_species = []
    total = 0

    for line in f:
        #print('l='+line)
        num = line.count('\t')
        #print('num='+str(num))

        if i != 0:
            count = 0
            for j in range(num+1):
                #y =  get_data(line, j)
                #print('y='+str(y)+'\n')
                species_dict[list_o_species[j]].append(get_data(line, j))
                #print('j='+str(j))
        else:
            for j in range(num+1):
                species_dict[line.split('\t')[j].strip()] = []
                u = line.split('\t')[j].strip()
                #print('u='+str(u)+'\n')
                x = line.split('\t')[j].strip()
                list_o_species.append(x)
        i = 1

#for key, val in species_dict.items():
    #print(key, '>', val)


dm_list =[]
names = []
name2 = []


i = 0
for l in species_dict:
    if i > 1:
        dm_list.append(species_dict[l])
        names.append(l)
    i+=1
    #print i


# print(names)
# print('names=',len(names))
# print(dm_list)
# print('dm=',len(dm_list))

d = distance_matrix(dm_list, dm_list)
l = pdist(dm_list)
pm = squareform(l)

print('d=',d)
print('l=',l)
print('pm',pm)

linked = linkage(pm, 'ward')

#labelList = range(1, 25)

plt.figure(figsize=(12,12))
dendrogram(linked,
            orientation='top',
            labels=names,
            #distance_sort='descending',
            show_leaf_counts=True)

#plt.savefig('blue_p120s30pe10n3_p34.png')
plt.savefig('d_ward.jpg')
plt.show()