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
        self.ifCount = 0
        self.WhileCount = 0

    def visitProgram(self, ctx:DECAFParser.ProgramContext):
        return self.visitChildren(ctx)

    '''Estos son los metodos para obtener el la informacion de todos los tipos de funciones
        Cada uno hace distincion si es sin metodos o con metodos'''

    def visitMetoInt(self, ctx:DECAFParser.MetoIntContext):
        if self.ambito != "global":
            self.interCode += "\nEnd " + str(self.ambito) + "\n"
        self.ambito = str(ctx.Id())
        self.interCode += "\nDef " + str(ctx.Id())
        # print(str(ctx.Id()))
        self.metodos[str(ctx.Id())] = {}
        self.metodos[str(ctx.Id())]['tipo'] = 'int'
        self.metodos[str(ctx.Id())]['offset'] = 0
        self.metodos[str(ctx.Id())]['return'] = ''
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitMetoIntWithParam(self, ctx:DECAFParser.MetoIntWithParamContext):
        if self.ambito != "global":
            self.interCode += "\nEnd " + str(self.ambito) + "\n"
        self.ambito = str(ctx.Id())
        self.interCode += "\nDef " + str(ctx.Id())

        self.metodos[str(ctx.Id())] = {}
        self.metodos[str(ctx.Id())]['tipo'] = 'int'
        self.metodos[str(ctx.Id())]['params'] = {}
        self.metodos[str(ctx.Id())]['offset'] = 0
        self.metodos[str(ctx.Id())]['return'] = ''
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitMetoChar(self, ctx:DECAFParser.MetoCharContext):
        if self.ambito != "global":
            self.interCode += "\nEnd " + str(self.ambito) + "\n"
        self.ambito = str(ctx.Id())
        self.interCode += "\nDef " + str(ctx.Id())

        self.metodos[str(ctx.Id())] = {}
        self.metodos[str(ctx.Id())]['tipo'] = 'char'
        self.metodos[str(ctx.Id())]['offset'] = 0
        self.metodos[str(ctx.Id())]['return'] = ''
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitMetoCharWithParam(self, ctx:DECAFParser.MetoCharWithParamContext):
        if self.ambito != "global":
            self.interCode += "\nEnd " + str(self.ambito) + "\n"
        self.ambito = str(ctx.Id())
        self.interCode += "\nDef " + str(ctx.Id())

        self.metodos[str(ctx.Id())] = {}
        self.metodos[str(ctx.Id())]['tipo'] = 'char'
        self.metodos[str(ctx.Id())]['params'] = {}
        self.metodos[str(ctx.Id())]['offset'] = 0
        self.metodos[str(ctx.Id())]['return'] = ''
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitMetoBool(self, ctx:DECAFParser.MetoBoolContext):
        if self.ambito != "global":
            self.interCode += "\nEnd " + str(self.ambito) + "\n"
        self.ambito = str(ctx.Id())
        self.interCode += "\nDef " + str(ctx.Id())

        self.metodos[str(ctx.Id())] = {}
        self.metodos[str(ctx.Id())]['tipo'] = 'boolean'
        self.metodos[str(ctx.Id())]['offset'] = 0
        self.metodos[str(ctx.Id())]['return'] = ''
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitMetoBoolWithParam(self, ctx:DECAFParser.MetoBoolWithParamContext):
        if self.ambito != "global":
            self.interCode += "\nEnd " + str(self.ambito) + "\n"
        self.ambito = str(ctx.Id())
        self.interCode += "\nDef " + str(ctx.Id())

        self.metodos[str(ctx.Id())] = {}
        self.metodos[str(ctx.Id())]['tipo'] = 'boolean'
        self.metodos[str(ctx.Id())]['params'] = {}
        self.metodos[str(ctx.Id())]['offset'] = 0
        self.metodos[str(ctx.Id())]['return'] = ''
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitMetoVoid(self, ctx:DECAFParser.MetoVoidContext):
        if self.ambito != "global":
            self.interCode += "\nEnd " + str(self.ambito) + "\n"
        self.ambito = str(ctx.Id())
        self.interCode += "\nDef " + str(ctx.Id())

        self.metodos[str(ctx.Id())] = {}
        self.metodos[str(ctx.Id())]['tipo'] = 'void'
        self.metodos[str(ctx.Id())]['offset'] = 0
        # print(ctx.Id())
        # print(ctx.getText())
        
        return self.visitChildren(ctx)

    def visitMetoVoidWithParam(self, ctx:DECAFParser.MetoVoidWithParamContext):
        if self.ambito != "global":
            self.interCode += "\nEnd " + str(self.ambito)
        self.ambito = str(ctx.Id())
        self.interCode += "\nDef " + str(ctx.Id())

        self.metodos[str(ctx.Id())] = {}
        self.metodos[str(ctx.Id())]['tipo'] = 'void'
        self.metodos[str(ctx.Id())]['params'] = {}
        self.metodos[str(ctx.Id())]['offset'] = 0
        # print(ctx.getText())
        
        return self.visitChildren(ctx)

    '''Con esta funcion puedo ir obteniendo cada uno de los parametros de cada funcion'''
    def visitSingle_parameterDeclaration(self, ctx:DECAFParser.Single_parameterDeclarationContext):
        self.interCode += "\n\tParam " + str(ctx.Id())
        
        self.variables[str(ctx.Id())] = {}
        self.variables[str(ctx.Id())]['tipo'] = ctx.getText()[:-len(str(ctx.Id()))]
        self.variables[str(ctx.Id())]['ambito'] = str(self.ambito)
        # self.variables[str(ctx.Id())]['offset'] = 0
        self.variables[str(ctx.Id())]['offset'] = TYPEVALUES[self.variables[str(ctx.Id())]['tipo']]
        self.variables[str(ctx.Id())]['value'] = TYPEINITVALUE[self.variables[str(ctx.Id())]['tipo']]
        
        self.metodos[self.ambito]['params'][str(ctx.Id())] = self.variables[str(ctx.Id())]
        self.metodos[self.ambito]['offset'] += self.variables[str(ctx.Id())]['offset']

        return self.visitChildren(ctx)

    ''' 
    Aqui es donde visitamos los tipos de variables como variables tipo int, char, bool, lists y los structs
    '''
    '''Esta es la funcion encargada de obtener la informacion de las variables int, char, bool'''
    def visitNormal(self, ctx:DECAFParser.NormalContext):
        
        if(" " not in str(ctx.parentCtx)):
            self.ambito = "global"
        # print(str(ctx.Id()))
        # print(len(str(ctx.Id())))
        # print(ctx.getText()[:-len(str(ctx.Id())) - 1])
        
        
        if("[" not in ctx.getText()):
            self.variables[str(ctx.Id())] = {}
            self.variables[str(ctx.Id())]['tipo'] = ctx.getText()[:-len(str(ctx.Id())) - 1].replace('struct','struct ')
            self.variables[str(ctx.Id())]['ambito'] = str(self.ambito)
            self.variables[str(ctx.Id())]['offset'] = 0

            if("struct" not in self.variables[str(ctx.Id())]['tipo']):
                self.variables[str(ctx.Id())]['offset'] = TYPEVALUES[self.variables[str(ctx.Id())]['tipo']]
                self.variables[str(ctx.Id())]['value'] = TYPEINITVALUE[self.variables[str(ctx.Id())]['tipo']]
            elif("struct" in self.variables[str(ctx.Id())]['tipo']):
                self.variables[str(ctx.Id())]['offset'] = self.structs[self.variables[str(ctx.Id())]['tipo']]['offset']

        if("struct" in self.variables[str(ctx.Id())]['ambito']):
            # print(self.variables)
            self.structs[self.variables[str(ctx.Id())]['ambito']]['variables'][str(ctx.Id())] = self.variables[str(ctx.Id())]
            self.structs[self.variables[str(ctx.Id())]['ambito']]['offset'] += self.variables[str(ctx.Id())]['offset']
        
        if(self.variables[str(ctx.Id())]['ambito'] != 'global' and "struct" not in self.variables[str(ctx.Id())]['ambito']):
            self.metodos[self.ambito]['offset'] += self.variables[str(ctx.Id())]['offset']

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
            self.metodos[self.ambito]['offset'] += self.lists[str(ctx.Id())]['offset']

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

    # Visit a parse tree produced by DECAFParser#returnStmt.
    def visitReturnStmt(self, ctx:DECAFParser.ReturnStmtContext):
        '''Fix Return '''
        self.interCode +=  "\n\tReturn " + ctx.getText()[6: -1]
        return self.visitChildren(ctx)

    '''Obtener los valores en las declaraciones de variables'''
    def visitAsign_statement(self, ctx:DECAFParser.Asign_statementContext):
        # print(str(ctx.getText()))
        return self.visitChildren(ctx)

    def visitArg(self, ctx:DECAFParser.ArgContext):
        
        inter1 = self.interCode[0:self.interCode.rfind("\n")]
        inter2 = self.interCode[self.interCode.rfind("\n"):]

        print(inter1)
        print(inter2)
        self.interCode= inter1 + "\n\tParam " + str(ctx.getText()) + inter2 
        return self.visitChildren(ctx)

    def visitLocation(self, ctx:DECAFParser.LocationContext):
        # self.interCode= "\nParam " + str(ctx.Id()) + self.interCode +"\n"
        return self.visitChildren(ctx)

    def visitMethodCall(self, ctx:DECAFParser.MethodCallContext):
        print(ctx.Id())
        self.interCode += "\n\tCall " + str(ctx.Id())
        return self.visitChildren(ctx)

    def visitWhileStmt(self, ctx:DECAFParser.WhileStmtContext):
        self.position = "while"
        return self.visitChildren(ctx)

    # Visit a parse tree produced by DECAFParser#ifSt_statement.
    def visitIfSt_statement(self, ctx:DECAFParser.IfSt_statementContext):
        self.position = "if"
        return self.visitChildren(ctx)

    def visitElseStmt(self, ctx:DECAFParser.ElseStmtContext):
        # self.ifCount -= 1
        self.interCode += "\nFalseIFL" + str(self.ifCount) + ":"
        return self.visitChildren(ctx)

    def visitCond_op_expr(self, ctx:DECAFParser.Cond_op_exprContext):
        if self.position == "if":
            self.ifCount += 1
            self.interCode += "\n\tIFFalse " + str(ctx.getText()) + " goto FalseIFL" + str(self.ifCount)
        if self.position == "while":
            self.WhileCount += 1
            self.interCode += "\nWhileTrue" + str(self.WhileCount)+ ":" + "\n\tIFFalse " + str(ctx.getText()) + " goto FalseIFL" + str(self.ifCount)            
        self.position = ""
        return self.visitChildren(ctx)

    def visitArith_op_expr(self, ctx:DECAFParser.Arith_op_exprContext):
        if self.position == "if":
            self.ifCount += 1
            self.interCode += "\n\tIFFalse " + str(ctx.getText()) + " goto FalseIFL" + str(self.ifCount)
        if self.position == "while":
            self.WhileCount += 1
            self.interCode += "\nWhileTrue" + str(self.WhileCount)+ ":" + "\n\tIFFalse " + str(ctx.getText()) + " goto FalseIFL" + str(self.ifCount)            
        self.position = ""
        return self.visitChildren(ctx)

    def visitArith_higher_expr(self, ctx:DECAFParser.Arith_higher_exprContext):
        if self.position == "if":
            self.ifCount += 1
            self.interCode += "\n\tIFFalse " + str(ctx.getText()) + " goto FalseIFL" + str(self.ifCount)
        if self.position == "while":
            self.WhileCount += 1
            self.interCode += "\nWhileTrue" + str(self.WhileCount)+ ":" + "\n\tIFFalse " + str(ctx.getText()) + " goto FalseIFL" + str(self.ifCount)            
        self.position = ""
        return self.visitChildren(ctx)

    def visitRel_op_expr(self, ctx:DECAFParser.Rel_op_exprContext):
        if self.position == "if":
            self.ifCount += 1
            self.interCode += "\n\tIFFalse " + str(ctx.getText()) + " goto FalseIFL" + str(self.ifCount)
        if self.position == "while":
            self.WhileCount += 1
            self.interCode += "\nWhileTrue" + str(self.WhileCount)+ ":" + "\n\tIFFalse " + str(ctx.getText()) + " goto FalseIFL" + str(self.ifCount)            
        self.position = ""
        return self.visitChildren(ctx)

    def visitEq_op_expr(self, ctx:DECAFParser.Eq_op_exprContext):
        if self.position == "if":
            self.ifCount += 1
            self.interCode += "\n\tIFFalse " + str(ctx.getText()) + " goto FalseIFL" + str(self.ifCount)
        if self.position == "while":
            self.WhileCount += 1
            self.interCode += "\nWhileTrue" + str(self.WhileCount)+ ":" + "\n\tIFFalse " + str(ctx.getText()) + " goto FalseIFL" + str(self.ifCount)            
        self.position = ""
        return self.visitChildren(ctx)
#offset es el valor calculado tomando de referencnia desde 0