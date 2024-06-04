from anytree import Node, RenderTree

# 파싱 테이블 (parsing_table) 초기화
parsing_table = {
    # (state, terminal): (action,post state)
    (0, "vtype"): ("SHIFT", 5),
    (2, "vtype"): ("SHIFT", 5),
    (3, "vtype"): ("SHIFT", 5),
    (4, "vtype"): ("SHIFT", 5),
    (13, "vtype"): ("REDUCE", 5),
    (14, "vtype"): ("SHIFT", 19),
    (16, "vtype"): ("REDUCE", 6),
    (17, "vtype"): ("SHIFT", 5),
    (31, "vtype"): ("SHIFT", 5),
    (32, "vtype"): ("SHIFT", 5),
    (38, "vtype"): ("REDUCE", 36),
    (41, "vtype"): ("SHIFT", 53),
    (43, "vtype"): ("SHIFT", 55),
    (48, "vtype"): ("SHIFT", 53),
    (49, "vtype"): ("REDUCE", 26),
    (59, "vtype"): ("REDUCE", 27),
    (64, "vtype"): ("REDUCE", 19),
    (75, "vtype"): ("SHIFT", 53),
    (77, "vtype"): ("SHIFT", 53),
    (80, "vtype"): ("REDUCE", 34),
    (81, "vtype"): ("REDUCE", 29),
    (82, "vtype"): ("REDUCE", 28),
    (84, "vtype"): ("SHIFT", 53),
    (86, "vtype"): ("REDUCE", 33),
    (5, "id"): ("SHIFT", 10),
    (6, "id"): ("SHIFT", 12),
    (13, "id"): ("REDUCE", 5),
    (15, "id"): ("SHIFT", 28),
    (16, "id"): ("REDUCE", 6),
    (19, "id"): ("SHIFT", 34),
    (27, "id"): ("SHIFT", 28),
    (35, "id"): ("SHIFT", 28),
    (36, "id"): ("SHIFT", 28),
    (41, "id"): ("SHIFT", 54),
    (48, "id"): ("SHIFT", 54),
    (49, "id"): ("REDUCE", 26),
    (53, "id"): ("SHIFT", 62),
    (55, "id"): ("SHIFT", 63),
    (57, "id"): ("SHIFT", 28),
    (59, "id"): ("REDUCE", 27),
    (75, "id"): ("SHIFT", 54),
    (77, "id"): ("SHIFT", 54),
    (80, "id"): ("REDUCE", 34),
    (81, "id"): ("REDUCE", 29),
    (82, "id"): ("REDUCE", 28),
    (84, "id"): ("SHIFT", 54),
    (86, "id"): ("REDUCE", 33),
    (10, "semi"): ("SHIFT", 13),
    (11, "semi"): ("SHIFT", 16),
    (20, "semi"): ("REDUCE", 7),
    (21, "semi"): ("REDUCE", 8),
    (22, "semi"): ("REDUCE", 9),
    (23, "semi"): ("REDUCE", 10),
    (24, "semi"): ("REDUCE", 11),
    (25, "semi"): ("REDUCE", 13),
    (26, "semi"): ("REDUCE", 15),
    (28, "semi"): ("REDUCE", 17),
    (29, "semi"): ("REDUCE", 18),
    (44, "semi"): ("REDUCE", 12),
    (45, "semi"): ("REDUCE", 14),
    (46, "semi"): ("REDUCE", 16),
    (50, "semi"): ("SHIFT", 59),
    (62, "semi"): ("SHIFT", 13),
    (65, "semi"): ("SHIFT", 71),
    (10, "assign"): ("SHIFT", 15),
    (54, "assign"): ("SHIFT", 15),
    (62, "assign"): ("SHIFT", 15),
    (15, "literal"): ("SHIFT", 22),
    (57, "literal"): ("SHIFT", 22),
    (15, "character"): ("SHIFT", 23),
    (57, "character"): ("SHIFT", 23),
    (15, "boolstr"): ("SHIFT", 24),
    (57, "boolstr"): ("SHIFT", 24),
    (60, "boolstr"): ("SHIFT", 68),
    (61, "boolstr"): ("SHIFT", 68),
    (73, "boolstr"): ("SHIFT", 68),
    (25, "addsub"): ("SHIFT", 35),
    (26, "addsub"): ("REDUCE", 15),
    (28, "addsub"): ("REDUCE", 17),
    (29, "addsub"): ("REDUCE", 18),
    (45, "addsub"): ("REDUCE", 14),
    (26, "multdiv"): ("SHIFT", 36),
    (28, "multdiv"): ("REDUCE", 17),
    (29, "multdiv"): ("REDUCE", 18),
    (46, "multdiv"): ("REDUCE", 16),
    (10, "lparen"): ("SHIFT", 14),
    (15, "lparen"): ("SHIFT", 27),
    (27, "lparen"): ("SHIFT", 27),
    (35, "lparen"): ("SHIFT", 27),
    (36, "lparen"): ("SHIFT", 27),
    (51, "lparen"): ("SHIFT", 60),
    (52, "lparen"): ("SHIFT", 61),
    (57, "lparen"): ("SHIFT", 27),
    (14, "rparen"): ("REDUCE", 21),
    (18, "rparen"): ("SHIFT", 33),
    (25, "rparen"): ("REDUCE", 13),
    (26, "rparen"): ("REDUCE", 15),
    (28, "rparen"): ("REDUCE", 17),
    (29, "rparen"): ("REDUCE", 18),
    (34, "rparen"): ("REDUCE", 23),
    (37, "rparen"): ("SHIFT", 46),
    (42, "rparen"): ("REDUCE", 20),
    (44, "rparen"): ("REDUCE", 12),
    (45, "rparen"): ("REDUCE", 14),
    (46, "rparen"): ("REDUCE", 16),
    (63, "rparen"): ("REDUCE", 23),
    (66, "rparen"): ("SHIFT", 72),
    (67, "rparen"): ("REDUCE", 31),
    (68, "rparen"): ("REDUCE", 32),
    (69, "rparen"): ("SHIFT", 74),
    (70, "rparen"): ("REDUCE", 22),
    (76, "rparen"): ("REDUCE", 30),
    (15, "num"): ("SHIFT", 29),
    (27, "num"): ("SHIFT", 29),
    (35, "num"): ("SHIFT", 29),
    (36, "num"): ("SHIFT", 29),
    (57, "num"): ("SHIFT", 29),
    (12, "lbrace"): ("SHIFT", 17),
    (33, "lbrace"): ("SHIFT", 41),
    (72, "lbrace"): ("SHIFT", 75),
    (74, "lbrace"): ("SHIFT", 77),
    (83, "lbrace"): ("SHIFT", 84),
    (13, "rbrace"): ("REDUCE", 5),
    (16, "rbrace"): ("REDUCE", 6),
    (17, "rbrace"): ("REDUCE", 39),
    (30, "rbrace"): ("SHIFT", 38),
    (31, "rbrace"): ("REDUCE", 39),
    (32, "rbrace"): ("REDUCE", 39),
    (39, "rbrace"): ("REDUCE", 37),
    (40, "rbrace"): ("REDUCE", 38),
    (41, "rbrace"): ("REDUCE", 25),
    (48, "rbrace"): ("REDUCE", 25),
    (49, "rbrace"): ("REDUCE", 26),
    (56, "rbrace"): ("SHIFT", 64),
    (58, "rbrace"): ("REDUCE", 24),
    (59, "rbrace"): ("REDUCE", 27),
    (64, "rbrace"): ("REDUCE", 19),
    (71, "rbrace"): ("REDUCE", 35),
    (75, "rbrace"): ("REDUCE", 25),
    (77, "rbrace"): ("REDUCE", 25),
    (78, "rbrace"): ("SHIFT", 80),
    (79, "rbrace"): ("SHIFT", 81),
    (80, "rbrace"): ("REDUCE", 34),
    (81, "rbrace"): ("REDUCE", 29),
    (82, "rbrace"): ("REDUCE", 28),
    (84, "rbrace"): ("REDUCE", 25),
    (85, "rbrace"): ("SHIFT", 86),
    (86, "rbrace"): ("REDUCE", 33),
    (34, "comma"): ("SHIFT", 43),
    (63, "comma"): ("SHIFT", 43),
    (13, "if"): ("REDUCE", 5),
    (16, "if"): ("REDUCE", 6),
    (41, "if"): ("SHIFT", 51),
    (48, "if"): ("SHIFT", 51),
    (49, "if"): ("REDUCE", 26),
    (59, "if"): ("REDUCE", 27),
    (75, "if"): ("SHIFT", 51),
    (77, "if"): ("SHIFT", 51),
    (80, "if"): ("REDUCE", 34),
    (81, "if"): ("REDUCE", 29),
    (82, "if"): ("REDUCE", 28),
    (84, "if"): ("SHIFT", 51),
    (86, "if"): ("REDUCE", 33),
    (13, "while"): ("REDUCE", 5),
    (16, "while"): ("REDUCE", 6),
    (41, "while"): ("SHIFT", 52),
    (48, "while"): ("SHIFT", 52),
    (49, "while"): ("REDUCE", 26),
    (59, "while"): ("REDUCE", 27),
    (75, "while"): ("SHIFT", 52),
    (77, "while"): ("SHIFT", 52),
    (80, "while"): ("REDUCE", 34),
    (81, "while"): ("REDUCE", 29),
    (82, "while"): ("REDUCE", 28),
    (84, "while"): ("SHIFT", 52),
    (86, "while"): ("REDUCE", 33),
    (66, "comp"): ("SHIFT", 73),
    (67, "comp"): ("REDUCE", 31),
    (68, "comp"): ("REDUCE", 32),
    (69, "comp"): ("SHIFT", 73),
    (76, "comp"): ("REDUCE", 30),
    (80, "else"): ("SHIFT", 83),
    (13, "return"): ("REDUCE", 5),
    (16, "return"): ("REDUCE", 6),
    (41, "return"): ("REDUCE", 25),
    (47, "return"): ("SHIFT", 57),
    (48, "return"): ("REDUCE", 25),
    (49, "return"): ("REDUCE", 26),
    (58, "return"): ("REDUCE", 24),
    (59, "return"): ("REDUCE", 27),
    (75, "return"): ("REDUCE", 25),
    (77, "return"): ("REDUCE", 25),
    (80, "return"): ("REDUCE", 34),
    (81, "return"): ("REDUCE", 29),
    (82, "return"): ("REDUCE", 28),
    (84, "return"): ("REDUCE", 25),
    (86, "return"): ("REDUCE", 33),
    (0, "class"): ("SHIFT", 6),
    (2, "class"): ("SHIFT", 6),
    (3, "class"): ("SHIFT", 6),
    (4, "class"): ("SHIFT", 6),
    (13, "class"): ("REDUCE", 5),
    (16, "class"): ("REDUCE", 6),
    (38, "class"): ("REDUCE", 36),
    (64, "class"): ("REDUCE", 19),
    (0, "$"): ("REDUCE", 4),
    (1, "$"): ("ACCEPT", None),
    (2, "$"): ("REDUCE", 4),
    (3, "$"): ("REDUCE", 4),
    (4, "$"): ("REDUCE", 4),
    (7, "$"): ("REDUCE", 1),
    (8, "$"): ("REDUCE", 2),
    (9, "$"): ("REDUCE", 3),
    (13, "$"): ("REDUCE", 5),
    (16, "$"): ("REDUCE", 6),
    (38, "$"): ("REDUCE", 36),
    (64, "$"): ("REDUCE", 19),
    # 아래는 goto문 (state, non-terminal) : goto state
    (0, "CODE"): (1),
    (0, "VDECL"): (2),
    (0, "FDECL"): (3),
    (0, "CDECL"): (4),
    (2, "CODE"): (7),
    (2, "VDECL"): (2),
    (2, "FDECL"): (3),
    (2, "CDECL"): (4),
    (3, "CODE"): (8),
    (3, "VDECL"): (2),
    (3, "FDECL"): (3),
    (3, "CDECL"): (4),
    (4, "CODE"): (9),
    (4, "VDECL"): (2),
    (4, "FDECL"): (3),
    (4, "CDECL"): (4),
    (5, "ASSIGN"): (11),
    (14, "ARG"): (18),
    (15, "RHS"): (20),
    (15, "EXPR"): (21),
    (15, "MEXPR"): (25),
    (15, "PEXPR"): (26),
    (17, "VDECL"): (31),
    (17, "FDECL"): (32),
    (17, "ODECL"): (30),
    (27, "EXPR"): (37),
    (27, "MEXPR"): (25),
    (27, "PEXPR"): (26),
    (31, "VDECL"): (31),
    (31, "FDECL"): (32),
    (31, "ODECL"): (39),
    (32, "VDECL"): (31),
    (32, "FDECL"): (32),
    (32, "ODECL"): (40),
    (34, "MOREARGS"): (42),
    (35, "EXPR"): (44),
    (35, "MEXPR"): (25),
    (35, "PEXPR"): (26),
    (36, "MEXPR"): (45),
    (36, "PEXPR"): (26),
    (41, "VDECL"): (49),
    (41, "ASSIGN"): (50),
    (41, "BLOCK"): (47),
    (41, "STMT"): (48),
    (47, "RETURN"): (56),
    (48, "VDECL"): (49),
    (48, "ASSIGN"): (50),
    (48, "BLOCK"): (58),
    (48, "STMT"): (48),
    (53, "ASSIGN"): (11),
    (57, "RHS"): (65),
    (57, "EXPR"): (21),
    (57, "MEXPR"): (25),
    (57, "PEXPR"): (26),
    (60, "COND"): (66),
    (60, "LCOND"): (67),
    (61, "COND"): (69),
    (61, "LCOND"): (67),
    (63, "MOREARGS"): (70),
    (73, "LCOND"): (76),
    (75, "VDECL"): (49),
    (75, "ASSIGN"): (50),
    (75, "BLOCK"): (78),
    (75, "STMT"): (48),
    (77, "VDECL"): (49),
    (77, "ASSIGN"): (50),
    (77, "BLOCK"): (79),
    (77, "STMT"): (48),
    (80, "ELSE"): (82),
    (84, "VDECL"): (49),
    (84, "ASSIGN"): (50),
    (84, "BLOCK"): (85),
    (84, "STMT"): (48),
}


