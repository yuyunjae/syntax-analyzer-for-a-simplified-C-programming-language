import nltk
from nltk import Tree

# parsing_table { (current_state, symbol) : (action, value) ... (..:..) ... }
# shift example: (current_state, terminal): ('shift', post_state)
# reduce example: (current_state, terminal): ('reduce', grammar_number)
# goto example: (current_state, non_terminal): ('shift', goto_state)
parsing_table = {
    (0, 'vtype'): ('shift', 4),
    (0, '$'): ('reduce', 3),
    (0, 'CODE'): ('goto', 1),
    (0, 'VDECL'): ('goto', 2),
    (0, 'FDECL'): ('goto', 3),
    (1, '$'): ('accept', -1),
    (2, 'vtype'): ('shift', 4),
    (2, '$'): ('reduce', 3),
    (2, 'CODE'): ('goto', 5),
    (2, 'VDECL'): ('goto', 2),
    (2, 'FDECL'): ('goto', 3),
    (3, 'vtype'): ('shift', 4),
    (3, '$'): ('reduce', 3),
    (3, 'CODE'): ('goto', 6),
    (3, 'VDECL'): ('goto', 2),
    (3, 'FDECL'): ('goto', 3),
    (4, 'id'): ('shift', 7),
    (4, 'ASSIGN'): ('goto', 8),
    (5, '$'): ('reduce', 1),
    (6, '$'): ('reduce', 2),
    (7, 'semi'): ('shift', 9),
    (7, 'assign'): ('shift', 11),
    (7, 'lparen'): ('shift', 10),
    (8, 'semi'): ('shift', 12),
    (9, 'vtype'): ('reduce', 4),
    (9, 'id'): ('reduce', 4),
    (9, 'rbrace'): ('reduce', 4),
    (9, 'if'): ('reduce', 4),
    (9, 'while'): ('reduce', 4),
    (9, 'return'): ('reduce', 4),
    (9, '$'): ('reduce', 4),
    (10, 'vtype'): ('shift', 14),
    (10, 'rparen'): ('reduce', 20),
    (10, 'ARG'): ('goto', 13),
    (11, 'id'): ('shift', 23),
    (11, 'literal'): ('shift', 17),
    (11, 'character'): ('shift', 18),
    (11, 'boolstr'): ('shift', 19),
    (11, 'lparen'): ('shift', 22),
    (11, 'num'): ('shift', 24),
    (11, 'RHS'): ('goto', 15),
    (11, 'EXPR'): ('goto', 16),
    (11, 'TEXPR'): ('goto', 20),
    (11, 'FEXPR'): ('goto', 21),
    (12, 'vtype'): ('reduce', 5),
    (12, 'id'): ('reduce', 5),
    (12, 'rbrace'): ('reduce', 5),
    (12, 'if'): ('reduce', 5),
    (12, 'while'): ('reduce', 5),
    (12, 'return'): ('reduce', 5),
    (12, '$'): ('reduce', 5),
    (13, 'rparen'): ('shift', 25),
    (14, 'id'): ('shift', 26),
    (15, 'semi'): ('reduce', 6),
    (16, 'semi'): ('reduce', 7),
    (17, 'semi'): ('reduce', 8),
    (18, 'semi'): ('reduce', 9),
    (19, 'semi'): ('reduce', 10),
    (20, 'semi'): ('reduce', 12),
    (20, 'addsub'): ('shift', 27),
    (20, 'rparen'): ('reduce', 12),
    (21, 'semi'): ('reduce', 14),
    (21, 'addsub'): ('reduce', 14),
    (21, 'multdiv'): ('shift', 28),
    (21, 'rparen'): ('reduce', 14),
    (22, 'id'): ('shift', 23),
    (22, 'lparen'): ('shift', 22),
    (22, 'num'): ('shift', 24),
    (22, 'EXPR'): ('goto', 29),
    (22, 'TEXPR'): ('goto', 20),
    (22, 'FEXPR'): ('goto', 21),
    (23, 'semi'): ('reduce', 16),
    (23, 'addsub'): ('reduce', 16),
    (23, 'multdiv'): ('reduce', 16),
    (23, 'rparen'): ('reduce', 16),
    (24, 'semi'): ('reduce', 17),
    (24, 'addsub'): ('reduce', 17),
    (24, 'multdiv'): ('reduce', 17),
    (24, 'rparen'): ('reduce', 17),
    (25, 'lbrace'): ('shift', 30),
    (26, 'rparen'): ('reduce', 22),
    (26, 'comma'): ('shift', 32),
    (26, 'MOREARGS'): ('goto', 31),
    (27, 'id'): ('shift', 23),
    (27, 'lparen'): ('shift', 22),
    (27, 'num'): ('shift', 24),
    (27, 'EXPR'): ('goto', 33),
    (27, 'TEXPR'): ('goto', 20),
    (27, 'FEXPR'): ('goto', 21),
    (28, 'id'): ('shift', 23),
    (28, 'lparen'): ('shift', 22),
    (28, 'num'): ('shift', 24),
    (28, 'TEXPR'): ('goto', 34),
    (28, 'FEXPR'): ('goto', 21),
    (29, 'rparen'): ('shift', 35),
    (30, 'vtype'): ('shift', 42),
    (30, 'id'): ('shift', 43),
    (30, 'rbrace'): ('reduce', 24),
    (30, 'if'): ('shift', 40),
    (30, 'while'): ('shift', 41),
    (30, 'return'): ('reduce', 24),
    (30, 'VDECL'): ('goto', 38),
    (30, 'ASSIGN'): ('goto', 39),
    (30, 'BLOCK'): ('goto', 36),
    (30, 'STMT'): ('goto', 37),
    (31, 'rparen'): ('reduce', 19),
    (32, 'vtype'): ('shift', 44),
    (33, 'semi'): ('reduce', 11),
    (33, 'rparen'): ('reduce', 11),
    (34, 'semi'): ('reduce', 13),
    (34, 'addsub'): ('reduce', 13),
    (34, 'rparen'): ('reduce', 13),
    (35, 'semi'): ('reduce', 15),
    (35, 'addsub'): ('reduce', 15),
    (35, 'multdiv'): ('reduce', 15),
    (35, 'rparen'): ('reduce', 15),
    (36, 'return'): ('shift', 46),
    (36, 'RETURN'): ('goto', 45),
    (37, 'vtype'): ('shift', 42),
    (37, 'id'): ('shift', 43),
    (37, 'rbrace'): ('reduce', 24),
    (37, 'if'): ('shift', 40),
    (37, 'while'): ('shift', 41),
    (37, 'return'): ('reduce', 24),
    (37, 'VDECL'): ('goto', 38),
    (37, 'ASSIGN'): ('goto', 39),
    (37, 'BLOCK'): ('goto', 47),
    (37, 'STMT'): ('goto', 37),
    (38, 'vtype'): ('reduce', 25),
    (38, 'id'): ('reduce', 25),
    (38, 'rbrace'): ('reduce', 25),
    (38, 'if'): ('reduce', 25),
    (38, 'while'): ('reduce', 25),
    (38, 'return'): ('reduce', 25),
    (39, 'semi'): ('shift', 48),
    (40, 'lparen'): ('shift', 49),
    (41, 'lparen'): ('shift', 50),
    (42, 'id'): ('shift', 51),
    (42, 'ASSIGN'): ('goto', 8),
    (43, 'assign'): ('shift', 11),
    (44, 'id'): ('shift', 52),
    (45, 'rbrace'): ('shift', 53),
    (46, 'id'): ('shift', 23),
    (46, 'literal'): ('shift', 17),
    (46, 'character'): ('shift', 18),
    (46, 'boolstr'): ('shift', 19),
    (46, 'lparen'): ('shift', 22),
    (46, 'num'): ('shift', 24),
    (46, 'RHS'): ('goto', 54),
    (46, 'EXPR'): ('goto', 16),
    (46, 'TEXPR'): ('goto', 20),
    (46, 'FEXPR'): ('goto', 21),
    (47, 'rbrace'): ('reduce', 23),
    (47, 'return'): ('reduce', 23),
    (48, 'vtype'): ('reduce', 26),
    (48, 'id'): ('reduce', 26),
    (48, 'rbrace'): ('reduce', 26),
    (48, 'if'): ('reduce', 26),
    (48, 'while'): ('reduce', 26),
    (48, 'return'): ('reduce', 26),
    (49, 'boolstr'): ('shift', 57),
    (49, 'COND'): ('goto', 55),
    (49, 'TCOND'): ('goto', 56),
    (50, 'boolstr'): ('shift', 57),
    (50, 'COND'): ('goto', 58),
    (50, 'TCOND'): ('goto', 56),
    (51, 'semi'): ('shift', 9),
    (51, 'assign'): ('shift', 11),
    (52, 'rparen'): ('reduce', 22),
    (52, 'comma'): ('shift', 32),
    (52, 'MOREARGS'): ('goto', 59),
    (53, 'vtype'): ('reduce', 18),
    (53, '$'): ('reduce', 18),
    (54, 'semi'): ('shift', 60),
    (55, 'rparen'): ('shift', 61),
    (56, 'rparen'): ('reduce', 30),
    (56, 'comp'): ('shift', 62),
    (57, 'rparen'): ('reduce', 31),
    (57, 'comp'): ('reduce', 31),
    (58, 'rparen'): ('shift', 63),
    (59, 'rparen'): ('reduce', 21),
    (60, 'rbrace'): ('reduce', 34),
    (61, 'lbrace'): ('shift', 64),
    (62, 'boolstr'): ('shift', 57),
    (62, 'COND'): ('goto', 65),
    (62, 'TCOND'): ('goto', 56),
    (63, 'lbrace'): ('shift', 66),
    (64, 'vtype'): ('shift', 42),
    (64, 'id'): ('shift', 43),
    (64, 'rbrace'): ('reduce', 24),
    (64, 'if'): ('shift', 40),
    (64, 'while'): ('shift', 41),
    (64, 'return'): ('reduce', 24),
    (64, 'VDECL'): ('goto', 38),
    (64, 'ASSIGN'): ('goto', 39),
    (64, 'BLOCK'): ('goto', 67),
    (64, 'STMT'): ('goto', 37),
    (65, 'rparen'): ('reduce', 29),
    (66, 'vtype'): ('shift', 42),
    (66, 'id'): ('shift', 43),
    (66, 'rbrace'): ('reduce', 24),
    (66, 'if'): ('shift', 40),
    (66, 'while'): ('shift', 41),
    (66, 'return'): ('reduce', 24),
    (66, 'VDECL'): ('goto', 38),
    (66, 'ASSIGN'): ('goto', 39),
    (66, 'BLOCK'): ('goto', 68),
    (66, 'STMT'): ('goto', 37),
    (67, 'rbrace'): ('shift', 69),
    (68, 'rbrace'): ('shift', 70),
    (69, 'vtype'): ('reduce', 33),
    (69, 'id'): ('reduce', 33),
    (69, 'rbrace'): ('reduce', 33),
    (69, 'if'): ('reduce', 33),
    (69, 'while'): ('reduce', 33),
    (69, 'else'): ('shift', 72),
    (69, 'return'): ('reduce', 33),
    (69, 'ELSE'): ('goto', 71),
    (70, 'vtype'): ('reduce', 28),
    (70, 'id'): ('reduce', 28),
    (70, 'rbrace'): ('reduce', 28),
    (70, 'if'): ('reduce', 28),
    (70, 'while'): ('reduce', 28),
    (70, 'return'): ('reduce', 28),
    (71, 'vtype'): ('reduce', 27),
    (71, 'id'): ('reduce', 27),
    (71, 'rbrace'): ('reduce', 27),
    (71, 'if'): ('reduce', 27),
    (71, 'while'): ('reduce', 27),
    (71, 'return'): ('reduce', 27),
    (72, 'lbrace'): ('shift', 73),
    (73, 'vtype'): ('shift', 42),
    (73, 'id'): ('shift', 43),
    (73, 'rbrace'): ('reduce', 24),
    (73, 'if'): ('shift', 40),
    (73, 'while'): ('shift', 41),
    (73, 'return'): ('reduce', 24),
    (73, 'VDECL'): ('goto', 38),
    (73, 'ASSIGN'): ('goto', 39),
    (73, 'BLOCK'): ('goto', 74),
    (73, 'STMT'): ('goto', 37),
    (74, 'rbrace'): ('shift', 75),
    (75, 'vtype'): ('reduce', 32),
    (75, 'id'): ('reduce', 32),
    (75, 'rbrace'): ('reduce', 32),
    (75, 'if'): ('reduce', 32),
    (75, 'while'): ('reduce', 32),
    (75, 'return'): ('reduce', 32),
}


