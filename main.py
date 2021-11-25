import sys
from antlr4 import *
from DECAFLexer import DECAFLexer
from DECAFParser import DECAFParser
from codeGenerator import codeGenerator
from miVisitor import miVisitor
# import IntermidiateCode


def main(argv):
    input = FileStream(argv[1])
    lexer = DECAFLexer(input)
    stream = CommonTokenStream(lexer)
    parser = DECAFParser(stream)
    tree = parser.program()
    # print(tree.toStringTree(recog=parser))

    visitor = miVisitor()
    visitor.visit(tree)
    
    print('Variables')
    print(visitor.variables)
    print('Listas')
    print(visitor.lists)
    # print('Structs')
    # print(visitor.structs)
    # print('Metodos')
    # print(visitor.metodos)
    # print('enviroment')
    # print(visitor.enviroments)
    # print("Temporales")
    # print(visitor.temporals)
    
    # print(visitor.interCode)
    textIntermedio=open("CodigoIntermedio.txt","w") 
    textIntermedio.write(visitor.interCode)
    textIntermedio.close()
    
    with open('CodigoIntermedio.txt') as f:
        lines = f.readlines()
    # print(lines)
    MIPS = codeGenerator(lines)
    ARMCode=open("MIPS.txt","w") 
    ARMCode.write(MIPS) 
    ARMCode.close()

if __name__ == '__main__':
    main(sys.argv)


    # return self.visitChildren(ctx)