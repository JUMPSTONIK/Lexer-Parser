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
        self.variables = {}
        self.lists ={}
        self.structs = {}
        self.metodos = {}

    def visitProgram(self, ctx:DecafParser.ProgramContext):
        return self.visitChildren(ctx)

    '''Estos son los metodos para obtener el la informacion de todos los tipos de funciones
        Cada uno hace distincion si es sin metodos o con metodos'''

    def visitMetoInt(self, ctx:DecafParser.MetoIntContext):
        self.ambito = ctx.Id()
        # print(str(ctx.Id()))
        self.metodos[str(ctx.Id())] = {}
        self.metodos[str(ctx.Id())]['tipo'] = 'int'
        self.metodos[str(ctx.Id())]['offset'] = 0
        self.metodos[str(ctx.Id())]['return'] = ''
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitMetoIntWithParam(self, ctx:DecafParser.MetoIntWithParamContext):
        self.ambito = ctx.Id()
        self.metodos[str(ctx.Id())] = {}
        self.metodos[str(ctx.Id())]['tipo'] = 'int'
        self.metodos[str(ctx.Id())]['params'] = {}
        self.metodos[str(ctx.Id())]['offset'] = 0
        self.metodos[str(ctx.Id())]['return'] = ''
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitMetoChar(self, ctx:DecafParser.MetoCharContext):
        self.ambito = ctx.Id()
        self.metodos[str(ctx.Id())] = {}
        self.metodos[str(ctx.Id())]['tipo'] = 'char'
        self.metodos[str(ctx.Id())]['offset'] = 0
        self.metodos[str(ctx.Id())]['return'] = ''
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitMetoCharWithParam(self, ctx:DecafParser.MetoCharWithParamContext):
        self.ambito = ctx.Id()
        self.metodos[str(ctx.Id())] = {}
        self.metodos[str(ctx.Id())]['tipo'] = 'char'
        self.metodos[str(ctx.Id())]['params'] = {}
        self.metodos[str(ctx.Id())]['offset'] = 0
        self.metodos[str(ctx.Id())]['return'] = ''
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitMetoBool(self, ctx:DecafParser.MetoBoolContext):
        self.ambito = ctx.Id()
        self.metodos[str(ctx.Id())] = {}
        self.metodos[str(ctx.Id())]['tipo'] = 'boolean'
        self.metodos[str(ctx.Id())]['offset'] = 0
        self.metodos[str(ctx.Id())]['return'] = ''
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitMetoBoolWithParam(self, ctx:DecafParser.MetoBoolWithParamContext):
        self.ambito = ctx.Id()
        self.metodos[str(ctx.Id())] = {}
        self.metodos[str(ctx.Id())]['tipo'] = 'boolean'
        self.metodos[str(ctx.Id())]['params'] = {}
        self.metodos[str(ctx.Id())]['offset'] = 0
        self.metodos[str(ctx.Id())]['return'] = ''
        # print(ctx.getText())
        return self.visitChildren(ctx)

    def visitMetoVoid(self, ctx:DecafParser.MetoVoidContext):
        # print("----" + str(ctx.parentCtx))
        self.ambito = ctx.Id()
        self.metodos[str(ctx.Id())] = {}
        self.metodos[str(ctx.Id())]['tipo'] = 'void'
        self.metodos[str(ctx.Id())]['offset'] = 0
        # print(ctx.Id())
        # print(ctx.getText())
        
        return self.visitChildren(ctx)

    def visitMetoVoidWithParam(self, ctx:DecafParser.MetoVoidWithParamContext):
        self.ambito = ctx.Id()
        self.metodos[str(ctx.Id())] = {}
        self.metodos[str(ctx.Id())]['tipo'] = 'void'
        self.metodos[str(ctx.Id())]['params'] = {}
        self.metodos[str(ctx.Id())]['offset'] = 0
        # print(ctx.getText())
        
        return self.visitChildren(ctx)

    '''Con esta funcion puedo ir obteniendo cada uno de los parametros de cada funcion'''
    def visitSingle_parameterDeclaration(self, ctx:DecafParser.Single_parameterDeclarationContext):
        print(ctx.getText())
        return self.visitChildren(ctx)

    ''' 
    Aqui es donde visitamos los tipos de variables como variables tipo int, char, bool, lists y los structs
    '''
    '''Esta es la funcion encargada de obtener la informacion de las variables int, char, bool'''
    def visitNormal(self, ctx:DecafParser.NormalContext):
        
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
        # print(self.structs)
        # print(self.variables)
        # print(ctx.varType)
        return self.visitChildren(ctx)

    '''Esta es la funcion encargada de obtener la informacion de las variables del tipo lista'''
    def visitLista(self, ctx:DecafParser.ListaContext):
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
        
        return self.visitChildren(ctx)

    '''Esta es la funcion encargada de obtener la informacion de las variables de tipo struct'''
    def visitStructDeclaration(self, ctx:DecafParser.StructDeclarationContext):
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