context_free_grammar = [
  [["START"], ["CODE"]],
  [["CODE"], ["VDECL", "CODE"]],
  [["CODE"], ["FDECL", "CODE"]],
  [["CODE"], [""]],
  [["VDECL"], ["vtype", "id", "semi"]],
  [["VDECL"], ["vtype", "ASSIGN", "semi"]],
  [["ASSIGN"], ["id", "assign", "RHS"]],
  [["RHS"], ["EXPR"]],
  [["RHS"], ["literal"]],
  [["RHS"], ["character"]],
  [["RHS"], ["boolstr"]],
  [["EXPR"], ["TEXPR", "addsub", "EXPR"]],
  [["EXPR"], ["TEXPR"]],
  [["TEXPR"], ["FEXPR", "multdiv", "TEXPR"]],
  [["TEXPR"], ["FEXPR"]],
  [["FEXPR"], ["lparen", "EXPR", "rparen"]],
  [["FEXPR"], ["id"]],
  [["FEXPR"], ["num"]],
  [["FDECL"], ["vtype", "id", "lparen", "ARG", "rparen", "lbrace", "BLOCK", "RETURN", "rbrace"]],
  [["ARG"], ["vtype", "id", "MOREARGS"]],
  [["ARG"], [""]],
  [["MOREARGS"], ["comma", "vtype", "id", "MOREARGS"]],
  [["MOREARGS"], [""]],
  [["BLOCK"], ["STMT", "BLOCK"]],
  [["BLOCK"], [""]],
  [["STMT"], ["VDECL"]],
  [["STMT"], ["ASSIGN", "semi"]],
  [["STMT"], ["if", "lparen", "COND", "rparen", "lbrace", "BLOCK", "rbrace", "ELSE"]],
  [["STMT"], ["while", "lparen", "COND", "rparen", "lbrace", "BLOCK", "rbrace"]],
  [["COND"], ["TCOND", "comp", "COND"]],
  [["COND"], ["TCOND"]],
  [["TCOND"], ["boolstr"]],
  [["ELSE"], ["else", "lbrace", "BLOCK", "rbrace"]],
  [["ELSE"], [""]],
  [["RETURN"], ["return", "RHS", "semi"]]
]


