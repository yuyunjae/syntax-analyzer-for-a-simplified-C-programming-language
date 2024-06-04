# syntax-analyzer-for-a-simplified-C-programming-language
<br>
<h1>nltk 라이브러리 설치방법</h1><br>
pip install numpy<br>
pip install nltk<br>
<h1>프로그램 실행방법</h1><br>
파이썬이 설치되어 있다면, <br>
terminal에서 python syntax_analyzer.py [테스트 하고자 하는 파일 ex) accept_case_1.txt]<br>
위와 같은 명령어로 parsing 결과를 확인 할 수 있습니다.
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
