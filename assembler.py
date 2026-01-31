import sys

A_INSTRUCTION = "A_INSTRUCTION"
C_INSTRUCTION = "C_INSTRUCTION"
L_INSTRUCTION = "L_INSTRUCTION"

FULL_SYMBOLS_LUT = {
    "R0": 0,
    "R1": 1,
    "R2": 2,
    "R3": 3,
    "R4": 4,
    "R5": 5,
    "R6": 6,
    "R7": 7,
    "R8": 8,
    "R9": 9,
    "R10": 10,
    "R11": 11,
    "R12": 12,
    "R13": 13,
    "R14": 14,
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "SCREEN": 16384,
    "KBD": 24576,
}

def command_type(command):
    if "@" in command[0]:
        return A_INSTRUCTION
    elif "=" in command or ";" in command:
        return C_INSTRUCTION
    elif "(" in command and ")" in command:
        return L_INSTRUCTION
    else:
        raise ValueError("WTF >:( what command is this")


# jump    j j j   effect:
#
# null    0 0 0   no jump
# JGT     0 0 1   if comp > 0 jump
# JEQ     0 1 0   if comp = 0 jump
# JGE     0 1 1   if comp ≥ 0 jump
# JLT     1 0 0   if comp < 0 jump
# JNE     1 0 1   if comp ≠ 0 jump
# JLE     1 1 0   if comp ≤ 0 jump
# JMP     1 1 1   Unconditional jump
def get_jump_bits(command):
    if command is None:
        return "000"
    elif "JGT" in command:
        return "001"
    elif "JEQ" in command:
        return "010"
    elif "JGE" in command:
        return "011"
    elif "JLT" in command:
        return "100"
    elif "JNE" in command:
        return "101"
    elif "JLE" in command:
        return "110"
    elif "JMP" in command:
        return "111"
    else:
        return "000"


# dest    d d d   effect: the value is stored in:
#
# null    0 0 0   the value is not stored
# M       0 0 1   RAM[A]
# D       0 1 0   D   register
# DM      0 1 1   D register and RAM[A]
# A       1 0 0   A register
# AM      1 0 1   A register and RAM[A]
# AD      1 1 0   A register and D register
# ADM     1 1 1   A register, D register, and RAM[A]
def get_dest_bits(command):
    if not command:
        return "000"
    destination_substring = command.split("=")[0]
    if destination_substring == "M":
        return "001"
    elif destination_substring == "D":
        return "010"
    elif set(destination_substring) == {"D", "M"}:
        return "011"
    elif destination_substring == "A":
        return "100"
    elif destination_substring == "AM":
        return "101"
    elif destination_substring == "AD":
        return "110"
    elif destination_substring == "AMD" or destination_substring == "ADM":
        return "111"
    elif not destination_substring:
        return "000"
    else:
        raise ValueError(f"Invalid code {destination_substring}")


#     comp        c c c c c c
#
# a=0     a=1
#
# 0               1 0 1 0 1 0
# 1               1 1 1 1 1 1
# -1              1 1 1 0 1 0
# D               0 0 1 1 0 0
# A       M       1 1 0 0 0 0
# !D              0 0 1 1 0 1
# !A      !M      1 1 0 0 0 1
# -D              0 0 1 1 1 1
# -A      -M      1 1 0 0 1 1
# D+1             0 1 1 1 1 1
# A+1     M+1     1 1 0 1 1 1
# D-1             0 0 1 1 1 0
# A-1     M-1     1 1 0 0 1 0
# D+A     D+M     0 0 0 0 1 0
# D-A     D-M     0 1 0 0 1 1
# A-D     M-D     0 0 0 1 1 1
# D&A     D&M     0 0 0 0 0 0
# D|A     D|M     0 1 0 1 0 1
def get_comp_bits(command):
    ## returns a string of "a c1 c2 c3 c4 c5 c6"
    match command:
        case "0":
            return "0101010"
        case "1":
            return "0111111"
        case "-1":
            return "0111010"
        case "D":
            return "0001100"
        case "A":
            return "0110000"
        case "M":
            return "1110000"
        case "!D":
            return "0001101"
        case "!A":
            return "0110001"
        case "!M":
            return "1110001"
        case "-D":
            return "0001111"
        case "-A":
            return "0110011"
        case "-M":
            return "1110011"
        case "D+1":
            return "0011111"
        case "A+1":
            return "0110111"
        case "M+1":
            return "1110111"
        case "D-1":
            return "0110111"
        case "A-1":
            return "0110010"
        case "M-1":
            return "1110010"
        case "D+A":
            return "0000010"
        case "D+M":
            return "1000010"
        case "D-A":
            return "0010011"
        case "D-M":
            return "1010011"
        case "A-D":
            return "0000111"
        case "M-D":
            return "1000111"
        case "D&A":
            return "0000000"
        case "D&M":
            return "1000000"
        case "D|A":
            return "0010101"
        case "D|M":
            return "1010101"


