import angr
import os

maxSize = 1024 * 1000 # maximum size (b) of file that would be loaded

def is_ELF(filePath):
    f = open(filePath, 'rb')
    head = f.read(4)
    f.close()
    headList = [head[0], head[1], head[2], head[3]]
    if headList == [127,69,76,70]:
        return True
    return False

foldPath = '../bin_range/arm'

all_files = os.listdir(foldPath)

projName = {} # map the proj/cfg and its file name
cfgs = []

for file in all_files:
    filePath = os.path.join(foldPath, file)
    if is_ELF(filePath):
        if (os.path.getsize(filePath) <= maxSize):
            proj = angr.Project(filePath, auto_load_libs=False)
            cfg = proj.analyses.CFGFast(normalize=True)
            projName[proj] = file
            cfgs.append(cfg)

for cfg in cfgs:
    print(cfg.graph)




