// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// A = adress
// M = Stored data (at adress)
// D = Memory

//Scren starts at 16384 and ends at 24575	
(BEGIN)
(CHECK_KEYBOARD)
	// Set current to first pixel
	@16384
	D=A
	@current
	M=D
	// If keyboard is pressed set fill
	@KBD
	D=M
	@fillvalue
	M=-1
	@DRAW
	D;JNE
	// Set empty
	@fillvalue
	M=0
(DRAW)
	// Draw based on previous
	@fillvalue
	D=M
	@current
	A=M
	M=D
	// Jump back if finished drawing
	@current
	D=M
	@24575
	D=D-A
	@CHECK_KEYBOARD
	D;JGE
	// Advance pixel
	@current
	M=M+1
	// Continue drawing
	@DRAW
	0;JMP