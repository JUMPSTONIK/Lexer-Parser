import sys
from antlr4 import *
from DECAFLexer import DECAFLexer
from DECAFParser import DECAFParser
from miVisitor import miVisitor
# import IntermidiateCode


def main(argv):
    input = FileStream(argv[1])
    lexer = DECAFLexer(input)
    stream = CommonTokenStream(lexer)
    parser = DECAFParser(stream)
    tree = parser.program()
    

    visitor = miVisitor()
    visitor.visit(tree)
    # if visitor.ambito != "global":
    #     visitor.interCode = visitor.interCode + "\nEnd " + visitor.ambito
    print(visitor.interCode)
        
    
    # print('Variables')
    # print(visitor.variables)
    # print('Listas')
    # print(visitor.lists)
    # print('Structs')
    # print(visitor.structs)
    # print('Metodos')
    # print(visitor.metodos)
    # print('enviroment')
    # print(visitor.enviroments)
    print("Temporales")
    print(visitor.temporals)
    # content = ''
    # with open(argv[1]) as f:
    #     content = f.readlines()
    # print(content[0])

    # codigo_intermedio = IntermidiateCode.Generador(content)
    # IntermidiateCode.printCode(codigo_intermedio)

    # print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)


    # return self.visitChildren(ctx)