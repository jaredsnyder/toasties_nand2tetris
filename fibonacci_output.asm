//	push argument 1         // sets THAT, the base address of the

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
//	pop pointer 1           // that segment, to argument[1]

@4
D=0
D=D+A
@10000
M=D
@0
M=M-1
A=M
D=M
@10000
A=M
M=D
//	push constant 0         // sets the series' first and second

@0
D=A
@0
A=M
M=D
@0
M=M+1
//	pop that 0              // elements to 0 and 1, respectively       

@4
D=M
@0
D=D+A
@10000
M=D
@0
M=M-1
A=M
D=M
@10000
A=M
M=D
//	push constant 1   

@1
D=A
@0
A=M
M=D
@0
M=M+1
//	pop that 1              

@4
D=M
@1
D=D+A
@10000
M=D
@0
M=M-1
A=M
D=M
@10000
A=M
M=D
//	push argument 0         // sets n, the number of remaining elements

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
//	push constant 2         // to be computed, to argument[0] minus 2,

@2
D=A
@0
A=M
M=D
@0
M=M+1
//	sub                     // since 2 elements were already computed.

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
//	pop argument 0          

@2
D=M
@0
D=D+A
@10000
M=D
@0
M=M-1
A=M
D=M
@10000
A=M
M=D
//label LOOP

(LOOP)
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
//	if-goto COMPUTE_ELEMENT // if n > 0, goto COMPUTE_ELEMENT

@0
M=M-1
A=M
D=M
@COMPUTE_ELEMENT
D;JNE
//	goto END                // otherwise, goto END

@END
0;JMP
//label COMPUTE_ELEMENT

(COMPUTE_ELEMENT)
//	push that 0

@4
D=M
@0
A=D+A
D=M
@0
A=M
M=D
@0
M=M+1
//	push that 1

@4
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
//	pop that 2

@4
D=M
@2
D=D+A
@10000
M=D
@0
M=M-1
A=M
D=M
@10000
A=M
M=D
//	push pointer 1

@4
D=0
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
//	pop pointer 1 

@4
D=0
D=D+A
@10000
M=D
@0
M=M-1
A=M
D=M
@10000
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
//	pop argument 0          

@2
D=M
@0
D=D+A
@10000
M=D
@0
M=M-1
A=M
D=M
@10000
A=M
M=D
//	goto LOOP

@LOOP
0;JMP
//label END

(END)
