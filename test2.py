import angr
from IR_opt import ClearMinus, RemoveRedunantWrite, RemoveBitwidth, RemoveCopy, ConstFolding, LLEliminate, LSEliminate, SSEliminate
from VEX_opt.remove_unrelated_1 import RmUnrelated
from VEX_opt.rm_redundant_wr_2 import RmRedunantR
from VEX_opt.rm_bitwidth_op_3 import RmBitwidthOp
from VEX_opt.Put_Get_combine_4 import PGComb
from VEX_opt.rm_copy_5 import RmCopy
from VEX_opt import const_folding_6
from VEX_opt.Get_Get_Elimination_7 import GGEliminate
from VEX_opt import Load_Store_Op_8

proj1 = angr.Project('./C_files/dfs', auto_load_libs=False)
proj2 = angr.Project('./C_files/dfs', auto_load_libs=False)

cfg1 = proj1.analyses.CFGFast(normalize=True)
cfg2 = proj2.analyses.CFGFast(normalize=True)

blockList1 = []
blockList2 = []

for node in cfg1.nodes():
    if (not node.is_simprocedure):
        block = node.block.vex.statements
        block = ClearMinus(block)
        block = RemoveRedunantWrite(block)
        block = RemoveBitwidth(block)
        block = RemoveCopy(block)
        block = ConstFolding(block)
        block = LLEliminate(block)
        block = LSEliminate(block)
        block = SSEliminate(block)
        blockList1.append(block)

for node in cfg2.nodes():
    if (not node.is_simprocedure):
        block = node.block.vex.statements
        block = RmUnrelated(block)
        block = RmRedunantR(block)
        block = RmBitwidthOp(block)
        block = PGComb(block)
        block = RmCopy(block)
        block = const_folding_6.ConstFloding(block)
        block = GGEliminate(block)
        block = Load_Store_Op_8.LLEliminate(block)
        block = Load_Store_Op_8.LSEliminate(block)
        block = Load_Store_Op_8.SSEliminate(block)
        blockList2.append(block)

l = len(blockList1)
l1 = 0
l2 = 0
for i in range(0, l):
    print(len(blockList1[i]), len(blockList2[i]))
    l1 += len(blockList1[i])
    l2 += len(blockList2[i])

print(l1, l2)