# 문법 규칙 (grammar_rules) 초기화
grammar_rules = {
    0: ["START", "CODE"],
    1: ["CODE", "VDECL CODE"],
    2: ["CODE", "FDECL CODE"],
    3: ["CODE", "CDECL CODE"],
    4: ["CODE", ""],
    5: ["VDECL", "vtype id semi"],
    6: ["VDECL", "vtype ASSIGN semi"],
    7: ["ASSIGN", "id assign RHS"],
    8: ["RHS", "EXPR"],
    9: ["RHS", "literal"],
    10: ["RHS", "character"],
    11: ["RHS", "boolstr"],
    12: ["EXPR", "MEXPR addsub EXPR"],
    13: ["EXPR", "MEXPR"],
    14: ["MEXPR", "PEXPR multdiv MEXPR"],
    15: ["MEXPR", "PEXPR"],
    16: ["PEXPR", "lparen EXPR rparen"],
    17: ["PEXPR", "id"],
    18: ["PEXPR", "num"],
    19: ["FDECL", "vtype id lparen ARG rparen lbrace BLOCK RETURN rbrace"],
    20: ["ARG", "vtype id MOREARGS"],
    21: ["ARG", ""],
    22: ["MOREARGS", "comma vtype id MOREARGS"],
    23: ["MOREARGS", ""],
    24: ["BLOCK", "STMT BLOCK"],
    25: ["BLOCK", ""],
    26: ["STMT", "DECL"],
    27: ["STMT", "ASSIGN semi"],
    28: ["STMT", "if lparen COND rparen lbrace BLOCK rbrace ELSE"],
    29: ["STMT", "while lparen COND rparen lbrace BLOCK rbrace"],
    30: ["COND", "COND comp LCOND"],
    31: ["COND", "LCOND"],
    32: ["LCOND", "boolstr"],
    33: ["ELSE", "else lbrace BLOCK rbrace"],
    34: ["ELSE", ""],
    35: ["RETURN", "return RHS semi"],
    36: ["CDECL", "class id lbrace ODECL rbrace"],
    37: ["ODECL", "VDECL ODECL"],
    38: ["ODECL", "FDECL ODECL"],
    39: ["ODECL", ""],
}

