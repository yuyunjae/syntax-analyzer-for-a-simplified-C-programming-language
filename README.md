# syntax-analyzer-for-a-simplified-C-programming-language
<br>
nltk 라이브러리 설치방법<br>
pip install numpy<br>
pip install nltk<br>
<br>
<h1>CFG </h1>
<br>
<br>START -> CODE
<br>CODE -> VDECL CODE
<br>CODE -> FDECL CODE
<br>CODE -> ''
<br>VDECL -> vtype id semi
<br>VDECL -> vtype ASSIGN semi
<br>ASSIGN -> id assign RHS
<br>RHS -> EXPR
<br>RHS -> literal
<br>RHS -> character
<br>RHS -> boolstr
<br>EXPR -> TEXPR addsub EXPR
<br>EXPR -> TEXPR
<br>TEXPR -> FEXPR multdiv TEXPR
<br>TEXPR -> FEXPR
<br>FEXPR -> lparen EXPR rparen
<br>FEXPR -> id
<br>FEXPR -> num
<br>FDECL -> vtype id lparen ARG rparen lbrace BLOCK RETURN rbrace
<br>ARG -> vtype id MOREARGS 
<br>ARG -> ''
<br>MOREARGS -> comma vtype id MOREARGS 
<br>MOREARGS -> ''
<br>BLOCK -> STMT BLOCK 
<br>BLOCK -> ''
<br>STMT -> VDECL 
<br>STMT -> ASSIGN semi
<br>STMT -> if lparen COND rparen lbrace BLOCK rbrace ELSE
<br>STMT -> while lparen COND rparen lbrace BLOCK rbrace
<br>COND -> TCOND comp COND
<br>COND -> TCOND
<br>TCOND -> boolstr
<br>ELSE -> else lbrace BLOCK rbrace
<br>ELSE -> ''
<br>RETURN -> return RHS semi
