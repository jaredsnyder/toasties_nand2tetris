//function Sys.init 0

(Sys.init)
//	push constant 4

@4
D=A
@0
A=M
M=D
@0
M=M+1
//	call Main.fibonacci 1

@RETURN_ADDRESS_1
D=A
@0
A=M
M=D
@0
M=M+1
@1
D=M
@0
A=M
M=D
@0
M=M+1
@2
D=M
@0
A=M
M=D
@0
M=M+1
@3
D=M
@0
A=M
M=D
@0
M=M+1
@4
D=M
@0
A=M
M=D
@0
M=M+1
@0
D=M
@2
M=D
@2
M=M-1
M=M-1
M=M-1
M=M-1
M=M-1
M=M-1
@0
D=M
@1
M=D
@Main.fibonacci
0;JMP
(RETURN_ADDRESS_1)
//label END  

(END)
//	goto END  // loops infinitely

@END
0;JMP
//function Main.fibonacci 0

(Main.fibonacci)
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
//	push constant 2

@2
D=A
@0
A=M
M=D
@0
M=M+1
//	lt                     

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
@IS_LESS_THAN_0
D;JLT
@0
M=M-1
A=M
M=0
@LTEND_0
0;JMP
(IS_LESS_THAN_0)
@0
M=M-1
A=M
M=-1
(LTEND_0)
//	if-goto N_LT_2        

@0
M=M-1
A=M
D=M
@N_LT_2
D;JNE
//	goto N_GE_2

@N_GE_2
0;JMP
//label N_LT_2               // if n < 2 returns n

(N_LT_2)
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
A=D
D=M
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
0;JMP
//label N_GE_2               // if n >= 2 returns fib(n - 2) + fib(n - 1)

(N_GE_2)
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
//	push constant 2

@2
D=A
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
//	call Main.fibonacci 1  // computes fib(n - 2)

@RETURN_ADDRESS_2
D=A
@0
A=M
M=D
@0
M=M+1
@1
D=M
@0
A=M
M=D
@0
M=M+1
@2
D=M
@0
A=M
M=D
@0
M=M+1
@3
D=M
@0
A=M
M=D
@0
M=M+1
@4
D=M
@0
A=M
M=D
@0
M=M+1
@0
D=M
@2
M=D
@2
M=M-1
M=M-1
M=M-1
M=M-1
M=M-1
M=M-1
@0
D=M
@1
M=D
@Main.fibonacci
0;JMP
(RETURN_ADDRESS_2)
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
//	push constant 1

@1
D=A
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
//	call Main.fibonacci 1  // computes fib(n - 1)

@RETURN_ADDRESS_3
D=A
@0
A=M
M=D
@0
M=M+1
@1
D=M
@0
A=M
M=D
@0
M=M+1
@2
D=M
@0
A=M
M=D
@0
M=M+1
@3
D=M
@0
A=M
M=D
@0
M=M+1
@4
D=M
@0
A=M
M=D
@0
M=M+1
@0
D=M
@2
M=D
@2
M=M-1
M=M-1
M=M-1
M=M-1
M=M-1
M=M-1
@0
D=M
@1
M=D
@Main.fibonacci
0;JMP
(RETURN_ADDRESS_3)
//	add                    // returns fib(n - 1) + fib(n - 2)

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
A=D
D=M
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
0;JMP
