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
        

    print('Variables')
    print(visitor.variables)
    print('Listas')
    print(visitor.lists)
    print('Structs')
    print(visitor.structs)
    print('Metodos')
    print(visitor.metodos)

    # print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)


    # return self.visitChildren(ctx)