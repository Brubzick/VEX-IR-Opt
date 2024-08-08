import angr
from whole_process_2 import VexOptHash2
from whole_process_3 import VexOptHash3

proj1 = angr.Project('./C_files/dfs', auto_load_libs=False)
proj2 = angr.Project('./C_files/dfs3', auto_load_libs=False)

b1 = VexOptHash3(proj1)
b2 = VexOptHash3(proj2)

l1 = len(b1)
l2 = len(b2)
l = max(l1, l2)


for i in range(0,l):
    if ((i < l1)&(i < l2)):
        print(b1[i],'||||',b2[i])
    elif (i < l1):
        print(b1[i])
    else:
        print('             ','||||',b2[i])
