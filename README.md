VEX IR 优化方法的步骤实现在VEX_opt文件夹中，整合在外面的Vex_opt.py中。
输入的参数是一个列表，列表的元素是一个基本块的或连续的VEX IR语句。其中，列表的元素，即VEX IR语句，是angr中一个类stmt的对象。