isAccepted = False

def slrParser(tokens):
  numOfStep = 0
  parseTreeStack=[]
  stateStack = []
  stateStack.append(0) #initStateStack 초기 state는 0임
  index = 0
  nextSymbol = tokens[index] # 초기 symbol은 맨 첫번째 토큰임
  while(True):
    numOfStep += 1
    currentState = stateStack[len(stateStack)-1] #stateStack의 top
    

    
    if (currentState, nextSymbol) not in parsing_table: #만약, 해당하는 slr 테이블 칸에 값이 없다면, 에러 발생
      print("step",numOfStep,"[Parsing Error] : value is not exist in state:",currentState,", action:",nextSymbol)
      break
    action, value = parsing_table[currentState, nextSymbol]
    
    print("---------step",numOfStep,"-------")
    print("{current state:",currentState, "next symbol:",nextSymbol,"}")
    print("{",action , " : " , value, " }")
    print("parseTreeStack",parseTreeStack)
    #print("stateStack", stateStack)
    print("")
    if action == "shift":
      parseTreeStack.append([nextSymbol]) # shift를 하면 새로운 terminal이 들어옴 -> 즉 leaf 노드임
      index +=1
      nextSymbol = tokens[index]
      stateStack.append(value)
    elif action == "reduce":
      sizeOfalpha = len(context_free_grammar[value][1]) # A -> alpha alpha의 길이
      
      if context_free_grammar[value][1][0] != '':
        tmp = [] #임시 스택
        
        for i in range(len(parseTreeStack)-sizeOfalpha, len(parseTreeStack)):
          tmp.append(parseTreeStack[i])
        tmp.append(context_free_grammar[value][0][0])
        
        for i in range(0, sizeOfalpha):
          parseTreeStack.pop()
          stateStack.pop() #alpha의 길이만큼 stateStack을 pop시켜야 함
        parseTreeStack.append(tmp) #새로운 트리를 parseTree에 추가시킴
      else: #alpha가 엡실론인 경우
        tmp = [context_free_grammar[value][0][0]]
        parseTreeStack.append(tmp)
        
      #goto(pop이후 stateStack.top, A)를 stateStack에 push , 이때 A는 A -> alpha에서의 A임
      
      top = stateStack[len(stateStack)-1]
      A = context_free_grammar[value][0][0]
      #print(top, A)
      goto, gotoState = parsing_table[top,A]
      #print("gotoState:",gotoState)
      stateStack.append(gotoState)
      
      
      
    else: #accept 되었을 때
      print('accept !')
      return parseTreeStack


