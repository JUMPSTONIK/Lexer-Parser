def codeGenerator(codeLines, visitor):
    globalVars = {}
    localVars = {}
    temporals = {}
    FALSECONDS = {
        "==" : "bne",
        "!=" : "beq",
        ">" : "ble",
        "<" : "bge",
        ">=" : "blt",
        "<=" : "bgt"
    }
    OPERANDS = {
        "+" : "add",
        "/" : "div",
        "-" : "sub",
        "*" : "mul"
    }
    ambito = ""
    GLOBAL = ".data\nbuffer: .space 4"
    MIPSCODE = ""
    RCPARAMSCOUNT = 0
    for line in codeLines:
        # print(line)
        code = line.split()
        if len(code) != 0:
            # print("in")
            if len(code) == 1:
                # print(str(code))
                if code[0][-1] == ":":
                    MIPSCODE += "\n" + code[0]
                    
            elif len(code) == 2:
                # print(str(code))
                if code[0] == "Def":
                    # print(str(code))
                    ambito = code[1]
                    if code[1] == "main":
                        MIPSCODE += "\n\n" + code[1] + ":"
                    else:
                        MIPSCODE += "\n\n" + code[1] + ":"
                        raOffset = int(visitor.metodos[code[1]]['size'])
                        MIPSCODE += "\n\taddi $sp, $sp -" + str(raOffset + 4)
                        # if raOffset == 0:
                        #     raOffset = "$zero"
                        MIPSCODE += "\n\tsw $ra, " + str(raOffset) + "($sp)"

                elif code[0] == "End":
                    # print(str(code))
                    
                    if code[1] == "main":
                        MIPSCODE += "\n\tli $v0, 10 "
                        MIPSCODE +=  "\n\tsyscall"
                    else:
                        raOffset = int(visitor.metodos[code[1]]['size'])
                        # if raOffset == 0:
                        #     raOffset = "$zero"
                        MIPSCODE += "\n\tlw $ra " + str(raOffset) + "($sp)"
                        raOffset = int(visitor.metodos[code[1]]['size'])
                        MIPSCODE += "\n\taddi $sp, $sp, " + str((raOffset + 4) + (4 * RCPARAMSCOUNT))
                        MIPSCODE += "\n\tjr $ra"

                    RCPARAMSCOUNT = 0
                elif code[0] == 'goto':
                    # print(str(code))
                    MIPSCODE += "\n\tj " + code[1]
                elif code[0] == "Call":
                    # print(str(code))
                    MIPSCODE += "\n\tjal " + code[1]
                elif code[0] == "Param":
                    # print(str(code))
                    if "fp" in code[1]:
                        offset = code[1][code[1].find("[")+1:-1]
                        MIPSCODE += "\n\t lw $t7, " + offset +"($sp)"
                        MIPSCODE += "\n\taddi $sp, $sp, -4"
                        MIPSCODE += "\n\tsw $t7, 0($sp)"
                    elif "TR" in code[1]:
                        globalVarNameRigth = code[1][:code[1].find("[")]
                        MIPSCODE += "\n\tlw $t7, " + globalVarNameRigth +"($t4)"
                        MIPSCODE += "\n\taddi $sp, $sp, -4"
                        MIPSCODE += "\n\tsw $t7, 0($sp)"
                elif code[0] == "Rcparam":
                    # print(str(code))
                    # print(ambito)
                    offset = code[1][code[1].find("[")+1:-1]
                    MIPSCODE += "\n\tlw $t7, " + str((visitor.metodos[ambito]['size'] + 4 + int(offset)) + (4 * RCPARAMSCOUNT))+ "($sp)"
                    
                    MIPSCODE += "\n\tsw $t7, "+ str(offset) + "($sp)"
                    RCPARAMSCOUNT += 1
                elif code[0] == "Return":
                    # print(str(code))
                    if code[1].isnumeric():
                        # print(str(code))
                        if code[1] == "0":
                            MIPSCODE += "\n\tmove $v1, $zero"
                        else:
                            MIPSCODE += "\n\tli $v1, " + code[1]
                    elif "fp" in code[1]:
                        # print(str(code))
                        offset = code[1][code[1].find("[")+1:-1]
                        MIPSCODE += "\n\tlw $t7, " + offset + "($sp)"
                        MIPSCODE += "\n\tmove $v1, $t7"
                        pass
            elif len(code) == 3: 
                print(str(code))
                if "gp" in code[0] and code[2].isnumeric():
                    offset = code[0][code[0].find("[")+1:-1]
                    varname = "gp" + offset
                    # print(list(globalVars))
                    if varname not in list(globalVars):
                        globalVars[varname] ={}
                        globalVars[varname]['value'] = code[2]
                        GLOBAL += "\n" + varname + ": .word " + code[2]
                    else:
                        # print(str(code))
                        # MIPSCODE += "\n\tlw " + varname + ", " + code[2]
                        pass
                elif "fp" in code[0]:
                    # print(str(code))
                    offsetleft = code[0][code[0].find("[")+1:-1]
                    if code[2].isnumeric():
                        # print(str(code))
                        # localVars[ambito][code[0]] = {}
                        # localVars[ambito][code[0]]['value'] = code[2]
                        if code[2] == "0":
                            MIPSCODE += "\n\tmove $t7, $zero"  
                        else:   
                            MIPSCODE += "\n\tli $t7, " + code[2]
                        MIPSCODE += "\n\tsw $t7, " + offsetleft + "($sp)"
                    elif "t" in code[2]:
                        # print(str(code))
                        MIPSCODE += "\n\tsw $t0, " + offsetleft + "($sp)"
                    elif "TR" in code[2]:
                        # print(str(code))
                        globalVarNameRigth = code[2][:code[2].find("[")]
                        MIPSCODE += "\n\tlw $t0, " + globalVarNameRigth +"($t4)"
                        MIPSCODE += "\n\tsw $t0, " + offsetleft +"($sp)"
                    elif "fp" in code[2]:
                        # print(str(code))
                        offsetrigth = code[2][code[2].find("[")+1:-1]
                        # if offsetrigth == "0":
                        #     offsetrigth = "$zero"
                        MIPSCODE += "\n\tlw $t0, " + offsetrigth + "($sp)"
                        MIPSCODE += "\n\tsw $t0, " + offsetleft +"($sp)"
                        # pass
                elif "TL" in code[0]:
                    globalVarNameLeft = code[0][:code[0].find("[")]
                    # print(globalVarName)
                    # print(str(code))
                    if "t" in code[2]:
                        MIPSCODE += "\n\tsw $t0, " + globalVarNameLeft +"($t3)"
                    elif "TR" in code[2]:
                        globalVarNameRigth = code[2][:code[2].find("[")]
                        MIPSCODE += "\n\tlw $t0, " + globalVarNameRigth +"($t4)"
                        MIPSCODE += "\n\tsw $t0, " + globalVarNameLeft +"($t3)"
                    elif "fp" in code[2]:
                        offset = code[2][code[2].find("[")+1:-1]
                        # if offset == "0":
                        #     offset = "$zero"
                        MIPSCODE += "\n\tlw $t0, " + offset +"($sp)"
                        MIPSCODE += "\n\tsw $t0, " + globalVarNameLeft +"($t3)"
                    elif code[2].isnumeric():
                        if code[2] == "0":
                            """Aqui se puso move en lugar de li"""
                            MIPSCODE += "\n\tmove $t0, $zero"
                        else:
                            MIPSCODE += "\n\tli $t0, "+ code[2]
                        MIPSCODE += "\n\tsw $t0, " + globalVarNameLeft +"($t3)"

            elif len(code) == 4:
                # print(str(code))
                if "[" in code[0]:
                    nameVar = code[0][:code[0].find("[")]
                    # print(nameVar)
                    GLOBAL += "\n" + nameVar + ": .word 0" + (",0" * (int(code[-1])-1))
                elif "t" in code[0]:
                    if code[2] == "Call": 
                        MIPSCODE += "\n\tjal " + code[3]
                        MIPSCODE += "\n\tmove $t0, $v1"
            elif len(code) == 5:
                # pass
                # print(str(code))
                if "TL" in code[0]:
                    if (code[2].isnumeric() and ("TL" in code[4] or "fp" in code[4])) or (code[4].isnumeric() and ("TL" in code[2] or "fp" in code[2])):
                        # print(str(code))
                        if "fp" in code[-1]:
                            offset = code[-1][code[-1].find("[")+1:-1]
                            # print(offset)
                            MIPSCODE += "\n\tlw $t7, " + offset +"($sp)"
                            if code[3] == "*":
                                MIPSCODE += "\n\tmul $t3, $t7, " + code[2]
                            else:
                                MIPSCODE += "\n\taddi $t3, " + code[2] +", $t7"
                        elif "TL" in code[-1]:
                            MIPSCODE += "\n\taddi $t3, " + code[2] +", $t3"
                            
                elif "TR" in code[0]:
                    if (code[2].isnumeric() and ("TR" in code[4] or "fp" in code[4])) or (code[4].isnumeric() and ("TR" in code[2] or "fp" in code[2])):
                        # print(str(code))
                        if "fp" in code[-1]:
                            offset = code[-1][code[-1].find("[")+1:-1]
                            # print(offset)
                            MIPSCODE += "\n\tlw $t7, " + offset +"($sp)"
                            if code[3] == "*":
                                MIPSCODE += "\n\tmul $t4, $t7, " + code[2]
                            else:
                                MIPSCODE += "\n\taddi $t4, " + code[2] +", $t7"
                        elif "TL" in code[-1]:
                            MIPSCODE += "\n\taddi $t4, " + code[2] +", $t4"
                elif "t" in code[0]:
                    # print(str(code))
                    theresConst = False
                    result = "\n\t"
                    if code[2].isnumeric() or code[4].isnumeric():
                        theresConst = True
                    
                    if theresConst == False:
                        result += OPERANDS[code[3]] + " "
                    if theresConst == True and code[3] == "+":
                        result += "addi "
                    elif theresConst == True and code[3] != "+":
                        result += OPERANDS[code[3]] + " "

                    result += "$t0, "

                    if "fp" in code[2]:
                        offset = code[2][code[2].find("[")+1:-1]
                        MIPSCODE += "\n\tlw $t1, " + offset + "($sp)"
                        result += "$t1, "
                    elif code[2].isnumeric():
                        val = code[2]
                        if val == "0":
                            val = "$zero"
                        result += val +", "
                    
                    if "fp" in code[4]:
                        offset = code[4][code[4].find("[")+1:-1]
                        MIPSCODE += "\n\tlw $t2, " + offset + "($sp)"
                        result += "$t2"
                    elif "t" in code[4]:
                        result += "$t0"
                    elif code[4].isnumeric():
                        val = code[4]
                        if val == "0":
                            val = "$zero"
                        result += val

                    MIPSCODE += result
                    # print(result)
                    # pass
            elif len(code) == 6:
                # print(str(code))
                '''
                t5 = operador izquierdo
                t6 = operador derecho
                '''
                condicion = "\n\t" + FALSECONDS[code[2]] + " "

                if "gp" in code[1]:
                    offset = code[1][code[1].find("[")+1:-1]
                    varname = "gp" + offset
                    # MIPSCODE += "\n\tldr r10, " + varname
                elif "fp" in code[1]:
                    offset = code[1][code[1].find("[")+1:-1]
                    MIPSCODE += "\n\tlw $t5, " + offset + "($sp)"
                    condicion += "$t5, "
                elif code[1].isnumeric():
                    condicion += code[1] + ", "
                #esto es para arrays
                else:
                    varname = code[1][:code[1].find("[")]
                    MIPSCODE += "\n\tlw $t5, " + varname + "($t3)"
                    condicion += "$t5, "
                    pass

                if "gp" in code[3]:
                    offset = code[3][code[3].find("[")+1:-1]
                    varname = "gp" + offset
                    # MIPSCODE += "\n\tldr r10, " + varname
                elif "fp" in code[3]:
                    offset = code[3][code[3].find("[")+1:-1]
                    MIPSCODE += "\n\tlw $t6, " + offset + "($sp)"
                    condicion += "$t6, "
                elif code[3].isnumeric():
                    condicion += code[3] + ", "
                #esto es para arrays
                else:
                    varname = code[3][:code[3].find("[")]
                    MIPSCODE += "\n\tlw $t6, " + varname + "($t4)"
                    condicion += "$t6, "
                    
                condicion += code[-1]                  
                # print(condicion)
                MIPSCODE += condicion

                    


            
            
    GLOBAL += "\n.text \n\tj main"
    return GLOBAL + MIPSCODE