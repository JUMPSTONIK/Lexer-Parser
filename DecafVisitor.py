# Generated from Decaf.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DecafParser import DecafParser
else:
    from DecafParser import DecafParser

# This class defines a complete generic visitor for a parse tree produced by DecafParser.

class DecafVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DecafParser#program.
    def visitProgram(self, ctx:DecafParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#structDeclara.
    def visitStructDeclara(self, ctx:DecafParser.StructDeclaraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#varDecla.
    def visitVarDecla(self, ctx:DecafParser.VarDeclaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#methodDecla.
    def visitMethodDecla(self, ctx:DecafParser.MethodDeclaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#normal.
    def visitNormal(self, ctx:DecafParser.NormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#lista.
    def visitLista(self, ctx:DecafParser.ListaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#structDeclaration.
    def visitStructDeclaration(self, ctx:DecafParser.StructDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#varType.
    def visitVarType(self, ctx:DecafParser.VarTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#metoInt.
    def visitMetoInt(self, ctx:DecafParser.MetoIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#metoIntWithParam.
    def visitMetoIntWithParam(self, ctx:DecafParser.MetoIntWithParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#metoChar.
    def visitMetoChar(self, ctx:DecafParser.MetoCharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#metoCharWithParam.
    def visitMetoCharWithParam(self, ctx:DecafParser.MetoCharWithParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#metoBool.
    def visitMetoBool(self, ctx:DecafParser.MetoBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#metoBoolWithParam.
    def visitMetoBoolWithParam(self, ctx:DecafParser.MetoBoolWithParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#metoVoid.
    def visitMetoVoid(self, ctx:DecafParser.MetoVoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#metoVoidWithParam.
    def visitMetoVoidWithParam(self, ctx:DecafParser.MetoVoidWithParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#single_parameterDeclaration.
    def visitSingle_parameterDeclaration(self, ctx:DecafParser.Single_parameterDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#int_parameterType.
    def visitInt_parameterType(self, ctx:DecafParser.Int_parameterTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#char_parameterType.
    def visitChar_parameterType(self, ctx:DecafParser.Char_parameterTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#boolean_parameterType.
    def visitBoolean_parameterType(self, ctx:DecafParser.Boolean_parameterTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#block.
    def visitBlock(self, ctx:DecafParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#statement.
    def visitStatement(self, ctx:DecafParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#ifStmt.
    def visitIfStmt(self, ctx:DecafParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#whileStmt.
    def visitWhileStmt(self, ctx:DecafParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#returnStmt.
    def visitReturnStmt(self, ctx:DecafParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#location.
    def visitLocation(self, ctx:DecafParser.LocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#cond_op_expr.
    def visitCond_op_expr(self, ctx:DecafParser.Cond_op_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#boolliteral_expr.
    def visitBoolliteral_expr(self, ctx:DecafParser.Boolliteral_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#loca_expr.
    def visitLoca_expr(self, ctx:DecafParser.Loca_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#num_expr.
    def visitNum_expr(self, ctx:DecafParser.Num_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#arith_op_expr.
    def visitArith_op_expr(self, ctx:DecafParser.Arith_op_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#parentesisexpr_expr.
    def visitParentesisexpr_expr(self, ctx:DecafParser.Parentesisexpr_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#rel_op_expr.
    def visitRel_op_expr(self, ctx:DecafParser.Rel_op_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#methodCall_expr.
    def visitMethodCall_expr(self, ctx:DecafParser.MethodCall_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#charliteral_expr.
    def visitCharliteral_expr(self, ctx:DecafParser.Charliteral_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#arith_higher_expr.
    def visitArith_higher_expr(self, ctx:DecafParser.Arith_higher_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#negativo_expr.
    def visitNegativo_expr(self, ctx:DecafParser.Negativo_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#eq_op_expr.
    def visitEq_op_expr(self, ctx:DecafParser.Eq_op_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#negacion_expr.
    def visitNegacion_expr(self, ctx:DecafParser.Negacion_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#methodCall.
    def visitMethodCall(self, ctx:DecafParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#arg.
    def visitArg(self, ctx:DecafParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#arith_higher_op.
    def visitArith_higher_op(self, ctx:DecafParser.Arith_higher_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#arith_op.
    def visitArith_op(self, ctx:DecafParser.Arith_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#rel_op.
    def visitRel_op(self, ctx:DecafParser.Rel_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#eq_op.
    def visitEq_op(self, ctx:DecafParser.Eq_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#cond_op.
    def visitCond_op(self, ctx:DecafParser.Cond_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DecafParser#bool_literal.
    def visitBool_literal(self, ctx:DecafParser.Bool_literalContext):
        return self.visitChildren(ctx)



del DecafParser