def createParseTree(parseTreeStack):
  parseTree = '('
  parseTree += parseTreeStack[len(parseTreeStack)-1]
  if len(parseTreeStack)>=2:
    for i in range(0,len(parseTreeStack)-1):
      parseTree += createParseTree(parseTreeStack[i])
  parseTree += ')'
  return parseTree


#error case
#tokens = "vtype id assign character semi vtype id lparen vtype id comma vtype id comma vtype id rparen lbrace if lparen boolstr comp boolstr rparen lbrace while lparen boolstr rparen lbrace id assign literal semi rbrace rbrace else lbrace vtype id semi rbrace return character semi $"

#accept case
tokens = "vtype id assign character semi vtype id lparen vtype id comma vtype id comma vtype id rparen lbrace if lparen boolstr comp boolstr rparen lbrace while lparen boolstr rparen lbrace id assign literal semi rbrace rbrace else lbrace vtype id semi rbrace return character semi rbrace $"
#tokens = 'vtype id semi $'
splitedToken = tokens.split(" ") #띄어쓰기로 token 구분하기

parseTreeStack = slrParser(splitedToken)[0]

print(parseTreeStack)
print(len(parseTreeStack))
print(parseTreeStack[0][len(parseTreeStack[0])-1])

parseTreeString = createParseTree(parseTreeStack)
tree = Tree.fromstring(parseTreeString)
tree.draw()


