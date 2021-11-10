# Generated from DECAF.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DECAFParser import DECAFParser
else:
    from DECAFParser import DECAFParser

# This class defines a complete listener for a parse tree produced by DECAFParser.
class DECAFListener(ParseTreeListener):

    # Enter a parse tree produced by DECAFParser#program.
    def enterProgram(self, ctx:DECAFParser.ProgramContext):
        pass

    # Exit a parse tree produced by DECAFParser#program.
    def exitProgram(self, ctx:DECAFParser.ProgramContext):
        pass


    # Enter a parse tree produced by DECAFParser#structDeclara.
    def enterStructDeclara(self, ctx:DECAFParser.StructDeclaraContext):
        pass

    # Exit a parse tree produced by DECAFParser#structDeclara.
    def exitStructDeclara(self, ctx:DECAFParser.StructDeclaraContext):
        pass


    # Enter a parse tree produced by DECAFParser#varDecla.
    def enterVarDecla(self, ctx:DECAFParser.VarDeclaContext):
        pass

    # Exit a parse tree produced by DECAFParser#varDecla.
    def exitVarDecla(self, ctx:DECAFParser.VarDeclaContext):
        pass


    # Enter a parse tree produced by DECAFParser#methodDecla.
    def enterMethodDecla(self, ctx:DECAFParser.MethodDeclaContext):
        pass

    # Exit a parse tree produced by DECAFParser#methodDecla.
    def exitMethodDecla(self, ctx:DECAFParser.MethodDeclaContext):
        pass


    # Enter a parse tree produced by DECAFParser#normal.
    def enterNormal(self, ctx:DECAFParser.NormalContext):
        pass

    # Exit a parse tree produced by DECAFParser#normal.
    def exitNormal(self, ctx:DECAFParser.NormalContext):
        pass


    # Enter a parse tree produced by DECAFParser#lista.
    def enterLista(self, ctx:DECAFParser.ListaContext):
        pass

    # Exit a parse tree produced by DECAFParser#lista.
    def exitLista(self, ctx:DECAFParser.ListaContext):
        pass


    # Enter a parse tree produced by DECAFParser#structDeclaration.
    def enterStructDeclaration(self, ctx:DECAFParser.StructDeclarationContext):
        pass

    # Exit a parse tree produced by DECAFParser#structDeclaration.
    def exitStructDeclaration(self, ctx:DECAFParser.StructDeclarationContext):
        pass


    # Enter a parse tree produced by DECAFParser#varType.
    def enterVarType(self, ctx:DECAFParser.VarTypeContext):
        pass

    # Exit a parse tree produced by DECAFParser#varType.
    def exitVarType(self, ctx:DECAFParser.VarTypeContext):
        pass


    # Enter a parse tree produced by DECAFParser#metoInt.
    def enterMetoInt(self, ctx:DECAFParser.MetoIntContext):
        pass

    # Exit a parse tree produced by DECAFParser#metoInt.
    def exitMetoInt(self, ctx:DECAFParser.MetoIntContext):
        pass


    # Enter a parse tree produced by DECAFParser#metoIntWithParam.
    def enterMetoIntWithParam(self, ctx:DECAFParser.MetoIntWithParamContext):
        pass

    # Exit a parse tree produced by DECAFParser#metoIntWithParam.
    def exitMetoIntWithParam(self, ctx:DECAFParser.MetoIntWithParamContext):
        pass


    # Enter a parse tree produced by DECAFParser#metoChar.
    def enterMetoChar(self, ctx:DECAFParser.MetoCharContext):
        pass

    # Exit a parse tree produced by DECAFParser#metoChar.
    def exitMetoChar(self, ctx:DECAFParser.MetoCharContext):
        pass


    # Enter a parse tree produced by DECAFParser#metoCharWithParam.
    def enterMetoCharWithParam(self, ctx:DECAFParser.MetoCharWithParamContext):
        pass

    # Exit a parse tree produced by DECAFParser#metoCharWithParam.
    def exitMetoCharWithParam(self, ctx:DECAFParser.MetoCharWithParamContext):
        pass


    # Enter a parse tree produced by DECAFParser#metoBool.
    def enterMetoBool(self, ctx:DECAFParser.MetoBoolContext):
        pass

    # Exit a parse tree produced by DECAFParser#metoBool.
    def exitMetoBool(self, ctx:DECAFParser.MetoBoolContext):
        pass


    # Enter a parse tree produced by DECAFParser#metoBoolWithParam.
    def enterMetoBoolWithParam(self, ctx:DECAFParser.MetoBoolWithParamContext):
        pass

    # Exit a parse tree produced by DECAFParser#metoBoolWithParam.
    def exitMetoBoolWithParam(self, ctx:DECAFParser.MetoBoolWithParamContext):
        pass


    # Enter a parse tree produced by DECAFParser#metoVoid.
    def enterMetoVoid(self, ctx:DECAFParser.MetoVoidContext):
        pass

    # Exit a parse tree produced by DECAFParser#metoVoid.
    def exitMetoVoid(self, ctx:DECAFParser.MetoVoidContext):
        pass


    # Enter a parse tree produced by DECAFParser#metoVoidWithParam.
    def enterMetoVoidWithParam(self, ctx:DECAFParser.MetoVoidWithParamContext):
        pass

    # Exit a parse tree produced by DECAFParser#metoVoidWithParam.
    def exitMetoVoidWithParam(self, ctx:DECAFParser.MetoVoidWithParamContext):
        pass


    # Enter a parse tree produced by DECAFParser#single_parameterDeclaration.
    def enterSingle_parameterDeclaration(self, ctx:DECAFParser.Single_parameterDeclarationContext):
        pass

    # Exit a parse tree produced by DECAFParser#single_parameterDeclaration.
    def exitSingle_parameterDeclaration(self, ctx:DECAFParser.Single_parameterDeclarationContext):
        pass


    # Enter a parse tree produced by DECAFParser#int_parameterType.
    def enterInt_parameterType(self, ctx:DECAFParser.Int_parameterTypeContext):
        pass

    # Exit a parse tree produced by DECAFParser#int_parameterType.
    def exitInt_parameterType(self, ctx:DECAFParser.Int_parameterTypeContext):
        pass


    # Enter a parse tree produced by DECAFParser#char_parameterType.
    def enterChar_parameterType(self, ctx:DECAFParser.Char_parameterTypeContext):
        pass

    # Exit a parse tree produced by DECAFParser#char_parameterType.
    def exitChar_parameterType(self, ctx:DECAFParser.Char_parameterTypeContext):
        pass


    # Enter a parse tree produced by DECAFParser#boolean_parameterType.
    def enterBoolean_parameterType(self, ctx:DECAFParser.Boolean_parameterTypeContext):
        pass

    # Exit a parse tree produced by DECAFParser#boolean_parameterType.
    def exitBoolean_parameterType(self, ctx:DECAFParser.Boolean_parameterTypeContext):
        pass


    # Enter a parse tree produced by DECAFParser#block.
    def enterBlock(self, ctx:DECAFParser.BlockContext):
        pass

    # Exit a parse tree produced by DECAFParser#block.
    def exitBlock(self, ctx:DECAFParser.BlockContext):
        pass


    # Enter a parse tree produced by DECAFParser#ifSt_statement.
    def enterIfSt_statement(self, ctx:DECAFParser.IfSt_statementContext):
        pass

    # Exit a parse tree produced by DECAFParser#ifSt_statement.
    def exitIfSt_statement(self, ctx:DECAFParser.IfSt_statementContext):
        pass


    # Enter a parse tree produced by DECAFParser#while_statement.
    def enterWhile_statement(self, ctx:DECAFParser.While_statementContext):
        pass

    # Exit a parse tree produced by DECAFParser#while_statement.
    def exitWhile_statement(self, ctx:DECAFParser.While_statementContext):
        pass


    # Enter a parse tree produced by DECAFParser#return_statement.
    def enterReturn_statement(self, ctx:DECAFParser.Return_statementContext):
        pass

    # Exit a parse tree produced by DECAFParser#return_statement.
    def exitReturn_statement(self, ctx:DECAFParser.Return_statementContext):
        pass


    # Enter a parse tree produced by DECAFParser#method_call_statement.
    def enterMethod_call_statement(self, ctx:DECAFParser.Method_call_statementContext):
        pass

    # Exit a parse tree produced by DECAFParser#method_call_statement.
    def exitMethod_call_statement(self, ctx:DECAFParser.Method_call_statementContext):
        pass


    # Enter a parse tree produced by DECAFParser#block_statement.
    def enterBlock_statement(self, ctx:DECAFParser.Block_statementContext):
        pass

    # Exit a parse tree produced by DECAFParser#block_statement.
    def exitBlock_statement(self, ctx:DECAFParser.Block_statementContext):
        pass


    # Enter a parse tree produced by DECAFParser#asign_statement.
    def enterAsign_statement(self, ctx:DECAFParser.Asign_statementContext):
        pass

    # Exit a parse tree produced by DECAFParser#asign_statement.
    def exitAsign_statement(self, ctx:DECAFParser.Asign_statementContext):
        pass


    # Enter a parse tree produced by DECAFParser#char_asign_statement.
    def enterChar_asign_statement(self, ctx:DECAFParser.Char_asign_statementContext):
        pass

    # Exit a parse tree produced by DECAFParser#char_asign_statement.
    def exitChar_asign_statement(self, ctx:DECAFParser.Char_asign_statementContext):
        pass


    # Enter a parse tree produced by DECAFParser#unknown_statement.
    def enterUnknown_statement(self, ctx:DECAFParser.Unknown_statementContext):
        pass

    # Exit a parse tree produced by DECAFParser#unknown_statement.
    def exitUnknown_statement(self, ctx:DECAFParser.Unknown_statementContext):
        pass


    # Enter a parse tree produced by DECAFParser#ifStmt.
    def enterIfStmt(self, ctx:DECAFParser.IfStmtContext):
        pass

    # Exit a parse tree produced by DECAFParser#ifStmt.
    def exitIfStmt(self, ctx:DECAFParser.IfStmtContext):
        pass


    # Enter a parse tree produced by DECAFParser#elseStmt.
    def enterElseStmt(self, ctx:DECAFParser.ElseStmtContext):
        pass

    # Exit a parse tree produced by DECAFParser#elseStmt.
    def exitElseStmt(self, ctx:DECAFParser.ElseStmtContext):
        pass


    # Enter a parse tree produced by DECAFParser#whileStmt.
    def enterWhileStmt(self, ctx:DECAFParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by DECAFParser#whileStmt.
    def exitWhileStmt(self, ctx:DECAFParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by DECAFParser#returnStmt.
    def enterReturnStmt(self, ctx:DECAFParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by DECAFParser#returnStmt.
    def exitReturnStmt(self, ctx:DECAFParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by DECAFParser#location.
    def enterLocation(self, ctx:DECAFParser.LocationContext):
        pass

    # Exit a parse tree produced by DECAFParser#location.
    def exitLocation(self, ctx:DECAFParser.LocationContext):
        pass


    # Enter a parse tree produced by DECAFParser#cond_op_expr.
    def enterCond_op_expr(self, ctx:DECAFParser.Cond_op_exprContext):
        pass

    # Exit a parse tree produced by DECAFParser#cond_op_expr.
    def exitCond_op_expr(self, ctx:DECAFParser.Cond_op_exprContext):
        pass


    # Enter a parse tree produced by DECAFParser#boolliteral_expr.
    def enterBoolliteral_expr(self, ctx:DECAFParser.Boolliteral_exprContext):
        pass

    # Exit a parse tree produced by DECAFParser#boolliteral_expr.
    def exitBoolliteral_expr(self, ctx:DECAFParser.Boolliteral_exprContext):
        pass


    # Enter a parse tree produced by DECAFParser#loca_expr.
    def enterLoca_expr(self, ctx:DECAFParser.Loca_exprContext):
        pass

    # Exit a parse tree produced by DECAFParser#loca_expr.
    def exitLoca_expr(self, ctx:DECAFParser.Loca_exprContext):
        pass


    # Enter a parse tree produced by DECAFParser#num_expr.
    def enterNum_expr(self, ctx:DECAFParser.Num_exprContext):
        pass

    # Exit a parse tree produced by DECAFParser#num_expr.
    def exitNum_expr(self, ctx:DECAFParser.Num_exprContext):
        pass


    # Enter a parse tree produced by DECAFParser#arith_op_expr.
    def enterArith_op_expr(self, ctx:DECAFParser.Arith_op_exprContext):
        pass

    # Exit a parse tree produced by DECAFParser#arith_op_expr.
    def exitArith_op_expr(self, ctx:DECAFParser.Arith_op_exprContext):
        pass


    # Enter a parse tree produced by DECAFParser#parentesisexpr_expr.
    def enterParentesisexpr_expr(self, ctx:DECAFParser.Parentesisexpr_exprContext):
        pass

    # Exit a parse tree produced by DECAFParser#parentesisexpr_expr.
    def exitParentesisexpr_expr(self, ctx:DECAFParser.Parentesisexpr_exprContext):
        pass


    # Enter a parse tree produced by DECAFParser#rel_op_expr.
    def enterRel_op_expr(self, ctx:DECAFParser.Rel_op_exprContext):
        pass

    # Exit a parse tree produced by DECAFParser#rel_op_expr.
    def exitRel_op_expr(self, ctx:DECAFParser.Rel_op_exprContext):
        pass


    # Enter a parse tree produced by DECAFParser#methodCall_expr.
    def enterMethodCall_expr(self, ctx:DECAFParser.MethodCall_exprContext):
        pass

    # Exit a parse tree produced by DECAFParser#methodCall_expr.
    def exitMethodCall_expr(self, ctx:DECAFParser.MethodCall_exprContext):
        pass


    # Enter a parse tree produced by DECAFParser#charliteral_expr.
    def enterCharliteral_expr(self, ctx:DECAFParser.Charliteral_exprContext):
        pass

    # Exit a parse tree produced by DECAFParser#charliteral_expr.
    def exitCharliteral_expr(self, ctx:DECAFParser.Charliteral_exprContext):
        pass


    # Enter a parse tree produced by DECAFParser#arith_higher_expr.
    def enterArith_higher_expr(self, ctx:DECAFParser.Arith_higher_exprContext):
        pass

    # Exit a parse tree produced by DECAFParser#arith_higher_expr.
    def exitArith_higher_expr(self, ctx:DECAFParser.Arith_higher_exprContext):
        pass


    # Enter a parse tree produced by DECAFParser#negativo_expr.
    def enterNegativo_expr(self, ctx:DECAFParser.Negativo_exprContext):
        pass

    # Exit a parse tree produced by DECAFParser#negativo_expr.
    def exitNegativo_expr(self, ctx:DECAFParser.Negativo_exprContext):
        pass


    # Enter a parse tree produced by DECAFParser#eq_op_expr.
    def enterEq_op_expr(self, ctx:DECAFParser.Eq_op_exprContext):
        pass

    # Exit a parse tree produced by DECAFParser#eq_op_expr.
    def exitEq_op_expr(self, ctx:DECAFParser.Eq_op_exprContext):
        pass


    # Enter a parse tree produced by DECAFParser#negacion_expr.
    def enterNegacion_expr(self, ctx:DECAFParser.Negacion_exprContext):
        pass

    # Exit a parse tree produced by DECAFParser#negacion_expr.
    def exitNegacion_expr(self, ctx:DECAFParser.Negacion_exprContext):
        pass


    # Enter a parse tree produced by DECAFParser#methodCall.
    def enterMethodCall(self, ctx:DECAFParser.MethodCallContext):
        pass

    # Exit a parse tree produced by DECAFParser#methodCall.
    def exitMethodCall(self, ctx:DECAFParser.MethodCallContext):
        pass


    # Enter a parse tree produced by DECAFParser#arg.
    def enterArg(self, ctx:DECAFParser.ArgContext):
        pass

    # Exit a parse tree produced by DECAFParser#arg.
    def exitArg(self, ctx:DECAFParser.ArgContext):
        pass


    # Enter a parse tree produced by DECAFParser#arith_higher_op.
    def enterArith_higher_op(self, ctx:DECAFParser.Arith_higher_opContext):
        pass

    # Exit a parse tree produced by DECAFParser#arith_higher_op.
    def exitArith_higher_op(self, ctx:DECAFParser.Arith_higher_opContext):
        pass


    # Enter a parse tree produced by DECAFParser#arith_op.
    def enterArith_op(self, ctx:DECAFParser.Arith_opContext):
        pass

    # Exit a parse tree produced by DECAFParser#arith_op.
    def exitArith_op(self, ctx:DECAFParser.Arith_opContext):
        pass


    # Enter a parse tree produced by DECAFParser#rel_op.
    def enterRel_op(self, ctx:DECAFParser.Rel_opContext):
        pass

    # Exit a parse tree produced by DECAFParser#rel_op.
    def exitRel_op(self, ctx:DECAFParser.Rel_opContext):
        pass


    # Enter a parse tree produced by DECAFParser#eq_op.
    def enterEq_op(self, ctx:DECAFParser.Eq_opContext):
        pass

    # Exit a parse tree produced by DECAFParser#eq_op.
    def exitEq_op(self, ctx:DECAFParser.Eq_opContext):
        pass


    # Enter a parse tree produced by DECAFParser#cond_op.
    def enterCond_op(self, ctx:DECAFParser.Cond_opContext):
        pass

    # Exit a parse tree produced by DECAFParser#cond_op.
    def exitCond_op(self, ctx:DECAFParser.Cond_opContext):
        pass


    # Enter a parse tree produced by DECAFParser#bool_literal.
    def enterBool_literal(self, ctx:DECAFParser.Bool_literalContext):
        pass

    # Exit a parse tree produced by DECAFParser#bool_literal.
    def exitBool_literal(self, ctx:DECAFParser.Bool_literalContext):
        pass