root = []  # 트리의 루트 부분만 존재


def parse_input(input_tokens):
    stack = [0]  # 스택 초기화
    output = []  # 출력 스택 초기화

    while True:
        state = stack[-1]  # 스택의 최상위 상태 가져오기
        if input_tokens != []:  # 입력이 비었을 때 오류 방지
            token = input_tokens[0]  # 입력 토큰의 첫 번째 요소 가져오기

        # print(state, "#", token)
        action = parsing_table.get((state, token))  # 파싱 테이블에서 동작 가져오기

        if action is None:
            # 파싱 오류 처리
            print(stack)
            print(
                "Parsing error: Unexpected token '{}' at position {}".format(
                    token, state
                )
            )
            return False, None
        print(action)
        action_type, action_value = action
        # print(action_type, "##", action_value, "##", token)
        # print(stack)

        if action_type == "SHIFT":
            # SHIFT 동작 수행
            stack.append(token)  # 스택에 토큰 추가
            stack.append(action_value)  # 스택에 다음 상태 추가
            input_tokens = input_tokens[1:]  # 입력 토큰에서 처리한 토큰 제거
            root.append(Node(token))

        elif action_type == "REDUCE":
            # REDUCE 동작 수행
            reduce_rule = grammar_rules[action_value]  # 규칙 가져오기
            lhs, rhs = reduce_rule
            # print(rhs,"&&", lhs)

            reduce_length = 2 * (rhs.count(" "))
            if rhs != "":
                reduce_length += 2  # 공백 수로 단어를 세므로 + 2

            for x in range(reduce_length):
                a = stack.pop()  # 스택에서 규칙에 해당하는 요소들 제거
                # print("POP :",a)

            newNode = Node(lhs)  # 새로운 노드 생성
            index = len(root) - int(reduce_length / 2)
            for x in range(int(reduce_length / 2)):
                node = root.pop(index)  # 삭제하는 노드 수만큼 루트 배열에서 제거(트리에는 남아있음)
                node.parent = newNode  # 새로 생성한 노드가 그것들의 부모가 됨
            root.append(newNode)  # 루트 배열에 부모 추가

            state = stack[-1]  # 스택의 최상위 상태 가져오기
            stack.append(lhs)  # 스택에 LHS(왼쪽 항) 추가

            # print(state, "#goto#", lhs)
            goto = parsing_table.get((state, lhs))  # GOTO 동작 가져오기
            if goto is None:
                # 파싱 오류 처리
                print("Parsing error: Invalid goto")
                return False, None

            print("('GOTO',", goto, ")")

            goto_state = goto  # GOTO 동작에서 다음 상태 가져오기
            stack.append(goto_state)  # 스택에 다음 상태 추가
            output.append(reduce_rule)  # 출력 스택에 규칙 추가

        elif action_type == "ACCEPT":
            # ACCEPT 동작 수행
            break

    return True, output


# 입력 토큰 문자열 입력시 split해서 배열로 넘겨 진행 => 후에 실행 인자로 바꿔야함
input_tokens = "vtype id lparen vtype id comma vtype id comma vtype id rparen lbrace if lparen boolstr comp boolstr comp boolstr comp boolstr rparen lbrace while lparen boolstr comp boolstr comp boolstr rparen lbrace id assign character semi vtype id semi rbrace rbrace return lparen num multdiv num addsub num rparen multdiv num addsub num multdiv lparen num addsub num rparen semi rbrace"
# input_tokens = "vtype id semi"
input_tokens_list = input_tokens.split(" ")
input_tokens_list.append("$")

# 파싱 수행
result, parse_tree = parse_input(input_tokens_list)

if result:
    print("Parsing successful!")
    print("Parse tree:")
    for pre, fill, node in RenderTree(root[0]):
        print("%s%s" % (pre, node.name))
    # TODO: tree 좌우반전 해결, 주석 달기
    # for rule in parse_tree:  # 임시로 parse tree에서 사용한 rule들 출력하게 한 부분
    #     print(rule)
else:
    print("Parsing failed.")
