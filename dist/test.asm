LOAD 'AAA'
STORE C
LOAD MYDATA
STORE B
LOAD 0004
STORE D
LOOP1:
PRINT C
LOAD C
STORE [B]
INC C
INC B
DEC D
JNZ LOOP1
STORE [001A]
HALT
MYDATA: