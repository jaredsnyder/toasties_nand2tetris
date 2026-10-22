//function Sys.init 0

(Sys.init)
//	push constant 4000	// tests that THIS and THAT are handled correctly

@4000
D=A
@0
A=M
M=D
@0
M=M+1
//	pop pointer 0

@3
D=0
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
//	push constant 5000

@5000
D=A
@0
A=M
M=D
@0
M=M+1
//	pop pointer 1

@4
D=0
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
//	call Sys.main 0

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
@0
D=M
@1
M=D
@Sys.main
0;JMP
(RETURN_ADDRESS_1)
//	pop temp 1

@5
D=M
@1
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
//	label LOOP

(LOOP)
//	goto LOOP

@LOOP
0;JMP
//function Sys.main 5

(Sys.main)
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
@0
D=A
@0
A=M
M=D
@0
M=M+1
//	push constant 4001

@4001
D=A
@0
A=M
M=D
@0
M=M+1
//	pop pointer 0

@3
D=0
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
//	push constant 5001

@5001
D=A
@0
A=M
M=D
@0
M=M+1
//	pop pointer 1

@4
D=0
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
//	push constant 200

@200
D=A
@0
A=M
M=D
@0
M=M+1
//	pop local 1

@1
D=M
@1
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
//	push constant 40

@40
D=A
@0
A=M
M=D
@0
M=M+1
//	pop local 2

@1
D=M
@2
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
//	push constant 6

@6
D=A
@0
A=M
M=D
@0
M=M+1
//	pop local 3

@1
D=M
@3
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
//	push constant 123

@123
D=A
@0
A=M
M=D
@0
M=M+1
//	call Sys.add12 1

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
@Sys.add12
0;JMP
(RETURN_ADDRESS_2)
//	pop temp 0

@5
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
//	push local 2

@1
D=M
@2
A=D+A
D=M
@0
A=M
M=D
@0
M=M+1
//	push local 3

@1
D=M
@3
A=D+A
D=M
@0
A=M
M=D
@0
M=M+1
//	push local 4

@1
D=M
@4
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
//function Sys.add12 0

(Sys.add12)
//	push constant 4002

@4002
D=A
@0
A=M
M=D
@0
M=M+1
//	pop pointer 0

@3
D=0
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
//	push constant 5002

@5002
D=A
@0
A=M
M=D
@0
M=M+1
//	pop pointer 1

@4
D=0
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
//	push constant 12

@12
D=A
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
