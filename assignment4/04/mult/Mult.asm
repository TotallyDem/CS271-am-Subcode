// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.

(START)
	// Initialize product to 0.
	@R2
	M=0
(LOOP)
	@R1
	D=M
	@END
	D;JLE // If R1 <= 0 stop
	@R0
	D=M
	@R2
	M=M+D // Add R0 to R2
	@R1
	M=M-1 // R1 -= 1
	// Loop
	@LOOP
	0;JMP
(END)
	// stop
	@END
	0;JMP