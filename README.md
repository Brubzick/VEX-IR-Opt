VEX IR 优化方法的步骤实现在VEX_opt文件夹中，整合在外面的Vex_opt.py中。  
VEX_opt文件夹中，文件名的最后一个数字表示步骤顺序：
1. 清除无关的语句
2. 清除多余的寄存器写入
3. 移除比特宽度和顺序的操作
4. 移除寄存器读写的冗余
5. 移除冗余的复制变量的操作
6. 常数折叠
7. 移除寄存器读取的冗余
8. 移除内存读写相关的冗余
部分的步骤与顺序和专利申请书里写的有点不一样。  

输入的参数是一个列表，列表的元素是一个基本块的或连续的VEX IR语句。其中，列表的元素，即VEX IR语句，是angr中一个类的对象，包含了.tag等属性。  
具体的实现方法为(例)：  
```python
import angr  
proj = angr.Project('path_to_binary', auto_load_libs=False)  
cfg = proj.analyses.CFGFast(normalize=True)  
for node in cfg.nodes():  
    if (not node.is_simprocedure):  
        block = node.block.vex.statements
```
上面的block即为一个符合要求的输入，详见：https://docs.angr.io/

