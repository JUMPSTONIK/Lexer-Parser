from DecafParser import DecafParser
from DecafVisitor import DecafVisitor
from TablaDeSimbolos import *

class miVisitor(DecafVisitor):
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
        self.variables = []
        self.structs = []
        self.vars = {}
        self.lists ={}
        self.strucs = {}


    def visitProgram(self, ctx:DecafParser.ProgramContext):
        return self.visitChildren(ctx)

    '''Estos son los metodos para obtener el la informacion de todos los tipos de funciones
        Cada uno hace distincion si es sin metodos o con metodos'''

    def visitMetoInt(self, ctx:DecafParser.MetoIntContext):
        self.ambito = ctx.Id()
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitMetoIntWithParam(self, ctx:DecafParser.MetoIntWithParamContext):
        self.ambito = ctx.Id()
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitMetoChar(self, ctx:DecafParser.MetoCharContext):
        self.ambito = ctx.Id()
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitMetoCharWithParam(self, ctx:DecafParser.MetoCharWithParamContext):
        self.ambito = ctx.Id()
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitMetoBool(self, ctx:DecafParser.MetoBoolContext):
        self.ambito = ctx.Id()
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitMetoBoolWithParam(self, ctx:DecafParser.MetoBoolWithParamContext):
        self.ambito = ctx.Id()
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitMetoVoid(self, ctx:DecafParser.MetoVoidContext):
        # print("----" + str(ctx.parentCtx))
        self.ambito = ctx.Id()
        # print(ctx.Id())
        # print(ctx.getText())
        
        return self.visitChildren(ctx)

    def visitMetoVoidWithParam(self, ctx:DecafParser.MetoVoidWithParamContext):
        self.ambito = ctx.Id()
        # print(ctx.getText())
        
        return self.visitChildren(ctx)
    #'''
    def visitVarType(self, ctx:DecafParser.VarTypeContext):
        
        # print("ambito es " + str(self.ambito))

        self.variables[len(self.variables)-1].ambito = self.ambito
        
        if( "struct" in str(ctx.getText())):
            vartype = str(ctx.getText()).replace("struct", "struct ")
            # print("tipo de variable " + vartype)
            self.variables[len(self.variables)-1].tipo = vartype
            for struct in self.structs:
                if struct.nombre == vartype:
                    self.variables[len(self.variables)-1].offset = struct.offset
                    if "struct" in str(self.ambito):
                        self.structs[len(self.structs)-1].offset += struct.offset
                    break
                    
        else:
            # print("tipo de variable " + str(ctx.getText()))
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
    #'''


    ''' 
    Aqui es donde visitamos los tipos de variables como variables tipo int, char, bool, lists y los structs
    '''
    '''Esta es la funcion encargada de obtener la informacion de las variables int, char, bool'''
    def visitNormal(self, ctx:DecafParser.NormalContext):
        var = Variables()
        self.variables.append(var)
        if(" " not in str(ctx.parentCtx)):
            self.ambito = "global"

        self.variables[len(self.variables)-1].nombre = str(ctx.Id())
        # print(str(ctx.Id()))
        # print(len(str(ctx.Id())))
        # print(ctx.getText()[:-len(str(ctx.Id())) - 1])
        
        
        if("[" not in ctx.getText()):
            self.vars[str(ctx.Id())] = {}
            self.vars[str(ctx.Id())]['tipo'] = ctx.getText()[:-len(str(ctx.Id())) - 1].replace('struct','struct ')
            self.vars[str(ctx.Id())]['ambito'] = str(self.ambito)
            self.vars[str(ctx.Id())]['offset'] = 0
            
            if("struct" not in self.vars[str(ctx.Id())]['tipo']):
                self.vars[str(ctx.Id())]['offset'] = TYPEVALUES[self.vars[str(ctx.Id())]['tipo']]
                self.vars[str(ctx.Id())]['value'] = TYPEINITVALUE[self.vars[str(ctx.Id())]['tipo']]
            elif("struct" in self.vars[str(ctx.Id())]['tipo']):
                self.vars[str(ctx.Id())]['offset'] = self.strucs[self.vars[str(ctx.Id())]['tipo']]['offset']

        if("struct" in self.vars[str(ctx.Id())]['ambito']):
            print(self.vars)
            self.strucs[self.vars[str(ctx.Id())]['ambito']]['variables'][str(ctx.Id())] = self.vars[str(ctx.Id())]
            # print(self.vars[str(ctx.Id())]['offset'])
            self.strucs[self.vars[str(ctx.Id())]['ambito']]['offset'] += self.vars[str(ctx.Id())]['offset']
        # print(self.strucs)
        # print(self.vars)
        # print(ctx.varType)
        return self.visitChildren(ctx)

    '''Esta es la funcion encargada de obtener la informacion de las variables del tipo lista'''
    def visitLista(self, ctx:DecafParser.ListaContext):
        # print(ctx.Num())
        if(" " not in str(ctx.parentCtx)):
            self.ambito = "global"
            
        var = Variables()
        self.variables.append(var)
        self.variables[len(self.variables) - 1].size = int(str(ctx.Num()))
        self.variables[len(self.variables) - 1].nombre = str(ctx.Id())

        self.lists[str(ctx.Id())] = {}
        self.lists[str(ctx.Id())]['size'] = int(str(ctx.Num()))
        print(ctx.getText())
        self.lists[str(ctx.Id())]['tipo'] = ctx.getText()[:-(len(str(ctx.Num())) + len(str(ctx.Id()))) - 3].replace('struct','struct ')
        # print("antes de anadir ambito " + str(self.ambito))
        self.lists[str(ctx.Id())]['ambito'] = str(self.ambito)
        if("struct" not in self.lists[str(ctx.Id())]['tipo']):
            self.lists[str(ctx.Id())]['offset'] = TYPEVALUES[self.lists[str(ctx.Id())]['tipo']] * self.lists[str(ctx.Id())]['size']
        else:
            self.lists[str(ctx.Id())]['offset'] = 0
        # print("nombre de la variable es " + str(ctx.Id()))
        # print("tamaño de la lista es " + str(ctx.Num()))
            
        return self.visitChildren(ctx)

    '''Esta es la funcion encargada de obtener la informacion de las variables de tipo struct'''
    def visitStructDeclaration(self, ctx:DecafParser.StructDeclarationContext):
        # print("----" + str(ctx.parentCtx))
        self.ambito = "struct "
        self.ambito += str(ctx.Id())
        name = 'struct ' + str(ctx.Id())
        struct = Structs()
        self.strucs[name] = {}
        self.strucs[name]['ambito'] = 'global'
        self.strucs[name]['offset'] = 0
        self.strucs[name]['variables'] = {}
        struct.nombre = self.ambito
        self.structs.append(struct)
        # print(len(self.structs))

        # print("esta en el " + str(self.ambito))
        return self.visitChildren(ctx)
