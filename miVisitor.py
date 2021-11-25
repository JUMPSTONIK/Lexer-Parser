from DECAFParser import DECAFParser
from DECAFVisitor import DECAFVisitor
from TablaDeSimbolos import *

class miVisitor(DECAFVisitor):
    def __init__(self):
        TYPEVALUES = {
            "int" : 4,
            "char" : 2,
            "boolean" : 1
        }
        TYPEINITVALUE = {
        "int" : 0,
        "char" : "",
        "boolean" : False
        }
        self.ambito = "global"
        self.contMainVoids = 0
        self.variables = {}
        self.lists ={}
        self.structs = {}
        self.metodos = {}
        self.interCode = ""
        self.position = ""
        self.operandsCount = 0
        # self.inOp = False
        self.ifCount = 0
        self.WhileCount = 0
        self.enviroments = {}
        self.enviroments['global'] = {"offset": 0}
        self.OpCode = []
        self.OpTemporal = {}
        self.temporalsCount = 0
        self.temporals = {}
        self.closetags = []
        self.savedOP = []
        self.lastIF = ""
        self.fromArray = False

    def visitProgram(self, ctx:DECAFParser.ProgramContext):
        return self.visitChildren(ctx)

    '''Estos son los metodos para obtener el la informacion de todos los tipos de funciones
        Cada uno hace distincion si es sin metodos o con metodos'''

    def visitMetoInt(self, ctx:DECAFParser.MetoIntContext):
            
        self.closetags.append("\nEnd " + str(ctx.Id()) + "\n")
        self.ambito = str(ctx.Id())

        self.interCode += "\nDef " + str(ctx.Id())

        self.enviroments[str(ctx.Id())] = {"offset": 0}
        # print(str(ctx.Id()))
        self.metodos[str(ctx.Id())] = {}
        self.metodos[str(ctx.Id())]['tipo'] = 'int'
        self.metodos[str(ctx.Id())]['size'] = 0
        self.metodos[str(ctx.Id())]['return'] = ''
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitMetoIntWithParam(self, ctx:DECAFParser.MetoIntWithParamContext):
            
        self.closetags.append("\nEnd " + str(ctx.Id()) + "\n")
        self.ambito = str(ctx.Id())

        self.interCode += "\nDef " + str(ctx.Id())

        self.enviroments[str(ctx.Id())] = {"offset": 0}

        self.metodos[str(ctx.Id())] = {}
        self.metodos[str(ctx.Id())]['tipo'] = 'int'
        self.metodos[str(ctx.Id())]['params'] = {}
        self.metodos[str(ctx.Id())]['size'] = 0
        self.metodos[str(ctx.Id())]['return'] = ''
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitMetoChar(self, ctx:DECAFParser.MetoCharContext):
            
        self.closetags.append("\nEnd " + str(ctx.Id()) + "\n")
        self.ambito = str(ctx.Id())

        self.interCode += "\nDef " + str(ctx.Id())

        self.enviroments[str(ctx.Id())] = {"offset": 0}

        self.metodos[str(ctx.Id())] = {}
        self.metodos[str(ctx.Id())]['tipo'] = 'char'
        self.metodos[str(ctx.Id())]['size'] = 0
        self.metodos[str(ctx.Id())]['return'] = ''
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitMetoCharWithParam(self, ctx:DECAFParser.MetoCharWithParamContext):
            
        self.closetags.append("\nEnd " + str(ctx.Id()) + "\n")
        self.ambito = str(ctx.Id())

        self.interCode += "\nDef " + str(ctx.Id())

        self.enviroments[str(ctx.Id())] = {"offset": 0}

        self.metodos[str(ctx.Id())] = {}
        self.metodos[str(ctx.Id())]['tipo'] = 'char'
        self.metodos[str(ctx.Id())]['params'] = {}
        self.metodos[str(ctx.Id())]['size'] = 0
        self.metodos[str(ctx.Id())]['return'] = ''
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitMetoBool(self, ctx:DECAFParser.MetoBoolContext):
            
        self.closetags.append("\nEnd " + str(ctx.Id()) + "\n")
        self.ambito = str(ctx.Id())

        self.interCode += "\nDef " + str(ctx.Id())

        self.enviroments[str(ctx.Id())] = {"offset": 0}

        self.metodos[str(ctx.Id())] = {}
        self.metodos[str(ctx.Id())]['tipo'] = 'boolean'
        self.metodos[str(ctx.Id())]['size'] = 0
        self.metodos[str(ctx.Id())]['return'] = ''
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitMetoBoolWithParam(self, ctx:DECAFParser.MetoBoolWithParamContext):
            
        self.closetags.append("\nEnd " + str(ctx.Id()) + "\n")
        self.ambito = str(ctx.Id())

        self.interCode += "\nDef " + str(ctx.Id())

        self.enviroments[str(ctx.Id())] = {"offset": 0}

        self.metodos[str(ctx.Id())] = {}
        self.metodos[str(ctx.Id())]['tipo'] = 'boolean'
        self.metodos[str(ctx.Id())]['params'] = {}
        self.metodos[str(ctx.Id())]['size'] = 0
        self.metodos[str(ctx.Id())]['return'] = ''
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitMetoVoid(self, ctx:DECAFParser.MetoVoidContext):
        
        self.closetags.append("\nEnd " + str(ctx.Id()) + "\n")
        self.ambito = str(ctx.Id())

        self.interCode += "\nDef " + str(ctx.Id())
            
        self.enviroments[str(ctx.Id())] = {"offset": 0}

        self.metodos[str(ctx.Id())] = {}
        self.metodos[str(ctx.Id())]['tipo'] = 'void'
        self.metodos[str(ctx.Id())]['size'] = 0
        # print(ctx.Id())
        # print(ctx.getText())
        
        return self.visitChildren(ctx)

    def visitMetoVoidWithParam(self, ctx:DECAFParser.MetoVoidWithParamContext):
        
        self.closetags.append("\nEnd " + str(ctx.Id()) + "\n")
        self.ambito = str(ctx.Id())

        self.interCode += "\nDef " + str(ctx.Id())

        self.enviroments[str(ctx.Id())] = {"offset": 0}

        self.metodos[str(ctx.Id())] = {}
        self.metodos[str(ctx.Id())]['tipo'] = 'void'
        self.metodos[str(ctx.Id())]['params'] = {}
        self.metodos[str(ctx.Id())]['size'] = 0
        # print(ctx.getText())
        
        return self.visitChildren(ctx)

    '''Con esta funcion puedo ir obteniendo cada uno de los parametros de cada funcion'''
    def visitSingle_parameterDeclaration(self, ctx:DECAFParser.Single_parameterDeclarationContext):
        # print(str(ctx.Id()))
        self.variables[str(ctx.Id())] = {}
        self.variables[str(ctx.Id())]['tipo'] = ctx.getText()[:-len(str(ctx.Id()))]
        self.variables[str(ctx.Id())]['ambito'] = str(self.ambito)
        # self.variables[str(ctx.Id())]['offset'] = 0
        self.variables[str(ctx.Id())]['offset'] = self.enviroments[self.ambito]['offset']
        self.enviroments[self.ambito]['offset'] += TYPEVALUES[self.variables[str(ctx.Id())]['tipo']]
        self.variables[str(ctx.Id())]['value'] = TYPEINITVALUE[self.variables[str(ctx.Id())]['tipo']]
        
        self.metodos[self.ambito]['params'][str(ctx.Id())] = self.variables[str(ctx.Id())]
        self.metodos[self.ambito]['size'] += TYPEVALUES[self.variables[str(ctx.Id())]['tipo']]

        if self.ambito == "global":
            self.interCode += "\n\tgp[" + str(self.variables[str(ctx.Id())]['offset']) + "] = " + str(self.variables[str(ctx.Id())]['value'])
        else:
            self.interCode += "\n\tfp[" + str(self.variables[str(ctx.Id())]['offset']) + "] = " + str(self.variables[str(ctx.Id())]['value'])
        
        self.interCode += "\n\tRcparam " + "fp[" + str(self.variables[str(ctx.Id())]['offset']) + "]"

        return self.visitChildren(ctx)

    ''' 
    Aqui es donde visitamos los tipos de variables como variables tipo int, char, bool, lists y los structs
    '''
    '''Esta es la funcion encargada de obtener la informacion de las variables int, char, bool'''
    def visitNormal(self, ctx:DECAFParser.NormalContext):
        # print(self.interCode)
        # print(self.ambito)
        if(" " not in str(ctx.parentCtx)):
            # print(self.ambito)
            self.ambito = "global"
        # print(self.ambito)
        # print(str(ctx.Id()))
        # print(len(str(ctx.Id())))
        # print(ctx.getText()[:-len(str(ctx.Id())) - 1])
        
        
        if("[" not in ctx.getText()):
            self.variables[str(ctx.Id())] = {}
            self.variables[str(ctx.Id())]['tipo'] = ctx.getText()[:-len(str(ctx.Id())) - 1].replace('struct','struct ')
            self.variables[str(ctx.Id())]['ambito'] = str(self.ambito)
            self.variables[str(ctx.Id())]['offset'] = 0

            if("struct" not in self.variables[str(ctx.Id())]['tipo']):
                # self.variables[str(ctx.Id())]['offset'] = TYPEVALUES[self.variables[str(ctx.Id())]['tipo']]
                self.variables[str(ctx.Id())]['offset'] = self.enviroments[self.ambito]['offset']
                self.enviroments[self.ambito]['offset'] += TYPEVALUES[self.variables[str(ctx.Id())]['tipo']]
                self.variables[str(ctx.Id())]['value'] = TYPEINITVALUE[self.variables[str(ctx.Id())]['tipo']]
            elif("struct" in self.variables[str(ctx.Id())]['tipo']):
                self.variables[str(ctx.Id())]['offset'] = self.structs[self.variables[str(ctx.Id())]['tipo']]['offset']

        if("struct" in self.variables[str(ctx.Id())]['ambito']):
            # print(self.variables)
            self.structs[self.variables[str(ctx.Id())]['ambito']]['variables'][str(ctx.Id())] = self.variables[str(ctx.Id())]
            self.structs[self.variables[str(ctx.Id())]['ambito']]['offset'] += self.variables[str(ctx.Id())]['offset']
        
        if(self.variables[str(ctx.Id())]['ambito'] != 'global' and "struct" not in self.variables[str(ctx.Id())]['ambito']):
            self.metodos[self.ambito]['size'] += TYPEVALUES[self.variables[str(ctx.Id())]['tipo']]
        # print(self.interCode)
        # print(self.ambito)
        # print(self.variables)
        if self.ambito == "global":
            self.interCode += "\n\tgp[" + str(self.variables[str(ctx.Id())]['offset']) + "] = " + str(self.variables[str(ctx.Id())]['value'])
        else:
            self.interCode += "\n\tfp[" + str(self.variables[str(ctx.Id())]['offset']) + "] = " + str(self.variables[str(ctx.Id())]['value'])
        return self.visitChildren(ctx)

    '''Esta es la funcion encargada de obtener la informacion de las variables del tipo lista'''
    def visitLista(self, ctx:DECAFParser.ListaContext):
        # print(ctx.Num())
        if(" " not in str(ctx.parentCtx)):
            self.ambito = "global"
            
        

        self.lists[str(ctx.Id())] = {}
        self.lists[str(ctx.Id())]['size'] = int(str(ctx.Num()))
        # print(ctx.getText())
        self.lists[str(ctx.Id())]['tipo'] = ctx.getText()[:-(len(str(ctx.Num())) + len(str(ctx.Id()))) - 3].replace('struct','struct ')
        # print("antes de anadir ambito " + str(self.ambito))
        self.lists[str(ctx.Id())]['ambito'] = str(self.ambito)
        self.lists[str(ctx.Id())]['arrays'] = {}
        if("struct" not in self.lists[str(ctx.Id())]['tipo']):
            # self.lists[str(ctx.Id())]['offset'] = TYPEVALUES[self.lists[str(ctx.Id())]['tipo']] * self.lists[str(ctx.Id())]['size']
            self.lists[str(ctx.Id())]['offset'] = self.enviroments[self.ambito]['offset']
            self.enviroments[self.ambito]['offset'] += TYPEVALUES[self.lists[str(ctx.Id())]['tipo']] * int(str(ctx.Num()))
            self.lists[str(ctx.Id())]['value'] = TYPEINITVALUE[self.lists[str(ctx.Id())]['tipo']]
            
        elif("struct" in self.variables[str(ctx.Id())]['tipo']):
                self.lists[str(ctx.Id())]['offset'] = self.structs[self.lists[str(ctx.Id())]['tipo']]['offset'] * self.lists[str(ctx.Id())]['size']
        
            
        if("struct" in self.lists[str(ctx.Id())]['ambito']):
            # print(self.variables)
            self.structs[self.lists[str(ctx.Id())]['ambito']]['variables'][str(ctx.Id())] = self.lists[str(ctx.Id())]
            self.structs[self.lists[str(ctx.Id())]['ambito']]['offset'] += self.lists[str(ctx.Id())]['offset']
        
        if(self.lists[str(ctx.Id())]['ambito'] != 'global' and "struct" not in self.lists[str(ctx.Id())]['ambito']):
            self.metodos[self.ambito]['size'] += TYPEVALUES[self.lists[str(ctx.Id())]['tipo']] * int(str(ctx.Num()))

        for x in range(0, int(str(ctx.Num()))):
                setOffset = self.lists[str(ctx.Id())]['offset'] + (TYPEVALUES[self.lists[str(ctx.Id())]['tipo']] * x)
                # print(setOffset)
                self.lists[str(ctx.Id())]['arrays'][str(ctx.Id()) + "[" + str(x) + "]" ] = {}
                self.lists[str(ctx.Id())]['arrays'][str(ctx.Id()) + "[" + str(x) + "]" ]["offset"] = setOffset
                

        if self.ambito == "global":
            self.interCode += "\n\t" + str(ctx.Id()) +"[" + str(self.lists[str(ctx.Id())]['offset']) + "] = " + str(self.lists[str(ctx.Id())]['value']) + ", " + str(self.lists[str(ctx.Id())]['size'])
            pass
            
        else:
            for x in range(0, int(str(ctx.Num()))):
                setOffset = self.lists[str(ctx.Id())]['offset'] + (TYPEVALUES[self.lists[str(ctx.Id())]['tipo']] * x)
                # print(setOffset)
                self.interCode += "\n\tfp[" + str(setOffset) + "] = " + str(self.lists[str(ctx.Id())]['value'])
        

        return self.visitChildren(ctx)

    '''Esta es la funcion encargada de obtener la informacion de las variables de tipo struct'''
    def visitStructDeclaration(self, ctx:DECAFParser.StructDeclarationContext):
        # print("----" + str(ctx.parentCtx))
        self.ambito = "struct "
        self.ambito += str(ctx.Id())
        name = 'struct ' + str(ctx.Id())
        
        self.structs[name] = {}
        self.structs[name]['ambito'] = 'global'
        self.structs[name]['offset'] = 0
        self.structs[name]['variables'] = {}
        # print(len(self.structs))

        # print("esta en el " + str(self.ambito))
        return self.visitChildren(ctx)

    def visitAsign_statement(self, ctx:DECAFParser.Asign_statementContext):
        
        self.position = "asign"
        expresion = str(ctx.getText())[str(ctx.getText()).find("=")+1:-1]
        asign = str(ctx.getText())[:str(ctx.getText()).find("=")]
        # print(asign)
        # print(asign)
        # print(expresion + "/////")
        if("*" not in expresion and "/" not in expresion and "%" not in expresion and "+" not in expresion and "-" not in expresion and "(" not in expresion):
            if "[" not in asign:
                if asign in self.variables:
                    if self.variables[asign]['ambito'] == 'global':
                        self.interCode += "\n\tgp[" + str(self.variables[asign]['offset']) + "] = "
                    else:
                        self.interCode += "\n\tfp[" + str(self.variables[asign]['offset']) + "] = "
                    if expresion in self.variables:
                        if self.variables[expresion]['ambito'] == 'global':
                            self.interCode += "gp[" + str(self.variables[expresion]['offset']) + "]"
                        else:
                            self.interCode += "fp[" + str(self.variables[expresion]['offset']) + "]"
                    elif "[" in expresion:
                        arrayName = expresion[:expresion.find("[")]
                        varInExpres = expresion[expresion.find("[") +1:-1]
                        if expresion in self.lists[arrayName]['arrays']:
                            if self.lists[arrayName]["ambito"] == "global":
                                self.interCode += expresion
                            else:
                                self.interCode += "fp[" + str(self.lists[arrayName]["arrays"][expresion]["offset"]) + "]"
                        else:
                            print(str(ctx.getText()))
                            print(varInExpres)
                            inter1 = self.interCode[0:self.interCode.rfind("\n")]
                            inter2 = self.interCode[self.interCode.rfind("\n"):]
                            """QQQQ"""
                            ParamCode = "\n\tTR = 4 * fp[" + str(self.variables[varInExpres]["offset"]) +"]"
                            if self.lists[arrayName]["ambito"] == "global":
                                self.interCode = inter1 + ParamCode + inter2 + arrayName + "[TR]"
                            else:
                                ParamCode += "\n\tTR = " + str(self.lists[arrayName]['offset']) + " + TR"
                                self.interCode = inter1 + ParamCode + inter2 +  "fp[TR]"

                    else:
                        self.interCode += expresion
                
                else:
                    
                    if self.variables[asign]['ambito'] == 'global':
                        self.interCode += "\n\tgp[" + str(self.variables[asign]['offset']) + "] = " + expresion
                    else:
                        self.interCode += "\n\tfp[" + str(self.variables[asign]['offset']) + "] = " + expresion
            else:
                arrayName = asign[:asign.find("[")]
                varInExpres = expresion[expresion.find("[")+1: -1] 
                # print("asign with [ and expresion without Ops")
                # print(arrayName)
                if asign in self.lists[arrayName]["arrays"]:
                    # print(asign + " ////")
                    if self.lists[asign[:asign.find("[")]]['ambito'] == 'global':
                        self.interCode += "\n\t" + asign + " = "
                    else:
                        self.interCode += "\n\tfp[" + str(self.lists[arrayName]["arrays"][asign]['offset']) + "] = "
                    # arrayName = expresion[:asign.find("[")]
                    # print(arrayName)
                    # print(expresion)
                    if expresion in self.lists[arrayName]["arrays"]:
                        if self.lists[arrayName]['ambito'] == 'global':
                            self.interCode += expresion
                        else:
                            self.interCode += "fp[" + str(self.lists[arrayName]["arrays"][expresion]['offset']) + "]"
                    #verifico la existencia de una variable en los []
                    elif varInExpres in self.variables:
                        # print(varInExpres)
                        inter1 = self.interCode[0:self.interCode.rfind("\n")]
                        inter2 = self.interCode[self.interCode.rfind("\n"):]
                        ParamCode = "\n\tTR = 4 * fp[" + str(self.variables[varInExpres]["offset"]) +"]"
                        if self.lists[arrayName]['ambito'] == "global":
                            # print(arrayName + " +++")
                            self.interCode = inter1 + ParamCode + inter2 + arrayName+ "[TR]"
                        else:
                            ParamCode += "\n\tTR = " + str(self.lists[arrayName]['offset']) + " + TR"
                            self.interCode = inter1 + ParamCode + inter2 + "fp[TR]"
                    else:
                        self.interCode += expresion
                    
                else:
                    '''Aqui va el codigo para los arrays que tienen una variable dentro. A[min] = '''
                    asignName = asign[:asign.find("[")]
                    varInAsign = asign[asign.find("[")+1:-1]
                    
                    

                    varInExpres = expresion[expresion.find("[")+1: -1] 

                    # inter1 = self.interCode[0:self.interCode.rfind("\n")]
                    # inter2 = self.interCode[self.interCode.rfind("\n"):]

                    leftParamCode = "\n\tTL = 4 * fp[" + str(self.variables[varInAsign]["offset"]) +"]"
                    
                    if self.lists[asignName]['ambito'] == 'global':
                        self.interCode += leftParamCode +"\n\t" + asignName + "[TL] = "
                    else:
                        leftParamCode += "\n\tTL = " + str(self.lists[asignName]['offset']) + " + TL"
                        self.interCode += leftParamCode + "\n\tfp[TL] = "
                    # arrayName = expresion[:asign.find("[")]
                    # print(expresion)
                    # print(expressName)
                    if "[" in expresion:
                        expressName = expresion[:asign.find("[")]
                        if expresion in self.lists[expressName]["arrays"]:
                            if self.lists[expressName]['ambito'] == 'global':
                                self.interCode += expresion
                            else:
                                self.interCode += "fp[" + str(self.lists[expressName]["arrays"][expresion]['offset']) + "]"
                        # #verifico la existencia de una variable en los []
                        elif varInExpres in self.variables:
                            # print(varInExpres)
                            inter1 = self.interCode[0:self.interCode.rfind("\n")]
                            inter2 = self.interCode[self.interCode.rfind("\n"):]

                            rigthParamCode = "\n\tTR = 4 * fp[" + str(self.variables[varInExpres]["offset"]) +"]"
                            if self.lists[expressName]['ambito'] == "global":
                                # print(arrayName + " +++")
                                self.interCode = inter1 + rigthParamCode + inter2 + expressName+ "[TR]"
                            else:
                                rigthParamCode += "\n\tTR = " + str(self.lists[expressName]['offset']) + " + TR"
                                self.interCode = inter1 + rigthParamCode + inter2 + "fp[TR]"
                    elif expresion in self.variables:
                        # print("a variable")
                        if self.variables[expresion]['ambito'] == 'global':
                            self.interCode += "gp[" + str(self.variables[expresion]['offset']) + "]"
                        else:
                            self.interCode += "fp[" + str(self.variables[expresion]['offset']) + "]"
                    else:
                        self.interCode += expresion
            self.position = ""
        else:
            print(str(ctx.getText())+ "out of OP")
            temp = "t" + str(self.temporalsCount)
            "HAY un error aqui"
            self.position = "asignL"
            self.OpTemporal[temp] = {'exp1': "", "op": "", 'exp2': ""}
            self.temporalsCount += 1
            
            code = "\n\t"
            if "[" not in asign:
                if self.variables[asign]['ambito'] == 'global':
                    code += "gp[" + str(self.variables[asign]['offset']) + "] = " + str(list(self.OpTemporal)[-1])
                else:
                    code += "fp[" + str(self.variables[asign]['offset']) + "] = " + str(list(self.OpTemporal)[-1])
                # self.position = "asign"
            else:
                '''Aqui ira el codigo de asignacion para los arrays'''
                print(str(ctx.getText()) + " in op")
                varname = str(ctx.getText())[:str(ctx.getText()).find("[")]
                "Revisar aqui por si acaso falta algo"
                print(varname)
                print(asign)
                if asign in self.lists[varname]['arrays']:
                    if self.lists[varname]['ambito'] == 'global':
                        code += asign + " = " + str(list(self.OpTemporal)[-1])
                    else:
                        code += "fp[" + str(self.lists[varname]['arrays'][asign]['offset']) + "] = " + str(list(self.OpTemporal)[-1])
                    # self.position = "asign"
                else:
                    varParam = asign[asign.find("[")+1:-1]
                    # print(varParam + " dddd")
                    leftParamCode = "\n\tTL = 4 * fp[" + str(self.variables[varParam]["offset"]) +"]"
                    
                    if self.lists[varname]['ambito'] == 'global':
                        code += varname + "[TL] = " + str(list(self.OpTemporal)[-1])
                    else:
                        leftParamCode += "\n\tTL = " + str(self.lists[varname]['offset']) + " + TL"
                        code += "fp[TL] = " + str(list(self.OpTemporal)[-1])
                    code = leftParamCode + code
            
            # self.position = "asign"
            # print(str(self.OpCode) + " before")
            
            self.OpCode.insert(0,code)  
            print(str(self.OpCode) + " after asign")
            print(self.OpTemporal)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DECAFParser#returnStmt.
    def visitReturnStmt(self, ctx:DECAFParser.ReturnStmtContext):
        self.position = "return"
        expresion = str(ctx.getText())[6:-1]
        # print(expresion)
        if("*" not in expresion and "/" not in expresion and "%" not in expresion and "+" not in expresion and "-" not in expresion and "(" not in expresion):
            if expresion in self.variables:
                if self.variables[expresion]['ambito'] == 'global':
                    self.interCode += "\n\tReturn " + "gp[" + str(self.variables[expresion]['offset']) + "]"
                else:
                    self.interCode += "\n\tReturn " + "fp[" + str(self.variables[expresion]['offset']) + "]"
                self.position = ""
                pass
            else:
                self.interCode += "\n\tReturn " + expresion
                self.position = ""
        else:
            temp = "t" + str(self.temporalsCount)
            self.OpTemporal[temp] = {'exp1': "", "op": "", 'exp2': ""}
            self.temporalsCount += 1
            self.OpCode.insert(0,"\n\tReturn " + str(list(self.OpTemporal)[-1]))  
            # print(self.OpCode)
        return self.visitChildren(ctx)

    def visitArg(self, ctx:DECAFParser.ArgContext):
        expresion = str(ctx.getText())
        if self.position == "return":
            if("*" not in expresion and "/" not in expresion and "%" not in expresion and "+" not in expresion and "-" not in expresion and "(" not in expresion):
                
                if expresion in self.variables:

                    if self.variables[expresion]['ambito'] == 'global':
                        self.interCode += "\n\tParam " + "gp[" + str(self.variables[expresion]['offset']) + "]"
                    else:
                        self.interCode += "\n\tParam " + "fp[" + str(self.variables[expresion]['offset']) + "]"
                    
                elif expresion.isnumeric():
                    # print(expresion)
                    # self.interCode += "\n\tParam " + expresion
                    # print(self.temporals)
                    self.OpCode.insert(0, "\n\tParam " + expresion)
                else:
                    self.interCode += "\n\tParam " + expresion
                # self.position = ""
            else:
                self.OpCode.insert(0, "\n\tParam " + str(list(self.OpTemporal)[-1])) 
                
        else:
            
            inter1 = self.interCode[0:self.interCode.rfind("\n")]
            inter2 = self.interCode[self.interCode.rfind("\n"):]
            
            if("*" not in str(ctx.getText()) and "/" not in str(ctx.getText()) and "%" not in str(ctx.getText()) and "+" not in str(ctx.getText()) and "-" not in str(ctx.getText()) and "(" not in str(ctx.getText())):
                '''volver aqui para arreglar el envio de parametros numericos'''
                # print(str(ctx.getText()))
                if "[" not in str(ctx.getText()):
                    if str(ctx.getText()) in self.variables:
                        if self.variables[str(ctx.getText())]['ambito'] == 'global':
                            self.interCode= inter1 + "\n\tParam " + "gp[" + str(self.variables[str(ctx.getText())]['offset']) + "]" + inter2 
                        else:
                            self.interCode= inter1 + "\n\tParam " + "fp[" + str(self.variables[str(ctx.getText())]['offset']) + "]" + inter2 
                    elif str(ctx.getText()).isnumeric():

                        '''Aqui se arregla el enviar parametros numericos'''
                        self.interCode= inter1 + "\n\tParam " + expresion + inter2
                        # self.interCode += "\n\tParam " + expresion
                        '''Despues de pasar de este punto, ya esta el t0 call y su siguiente temporal'''
                        # print(self.OpTemporal)
                        # self.OpTemporal = {}
                        pass
                else:
                    varname = str(ctx.getText())[:str(ctx.getText()).find("[")]
                    # print("in var[i]")
                    # print(varname)
                    # print(str(ctx.getText()))
                    if str(ctx.getText()) in self.lists[varname]["arrays"]:
                        # print("yeeeeeeeeeeeee")
                        if self.lists[varname]['ambito'] == 'global':
                            self.interCode= inter1 + "\n\tParam " +  str(ctx.getText()) + inter2 
                        else:
                            self.interCode= inter1 + "\n\tParam " + "fp[" + str(self.lists[varname]["arrays"][str(ctx.getText())]['offset']) + "]" + inter2 
                            # print(self.OpTemporal)
                            # print(self.position)
                    else:
                        code = "\n\t"
                        '''Aqui ira el codigo de asignacion para los arrays'''
                        varNum = str(ctx.getText())[str(ctx.getText()).find("[")+1:-1]
                        # print("in var[x]")
                        # print(varname)
                        # print(varNum)
                        # print(str(ctx.getText()))
                        
                        leftParamCode = "\n\tTR = 4 * fp[" + str(self.variables[varNum]["offset"]) +"]"
                        if self.lists[varname]['ambito'] == 'global':
                            code += "Param " + varname + "[TR]" 
                        else:
                            leftParamCode += "\n\tTR = " + str(self.lists[varname]['offset']) + " + TR"
                            code += "Param fp[TR]"
                        code = leftParamCode + code
                        self.interCode = inter1 + code + inter2
        # self.operandsCount = 0
        return self.visitChildren(ctx)

    def visitMethodCall(self, ctx:DECAFParser.MethodCallContext):
        # print(ctx.Id())
        # print(self.position)
        if self.position == "return" or self.position == "asign":
            # print("in return")
            if self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'] == "" and self.OpTemporal[list(self.OpTemporal)[-1]]['exp2'] == "":
                # print(self.OpTemporal)
                "volver aqui para ver lo del problema de los metodos"
                # print("in methodCall")
                self.temporalsCount -= 1
                temp = "t" + str(self.temporalsCount)
                self.OpTemporal[temp] = {'exp1': "", "op": "", 'exp2': ""}
                self.OpTemporal[temp]["op"] = "Call"
                self.OpTemporal[temp]["exp2"] = str(ctx.Id())
                self.interCode += "\n\t" + temp + " = Call " + str(ctx.Id())
                self.temporalsCount += 1
                temp = "t" + str(self.temporalsCount)
                self.OpTemporal[temp] = {'exp1': "", "op": "", 'exp2': ""}
                self.OpTemporal[temp]["exp1"] = "t" + str(self.temporalsCount-1)
                # print(self.OpCode)
                
                # print(self.OpCode[-1])
                # print(self.temporals)
                pass
            elif self.OpTemporal[list(self.OpTemporal)[-1]]['exp2'] == "" and self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'] != "":
                #asignamos temporal a la ultima expresion del ultimo temporal
                # print(self.OpTemporal)
                self.OpTemporal[list(self.OpTemporal)[-1]]['exp2'] = "t" + str(self.temporalsCount)
                code = "\n\t" + list(self.OpTemporal)[-1] + " = " + self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'] + " " + self.OpTemporal[list(self.OpTemporal)[-1]]['op'] + " " + self.OpTemporal[list(self.OpTemporal)[-1]]['exp2']
                self.OpCode.insert(0,code)
                temp = "t" + str(self.temporalsCount)
                self.OpTemporal[temp] = {'exp1': "", "op": "", 'exp2': ""}
                
                self.OpTemporal[temp]['op'] = "Call"
                self.OpTemporal[temp]['exp2'] = str(ctx.Id())
                code = "\n\t" + temp + " = " + self.OpTemporal[temp]['op'] + " " + self.OpTemporal[temp]['exp2']
                self.OpCode.insert(0,code)
                
                self.temporalsCount += 1
                temp = "t" + str(self.temporalsCount)
                self.OpTemporal[temp] = {'exp1': "", "op": "", 'exp2': ""}
                if self.OpTemporal["t" + str(self.temporalsCount-1)]["exp1"] == "" and self.OpTemporal["t" + str(self.temporalsCount-2)] == "":
                    self.OpTemporal[temp]["exp1"] = self.OpTemporal["t" + str(self.temporalsCount-1)]["exp1"]
                # print(self.OpTemporal)
        
        else:
            # print(str(ctx.Id()))
            self.position = "metodo"
            self.interCode += "\n\tCall " + str(ctx.Id())
        # print(self.OpCode)
        # print(self.OpTemporal)
        return self.visitChildren(ctx)

    def visitWhileStmt(self, ctx:DECAFParser.WhileStmtContext):
        self.position = "while"
        self.WhileCount += 1
        self.fromArray = False
        self.operandsCount = 0
        self.closetags.append("\nFalseWhileL" + str(self.WhileCount) + ":")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DECAFParser#ifSt_statement.
    def visitIfSt_statement(self, ctx:DECAFParser.IfSt_statementContext):
        self.position = "if"
        self.ifCount += 1
        self.operandsCount = 0
        self.fromArray = False
        self.closetags.append("\nFalseIfL" + str(self.ifCount) + ":")
        return self.visitChildren(ctx)

    

    def visitCond_op_expr(self, ctx:DECAFParser.Cond_op_exprContext):

        if self.position == "if":
            # print(str(ctx.getText()))
            self.interCode += "\n\tIFFalse " 
            if self.variables[str(ctx.getText())[:str(ctx.getText()).find("=")]]["ambito"] == "global":
                self.interCode += "gp[" + str(self.variables[str(ctx.getText())[:str(ctx.getText()).find("=")]]["offset"]) + "]"
            else:
                self.interCode += "fp[" + str(self.variables[str(ctx.getText())[:str(ctx.getText()).find("=")]]["offset"]) + "]"
            self.interCode += " goto FalseIfL" + str(self.ifCount)
        if self.position == "while":
            
            self.interCode += "\nWhileTrue" + str(self.WhileCount)+ ":" + "\n\tIFFalse " 
            if self.variables[str(ctx.getText())[:str(ctx.getText()).find("=")]]["ambito"] == "global":
                self.interCode += "gp[" + str(self.variables[str(ctx.getText())[:str(ctx.getText()).find("=")]]["offset"]) + "]"
            else:
                self.interCode += "fp[" + str(self.variables[str(ctx.getText())[:str(ctx.getText()).find("=")]]["offset"]) + "]"
            self.interCode += " goto FalseWhileL" + str(self.WhileCount)
        return self.visitChildren(ctx)

    def visitArith_higher_op(self, ctx:DECAFParser.Arith_higher_opContext):
        if self.position == "return" or self.position == "asign":
            # print(str(self.temporals) + ";;;")
            self.fromArray = False
            self.OpTemporal[list(self.OpTemporal)[-1]]['op'] = str(ctx.getText())
            # print(self.position + " in arith high")
            print(self.OpTemporal)

        return self.visitChildren(ctx)

    def visitArith_op(self, ctx:DECAFParser.Arith_opContext):
        if self.position == "return" or self.position == "asign":
            '''algo habia aca, recordar'''
            # print(str(ctx.getText()))
            # print(self.temporals)
            self.fromArray = False
            self.OpTemporal[list(self.OpTemporal)[-1]]['op'] = str(ctx.getText())
            print(self.position + " in arith high")
            print(self.OpTemporal)
            # self.savedOP.append(str(ctx.getText()))
            # print(str(self.temporals) + ";;;")
            # print(self.temporals)
        return self.visitChildren(ctx)

    def visitRel_op_expr(self, ctx:DECAFParser.Rel_op_exprContext):
        if self.position == "if":
            self.interCode += "\n\tIFFalse " 
            
        if self.position == "while":
            self.interCode += "\nWhileTrue" + str(self.WhileCount)+ ":" + "\n\tIFFalse " 
            
        return self.visitChildren(ctx)

    def visitEq_op_expr(self, ctx:DECAFParser.Eq_op_exprContext):
        if self.position == "if":
            self.interCode += "\n\tIFFalse " 

        if self.position == "while":
            self.interCode += "\nWhileTrue" + str(self.WhileCount)+ ":" + "\n\tIFFalse " 
            
        return self.visitChildren(ctx)

    def visitNormal_location(self, ctx:DECAFParser.Normal_locationContext):
        print("\n"+self.position + " in Location")
        print(self.OpTemporal)
        print(self.OpCode)
        # print(self.temporals)
        if self.fromArray == False:
            if self.position == "if" or self.position == "while":
                if self.variables[str(ctx.Id())]["ambito"] == "global":
                    self.interCode += "gp[" + str(self.variables[str(ctx.Id())]["offset"]) + "]"
                else:
                    self.interCode += "fp[" + str(self.variables[str(ctx.Id())]["offset"]) + "]"
                self.operandsCount += 1
                if self.operandsCount >= 2:
                    if self.position == "if":
                        self.interCode += " goto FalseIfL" + str(self.ifCount)
                    if self.position == "while":
                        self.interCode += " goto FalseWhileL" + str(self.WhileCount)
                    self.operandsCount = 0
            
            elif self.position == "return" or self.position == "asign":
                # print(self.position + " in Location")
                # print(self.OpTemporal)
                # print(self.temporals)
                if self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'] == "" and self.OpTemporal[list(self.OpTemporal)[-1]]['exp2'] == "":
                    if self.variables[str(ctx.Id())]['ambito'] == "global":
                        self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'] = "gp[" + str(self.variables[str(ctx.Id())]['offset']) + "]"
                    else:
                        self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'] = "fp[" + str(self.variables[str(ctx.Id())]['offset']) + "]"
                elif self.OpTemporal[list(self.OpTemporal)[-1]]['exp2'] == "" and self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'] != "" and self.OpTemporal[list(self.OpTemporal)[-1]]['op'] != "":
                    #asignamos temporal a la ultima expresion del ultimo temporal
                    self.temporalsCount += 1
                    self.OpTemporal[list(self.OpTemporal)[-1]]['exp2'] = "t" + str(self.temporalsCount)
                    #generamos codigo que ira al OpCode
                    code = "\n\t" + list(self.OpTemporal)[-1] + " = " + self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'] + " " + self.OpTemporal[list(self.OpTemporal)[-1]]['op'] + " " + self.OpTemporal[list(self.OpTemporal)[-1]]['exp2']
                    #creamos nueva temporal
                    temp = "t" + str(self.temporalsCount)
                    self.OpTemporal[temp] = {'exp1': "", "op": "", 'exp2': ""}
                    self.temporalsCount += 1
                    #asignamos el valor que visitamos al siguiente temporal
                    if self.variables[str(ctx.Id())]['ambito'] == "global":
                        self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'] = "gp[" + str(self.variables[str(ctx.Id())]['offset']) + "]"
                    else:
                        self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'] = "fp[" + str(self.variables[str(ctx.Id())]['offset']) + "]"
                    
                    self.OpCode.insert(0,code)
            elif self.position == "asignL":
                self.position = "asign"
        else:
            self.fromArray = True
        return self.visitChildren(ctx)

    def visitArray_location(self, ctx:DECAFParser.Array_locationContext):
        self.fromArray = True
        # print("before")
        # print(self.position)
        # print(self.OpCode)
        # print(self.OpTemporal)
        var = str(ctx.Id())
        arr = str(ctx.getText())
        # print(var)
        # print(arr)
        if self.position == "if" or self.position == "while":
            # print("im in")
            # print(str(ctx.getText()))
            if arr in self.lists[var]['arrays']:
                # print(arr)
                if self.lists[var]["ambito"] == "global":
                    # print("in array location global")
                    self.interCode += arr
                else:
                    # print("in array location local")
                    self.interCode += "fp[" + str(self.lists[var]['arrays'][arr]["offset"]) + "]"
                # self.operandsCount += 1
            else:
                # print("hola")
                inter1 = self.interCode[0:self.interCode.rfind("\n")]
                # print("inter2")
                inter2 = self.interCode[self.interCode.rfind("\n"):]
                # print(inter2)
                varInArr = arr[arr.find("[")+1:-1]
                
                if self.operandsCount == 0:
                    ParamCode = "\n\tTL = 4 * fp[" + str(self.variables[varInArr]["offset"]) +"]"
                    # pass
                elif self.operandsCount == 1:
                    ParamCode = "\n\tTR = 4 * fp[" + str(self.variables[varInArr]["offset"]) +"]"
                # print("param code")
                # print(ParamCode)
            #         # code += "Param" + varname + "[TR]"
                # print(varInArr)
                if self.lists[var]["ambito"] == "global":
                    # print(varInArr)
                    # print("in array location global")
                    self.interCode = inter1 + ParamCode + inter2
                    if self.operandsCount == 0:
                        self.interCode += " " + var + "[TL]"
                        # pass
                    elif self.operandsCount == 1:
                        self.interCode += " " + var + "[TR]"
                else:
                    if self.operandsCount == 0:
                        ParamCode += "\n\tTL = " + str(self.lists[var]['offset']) + " + TL"
                        self.interCode = inter1 + ParamCode + inter2
                        self.interCode += " fp[TL]" 
                    else:
                        ParamCode += "\n\tTR = " + str(self.lists[var]['offset']) + " + TR"
                        self.interCode = inter1 + ParamCode + inter2
                        self.interCode += " fp[TR]" 

            self.operandsCount += 1
            if self.operandsCount >= 2:
                if self.position == "if":
                    self.interCode += " goto FalseIfL" + str(self.ifCount)
                if self.position == "while":
                    self.interCode += " goto FalseWhileL" + str(self.WhileCount)
                self.operandsCount = 0

        elif self.position == "return" or self.position == "asign":
            print("in Operation")
            print(var)
            print(arr)
            if self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'] == "" and self.OpTemporal[list(self.OpTemporal)[-1]]['exp2'] == "":
                if arr in self.lists[var]['arrays']:
                    if self.lists[var]['ambito'] == "global":
                        self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'] = arr
                    else:
                        self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'] = "fp[" + str(self.lists[var]["arrays"][arr]['offset']) + "]"
                else:
                    varInArray = arr[arr.find("[")+1:-1]
                    print(varInArray)
                    rigthParamCode = "\n\tTR = 4 * fp[" + str(self.variables[varInArray]["offset"]) +"]"
                    if self.lists[var]['ambito'] == "global":
                        self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'] = var + "[TR]"
                        # self.OpCode.insert(1,rigthParamCode) 
                    else:
                        rigthParamCode += "\n\tTR = " + str(self.lists[var]['offset']) + " + TR"
                        self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'] = "fp[" + str(self.lists[var]["arrays"][arr]['offset']) + "]"
                    self.OpCode.insert(0,rigthParamCode) 

            elif self.OpTemporal[list(self.OpTemporal)[-1]]['exp2'] == "" and self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'] != "" and self.OpTemporal[list(self.OpTemporal)[-1]]['op'] != "":
                #asignamos temporal a la ultima expresion del ultimo temporal
                rigthParamCode = ""
                self.temporalsCount += 1
                self.OpTemporal[list(self.OpTemporal)[-1]]['exp2'] = "t" + str(self.temporalsCount)
                #generamos codigo que ira al OpCode
                code = "\n\t" + list(self.OpTemporal)[-1] + " = " + self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'] + " " + self.OpTemporal[list(self.OpTemporal)[-1]]['op'] + " " + self.OpTemporal[list(self.OpTemporal)[-1]]['exp2']
                # creamos nueva temporal
                temp = "t" + str(self.temporalsCount)
                self.OpTemporal[temp] = {'exp1': "", "op": "", 'exp2': ""}
                self.temporalsCount += 1
                #asignamos el valor que visitamos al siguiente temporal
                if arr in self.lists[var]['arrays']:
                    if self.lists[var]['ambito'] == "global":
                        self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'] = arr
                    else:
                        self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'] = "fp[" + str(self.lists[var]["arrays"][arr]['offset']) + "]"
                else:
                    varInArray = arr[arr.find("[")+1:-1]
                    print(varInArray)
                    rigthParamCode = "\n\tTR = 4 * fp[" + str(self.variables[varInArray]["offset"]) +"]"
                    if self.lists[var]['ambito'] == "global":
                        self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'] = var + "[TR]"
                    else:
                        rigthParamCode += "\n\tTR = " + str(self.lists[var]['offset']) + " + TR"
                        print(var)
                        print(arr)
                        # """Aqui hay un error"""
                        self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'] = "fp[TR]"
                    # self.OpCode.append(rigthParamCode)
                
                print(str(self.OpCode))
                # print(rigthParamCode + "]]]]]")
                if rigthParamCode != "":
                    code = rigthParamCode + code 
                    self.OpCode.insert(1,code)
                else:
                    code = code + rigthParamCode
                    self.OpCode.insert(0,code)
        elif self.position == "asignL":
                self.position = "asign"

        return self.visitChildren(ctx)

    def visitNum_expr(self, ctx:DECAFParser.Num_exprContext):
        # self.operandsCount += 1
        # print(str(ctx.getText()))
        # print(str(self.fromArray) + "////")
        if self.fromArray == False:
            # print("inside")
            if (self.position == "if" or self.position == "while"):
                self.interCode += str(ctx.Num())
                self.operandsCount += 1
                if self.operandsCount >= 2:
                    if self.position == "if":
                        self.interCode += " goto FalseIfL" + str(self.ifCount)
                    if self.position == "while":
                        self.interCode += " goto FalseWhileL" + str(self.WhileCount)
                    self.operandsCount = 0
        # print(self.fromArray)
        
            if self.position == "return" or self.position == "asign":
                # print(self.position + " in Num")
                # print(self.OpTemporal)
                if self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'] == "" and self.OpTemporal[list(self.OpTemporal)[-1]]['exp2'] == "":    
                    self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'] = str(ctx.Num())
                elif self.OpTemporal[list(self.OpTemporal)[-1]]['exp2'] == "" and self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'] != "":
                    #asignamos temporal a la ultima expresion del ultimo temporal
                    self.temporalsCount += 1
                    self.OpTemporal[list(self.OpTemporal)[-1]]['exp2'] = "t" + str(self.temporalsCount)
                    #generamos codigo que ira al OpCode
                    code = "\n\t" + list(self.OpTemporal)[-1] + " = " + self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'] + " " + self.OpTemporal[list(self.OpTemporal)[-1]]['op'] + " " + self.OpTemporal[list(self.OpTemporal)[-1]]['exp2']
                    #creamos nueva temporal
                    temp = "t" + str(self.temporalsCount)
                    self.OpTemporal[temp] = {'exp1': "", "op": "", 'exp2': ""}
                    self.temporalsCount += 1
                    #asignamos el valor que visitamos al siguiente temporal
                    self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'] = str(ctx.Num())
                    
                    self.OpCode.insert(0,code)
            elif self.position == "asignL":
                self.position = "asign"
        else:
            self.fromArray = True
        
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DECAFParser#rel_op.
    def visitRel_op(self, ctx:DECAFParser.Rel_opContext):
        if self.position == "if" or self.position == "while":
            self.fromArray = False
            self.interCode += " " + str(ctx.getText()) + " "
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#eq_op.
    def visitEq_op(self, ctx:DECAFParser.Eq_opContext):
        if self.position == "if" or self.position == "while":
            # self.inOp = True
            self.fromArray = False
            self.interCode += " " + str(ctx.getText()) + " "
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#cond_op.
    def visitCond_op(self, ctx:DECAFParser.Cond_opContext):
        if self.position == "if" or self.position == "while":
            # self.inOp = True
            self.fromArray = False
            self.interCode += " " + str(ctx.getText()) + " "
        return self.visitChildren(ctx)

    def visitEndline(self, ctx:DECAFParser.EndlineContext):
        if self.position == "return" or self.position == "asign":
            print("\nin Endline")
            print(self.OpCode)
            print(self.OpTemporal)
            if len(self.OpCode) >= 2:
                    line1 = self.OpCode[0].split()
                    line2 = self.OpCode[1].split()
                    # print("lines")
                    print(str(line1))
                    try:
                        if "t" in line1[2] and "t" in line1[4]:
                            line2[-1] = line1[0]
                            newline1 = "\n\t"+line1[0] + " = " + line1[2] + " " + line1[3] + " " + line1[4]
                            newline2 = "\n\t"+line2[0] + " = " + line2[2]
                            self.OpCode[0] = newline1
                            self.OpCode[1] = newline2
                    except:
                        pass
                    # print(str(line1))
                    # print(str(line2))
                    # if 

            if self.OpTemporal[list(self.OpTemporal)[-1]]['exp2'] == '':
                # print("in Endline")
                # print(self.OpCode[0])
                # print(self.OpCode[1])
                # print(self.OpTemporal)
                # print(self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'])
                if "TR" not in self.OpCode[0]:
                    self.OpCode[0] = self.OpCode[0].replace(list(self.OpTemporal)[-1], self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'])
                else:
                    self.OpCode[1] = self.OpCode[1].replace(list(self.OpTemporal)[-1], self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'])
                    self.OpCode[0] = self.OpCode[0].replace(list(self.OpTemporal)[-1], self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'])
                
                "Volver aqui para ver las expresiones y sus temporales. decomentar la siguiente linea"
                # print(self.OpCode)
                try:
                    self.OpTemporal[list(self.OpTemporal)[-2]]['exp2'] = self.OpTemporal[list(self.OpTemporal)[-1]]['exp1']
                except:
                    pass
                self.OpTemporal.popitem()
                self.temporalsCount -= 1
                # print(self.temporalsCount)
                # print(self.OpCode[0])
            print(str(self.OpCode))
            for line in self.OpCode:
                self.interCode += line
            self.temporals.update(self.OpTemporal)
            # print(self.temporals)
            self.OpTemporal = {}
            # print(self.OpTemporal)
            self.OpCode = []
            self.position = ""
        else:
            # print(self.temporals)
            # print(self.OpCode)
            # print(self.position)
        # elif self.position == "asign":
        #     for line in self.OpCode:
        #         self.interCode += line
        #     self.temporals.update(self.OpTemporal)
        #     # print(self.temporals)
        #     self.OpTemporal = {}
        #     # print(self.OpTemporal)
        #     self.OpCode = []
        #     self.position = ""
        # print(self.ambito)
        # print(self.interCode)
            pass
        self.OpTemporal = {}
        # print(self.OpTemporal)
        self.OpCode = []
        self.position = ""
        self.fromArray = False
        return self.visitChildren(ctx)

    def visitElseStmt(self, ctx:DECAFParser.ElseStmtContext):
        # self.closetags.append("")
        closetag = self.lastIF 
        val = closetag[closetag.rfind("L") + 1:-1]
        inter1 = self.interCode[0:self.interCode.rfind("\n")]
        inter2 = self.interCode[self.interCode.rfind("\n"):]
        self.interCode = inter1 + "\n\tgoto TrueIfL" + val + inter2
        gotoTrueIF = "\nTrueIfL" + val +":"
        # print(gotoTrueIF)
        self.closetags.append(gotoTrueIF)
        return self.visitChildren(ctx)

    def visitCloseKey(self, ctx:DECAFParser.CloseKeyContext):
        # print(self.closetags)
        closetag = self.closetags[-1]
        if "While" in closetag:
            
            closetag = self.closetags.pop()
            val = closetag[closetag.rfind("L") + 1:-1]
            self.interCode += "\n\tgoto WhileTrue" + str(val)
            # print(val)
            self.interCode +=  closetag
        elif "If" in closetag:
            closetag = self.closetags.pop()
            self.lastIF = closetag
            # val = closetag[closetag.rfind("L") + 1:-1]
            # self.interCode += "\n\tgoto TrueIfL" + val
            # gotoTrueIF = "\nTrueIfL" + val +":"
            # # print(gotoTrueIF)
            # self.closetags.append(gotoTrueIF)
            self.interCode +=  closetag
        else:
            closetag = self.closetags.pop()
            self.interCode +=  closetag


        # print(self.closetags)
        return self.visitChildren(ctx)
