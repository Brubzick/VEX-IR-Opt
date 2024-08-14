import angr
from process_strands import VexOptStrands
from strands_compare import Compare

proj1 = angr.Project('../bin_range/file/file_5.38_x86', auto_load_libs=False)
proj2 = angr.Project('../bin_range/file/file_5.38_arm', auto_load_libs=False)
proj3 = angr.Project('../C_bin/other_source/whatever_gcc_O0', auto_load_libs=False)
proj4 = angr.Project('../C_bin/dfs_gcc_O0', auto_load_libs=False)
proj5 = angr.Project('../C_bin/dfs_gcc2_O1', auto_load_libs=False)

blockList1 = VexOptStrands(proj1)
blockList2 = VexOptStrands(proj2)
blockList3 = VexOptStrands(proj3)
blockList4 = VexOptStrands(proj4)
blockList5 = VexOptStrands(proj5)


base = [blockList1, blockList2, blockList3, blockList4, blockList5]
simScore = Compare(blockList1, blockList2, mode='small', base=base)

print(simScore)