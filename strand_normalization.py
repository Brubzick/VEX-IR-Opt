
def GetName(stmt_str):

    stmt_str = stmt_str.replace(',', ' ')
    stmt_str = stmt_str.replace('(', ' ')
    stmt_str = stmt_str.replace(')', ' ')

    variables = []
    stmt_str_list = stmt_str.split()

    for i in range(0, len(stmt_str_list)):
        if stmt_str_list[i][0] == 't':
            variables.append(stmt_str_list[i])
    
    return variables
        

def TypeNorm(stmt):
    stmt_str = str(stmt)
    tag = stmt.tag
    norm = tag

    match tag:
        case 'Ist_Put':
            if stmt.data.tag == 'Iex_Const':
                norm = 'Put.cons'
            else:
                norm = 'Put'  

        case 'Ist_PutI':
            stmt_str_list = stmt_str.split()
            for i in range(0, len(stmt_str_list)):
                if stmt_str_list[i] == '=':
                    tmp = stmt_str_list[i+1]
                    break
            if tmp[0:2] == '0x':
                norm = 'PutI.cons'
            else:
                norm = 'PutI'  

        case 'Ist_WrTmp':
            exType = stmt.data.tag
            match exType:
                case 'Iex_Get':
                    norm = 'Get'
                case 'Iex_RdTmp':
                    norm = 'Copy'
                case 'Iex_Const':
                    norm = 'Const'
                case 'Iex_Load':
                    norm = 'Load'
                case 'Iex_CCall':
                    norm = 'CCall'
                case 'Iex_Unop':
                    op = str(stmt.data.op)
                    for i in range(len(op)-1,-1,-1):
                        if (not op[i:].isdigit()):
                            break
                    norm = op[:i+1]
                case 'Iex_Binop':
                    op = str(stmt.data.op)
                    for i in range(len(op)-1,-1,-1):
                        if (not op[i:].isdigit()):
                            break
                    norm = op[:i+1]
                case 'Iex_Triop':
                    op = str(stmt.data.op)
                    for i in range(len(op)-1,-1,-1):
                        if (not op[i:].isdigit()):
                            break
                    norm = op[:i+1]
                case 'Iex_Qop':
                    op = str(stmt.data.op)
                    for i in range(len(op)-1,-1,-1):
                        if (not op[i:].isdigit()):
                            break
                    norm = op[:i+1]
                case _:
                    norm = stmt.data.tag

        case 'Ist_Store':
            if stmt.data.tag == 'Iex_Const':
                norm = 'STle.cons'
            else:
                norm = 'STle' 

        case _:
            norm = stmt.tag
    
    return norm


