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

@3000
D=M
@0
A=M
M=D
@0
M=M+1
//pop local 2

@0
M=M-1
A=M
D=M
@3002
M=D
