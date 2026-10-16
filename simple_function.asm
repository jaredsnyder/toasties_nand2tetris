//function SimpleFunction.test 2

(SimpleFunction.test)
@0
D=A
@0
A=M
M=D
@0
M=M+1
@0
D=A
@0
A=M
M=D
@0
M=M+1
//	push local 0

@1
D=M
@0
A=D+A
D=M
@0
A=M
M=D
@0
M=M+1
//	push local 1

@1
D=M
@1
A=D+A
D=M
@0
A=M
M=D
@0
M=M+1
//	add

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
//	not

@0
M=M-1
A=M
D=M
D=!D
M=D
@0
M=M+1
//	push argument 0

@2
D=M
@0
A=D+A
D=M
@0
A=M
M=D
@0
M=M+1
//	add

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
//	push argument 1

@2
D=M
@1
A=D+A
D=M
@0
A=M
M=D
@0
M=M+1
//	sub

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
//	return
@1
D=M
@0
D=D+A
@13
M=D
@13
D=M
D=D-1
D=D-1
D=D-1
D=D-1
D=D-1
@14
M=D
@2
D=M
@0
D=D+A
@15
M=D
@0
M=M-1
A=M
D=M
@15
A=M
M=D
D=A
@0
M=D+1
@13
D=M
D=D-1
A=D
D=M
@4
M=D
@13
D=M
D=D-1
D=D-1
A=D
D=M
@3
M=D
@13
D=M
D=D-1
D=D-1
D=D-1
A=D
D=M
@2
M=D
@13
D=M
D=D-1
D=D-1
D=D-1
D=D-1
A=D
D=M
@1
M=D
@14
A=M