def convert_to_binary(value):
    print(f"convert_to_binary input: {value}")
    value_int = int(value)
    bin_str = None
    if value_int >= 0:
        bin_str = "0{0:015b}".format(value_int)
    elif value_int < 0:
        print(value_int)
        bin_value = bin(0b111111111111111 & value_int)
        bin_str = "0" + str(bin_value)[2:]
    return bin_str


# TODO: Handle invalid instructions
def parse_c_instruction(command):
    # D = D+1 ; JLE
    # JGE
    # D = D+1
    # A ; JLE
    comp, dest, jump = None, None, None
    if "=" in command:
        # there will be a dest and comp
        # there may or may not be a jump
        dest, the_rest = command.split("=")
        if ";" in the_rest:
            comp, jump = the_rest.split(";")
        else:
            comp = the_rest
            jump = None
    else:
        # there will not be any dest or comp
        # there will be a jump
        dest = None
        if ";" in command:
            comp, jump = command.split(";")
    print(f"comp: {comp}")
    print(f"jump: {jump}")
    print(f"dest: {dest}")

    jump_bits = get_jump_bits(jump)
    dest_bits = get_dest_bits(dest)
    comp_bits = get_comp_bits(comp)

    return comp_bits, dest_bits, jump_bits


def symbol_parser(line, i):
    stripped_line = line.strip()
    if stripped_line[0] == "(" and stripped_line[-1]==")":
        if stripped_line[1:-1] in FULL_SYMBOLS_LUT:
            raise ValueError("NO! NOO!!!!")
        FULL_SYMBOLS_LUT[stripped_line[1:-1]]=i
        print(stripped_line[1:-1],i, convert_to_binary(i))

def command_parser(command):
    # TODO make sure it handles whitespace properly
    # TODO semicolons
    print(f"command: {command}")

    clean_command = command.strip()
    print(f"clean_command: {clean_command}")

    command_type_value = command_type(clean_command)
    print(f"command_type_value: {command_type_value}")
    if command_type_value == A_INSTRUCTION:
        cleaner_command = clean_command[1:]
        if cleaner_command in FULL_SYMBOLS_LUT:
            return convert_to_binary(FULL_SYMBOLS_LUT[cleaner_command])
        return convert_to_binary(cleaner_command)

    elif command_type_value == C_INSTRUCTION:
        comp, dest, jump = parse_c_instruction(clean_command)
        return f"111{comp}{dest}{jump}"
    
    elif command_type_value == L_INSTRUCTION:
        return


def is_skipped_line(line) -> bool:
    if not line.strip():
        return True
    if line.strip()[0:2] == "//":
        return True
    return False


def main():
    if len(sys.argv) != 3:
        print("I need the input AND output filenames")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    with open(input_path, "r") as f_input:
        lines = f_input.readlines()

    # Pass for user defined symbols
    for i, line in enumerate(lines):
        if is_skipped_line(line):
            continue
        symbol_parser(line, i)

    output = []

    # Pass for command identification
    for line in lines:
        print(line)
        if is_skipped_line(line):
            continue
        print("\n")
        parsed = command_parser(line.replace("\n", ""))
        print(f"parsed: {parsed}")
        if not parsed:
            continue
        output.append(parsed)

    output_with_newlines = [x + "\n" for x in output]

    with open(output_path, "w") as outfile:
        outfile.writelines(output_with_newlines)

if __name__ == "__main__":
    main()