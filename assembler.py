INPUT_FILENAME = "add.asm"
OUTPUT_FILENAME = "add.hack"

def command_type(command):
    if "@" in command[0]:
        return 'A_COMMAND'
    elif '=' in command:
        return 'C_COMMAND'
    elif '(' in command and ')' in command:
        return 'L_COMMAND'
    else:
        raise ValueError("WTF >:( what command is this")
    
def jump(command):
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
    
def dest(command):
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

def convert_to_binary(value):
    value_int = int(value)
    if value_int >= 0:
        bin_str = '0{0:015b}'.format(value_int)
    elif value_int < 0:
        print(value_int)
        bin_value = bin(0b111111111111111 & value_int)
        bin_str = "0"+str(bin_value)[2:]
    return bin_str

def parser(command):
    # TODO make sure it handles whitespace properly
    # TODO semicolons
    clean_command = command.strip()
    command_type_value = command_type(clean_command)
    if command_type_value == 'A_INSTRUCTION':
        return '0{0:15b}'.format(6)
    elif command_type_value == "C_INSTRUCTION":
        jump_bits = jump(command)
        dest_bits = dest(command)
    return bytecode



if __name__ == "__main__":
    output = []
    for line in open(INPUT_FILENAME).readlines():
        if not line.strip():
            continue
        output.append(parser(line.replace("\n","")))
    
    output_with_newlines = [x+"\n" for x in output]
    with open(OUTPUT_FILENAME, 'w') as outfile:
        outfile.writelines(output_with_newlines)

  