@17
D=A
@SP
M=M+1
A=M-1
M=D
@17
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
D=D-M
M=-1
@COMMAND3
D;JEQ
@SP
A=M-1
M=0
(COMMAND3)
@17
D=A
@SP
M=M+1
A=M-1
M=D
@16
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
D=D-M
M=-1
@COMMAND6
D;JEQ
@SP
A=M-1
M=0
(COMMAND6)
@16
D=A
@SP
M=M+1
A=M-1
M=D
@17
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
D=D-M
M=-1
@COMMAND9
D;JEQ
@SP
A=M-1
M=0
(COMMAND9)
@892
D=A
@SP
M=M+1
A=M-1
M=D
@891
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
D=D-M
M=-1
@COMMAND12
D;JGT
@SP
A=M-1
M=0
(COMMAND12)
@891
D=A
@SP
M=M+1
A=M-1
M=D
@892
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
D=D-M
M=-1
@COMMAND15
D;JGT
@SP
A=M-1
M=0
(COMMAND15)
@891
D=A
@SP
M=M+1
A=M-1
M=D
@891
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
D=D-M
M=-1
@COMMAND18
D;JGT
@SP
A=M-1
M=0
(COMMAND18)
@32767
D=A
@SP
M=M+1
A=M-1
M=D
@32766
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
D=D-M
M=-1
@COMMAND21
D;JLT
@SP
A=M-1
M=0
(COMMAND21)
@32766
D=A
@SP
M=M+1
A=M-1
M=D
@32767
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
D=D-M
M=-1
@COMMAND24
D;JLT
@SP
A=M-1
M=0
(COMMAND24)
@32766
D=A
@SP
M=M+1
A=M-1
M=D
@32766
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
D=D-M
M=-1
@COMMAND27
D;JLT
@SP
A=M-1
M=0
(COMMAND27)
@57
D=A
@SP
M=M+1
A=M-1
M=D
@31
D=A
@SP
M=M+1
A=M-1
M=D
@53
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
M=D+M
@112
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
M=M-D
@SP
A=M-1
M=-M
@SP
AM=M-1
D=M
A=A-1
M=D&M
@82
D=A
@SP
M=M+1
A=M-1
M=D
@SP
AM=M-1
D=M
A=A-1
M=D|M
@SP
A=M-1
M=!M
(END)
@END
0;JMP
