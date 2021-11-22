def codeGenerator(codeLines):
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
    ambito = ""
    GLOBAL = ".data"
    ARMCODE = ""
    for line in codeLines:
        # print(line)
        code = line.split()
        if len(code) != 0:
            # print("in")
            if len(code) == 1:
                if code[0][-1] == ":":
                    ARMCODE += "\n" + code[0]

            if len(code) == 2:

                if code[0] == "Def":
                    ARMCODE += "\n" + code[1] + ":"
                    ambito = code[1]
                    localVars[ambito]= {}

                elif code[0] == "End":
                    if code[1] == "main":
                        ARMCODE += "\n\tbkpt"
                    else:
                        ARMCODE += "\n\tbx lr"
                elif code[0] == 'goto':
                    ARMCODE += "\n\tb " + code[1]
            if len(code) == 3: 
                if "gp" in code[0] and code[2].isnumeric():
                    offset = code[0][code[0].find("[")+1:-1]
                    varname = "gp" + offset
                    # print(list(globalVars))
                    if varname not in list(globalVars):
                        globalVars[varname] ={}
                        globalVars[varname]['value'] = code[2]
                        GLOBAL += "\n" + varname + ": .word " + code[2]
                    else:
                        ARMCODE += "\n\tldr " + varname + ", #" + code[2]
                        # ARMCODE += "\n\tstr " + code[2] +", [R10]"
                elif "fp" in code[0] and code[2].isnumeric():
                    print(line)
                    offset = code[0][code[0].find("[")+1:-1]
                    # varname = "fp" + offset
                    # print(list(localVars[ambito]))
                    # if code[0] not in list(localVars[ambito]):
                    # print("im inside")
                    localVars[ambito][code[0]] = {}
                    localVars[ambito][code[0]]['value'] = code[2]
                        # print(localVars)
                    # else:
                        # print("im inside")
                    # localVars[ambito][code[0]]['value'] = code[2]
                    ARMCODE += "\n\tmov r6, #" + code[2]
                    ARMCODE += "\n\tmov r7, #" + offset
                    ARMCODE += "\n\tstr " + "R6" +", [r7]"
                # elif "t" in code[0] and code[2] == "Call":

            if len(code) == 6:

                    if "gp" in code[1]:
                        offset = code[1][code[1].find("[")+1:-1]
                        varname = "gp" + offset
                        ARMCODE += "\n\tldr r10, " + varname
                    elif "fp" in code[1]:
                        offset = code[1][code[1].find("[")+1:-1]
                        ARMCODE += "\n\tmov r7, #" + offset
                        ARMCODE += "\n\tldr r10, " + "[r7]"

                    if "gp" in code[3]:
                        offset = code[3][code[3].find("[")+1:-1]
                        varname = "gp" + offset
                        ARMCODE += "\n\tldr r9, " + varname
                    elif "fp" in code[3]:
                        offset = code[3][code[3].find("[")+1:-1]
                        ARMCODE += "\n\tmov r7, #" + offset
                        ARMCODE += "\n\tldr r9, " + "[r7]"

                    if ("gp" in code[1] or "fp" in code[1]) and ("gp" in code[3] or "fp" in code[3]):
                        ARMCODE += "\n\tcmp r10, r9"
                    elif ("gp" in code[1] or "fp" in code[1]) and ("gp" not in code[3] or "fp" not in code[3]):
                        ARMCODE += "\n\tcmp r10, #" + code[3]
                    elif ("gp" not in code[1] or "fp" not in code[1]) and ("gp" in code[3] or "fp" in code[3]):
                        ARMCODE += "\n\tcmp #" + code[1] + ", r9" 

                    ARMCODE += "\n\t" + FALSECONDS[code[2]] + " " + code[-1]                    


                    


            
            
    GLOBAL += "\n.text\n.global main"
    return GLOBAL + ARMCODE