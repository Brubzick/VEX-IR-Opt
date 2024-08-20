import angr

p1 = angr.Project('../C_bin/dfs_gcc_O0', auto_load_libs=False)
p2 = angr.Project('../C_bin/dfs_gcc2_O0', auto_load_libs=False)

cfg1 = p1.analyses.CFGFast(normalize=True)
cg1 = cfg1.functions.callgraph

cfg2 = p2.analyses.CFGFast(normalize=True)
cg2 = cfg2.functions.callgraph

edge = list(cg1.edges)[0]

print(hex(edge[0]), hex(edge[1]))

# addrs1 = cg1.nodes
# addrs2 = cg2.nodes

# for addr in addrs1:
#     func = cfg1.functions.function(addr)
#     if (not func.is_simprocedure):
#         print(func.name)
#         for n in func.nodes:
#             if hasattr(n, 'is_hook'):
#                 if (not n.is_hook):
#                     print(n)
    
# print('=======================================================================================================')

# for addr in addrs2:
#     func = cfg2.functions.function(addr)
#     if (not func.is_simprocedure):
#         print(func.name)
#         for n in func.nodes:
#             if hasattr(n, 'is_hook'):
#                 if (not n.is_hook):
#                     print(n)