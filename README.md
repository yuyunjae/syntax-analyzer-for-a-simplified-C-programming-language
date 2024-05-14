# syntax-analyzer-for-a-simplified-C-programming-language


START -> CODE
CODE -> VDECL CODE
CODE -> FDECL CODE
CODE -> ''
VDECL -> vtype id semi
VDECL -> vtype ASSIGN semi
ASSIGN -> id assign RHS
RHS -> EXPR
RHS -> literal
RHS -> character
RHS -> boolstr
EXPR -> TEXPR addsub EXPR
EXPR -> TEXPR
TEXPR -> FEXPR multdiv TEXPR
TEXPR -> FEXPR
FEXPR -> lparen EXPR rparen
FEXPR -> id
FEXPR -> num
FDECL -> vtype id lparen ARG rparen lbrace BLOCK RETURN rbrace
ARG -> vtype id MOREARGS 
ARG -> ''
MOREARGS -> comma vtype id MOREARGS 
MOREARGS -> ''
BLOCK -> STMT BLOCK 
BLOCK -> ''
STMT -> VDECL 
STMT -> ASSIGN semi
STMT -> if lparen COND rparen lbrace BLOCK rbrace ELSE
STMT -> while lparen COND rparen lbrace BLOCK rbrace
COND -> TCOND comp COND
COND -> TCOND
TCOND -> boolstr
ELSE -> else lbrace BLOCK rbrace
ELSE -> ''
RETURN -> return RHS semi
