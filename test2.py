import angr
from vex_opt import VexOpt
from find_longest_path import FindLongest
from get_strands import GetStrands
from strand_normalization import TypeNorm
from hash import GetHashedStrands

proj1 = angr.Project('./C_files/dfs', auto_load_libs=False)
proj2 = angr.Project('./C_files/hello3', auto_load_libs=False)

cfg1 = proj1.analyses.CFGFast(normalize=True)
cfg2 = proj2.analyses.CFGFast(normalize=True)

p1 = FindLongest(cfg1)
p2 = FindLongest(cfg2)

b1 = []
b2 = []

for node in p1:
    if (not node.is_simprocedure):
        b1.extend(node.block.vex.statements)
for node in p2:
    if (not node.is_simprocedure):
        b2.extend(node.block.vex.statements)

b1 = VexOpt(b1)
b2 = VexOpt(b2)

# for node in p1:
#     if (not node.is_simprocedure):
#         block = VexOpt(node.block.vex.statements)
#         b1.append(block)
# for node in p2:
#     if (not node.is_simprocedure):
#         block = VexOpt(node.block.vex.statements)
#         b2.append(block)

strands1 = GetStrands(b1)
strands2 = GetStrands(b2)

for i in range(0, len(strands1)):
    for j in range(0, len(strands1[i])):
        strands1[i][j] = TypeNorm(strands1[i][j])
for i in range(0, len(strands2)):
    for j in range(0, len(strands2[i])):
        strands2[i][j] = TypeNorm(strands2[i][j])

for i in range(0, len(strands1)):
    strands1[i] = ''.join(strands1[i])
for i in range(0, len(strands2)):
    strands2[i] = ''.join(strands2[i])

sSet1 = set(strands1)
sSet2 = set(strands2)
print(len(sSet1), len(sSet2))

point = 0
for s2 in sSet2:
    mp = 0
    for s1 in sSet1:
        if s2 == s1:
            mp = 1
            break
        else:
            if s1 in s2:
                tp = len(s1)/len(s2)
                if tp > mp:
                    mp = tp
            elif s2 in s1:
                tp = len(s2)/len(s1)
                if tp > mp:
                    mp = tp
    point += mp

print(point)

hashedSet1 = set(GetHashedStrands(strands1))
hashedSet2 = set(GetHashedStrands(strands2))

intersection = hashedSet1.intersection(hashedSet2)

print(len(intersection),len(hashedSet1), len(hashedSet2))