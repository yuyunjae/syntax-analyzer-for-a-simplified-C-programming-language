# 문법 dictionary 생성
from bs4 import BeautifulSoup

# HTML 파일을 읽어옵니다. # html파일 경로
with open(r"./parsetable.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# BeautifulSoup을 사용하여 HTML을 파싱합니다.
soup = BeautifulSoup(html_content, 'html.parser')

# id가 lrTableView인 div 태그를 찾습니다.
lr_table_view_div = soup.find('div', id='lrTableView')

if lr_table_view_div:
    # div 태그 내의 모든 th와 td 태그를 찾습니다.
    th_tags = lr_table_view_div.find_all('th')
    td_tags = lr_table_view_div.find_all('td')

    # th 태그의 텍스트를 출력합니다.
    symbol = []
    table = []

    check_symbol = False
    for th in th_tags:
        print(f"TH Tag: {th.text.strip()}")
        if (check_symbol):
            symbol.append(th.text.strip())
        if (th.text.strip() == "GOTO"):
            check_symbol = True

    # td 태그의 텍스트를 출력합니다.

    for i, td in enumerate(td_tags):
        print(f"TD Tag: {td.text.strip()}")
        command = td.text.strip()
        if i % (len(symbol) + 1) == 0:
            table.append([])
        elif command == "":
            table[-1].append(command)
        elif command.isdigit():
            table[-1].append(int(command))
        elif command[0] == 's':
            table[-1].append(('shift', int(command[1:])))
        elif command[0] == 'r':
            table[-1].append(('reduce', int(command[1:])))
        elif command == "acc":
            table[-1].append(('accept', -1))

    print(symbol)
    print(table)
    print("\n\n")

    # (state, symbol) : (action, value)
    # arsing_table = {
    # (0, "vtype") : ("shift", 4)
    # }
    print("parsing_table = {")

    for i, table_row in enumerate(table):
        for j, table_val in enumerate(table_row):
            if table_val:
                print(f"    ({i}, '{symbol[j]}'): ", end='')
                if str(type(table_val)) == "<class 'tuple'>":
                    print(table_val, end=",\n")
                elif str(type(table_val)) == "<class 'int'>":
                    print(f"('goto', {table_val})", end=",\n")

    print("}", end='')

else:
    print("Div with id 'lrTableView' not found")
