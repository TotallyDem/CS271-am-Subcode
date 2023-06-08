import sys

def generate_machine_code(line: str) -> str:
    # Generates machine code based on instruction
    nexttokendest = 16 # In case we need to add a new token
    if line[0] == "(": # skip loop components
        output = ""
    # A instructions
    elif line[0] == "@":
        line = line[1:] # Stripping out @ symbol
        try : # Checking if we are directly accessing memory with number or a token
            intline = int(line)
            if (intline < 0) or (intline > 32767):
                raise Exception("Out of range error")
            else:
                output = '{0:016b}'.format(intline)
        except ValueError:
            try:
                output = '{0:016b}'.format(tokendict[line])
            except:
                tokendict[line] = nexttokendest
                output = '{0:016b}'.format(nexttokendest)
                nexttokendest += 1
    # Everything else should be C instructions
    else:
        jump = "000"
        dest = "000"
        current = line
        if "=" in current:
            splitline = line.split("=")
            splitline[0] = ''.join(sorted(splitline[0]))
            dest = destdict[splitline[0]]
            current = splitline[1]
        if ";" in current:
            splitline = line.split(";")
            comp = compdict[splitline[0]]
            jump = jumpdict[splitline[1]]
        else:
            comp = compdict[current]
        output = "111" + comp + dest + jump
    return output

def init_loop_locations(parsedlines):
    codeline = 0
    for line in parsedlines:
        if line[0] == "(":
            #parse jump coordinates
            line = line[1:-1]
            try:
                int(line)
                raise Exception("Invalid jump name: \""+line+"\"")
            except ValueError:
                if line in tokendict:
                    raise Exception("Token already used: \""+line+"\"")
                else:
                    tokendict[line] = codeline
        else:
            codeline += 1

def init_jump_lookup_dict() -> dict:
    # build jump lookup dictionary as a jump type (as a string) as the key and its dest bits (as a string) as value
    jump_lookup = {}
    jump_lookup["null"] = "000"
    jump_lookup["JGT"]  = "001"
    jump_lookup["JEQ"]  = "010"
    jump_lookup["JGE"]  = "011"
    jump_lookup["JLT"]  = "100"
    jump_lookup["JNE"]  = "101"
    jump_lookup["JLE"]  = "110"
    jump_lookup["JMP"]  = "111"

    return jump_lookup

def init_dest_lookup_dict() -> dict:
    # build dest lookup dictionary as a dest register (as a string) as the key and its dest bits (as a string) as value
    dest_lookup = {}
    dest_lookup["null"] = "000"
    dest_lookup["M"]    = "001"
    dest_lookup["D"]    = "010"
    dest_lookup["DM"]   = "011"
    dest_lookup["A"]    = "100"
    dest_lookup["AM"]   = "101"
    dest_lookup["AD"]   = "110"
    dest_lookup["ADM"]  = "111"

    return dest_lookup

def init_comp_lookup_dict() -> dict:
    # build comp lookup dictionary as a comp instruction (as a string) as the key and its control bits (as a string) as value
    comp_lookup = {}
    comp_lookup["0"]   = "0101010"
    comp_lookup["1"]   = "0111111"
    comp_lookup["-1"]  = "0111010"
    comp_lookup["D"]   = "0001100"
    comp_lookup["A"]   = "0110000"
    comp_lookup["!D"]  = "0001101"
    comp_lookup["!A"]  = "0110001"
    comp_lookup["-D"]  = "0001111"
    comp_lookup["-A"]  = "0110011"
    comp_lookup["D+1"] = "0011111"
    comp_lookup["A+1"] = "0110111"
    comp_lookup["D-1"] = "0001110"
    comp_lookup["A-1"] = "0110010"
    comp_lookup["D+A"] = "0000010"
    comp_lookup["D-A"] = "0010011"
    comp_lookup["A-D"] = "0000111"
    comp_lookup["D&A"] = "0000000"
    comp_lookup["D|A"] = "0010101"
    comp_lookup["M"]   = "1110000"
    comp_lookup["!M"]  = "1110001"
    comp_lookup["-M"]  = "1110011"
    comp_lookup["M+1"] = "1110111"
    comp_lookup["M-1"] = "1110010"
    comp_lookup["D+M"] = "1000010"
    comp_lookup["D-M"] = "1010011"
    comp_lookup["M-D"] = "1000111"
    comp_lookup["D&M"] = "1000000"
    comp_lookup["D|M"] = "1010101"

    return comp_lookup

def init_token_lookup_dict() -> dict:
    token_lookup = {}
    token_lookup["R0"] = 0
    token_lookup["R1"] = 1
    token_lookup["R2"] = 2
    token_lookup["R3"] = 3
    token_lookup["R4"] = 4
    token_lookup["R5"] = 5
    token_lookup["R6"] = 6
    token_lookup["R7"] = 7
    token_lookup["R8"] = 8
    token_lookup["R9"] = 9
    token_lookup["R10"] = 10
    token_lookup["R11"] = 11
    token_lookup["R12"] = 12
    token_lookup["R13"] = 13
    token_lookup["R14"] = 14
    token_lookup["R15"] = 15
    token_lookup["SCREEN"] = 16384
    token_lookup["KBD"] = 24576
    token_lookup["SP"] = 0
    token_lookup["LCL"] = 1
    token_lookup["ARG"] = 2
    token_lookup["THIS"] = 3
    token_lookup["THAT"] = 4
    token_lookup["LOOP"] = 4
    token_lookup["STOP"] = 18
    token_lookup["i"] = 16
    token_lookup["sum"] = 17

    return token_lookup

def parse(input_line: str) -> str:
    # strip white space
    output_line = input_line.strip()

    # double forward slash detector with split
    output_line =  output_line.split("//")[0].strip()

    return output_line

def main():
    # open file, read into a list
    input_filename = sys.argv[1]
    input_file_contents = []
    with open(input_filename, "r") as input_file:
        input_file_contents = input_file.readlines()

    # call parser on each line
    parsed_lines = []
    for line in input_file_contents:
        parsed_line = parse(line)
        if parsed_line != "":
            parsed_lines.append(parsed_line)

    # generate machine code
    # create generate machine code function, which will use the lookup dictionaries to create machine code binary values
    global jumpdict ; jumpdict = init_jump_lookup_dict()
    global destdict ; destdict = init_dest_lookup_dict()
    global compdict ; compdict = init_comp_lookup_dict()
    global tokendict ; tokendict = init_token_lookup_dict()
    outputcode = ""
    
    init_loop_locations(parsed_lines)
    for line in parsed_lines:
        # Checking for A instructions
        output = generate_machine_code(line)
        if output != "":
            outputcode += output + "\n"
    outputfile = open("output.hack", "w")
    outputfile.write(outputcode)
    outputfile.close()


                


if __name__ == "__main__":
    main()
    print("Parsing completed, have a nice day.")