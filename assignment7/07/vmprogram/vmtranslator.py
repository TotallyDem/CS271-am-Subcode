import sys
import assembler

# 5-12 temp var
# 16-255 static var
# 256-2047 SP

#TODO add label [label]
#TODO add goto [label]
#TODO add if-goto [label]

#TODO Function [functionName] [nVars]
#TODO Ca    ll [functionName] [nArgs]

def pointerretur(name) -> str:
    pass

def init_dest_lookup_dict() -> dict:
    # build dest lookup dictionary as a dest register (as a string) as the key and its dest bits (as a string) as value
    dest_lookup = {}
    dest_lookup["local"]    = ""
    dest_lookup["argument"] = ""
    dest_lookup["this"]     = ""
    dest_lookup["that"]     = ""
    dest_lookup["constant"] = "@SP\n"
    dest_lookup["static"]   = ""
    dest_lookup["pointer"]  = ""
    dest_lookup["temp"]     = ""

    return dest_lookup

def parse(input_line: str) -> str:
    # strip white space
    output_line = input_line.strip()

    # double forward slash detector with split
    output_line =  output_line.split("//")[0].strip()

    return output_line

def main():
    # open file, read into a list
    input_filename = sys.argv[1]
    filename = input_filename.split(".")[0]
    input_file_contents = []
    with open(input_filename, "r") as input_file:
        input_file_contents = input_file.readlines()

    # call parser on each line
    parsed_lines = []
    for line in input_file_contents:
        parsed_line = parse(line)
        if parsed_line != "":
            parsed_lines.append(parsed_line)
    memloc = init_dest_lookup_dict()
    # translate and process 
    code = ""
    command = 0
    for line in parsed_lines:
        command += 1
        current = line.split(" ")
        context = memloc[current[1]]
        if current[0] == "push":
            code += f"@{current[2]}\n"
            code += "D=A\n"
            code += memloc[current[1]]
            code += "M=M+1\n"
            code += "A=M-1\n"
            code += "M=D\n"
        elif current[0] == "pop":
            code += memloc[current[1]]
            code += "AM=M-1\n"
            code += "D=M\n"
        elif current[0] == "add":
            code += "@SP\n"
            code += "AM=M-1\n"
            code += "D=M\n"
            code += "A=A-1\n"
            code += "M=D+M\n"
        elif current[0] == "sub":
            code += "@SP\n"
            code += "AM=M-1\n"
            code += "D=M\n"
            code += "A=A-1\n"
            code += "M=M-D\n"
        elif current[0] == "neg":
            code += "@SP\n"
            code += "A=M-1\n"
            code += "M=-M\n"
        elif current[0] == "eq":
            code += "@SP\n"
            code += "AM=M-1\n"
            code += "D=M\n"
            code += "A=A-1\n"
            code += "D=D-M\n"
            code += "M=-1\n"
            code += f"@COMMAND{command}\n"
            code += "D;JEQ\n"
            code += "@SP\n"
            code += "A=M-1\n"
            code += "M=0\n"
            code += f"(COMMAND{command})\n"
        elif current[0] == "gt":
            code += "@SP\n"
            code += "AM=M-1\n"
            code += "D=M\n"
            code += "A=A-1\n"
            code += "D=D-M\n"
            code += "M=-1\n"
            code += f"@COMMAND{command}\n"
            code += "D;JLT\n"
            code += "@SP\n"
            code += "A=M-1\n"
            code += "M=0\n"
            code += f"(COMMAND{command})\n"
        elif current[0] == "lt":
            code += "@SP\n"
            code += "AM=M-1\n"
            code += "D=M\n"
            code += "A=A-1\n"
            code += "D=D-M\n"
            code += "M=-1\n"
            code += f"@COMMAND{command}\n"
            code += "D;JGT\n"
            code += "@SP\n"
            code += "A=M-1\n"
            code += "M=0\n"
            code += f"(COMMAND{command})\n"
        elif current[0] == "and":
            code += "@SP\n"
            code += "AM=M-1\n"
            code += "D=M\n"
            code += "A=A-1\n"
            code += "M=D&M\n"
        elif current[0] == "or":
            code += "@SP\n"
            code += "AM=M-1\n"
            code += "D=M\n"
            code += "A=A-1\n"
            code += "M=D|M\n"
        elif current[0] == "not":
            code += "@SP\n"
            code += "A=M-1\n"
            code += "M=!M\n"
        else:
            raise Exception("Command not supported")
    code += "(END)\n@END\n0;JMP\n"
    outputfile = open(f"{filename}.asm", "w")
    outputfile.write(code)
    outputfile.close()
    assembler.main(f"{filename}.asm")

if __name__ == "__main__":
    main()
    