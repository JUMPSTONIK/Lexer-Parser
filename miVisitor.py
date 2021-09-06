from DecafParser import DecafParser
from DecafVisitor import DecafVisitor
from TablaDeSimbolos import *

class miVisitor(DecafVisitor):
    def __init__(self):
        self.ambito = "global"
        self.contMainVoids = 0
        self.variables = []
        self.structs = []


    def visitProgram(self, ctx:DecafParser.ProgramContext):
        return self.visitChildren(ctx)

    def visitStructDeclaration(self, ctx:DecafParser.StructDeclarationContext):
        # print("----" + str(ctx.parentCtx))
        self.ambito = "struct "
        self.ambito += str(ctx.Id())
        struct = Structs()
        struct.nombre = self.ambito
        self.structs.append(struct)
        # print(len(self.structs))

        # print("esta en el " + str(self.ambito))
        return self.visitChildren(ctx)

    def visitMetoInt(self, ctx:DecafParser.MetoIntContext):
        self.ambito = ctx.Id()
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitMetoIntWithParam(self, ctx:DecafParser.MetoIntWithParamContext):
        self.ambito = ctx.Id()
        # print(ctx.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#metoChar.
    def visitMetoChar(self, ctx:DecafParser.MetoCharContext):
        self.ambito = ctx.Id()
        # print(ctx.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#metoCharWithParam.
    def visitMetoCharWithParam(self, ctx:DecafParser.MetoCharWithParamContext):
        self.ambito = ctx.Id()
        # print(ctx.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#metoBool.
    def visitMetoBool(self, ctx:DecafParser.MetoBoolContext):
        self.ambito = ctx.Id()
        # print(ctx.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#metoBoolWithParam.
    def visitMetoBoolWithParam(self, ctx:DecafParser.MetoBoolWithParamContext):
        self.ambito = ctx.Id()
        # print(ctx.getText())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#metoVoid.
    def visitMetoVoid(self, ctx:DecafParser.MetoVoidContext):
        # print("----" + str(ctx.parentCtx))
        self.ambito = ctx.Id()
        # print(ctx.getText())

        if( "return" in ctx.getText()):
            print(ctx.getText())
            print("error: Los metodos de tipo void no devuelven ningun valor. existe un <return> en su void")
        if("voidmain(void)" in ctx.getText() ):
            self.contMainVoids += 1
        if(self.contMainVoids == 0):
            print("error: No ha sido declarada una funcion main para la ejecucion del programa")
        elif(self.contMainVoids > 1):
            print(ctx.getText())
            print("error: No puede tener mas de un <void main(void){}> para la ejecucion del archivo")
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#metoVoidWithParam.
    def visitMetoVoidWithParam(self, ctx:DecafParser.MetoVoidWithParamContext):
        self.ambito = ctx.Id()
        # print(ctx.getText())
        if( "return" in ctx.getText()):
            print(ctx.getText())
            print("error: Los metodos de tipo void no devuelven ningun valor. existe un <return> en su void")
        return self.visitChildren(ctx)
    
    def visitVarType(self, ctx:DecafParser.VarTypeContext):
        
        print("ambito es " + str(self.ambito))

        self.variables[len(self.variables)-1].ambito = self.ambito
        
        if( "struct" in str(ctx.getText())):
            vartype = str(ctx.getText()).replace("struct", "struct ")
            print("tipo de variable " + vartype)
            self.variables[len(self.variables)-1].tipo = vartype
            for struct in self.structs:
                if struct.nombre == vartype:
                    self.variables[len(self.variables)-1].offset = struct.offset
                    if "struct" in str(self.ambito):
                        self.structs[len(self.structs)-1].offset += struct.offset
                    break
                    
        else:
            print("tipo de variable " + str(ctx.getText()))
            self.variables[len(self.variables)-1].tipo = str(ctx.getText())
            self.variables[len(self.variables)-1].setOffset()
            if ("struct" in str(self.ambito)):
                if str(ctx.getText()) == "int" and self.variables[len(self.variables)-1].size == 0:
                    self.structs[len(self.structs)-1].offset += 4
                elif str(ctx.getText()) == "int" and self.variables[len(self.variables)-1].size != 0:
                    self.structs[len(self.structs)-1].offset += 4 * self.variables[len(self.variables)-1].size
                elif str(ctx.getText()) == "char" and self.variables[len(self.variables)-1].size == 0:
                    self.structs[len(self.structs)-1].offset += 2
                elif str(ctx.getText()) == "char" and self.variables[len(self.variables)-1].size != 0:
                    self.structs[len(self.structs)-1].offset += 2 * self.variables[len(self.variables)-1].size
                elif str(ctx.getText()) == "boolean" and self.variables[len(self.variables)-1].size == 0:
                    self.structs[len(self.structs)-1].offset += 1
                elif str(ctx.getText()) == "boolean" and self.variables[len(self.variables)-1].size != 0:
                    self.structs[len(self.structs)-1].offset += 1 * self.variables[len(self.variables)-1].size        
        
        return self.visitChildren(ctx)

    def visitNormal(self, ctx:DecafParser.NormalContext):
        var = Variables()
        self.variables.append(var)
        # print("----" + str(ctx.parentCtx))
        if(" " not in str(ctx.parentCtx)):
            self.ambito = "global"
        # print("----" + str(ctx.parentCtx))
        # print("esta en el " + str(self.ambito))
        print( "nombre de la variable es " + str(ctx.Id()))
        self.variables[len(self.variables)-1].nombre = str(ctx.Id())
        # print(ctx.vartype)
        # print(ctx.Id())
        return self.visitChildren(ctx)

    def visitLista(self, ctx:DecafParser.ListaContext):
        # print(ctx.Num())
        
        if(ctx.Num()== 0):
            print(ctx.getText())
            print("error: la listas deben tener un tamaño mayor a 0")
        elif(ctx.Num() == None):
            print(ctx.getText()  + "]")
            print("error: la listas deben tener numeros enteros nada mas y ser mayor a 0. Siempre debe definir el tamaño de la lista")
        else:
            var = Variables()
            self.variables.append(var)
            self.variables[len(self.variables) - 1].size = int(str(ctx.Num()))
            self.variables[len(self.variables) - 1].nombre = str(ctx.Id())
            print("nombre de la variable es " + str(ctx.Id()))
            print("tamaño de la lista es " + str(ctx.Num()))
            
        return self.visitChildren(ctx)

    def visitIfStmt(self, ctx:DecafParser.IfStmtContext):
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitRel_op_expr(self, ctx:DecafParser.Rel_op_exprContext):
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitEq_op_expr(self, ctx:DecafParser.Eq_op_exprContext):
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitCond_op_expr(self, ctx:DecafParser.Cond_op_exprContext):
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitParentesisexpr_expr(self, ctx:DecafParser.Parentesisexpr_exprContext):
        # print(ctx.getText())
        return self.visitChildren(ctx)


    def visitWhileStmt(self, ctx:DecafParser.WhileStmtContext):
        return self.visitChildren(ctx)
