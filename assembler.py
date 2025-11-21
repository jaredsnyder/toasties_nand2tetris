INPUT_FILENAME = "add.asm"
OUTPUT_FILENAME = "add.hack"

A_INSTRUCTION = "A_INSTRUCTION"
C_INSTRUCTION = "C_INSTRUCTION"
L_INSTRUCTION = "L_INSTRUCTION"

def command_type(command):
    if "@" in command[0]:
        return A_INSTRUCTION
    elif '=' in command:
        return C_INSTRUCTION
    elif '(' in command and ')' in command:
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
    if 'JGT' in command:
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
        return '110'
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
    destination_substring = command.split("=")[0]
    if destination_substring == "M":
        return "001"
    elif destination_substring == "D":
        return "010"
    elif set(destination_substring) == {"D","M"}:
        return "011"
    elif destination_substring == 'A':
        return "100"
    elif destination_substring == 'AM':
        return "101"
    elif destination_substring == 'AD':
        return "110"
    elif destination_substring == 'AMD' or destination_substring == 'ADM':
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
    pass


def convert_to_binary(value):
    print(f"convert_to_binary input: {value}")
    value_int = int(value)
    if value_int >= 0:
        bin_str = '0{0:015b}'.format(value_int)
    elif value_int < 0:
        print(value_int)
        bin_value = bin(0b111111111111111 & value_int)
        bin_str = "0"+str(bin_value)[2:]
    return bin_str

# TODO: Handle invalid instructions
def parse_c_instruction(command):
    # D = D+1 ; JLE
    # JGE
    # D = D+1
    # A ; JLE
    comp, dest, jump = None
    if (command.contains("=")):
        # there will be a dest and comp
        # there may or may not be a jump
        dest, the_rest = command.split("=")
        if (the_rest.contains(";")):
            comp, jump = the_rest.split(";")
        else:
            comp = the_rest
            jump = None
    else:
        # there will not be any dest or comp
        # there will be a jump
        dest = None
        if (command.contains(";")):
            comp, jump = command.split(";")
    jump_bits = get_jump_bits(jump)
    dest_bits = get_dest_bits(dest)
    comp_bits = get_comp_bits(comp)

    return comp_bits, dest_bits, jump_bits

def parser(command):
    # TODO make sure it handles whitespace properly
    # TODO semicolons
    print(f"command: {command}")

    clean_command = command.strip()
    print(f"clean_command: {clean_command}")

    command_type_value = command_type(clean_command)
    print(f"command_type_value: {command_type_value}")
    if command_type_value == A_INSTRUCTION:
        cleaner_command = clean_command[1:]
        return convert_to_binary(cleaner_command)
    elif command_type_value == C_INSTRUCTION:
        comp, dest, jump = parse_c_instruction(clean_command)
        return f"1{comp}{dest}{jump}"


if __name__ == "__main__":
    output = []
    for line in open(INPUT_FILENAME).readlines():
        print("\n")
        if not line.strip():
            continue
        parsed = parser(line.replace("\n",""))
        print(f"parsed: {parsed}")
        if not parsed:
            continue
        output.append(parsed)

    output_with_newlines = [x+"\n" for x in output]
    with open(OUTPUT_FILENAME, 'w') as outfile:
        outfile.writelines(output_with_newlines)
