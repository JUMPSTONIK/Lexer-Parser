import sys
from antlr4 import *
from DecafLexer import DecafLexer
from DecafParser import DecafParser
from miVisitor import miVisitor



def main(argv):
    input = FileStream(argv[1])
    lexer = DecafLexer(input)
    stream = CommonTokenStream(lexer)
    parser = DecafParser(stream)
    tree = parser.program()
    

    visitor = miVisitor()
    visitor.visit(tree)

    # Mostrar las variables
    print("\nvariables")
    for item in visitor.variables:
        item.showValues()
        
    # agregar las variable correspondientes a su struct y ambito
    for i in range(0, len(visitor.structs)):
        for var in visitor.variables:
            if visitor.structs[i].nombre == var.ambito:
                visitor.structs[i].variables.append(var)
    print('Variables')
    print(visitor.vars)
    print('listas')
    print(visitor.lists)
    print('structs')
    print(visitor.strucs)

    # Mostrar los Structs
    for struct in visitor.structs:
        print("\n=========")
        print("Struct\n")
        print(struct.nombre)
        struct.showValues()
        struct.showVariables()



    # print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)


    # return self.visitChildren(ctx)