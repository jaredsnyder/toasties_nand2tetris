//push constant 7

@7
D=A
@0
A=M
M=D
@0
M=M+1
//push constant 8

@8
D=A
@0
A=M
M=D
@0
M=M+1
//push local 0

@2048
D=M
@0
A=M
M=D
@0
M=M+1
//lt

@0
M=M-1
A=M
D=M
@0
M=M-1
A=M
D=M-D
M=D
@0
M=M+1
@IS_LESS_THAN
D;JLT
@0
M=M-1
A=M
M=0
@END
0;JMP
(IS_LESS_THAN)
@0
M=M-1
A=M
M=-1
(END)
