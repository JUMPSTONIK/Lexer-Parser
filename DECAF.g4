grammar DECAF;

@lexer::namespace{CustomIde}
@parser::namespace{CustomIde}

program 
	:   'class' Id '{' (declaration)* '}'
	;

declaration 
	:   structDeclaration#structDeclara
	|   varDeclaration#varDecla
	|   methodDeclaration#methodDecla
	;
	 
varDeclaration 
	:vartype=varType Id endline #normal										
	|vartype= varType  Id '[' Num ']' endline #lista
								
	;

structDeclaration
	:   'struct' Id '{' (varDeclaration)*  '}'  
	;



varType
	:   'int'														
	|   'char'														
	|   'boolean'													
	|   'struct' Id												
	|   structDeclaration											
	|   'void'														
	;

methodDeclaration
	:   metoInt = 'int' Id '(void)' block	#metoInt
	|	metoIntWithParam='int' Id '(' (parameter (',' parameter)*)? ')' block #metoIntWithParam
	|	metoChar = 'char' Id '(void)' block	#metoChar
	|   metoCharWithParam='char' Id '(' (parameter (',' parameter)*)? ')' block #metoCharWithParam  
	| 	metoBool = 'bool' Id '(void)' block	#metoBool
	|   metoBoolWithParam='boolean' Id '(' (parameter (',' parameter)*)? ')' block	#metoBoolWithParam
	|   metoVoid = 'void' Id '(void)' block	#metoVoid
	|   metoVoidWithParam = 'void' Id '(' (parameter (',' parameter)*)? ')' block	#metoVoidWithParam
	;

parameter
	:   param = parameterType Id#single_parameterDeclaration
	;

parameterType
	:   'int'#int_parameterType
	|   'char'#char_parameterType
	|   'boolean'#boolean_parameterType
	;

block
	:   '{'(varDeclaration)* (statement)*  closeKey  
	;


statement
   	:   ifStmt#ifSt_statement
	|   whileStmt#while_statement
	|   returnStmt#return_statement
	|   methodCall 	endline #method_call_statement									
	|   block#block_statement														
	|   location '=' expression endline #asign_statement							
	|   location '=' '(char)' expression endline#char_asign_statement						
	|   (expression)? endline#unknown_statement										
	;

ifStmt
	:'if' '(' expression ')' block1 = block (elseStmt)?
	;
elseStmt
	:'else' block_else= block
	;
whileStmt
	:'while' '(' expression ')' block
	;
returnStmt
	:'return' (expression)? endline	
	;
location  
	: Id ('.' location)? #normal_location										
	| Id '[' expression ']' ('.' location)?	#array_location					
	;


expression  //ya
	:   location#loca_expr											
	|   methodCall#methodCall_expr											
	|   Num#num_expr												
	|   CharacterLiteral#charliteral_expr										
	|   bool_literal#boolliteral_expr
	|   derecha = expression arith_higher_op izquierda=expression#arith_higher_expr										
	|   derecha =expression arith_op izquierda=expression#arith_op_expr								
	|   derecha =expression rel_op izquierda=expression#rel_op_expr							
	|   derecha =expression eq_op izquierda=expression#eq_op_expr									
	|   derecha =expression cond_op izquierda=expression#cond_op_expr							
	|   '-' expression#negativo_expr												
	|   '!' expression#negacion_expr											
	|   '(' expression ')'#parentesisexpr_expr											
	;

methodCall
	:	Id '(' (arg (',' arg)*)? ')' //ya
	;

arg
	:   Param = expression //ya
	;

arith_higher_op
    : '*' 
    | '/' 
    | '%' 
    ;

arith_op
	:   '+'
	|   '-'
	;

rel_op
	:   '<'
	|   '>'
	|   '<='
	|   '>='
	;

eq_op
	:   '=='
	|   '!='
	;

cond_op
	:   '&&'
	|   '||'
	;
	
bool_literal //ya
	:   'true'
	|   'false'
	;

Id
	:   Letter (Letter|Digit)*
	;

Num
	:   Digit+
	;

CharacterLiteral
	:   '\'' SingleCharacter '\''
	;

fragment
SingleCharacter
	:   ~['\\]
	;

endline
	: ';'
	;

closeKey
	: '}'
	;

Digit 
	:   [0-9]
	;

Letter
	:   [a-zA-Z]
	;

WS: [ \t\r\n\u000C]+ -> skip;
 
COMMENT
	:   '/*' .*? '*/' -> skip
	;

LINE_COMMENT
	:   '//' ~[\r\n]* -> skip
	;