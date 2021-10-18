
def Generador(content):
    codigo = []
    # codigo.append('DEF main:')
    declaraciones = {}
    globalVars = []
    contWhile = 0
    contIfs = 0
    globales = 0
    ambito = 'global'
    inStruct = False
    offset = 0
    contTemp = 0
    condicionales = []
    for line in content:
        # print(line)
        #detectado si la linea es un struct
        if("struct" in line and "{" in line):
            inStruct = True
            continue
        #ya que no es un struct, veremos si se encuentra en uno y si tiene una llave de cierre
        #lo que indica que ya salio del struct
        if("}" in line and inStruct == True):
            inStruct = False
            continue
        #sino, verficamos si en esa linea esta activado el struct, para pasar
        elif(inStruct == True):
            continue
        
        if("struct" in line and ";" in line and ambito == 'global'):
            globalVars.append(line)
            continue
        elif("boolean" in line and ";" in line and ambito == 'global'):
            globalVars.append(line)
            continue
        elif("int" in line and ";" in line and ambito == 'global'):
            globalVars.append(line)
            continue
        elif("char" in line and ";" in line and ambito == 'global'):
            globalVars.append(line)
            continue

        #reemplazamos la estructura inicial de las funciones
        if(("int" in line or "char" in line or "boolean" in line or "void" in line) and "{" in line):
            # print(line)
            line = line.replace("int", "DEF")
            line = line.replace("char", "DEF")
            line = line.replace("boolean", "DEF")
            line = line.replace("void", "DEF")
            pospar0 = line.find(" ")
            pospar1 = line.find("(")
            pospar2 = line.find("{") +1 
            ambito = line[pospar0:pospar1]
            finPartFunc = line[pospar1:pospar2]
            line = line.replace(finPartFunc, ":")
            codigo.append(line)
            continue
            
        if("while" in line):
            codigo.append("START_WHILE" + str(contWhile) + ":")
            condicionales.append("WHILE" + str(contWhile))
            line = line.strip()
            line = line.replace("while", "\tIF_WHILE" +str(contWhile))
            line = line.replace("(", " ")
            line = line.replace(")", " ")
            line = line.replace("{", "GOTO WHILE_TRUE" + str(contWhile))
            codigo.append(line)
            codigo.append("\tGOTO END_WHILE" + str(contWhile))
            codigo.append("WHILE_TRUE" + str(contWhile) + ":")
            contWhile += 1
            continue

        if("if" in line):
            condicionales.append("IF" + str(contIfs))
            line = line.strip()
            line = line.replace("if", "\tIF")
            line = line.replace("(", " ")
            line = line.replace(")", " ")
            line = line.replace("{", "GOTO LABEL_TRUE_IF" + str(contIfs))
            codigo.append(line)
            codigo.append("\tGOTO LABEL_FALSE_IF" + str(contIfs))
            codigo.append("LABEL_TRUE_IF" + str(contIfs))
            contIfs += 1
            continue
        
        if("return" in line):
            line = line.strip()
            parts = line.split()
            line = line.replace("return", "RETURN")
            # line = line.replace(parts[1],declaracion[parts[1]]['temp'])
            codigo.append("\t"+line)
            continue
            
        if("=" in line):
            declaracion = line.split("=")
            var = declaracion[0]
            declaraciones[var] = {}
            value = declaracion[1]
            declaraciones[var]["value"] = str(value)
            declaraciones[var]["temp"] = "t" + str(contTemp)
            codigo.append("fp[" + str(offset) + "]")

            codigo.append(declaraciones[var]["temp"] + " := " + declaraciones[var]["value"])
            contTemp += 1
            continue

        # print(ambito)
        if("}" in line and ambito != 'global' and condicionales == []):
            # print(line)
            line = line.replace("}", "END DEF" + ambito)
            ambito = 'global'
            codigo.append(line.strip() +"\n")
            continue

        elif("}" in line and ambito != 'global' and condicionales != []):
            line = line.replace("}", "END_" + condicionales.pop() + ":")
            codigo.append(line.strip())
            continue
        


    return codigo
            


def printCode(codigo):
    for line in codigo:
        print(line)

