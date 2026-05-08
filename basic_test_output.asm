//push constant 10

@10
D=A
@0
A=M
M=D
@0
M=M+1
//pop local 0

@0
M=M-1
A=M
D=M
@300
M=D
//push constant 21

@21
D=A
@0
A=M
M=D
@0
M=M+1
//push constant 22

@22
D=A
@0
A=M
M=D
@0
M=M+1
//pop argument 2

@0
M=M-1
A=M
D=M
@402
M=D
//pop argument 1

@0
M=M-1
A=M
D=M
@401
M=D
//push constant 36

@36
D=A
@0
A=M
M=D
@0
M=M+1
//pop this 6

@0
M=M-1
A=M
D=M
@3006
M=D
//push constant 42

@42
D=A
@0
A=M
M=D
@0
M=M+1
//push constant 45

@45
D=A
@0
A=M
M=D
@0
M=M+1
//pop that 5

@0
M=M-1
A=M
D=M
@3015
M=D
//pop that 2

@0
M=M-1
A=M
D=M
@3012
M=D
//push constant 510

@510
D=A
@0
A=M
M=D
@0
M=M+1
//pop temp 6

@0
M=M-1
A=M
D=M
@11
M=D
//push local 0

@300
D=M
@0
A=M
M=D
@0
M=M+1
//push that 5

@3015
D=M
@0
A=M
M=D
@0
M=M+1
//add

@0
M=M-1
A=M
D=M
@0
M=M-1
A=M
D=D+M
M=D
@0
M=M+1
//push argument 1

@401
D=M
@0
A=M
M=D
@0
M=M+1
//sub

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
//push this 6

@3006
D=M
@0
A=M
M=D
@0
M=M+1
//push this 6

@3006
D=M
@0
A=M
M=D
@0
M=M+1
//add

@0
M=M-1
A=M
D=M
@0
M=M-1
A=M
D=D+M
M=D
@0
M=M+1
//sub

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
//push temp 6

@11
D=M
@0
A=M
M=D
@0
M=M+1
//add

@0
M=M-1
A=M
D=M
@0
M=M-1
A=M
D=D+M
M=D
@0
M=M+1
