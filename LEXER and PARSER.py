DL_OP = {'+':'ADD', '-':'SUBTRACT', '(':'PL', ')':'PI', '*':'MUL', '^':'EXPONENT', '&':'AND', '|':'OR', '/':'DIVIDE', '//':'MODULE', ':=':'EQUAL', '=':'ASSIGNMENT', '<':'LESS THAN', '>':'GREATER THAN', '<=':'LESS THAN OR EAQUL', '>=':'LESS THAN OR EAQUL', '!=':'NOT EQUAL', '%':'END OF LINE', ',' : 'vir' , '\t':'TAB'}
RS = {'protostar':'INTEGER TYPE', 'star':'REAL TYPE', 'planet':'WORD TYPE', 'asteroid':'CHARACTER TYPE', 'cluster':'ARRAY TYPE', 'nebula':'CONDITIONAL STATEMENTS', 'ring':'STATES A LOOP'}
letters = ['_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
           'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sym = []
file = open("test - Paria Sarzaeim.txt", "r")
read_file = file.read()
f = read_file.split("\n")
A = ""
B = ""
C = ""
D = ""
pattern = ""
lexeme = ""
token = ( "" , "" )
# col = 0
line = 0
lineLen = 0
next_line = False
state = True
blank = ""
tokens = []



#we seperate - numbers in negative numbers
def seperator(ch):
    for char in ch:
        if char == "-":
            tokens.append("MANFI")
        else:
            tokens.append(char)
            


#lexical analyzer
#splitting with space and tab and add to a list
while line < len(f):
    my_list = f[line].split()
    my_list2 = f[line].split("\t")

    
    if blank in my_list2 :
       x = 0
       try:
           while my_list2[x] == "":
               pattern = "DL_OP"
               lexeme = "\t"
               constant = DL_OP['\t']
               token = (pattern, lexeme, constant)
               tokens.append(str(lexeme))
               print(token)
               x += 1
       except IndexError:
           x = 0

    lineLen = 0
    while lineLen < len(my_list):
        for ch in my_list:

            i = 0
            if state:
                #check if it is a digit
                if ch in digits:
                    pattern = "PROTOSTAR"
                    lexeme = int(ch)
                    token = ( pattern , lexeme )
                    lineLen += 1

                try:
                    float(ch)
                    #check if it is a decimal number
                    if "." in ch:
                        pattern = "STAR"
                        lexeme = float(ch)
                        token = ( pattern , lexeme )
                        print(token)
                        seperator(ch)
                        lineLen += 1
                    else:
                        pattern = "PROTOSTAR"
                        lexeme = int(ch)
                        token = ( pattern , lexeme )
                        print(token)
                        seperator(ch)
                        lineLen += 1
                except ValueError:
                    if ch[0] in letters and ch[0:1] != "|.":
                        C = ""
                        if len(ch) > 1 and ch not in RS and (my_list[my_list.index(ch)-1] != "'" or my_list[my_list.index(ch)+1] != "'") and ch not in sym :
                            C = C + ch
                            pattern = "ID" #identifier
                            lexeme = C
                            token = ( pattern , lexeme )
                            tokens.append(str(lexeme))
                            print(token)
                            sym.append(ch)
                            lineLen += 1
                        elif my_list[my_list.index(ch)-1] == "'" and my_list[my_list.index(ch)+1] == "'" and len(ch) == 1:
                            pattern = "ASTEROID" #character
                            lexeme = ch
                            token = ( pattern , lexeme )
                            tokens.append(lexeme)
                            print(token)
                            lineLen += 1
                        elif len(ch) == 1 and ch not in sym:
                            pattern = "ID"
                            lexeme = ch
                            token = ( pattern , lexeme )
                            tokens.append(lexeme)
                            print(token)
                            sym.append(ch) #add to symbol table
                            lineLen += 1
                        elif ch in RS:
                            pattern = "RS" #reserved word
                            lexeme = ch.upper()
                            constant = RS[ch]
                            token = ( pattern , lexeme , constant )
                            tokens.append(lexeme)
                            print(token)
                            lineLen += 1
                        elif ch in sym:
                            pattern = "ID"
                            lexeme = ch
                            token = ( pattern , lexeme )
                            tokens.append(lexeme)
                            print(token)
                            lineLen += 1
                        else:
                            pattern = "PLANET" #word
                            lexeme = ch
                            token = ( pattern , lexeme )
                            print(token)
                            lineLen += 1
                            
                            
                    
                    elif ch == "'":
                        pattern = "Quetation"
                        lexeme = ch
                        token = ( pattern , lexeme )
                        tokens.append(lexeme)
                        print(token)
                        lineLen += 1
                    elif ch == "|.":
                        state = False
                        A = A + ch
                        pattern = "Comment Start"
                        lexeme = "|."
                        token = ( pattern , lexeme )
                        tokens.append(lexeme)
                        print(token)
                        lineLen += 1
                        if ch != ".|":
                            A = A + ch
                            lineLen += 1
                        break

                    elif ch in DL_OP:
                        pattern = "DL_OP"
                        lexeme = ch
                        constant = DL_OP[ch]
                        token = ( pattern , lexeme , constant )
                        tokens.append(lexeme)
                        print(token)
                        lineLen += 1
                    elif ch == "||":
                        pattern = "Comment"
                        lexeme = "||"
                        token = (pattern , lexeme )
                        tokens.append(lexeme)
                        print(token)
                        break
                    elif ch.startswith("@") or ch.startswith("!"):
                        pattern = "Error"
                        token = ( pattern , ch )
                        tokens.append(lexeme)
                        print(token)
                        lineLen += 1
            elif ch == ".|":
                state = True
                A = A + ch
                pattern = "Comment End"
                lexeme = ".|"
                token = ( pattern, lexeme )
                tokens.append(lexeme)
                print(token)

        break
    line += 1


sharp = ("#")
tokens.append(sharp)       



#parsing table
table = {}
table[("S'", "|.")] = ['#' , 'S']
table[("S'", "||")] = ['#' , 'S']
table[("S'", "ASTEROID")] = ['#' , 'S']
table[("S'", "PLANET")] = ['#' , 'S']
table[("S'", "STAR")] = ['#' , 'S']
table[("S'", "PROTOSTAR")] = ['#' , 'S']
table[ ("S'", "CLUSTER")] = ['#' , 'S']
table[("S'", "RING")] = ['#' , 'S']
table[("S'", "NEBULA")] = ['#' , 'S']
table[("S'", "#")] = ['#' , 'S']

table[("S", "|.")] = ['S' , 'T8']
table[("S", "||")] = ['S' , 'T8']
table[("S", "ASTEROID")] = ['S',  '%',  'T7']
table[("S", "PLANET")] = ["S", "%", "T5"]
table[("S", "STAR")] = ['S' ,'%' ,'T2']
table[("S", "PROTOSTAR")] = ['S' ,'%' ,'T2']
table[("S", "CLUSTER")] = ['S',  '%',  'T6']
table[("S", "RING")] = ['S' , 'T4']
table[("S", "NEBULA")] = ['S' , 'T3']
table[("S", "#")] = ["EPSILON"]
       
table[("T2", "STAR")] = ['Expression', ':=', 'ID', 'STAR']
table[("T2", "PROTOSTAR")] = ['Expression', ':=', 'ID', 'PROTOSTAR']

table[("T3", "NEBULA")] = ['\t', ')', 'CONDITION', '(', 'NEBULA']
table[("T4", "RING")] = ['\t', ')', 'CONDITION', '(', 'RING']

table[("Tab", "|.")] = ["EPSILON"]
table[("Tab", "||")] = ["EPSILON"]
table[("Tab", "ASTEROID")] = ["EPSILON"]
table[("Tab", "PLANET")] = ["EPSILON"]
table[("Tab", "STAR")] = ["EPSILON"]
table[("Tab", "PROTOSTAR")] = ["EPSILON"]
table[ ("Tab", "CLUSTER")] = ["EPSILON"]
table[ ("Tab", "\t")] = ["Tab" , "\t"]
table[("Tab", "RING")] = ["EPSILON"]
table[("Tab", "NEBULA")] = ["EPSILON"]
table[("Tab", "#")] = ["EPSILON"]
       
table[("Expression", "0")] = ['E', 'A']
table[("Expression", "1")] = ['E', 'A']
table[("Expression", "2")] = ['E', 'A']
table[("Expression", "3")] = ['E', 'A']
table[("Expression", "4")] = ['E', 'A']
table[("Expression", "5")] = ['E', 'A']
table[("Expression", "6")] = ['E', 'A']
table[("Expression", "7")] = ['E', 'A']
table[("Expression", "8")] = ['E', 'A']
table[("Expression", "9")] = ['E', 'A']
#table[("Expression", "id")] = ['E', 'A']
table[("Expression", "(")] = ['E', 'A']
table[("Expression", "MANFI")] = ['E', 'A']

table[("E", "|")] = ["EPSILON"]
table[("E", "&")] = ["EPSILON"]
table[("E", ">")] = ["EPSILON"]
table[("E", "<")] = ["EPSILON"]
table[("E", "=")] = ["EPSILON"]
table[("E", "(")] = ["EPSILON"]
table[("E", ")")] = ["EPSILON"]
table[("E", "+")] = ['E', 'A', '+']
table[("E", "-")] = ['E', 'A', '-']
table[("E", ".")] = ['E', 'A', '.']  
table[("E", "%")] = ["EPSILON"]

table[("A", "0")] = ['A1', 'U']
table[("A", "1")] = ['A1', 'U']
table[("A", "2")] = ['A1', 'U']
table[("A", "3")] = ['A1', 'U']
table[("A", "4")] = ['A1', 'U']
table[("A", "5")] = ['A1', 'U']
table[("A", "6")] = ['A1', 'U']
table[("A", "7")] = ['A1', 'U']
table[("A", "8")] = ['A1', 'U']    
table[("A", "9")] = ['A1', 'U']
table[("A", "(")] = ['A1', 'U']
table[("A", "MANFI")] = ['A1', 'U', 'MANFI']

table[("U", "0")] = ['NUMBER', 'D']
table[("U", "1")] = ['NUMBER', 'D']
table[("U", "2")] = ['NUMBER', 'D']
table[("U", "3")] = ['NUMBER', 'D']
table[("U", "4")] = ['NUMBER', 'D']
table[("U", "5")] = ['NUMBER', 'D']
table[("U", "6")] = ['NUMBER', 'D']
table[("U", "7")] = ['NUMBER', 'D']
table[("U", "8")] = ['NUMBER', 'D']
table[("U", "9")] = ['NUMBER', 'D']
table[("U", "(")] = ['NUMBER', 'D']

table[("A1", "|")] = ["EPSILON"] 
table[("A1", "&")] = ["EPSILON"] 
table[("A1", ">")] = ["EPSILON"] 
table[("A1", "<")] = ["EPSILON"]
table[("A1", "=")] = ["EPSILON"] 
table[("A1", ")")] = ["EPSILON"]
table[("A1", "(")] = ["EPSILON"]
table[("A1", "*")] = ['A1', 'D', '*']
table[("A1", "^")] = ['A1', 'D', '^']
table[("A1", "//")] = ['A1', 'D', '//']
table[("A1", "/")] = ['A1', 'D', '/']
table[("A1", "+")] = ["EPSILON"]
table[("A1", "-")] = ["EPSILON"]
table[("A1", ".")] = ["EPSILON"]
table[("A1", "%")] = ["EPSILON"]
table[("A1", "-")] = ["EPSILON"]
table[("A1", "MANFI")] = ["EPSILON"]

table[("D", "0")] = ["0"] 
table[("D", "1")] = ["1"] 
table[("D", "2")] = ["2"] 
table[("D", "3")] = ["3"] 
table[("D", "4")] = ["4"] 
table[("D", "5")] = ["5"] 
table[("D", "6")] = ["6"] 
table[("D", "7")] = ["7"] 
table[("D", "8")] = ["8"]
table[("D", "9")] = ["9"]  
table[("D", "(")] = [')', 'Expression', '(']


table[("CONDITION", "0")] = ['C', 'Expression', 'OPERATOR', 'Expression']
table[("CONDITION", "1")] = ['C', 'Expression', 'OPERATOR', 'Expression']
table[("CONDITION", "2")] = ['C', 'Expression', 'OPERATOR', 'Expression']
table[("CONDITION", "3")] = ['C', 'Expression', 'OPERATOR', 'Expression']
table[("CONDITION", "4")] = ['C', 'Expression', 'OPERATOR', 'Expression']
table[("CONDITION", "5")] = ['C', 'Expression', 'OPERATOR', 'Expression']
table[("CONDITION", "6")] = ['C', 'Expression', 'OPERATOR', 'Expression']
table[("CONDITION", "7")] = ['C', 'Expression', 'OPERATOR', 'Expression']
table[("CONDITION", "8")] = ['C', 'Expression', 'OPERATOR', 'Expression']
table[("CONDITION", "9")] = ['C', 'Expression', 'OPERATOR', 'Expression']  
#table[("CONDITION",  "id")] = ['C', 'Expression', 'OPERATOR', 'Expression']  
table[("CONDITION", '(' )]= ['C', 'Expression', 'OPERATOR', 'Expression']  
table[("CONDITION", "MANFI")] = ['C', 'Expression', 'OPERATOR', 'Expression'] 

table[("OPERATOR", ">")] = [">"] 
table[("OPERATOR", "<")] = ["<"] 
table[("OPERATOR", "=")] = ["="]

table[("C", "|")] = ['CONDITION', '|'] 
table[("C", "&")] = ['CONDITION', '&'] 
table[("C", ")")] = ["EPSILON"]
table[("C", "(")] = [')', 'CONDITION', '(']

table[("T5", "PLANET")] = ["WORD", "PLANET"]

table[("R", ":=")] = ["'", "'" ,":=" ]

table[("T6", "CLUSTER")] = ['K', 'CLUSTER']

table[("K", "PLANET")] = ['L', 'PLANET'] 
table[("K", "STAR")] = ['L', 'STAR'] 
table[("K", "PROTOSTAR")] = ['L', 'PROTOSTAR']


table[("SIZE", ",")] = ['COMMA', ','] 

table[("COMMA", "0")] = ['NUMBER1', 'NUMBER']
table[("COMMA", "1")] = ['NUMBER1', 'NUMBER'] 
table[("COMMA", "2")] = ['NUMBER1', 'NUMBER'] 
table[("COMMA", "3")] = ['NUMBER1', 'NUMBER'] 
table[("COMMA", "4")] = ['NUMBER1', 'NUMBER'] 
table[("COMMA", "5")] = ['NUMBER1', 'NUMBER'] 
table[("COMMA", "6")] = ['NUMBER1', 'NUMBER'] 
table[("COMMA", "7")] = ['NUMBER1', 'NUMBER'] 
table[("COMMA", "8")] = ['NUMBER1', 'NUMBER']
table[("COMMA", "9")] = ['NUMBER1', 'NUMBER'] 
table[("COMMA", ",")] = ['NUMBER', 'DIGIT'] 
table[("COMMA", ",")] = ['NUMBER', 'DIGIT'] 

table[("NUMBER1", ",")] = ['NUMBER', ','] 
table[("NUMBER1", "%")] = ["EPSILON"]
         
table[("DIGIT", "0")] = ["0"]
table[("DIGIT", "1")] = ["1"]
table[("DIGIT", "2")] = ["2"]
table[("DIGIT", "3")] = ["3"]
table[("DIGIT", "4")] = ["4"]
table[("DIGIT", "5")] = ["5"]
table[("DIGIT", "6")] = ["6"]
table[("DIGIT", "7")] = ["7"]
table[("DIGIT", "8")] = ["8"]
table[("DIGIT", "9")] = ["9"]

table[("NUMBER", "0")] = ['NUMBER', 'DIGIT']
table[("NUMBER", "1")] = ['NUMBER', 'DIGIT']
table[("NUMBER", "2")] = ['NUMBER', 'DIGIT']
table[("NUMBER", "3")] = ['NUMBER', 'DIGIT']
table[("NUMBER", "4")] = ['NUMBER', 'DIGIT']
table[("NUMBER", "5")] = ['NUMBER', 'DIGIT']
table[("NUMBER", "6")] = ['NUMBER', 'DIGIT']
table[("NUMBER", "7")] = ['NUMBER', 'DIGIT']
table[("NUMBER", "8")] = ['NUMBER', 'DIGIT']
table[("NUMBER", "9")] = ['NUMBER', 'DIGIT']


table[("NUMBER", ",")] = ["EPSILON"]
table[("NUMBER", "|")] = ["EPSILON"]       
table[("NUMBER", "&")] = ["EPSILON"] 
table[("NUMBER", ">")] = ["EPSILON"] 
table[("NUMBER", "<")] = ["EPSILON"]
table[("NUMBER", "=")] = ["EPSILON"]
table[("NUMBER", ")")] = ["EPSILON"] 
table[("NUMBER", "(")] = ["EPSILON"] 
table[("NUMBER", ".")] = ["EPSILON"]
table[("NUMBER", "*")] = ["EPSILON"]
table[("NUMBER", "^")] = ["EPSILON"]  
table[("NUMBER", "//")] = ["EPSILON"] 
table[("NUMBER", "/")] = ["EPSILON"] 
table[("NUMBER", "+")] = ["EPSILON"]
table[("NUMBER", "-")] = ["EPSILON"] 
table[("NUMBER", "%")] = ["EPSILON"]

table[("T7", "ASTEROID")] = ['CHAR', 'ASTEROID']
 

table[("T8", "|.")] = [".|" ,  "|."]  
table[("T8", "||")] = ["||" ]
                 


index = 0
while index < len(sym):
    for i in sym:
        table[("Expression", i)] = ['E', 'A']
        table[("A",  i)] = ['A1', 'U']
        table[("U",  i)] = ['NUMBER', 'D']
        table[("D",  i)] = ["ID"]
        table[("ID", i)] = [i]
        table[("CONDITION",  i)] = ['C', 'Expression', 'OPERATOR', 'Expression']
        table[("WORD",  i)] = ["R", "ID"]
        table[("L",  i)] = ['SIZE', 'ID']
        table[("CHAR",  i)] = ['R', 'ID'] 
        index += 1
    break
    
print("\n")
print(tokens)
print("\n")
    
    
#parser        
def parser(tokens, table):
    acceptable = True
    temp = 0
    j = 0
    stack=[]
    stack.append("S'")
    while len(stack) > 0 :
        top = stack[len(stack)-1]
        token = tokens[temp]
        if top == token and token != "#":
            stack.pop()
            top = stack[len(stack)-1]
            temp += 1

        elif top == token and top == "#":
            print("YES")
            break
                           
        else:	
            if (top, token) not in table.keys():
                acceptable = False
                break
            elif (top , token) in table:
                states = table[(top, token)]
                stack.pop()
                for char in states:
                    if char != "EPSILON":
                        stack.append(char)
                        top = stack[len(stack)-1]
                    elif char == "EPSILON":
                        j += 1
                

    if not acceptable:
        print("NO")
        print(stack)
        print(token)
        print(top)

        
    
parser(tokens, table)     
    