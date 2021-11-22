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
            print(self.ambito)
            self.ambito = "global"
        print(self.ambito)
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
        if("struct" not in self.lists[str(ctx.Id())]['tipo']):
            self.lists[str(ctx.Id())]['offset'] = TYPEVALUES[self.lists[str(ctx.Id())]['tipo']] * self.lists[str(ctx.Id())]['size']
        elif("struct" in self.variables[str(ctx.Id())]['tipo']):
                self.lists[str(ctx.Id())]['offset'] = self.structs[self.lists[str(ctx.Id())]['tipo']]['offset'] * self.lists[str(ctx.Id())]['size']
        
            
        if("struct" in self.lists[str(ctx.Id())]['ambito']):
            # print(self.variables)
            self.structs[self.lists[str(ctx.Id())]['ambito']]['variables'][str(ctx.Id())] = self.lists[str(ctx.Id())]
            self.structs[self.lists[str(ctx.Id())]['ambito']]['offset'] += self.lists[str(ctx.Id())]['offset']
        
        if(self.lists[str(ctx.Id())]['ambito'] != 'global' and "struct" not in self.lists[str(ctx.Id())]['ambito']):
            self.metodos[self.ambito]['size'] += TYPEVALUES[self.lists[str(ctx.Id())]['tipo']]

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
        # print(expresion + "/////")
        if("*" not in expresion and "/" not in expresion and "%" not in expresion and "+" not in expresion and "-" not in expresion and "(" not in expresion):
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
                    
                else:
                    self.interCode += expresion
            
            else:
                if self.variables[asign]['ambito'] == 'global':
                    self.interCode += "\n\tgp[" + str(self.variables[asign]['offset']) + "] = " + expresion
                else:
                    self.interCode += "\n\tfp[" + str(self.variables[asign]['offset']) + "] = " + expresion
            self.position = ""

        # elif ("*" not in expresion and "/" not in expresion and "%" not in expresion and "+" not in expresion and "-" not in expresion and "(" in expresion):
        #     print(expresion)
            
        #     temp = "t" + str(self.temporalsCount)
        #     self.OpTemporal[temp] = {'exp1': "", "op": "", 'exp2': ""}
        #     self.OpTemporal[temp]["op"] = "Call"
        #     self.OpTemporal[temp]["exp2"] = expresion[:expresion.find("(")]
        #     self.temporalsCount += 1
        #     self.interCode += "\n\t" + temp + " = Call " + self.OpTemporal[temp]["exp2"]
        #     print(self.OpCode)
        #     print(self.OpTemporal)
            
        else:
            
            temp = "t" + str(self.temporalsCount)
            
            self.position = "asignL"
            self.OpTemporal[temp] = {'exp1': "", "op": "", 'exp2': ""}
            self.temporalsCount += 1
            
            code = "\n\t"
            if self.variables[asign]['ambito'] == 'global':
                code += "gp[" + str(self.variables[asign]['offset']) + "] = " + str(list(self.OpTemporal)[-1])
            else:
                code += "fp[" + str(self.variables[asign]['offset']) + "] = " + str(list(self.OpTemporal)[-1])

            self.OpCode.insert(0,code)  
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
                    
                    
                else:
                    self.interCode += "\n\tParam " + expresion
                self.position = ""
            else:
                self.OpCode.insert(0, "\n\tParam " + str(list(self.OpTemporal)[-1])) 
                
        else:
            
            inter1 = self.interCode[0:self.interCode.rfind("\n")]
            inter2 = self.interCode[self.interCode.rfind("\n"):]
            
            if("*" not in str(ctx.getText()) and "/" not in str(ctx.getText()) and "%" not in str(ctx.getText()) and "+" not in str(ctx.getText()) and "-" not in str(ctx.getText()) and "(" not in str(ctx.getText())):
                print(str(ctx.getText()))
                if str(ctx.getText()) in self.variables:
                    if self.variables[str(ctx.getText())]['ambito'] == 'global':
                        self.interCode= inter1 + "\n\tParam " + "gp[" + str(self.variables[str(ctx.getText())]['offset']) + "]" + inter2 
                    else:
                        self.interCode= inter1 + "\n\tParam " + "fp[" + str(self.variables[str(ctx.getText())]['offset']) + "]" + inter2 
                elif str(ctx.getText()).isnumeric():
                    '''Aqui se arregla el enviar parametros numericos'''
                    pass
        return self.visitChildren(ctx)

    def visitMethodCall(self, ctx:DECAFParser.MethodCallContext):
        # print(ctx.Id())
        # print(self.position)
        if self.position == "return" or self.position == "asign":
            # print("in return")
            if self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'] == "" and self.OpTemporal[list(self.OpTemporal)[-1]]['exp2'] == "":
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
        
        # else:
        #     if self.position == "asign":
        #         self.temporalsCount -= 1
        #         temp = "t" + str(self.temporalsCount)
        #         self.OpTemporal[temp] = {'exp1': "", "op": "", 'exp2': ""}
        #         self.OpTemporal[temp]["op"] = "Call"
        #         self.OpTemporal[temp]["exp2"] = str(ctx.Id())
        #         self.interCode += "\n\t" + temp + " = Call " + str(ctx.Id())
        #         self.temporalsCount += 1
        else:
            self.interCode += "\n\tCall " + str(ctx.Id())
        # print(self.OpCode)
        # print(self.OpTemporal)
        return self.visitChildren(ctx)

    def visitWhileStmt(self, ctx:DECAFParser.WhileStmtContext):
        self.position = "while"
        self.WhileCount += 1
        self.closetags.append("\nFalseWhileL" + str(self.WhileCount) + ":")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DECAFParser#ifSt_statement.
    def visitIfSt_statement(self, ctx:DECAFParser.IfSt_statementContext):
        self.position = "if"
        self.ifCount += 1
        self.closetags.append("\nFalseIfL" + str(self.ifCount) + ":")
        return self.visitChildren(ctx)

    def visitElseStmt(self, ctx:DECAFParser.ElseStmtContext):
        # self.closetags.append("")
        return self.visitChildren(ctx)

    def visitCond_op_expr(self, ctx:DECAFParser.Cond_op_exprContext):

        if self.position == "if":
            
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
            self.OpTemporal[list(self.OpTemporal)[-1]]['op'] = str(ctx.getText())
            # print(self.position + " in arith high")
            # print(self.OpTemporal)

        return self.visitChildren(ctx)

    def visitArith_op(self, ctx:DECAFParser.Arith_opContext):
        if self.position == "return" or self.position == "asign":
            print(str(ctx.getText()))
            
            self.OpTemporal[list(self.OpTemporal)[-1]]['op'] = str(ctx.getText())
            # print(self.position + " in arith high")
            # print(self.OpTemporal)
            self.savedOP.append(str(ctx.getText()))
            # print(str(self.temporals) + ";;;")
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

    def visitLocation(self, ctx:DECAFParser.LocationContext):
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
        return self.visitChildren(ctx)

    def visitNum_expr(self, ctx:DECAFParser.Num_exprContext):
        if (self.position == "if" or self.position == "while"):
            self.interCode += str(ctx.Num())
            self.operandsCount += 1
            if self.operandsCount >= 2:
                if self.position == "if":
                    self.interCode += " goto FalseIfL" + str(self.ifCount)
                if self.position == "while":
                    self.interCode += " goto FalseWhileL" + str(self.WhileCount)
                self.operandsCount = 0
            

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
        
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DECAFParser#rel_op.
    def visitRel_op(self, ctx:DECAFParser.Rel_opContext):
        if self.position == "if" or self.position == "while":
            # self.inOp = True
            self.interCode += " " + str(ctx.getText()) + " "
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#eq_op.
    def visitEq_op(self, ctx:DECAFParser.Eq_opContext):
        if self.position == "if" or self.position == "while":
            # self.inOp = True
            self.interCode += " " + str(ctx.getText()) + " "
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#cond_op.
    def visitCond_op(self, ctx:DECAFParser.Cond_opContext):
        if self.position == "if" or self.position == "while":
            # self.inOp = True
            self.interCode += " " + str(ctx.getText()) + " "
        return self.visitChildren(ctx)

    def visitEndline(self, ctx:DECAFParser.EndlineContext):
        if self.position == "return" or self.position == "asign":
            # print(self.OpCode)
            # print(self.OpTemporal)
            if self.OpTemporal[list(self.OpTemporal)[-1]]['exp2'] == '':
                # print(self.OpCode[0])
                # print(list(self.OpTemporal)[-1])
                # print(self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'])
                self.OpCode[0] = self.OpCode[0].replace(list(self.OpTemporal)[-1],self.OpTemporal[list(self.OpTemporal)[-1]]['exp1'])
                try:
                    self.OpTemporal[list(self.OpTemporal)[-2]]['exp2'] = self.OpTemporal[list(self.OpTemporal)[-1]]['exp1']
                except:
                    pass
                self.OpTemporal.popitem()
                self.temporalsCount -= 1
                # print(self.temporalsCount)
                # print(self.OpCode[0])
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
        return self.visitChildren(ctx)

    def visitCloseKey(self, ctx:DECAFParser.CloseKeyContext):
        print(self.closetags)
        closetag = self.closetags.pop()
        if "While" in closetag:
            val = closetag[closetag.rfind("L") + 1:-1]
            self.interCode += "\n\tgoto WhileTrue" + str(val)
            # print(val)
        elif "FalseIf" in closetag:
            val = closetag[closetag.rfind("L") + 1:-1]
            self.interCode += "\n\tgoto TrueIfL" + val
            gotoTrueIF = "\nTrueIfL" + val +":"
            # print(gotoTrueIF)
            self.closetags.append(gotoTrueIF)
        
        self.interCode +=  closetag
        # print(self.closetags)
        return self.visitChildren(ctx)
