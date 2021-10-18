# Generated from DECAF.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DECAFParser import DECAFParser
else:
    from DECAFParser import DECAFParser

# This class defines a complete generic visitor for a parse tree produced by DECAFParser.

class DECAFVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DECAFParser#program.
    def visitProgram(self, ctx:DECAFParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#structDeclara.
    def visitStructDeclara(self, ctx:DECAFParser.StructDeclaraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#varDecla.
    def visitVarDecla(self, ctx:DECAFParser.VarDeclaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#methodDecla.
    def visitMethodDecla(self, ctx:DECAFParser.MethodDeclaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#normal.
    def visitNormal(self, ctx:DECAFParser.NormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#lista.
    def visitLista(self, ctx:DECAFParser.ListaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#structDeclaration.
    def visitStructDeclaration(self, ctx:DECAFParser.StructDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#varType.
    def visitVarType(self, ctx:DECAFParser.VarTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#metoInt.
    def visitMetoInt(self, ctx:DECAFParser.MetoIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#metoIntWithParam.
    def visitMetoIntWithParam(self, ctx:DECAFParser.MetoIntWithParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#metoChar.
    def visitMetoChar(self, ctx:DECAFParser.MetoCharContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#metoCharWithParam.
    def visitMetoCharWithParam(self, ctx:DECAFParser.MetoCharWithParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#metoBool.
    def visitMetoBool(self, ctx:DECAFParser.MetoBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#metoBoolWithParam.
    def visitMetoBoolWithParam(self, ctx:DECAFParser.MetoBoolWithParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#metoVoid.
    def visitMetoVoid(self, ctx:DECAFParser.MetoVoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#metoVoidWithParam.
    def visitMetoVoidWithParam(self, ctx:DECAFParser.MetoVoidWithParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#single_parameterDeclaration.
    def visitSingle_parameterDeclaration(self, ctx:DECAFParser.Single_parameterDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#int_parameterType.
    def visitInt_parameterType(self, ctx:DECAFParser.Int_parameterTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#char_parameterType.
    def visitChar_parameterType(self, ctx:DECAFParser.Char_parameterTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#boolean_parameterType.
    def visitBoolean_parameterType(self, ctx:DECAFParser.Boolean_parameterTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#block.
    def visitBlock(self, ctx:DECAFParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#ifSt_statement.
    def visitIfSt_statement(self, ctx:DECAFParser.IfSt_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#while_statement.
    def visitWhile_statement(self, ctx:DECAFParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#return_statement.
    def visitReturn_statement(self, ctx:DECAFParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#method_call_statement.
    def visitMethod_call_statement(self, ctx:DECAFParser.Method_call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#block_statement.
    def visitBlock_statement(self, ctx:DECAFParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#asign_statement.
    def visitAsign_statement(self, ctx:DECAFParser.Asign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#char_asign_statement.
    def visitChar_asign_statement(self, ctx:DECAFParser.Char_asign_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#unknown_statement.
    def visitUnknown_statement(self, ctx:DECAFParser.Unknown_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#ifStmt.
    def visitIfStmt(self, ctx:DECAFParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#whileStmt.
    def visitWhileStmt(self, ctx:DECAFParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#returnStmt.
    def visitReturnStmt(self, ctx:DECAFParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#location.
    def visitLocation(self, ctx:DECAFParser.LocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#cond_op_expr.
    def visitCond_op_expr(self, ctx:DECAFParser.Cond_op_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#boolliteral_expr.
    def visitBoolliteral_expr(self, ctx:DECAFParser.Boolliteral_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#loca_expr.
    def visitLoca_expr(self, ctx:DECAFParser.Loca_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#num_expr.
    def visitNum_expr(self, ctx:DECAFParser.Num_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#arith_op_expr.
    def visitArith_op_expr(self, ctx:DECAFParser.Arith_op_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#parentesisexpr_expr.
    def visitParentesisexpr_expr(self, ctx:DECAFParser.Parentesisexpr_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#rel_op_expr.
    def visitRel_op_expr(self, ctx:DECAFParser.Rel_op_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#methodCall_expr.
    def visitMethodCall_expr(self, ctx:DECAFParser.MethodCall_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#charliteral_expr.
    def visitCharliteral_expr(self, ctx:DECAFParser.Charliteral_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#arith_higher_expr.
    def visitArith_higher_expr(self, ctx:DECAFParser.Arith_higher_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#negativo_expr.
    def visitNegativo_expr(self, ctx:DECAFParser.Negativo_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#eq_op_expr.
    def visitEq_op_expr(self, ctx:DECAFParser.Eq_op_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#negacion_expr.
    def visitNegacion_expr(self, ctx:DECAFParser.Negacion_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#methodCall.
    def visitMethodCall(self, ctx:DECAFParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#arg.
    def visitArg(self, ctx:DECAFParser.ArgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#arith_higher_op.
    def visitArith_higher_op(self, ctx:DECAFParser.Arith_higher_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#arith_op.
    def visitArith_op(self, ctx:DECAFParser.Arith_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#rel_op.
    def visitRel_op(self, ctx:DECAFParser.Rel_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#eq_op.
    def visitEq_op(self, ctx:DECAFParser.Eq_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#cond_op.
    def visitCond_op(self, ctx:DECAFParser.Cond_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DECAFParser#bool_literal.
    def visitBool_literal(self, ctx:DECAFParser.Bool_literalContext):
        return self.visitChildren(ctx)



del DECAFParser