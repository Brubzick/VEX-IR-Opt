import angr
from IR_opt import VEXOpt

proj = angr.Project('./dfs', auto_load_libs=False)

cfg = proj.analyses.CFGFast(normalize=True)

for node in cfg.nodes():
    if (not node.is_simprocedure):
        for stmt in node.block.vex.statements:
            if stmt.tag =='Ist_Store':
                print(stmt, stmt.addr)
            elif stmt.tag == 'Ist_WrTmp':
                if stmt.data.tag == 'Iex_Load':
                    print(stmt, stmt.data.addr)