grammar DECAF;

/*------------------------------------------------------------------
 * LEXER RULES 
 *------------------------------------------------------------------*/
 
id	:	 Letter (Letter|Digit)*    		;

num	:	Digit (Digit)*			;

Digit
	:	[0-9]	;
Letter
	:	[a-zA-Z]	;

COMMENTS: '//' ~('\r' | '\n' )*  -> channel(HIDDEN);

/*------------------------------------------------------------------
 * PARSER RULES
 *------------------------------------------------------------------*/
 
program:	'class'  id '{' (declaration)* '}'		;
  
declaration
	:	 structDeclaration | varDeclaration | methodDeclaration 	;
	
varDeclaration 
	:	varType id ';' | varType id '[' num ']' ';' ;

structDeclaration 
	:	'struct' id '{' (varDeclaration)* '}' ';';

varType
	:	'int'| 'char' | 'boolean' | 'struct' id | structDeclaration | 'void';
	
methodDeclaration
	:	methodType id '(' (((var_type var_id) | 'void') (',' var_type var_id)*)? ')' block;

methodType
	:	'int' | 'char' | 'boolean' | 'void';

parameter
	:	parameterType id | parameterType id '['  ']';

parameterType
	:	'int' | 'char' | 'boolean' | 'void';
	
block	:	'{'  (varDeclaration)*  (statement)* '}';	

var_type
	:	'int' | 'boolean' | 'struct' id | structDeclaration;

var_id  
	:	id ('.' location)?;

statement
	: 	'if' '(' expression ')' block ('else' block)?
		| 'while' '(' expression ')' block
		| 'return' (expression)? ';'
		| methodCall ';'
		| block
		| location '=' expression ';'
		| (expression)? ';'
	;

location 
	:	id ('.' location)? | id '[' expression ']' ('.' location)?    ;

expression 
	:	location
		| methodCall
		| literal
		| expression op expression
		| '-' expression
		| '!' expression
		| '(' expression ')'
	;
	
methodCall
	:	id '(' (arg (',' arg)*)? ')'	;

arg	:	expression;
	
op	:	arith_op
		| rel_op
		| eq_op
		| cond_op
	;

arith_op
	:	'+'
		| '-'
		| '*'
		| '/'
		| '%'
	;

rel_op
	:	'<'
		| '>'
		| '<='
		| '>='
	;

eq_op
	:	'=='
		| '!='
	;

cond_op
	:	'&&'
		| '||'
	;

literal	:	int_literal | char_literal | bool_literal ;

int_literal
	:	num;
	
char_literal
	:	'\'' Letter '\'' 	;
	
bool_literal
	:	'true' | 'false';

SPACE
    :	[ \t\r\n\u000C]+ -> skip	;