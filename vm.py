# Chapter 7
# VM Language -> Assembly
# https://drive.google.com/file/d/1BPmhMLu_4QTcte0I5bK4QBHI8SACnQSt/view
#
# Key Slides
# -------------------------------------------
# Slide 47 - push
# Slide 70 - arithmetic operations
# Slide 83 - segments and stack in the ram

# Our VM is a "stack machine" architecture.
# It just uses a stack and some memory.
#
# Every high-level arithmetic or logical or branching expression in the high level Jack language
# can be translated into a sequence of VM commands that leverage the stack and the memory.
# So we'll store values in memory, and place them onto the stack for the "working memory" when we
# want to do arithmetic or logic or branch operations.
#
# The first goal is to the support the push / pop commands of the VM language.
# Push / pop commands transfer data between the stack and memory segments.
#
# push/pop {segment} {i}
# {segment} is one of the 8 areas of virtual memory in our VM. The segment is sequential, RAM-like memory.
# {i} is the index into a specific location of the virtual memory
#
# There are 8 kinds of memory segments: constant, local, argument, this, that, static, temp, pointer
# The reason for having this particular 8 is to support specific functionalities of the object-oriented language that
# would be too complex to manage using just RAM directly.
# So we'll see in the future why these specific 8 have been chosen for the next layer of abstraction over RAM.
# But we've used high level languages before, know there are different kinds of variables (local, constant, function
# arguments..), so we can start to guess that it's probably useful to represent and manage those kinds of variables separately.
#
# All this pushin and poppin and segments is just to prepare our VM's internal representation of the values, next steps will
# be leveraging the segments we set up to do stack arithmetic and stack logical operations. In Chapther 8 we'll handle
# branching control flow and function commands.

## Initialization
RAM = [0 for _ in range(16384)]

SP_address = 0
LCL_address = 1
ARG_address = 2
THIS_address = 3
THAT_address = 4

TEMP_RANGE = (5, 12)
STATIC_RANGE = (16, 255)
STACK_RANGE = (256, 2047)


def print_stack():
    print(RAM[STACK_RANGE[0] : RAM[SP_address] + 1])
    return


def constant_push(the_constant):
    """
    Takes in a the constant
    Returns list of strings, the order of assembly instructions that does 'push'
    """
    return [
        f"@{the_constant}",
        "D=A",
        f"@{SP_address}",
        "A=M",
        "M=D",
        f"@{SP_address}",
        "M=M+1",
    ]


"""
A is the memory address we are pointing to with the stack pointer, but we can use it as data, too
M is the value at memory address A
D is a spare register to use
"""


def binary_operator(instruction_list):
    grab_values_off_stack = [
        # take 0, load it into the A register.
        # M register will have the value at SP_address, which is the stack pointer
        # Setting A=0, M=value of SP
        # M now holds the value
        f"@{SP_address}",
        # set the Address to the value at the stack pointer
        "M=M-1",
        "A=M",
        # set the D register to the value
        "D=M",
        # decrement stack pointer
        f"@{SP_address}",
        "M=M-1",
        # get value on top of stack
        "A=M",
    ]
    set_stack_and_increment = [
        "M=D",
        # increment so stack pointer is pointed at "blank" spot
        "M=M+1",
    ]
    return grab_values_off_stack + instruction_list + set_stack_and_increment


def add():
    """
    adds two constants from the top of the stack
    places the result at the top of the stack

    """

    # CPU Emulator's  RAM visualizer tip:
    # left hand side is A
    # right hand side is D
    return binary_operator(["D=D+M"])


def sub():
    """
    subtracts two constants from the top of the stack
    subracting the top of the stack (last in) from the number below
    places the result at the top of the stack
    """

    # CPU Emulator's  RAM visualizer tip:
    # left hand side is A
    # right hand side is D
    return binary_operator(["D=M-D"])


def eq():
    """
    idea: subtract and not,
    that was if you get a zero, they are equal
    not to turn 0 into 1 (true, probably?)
    """
    pass


def is_skipped_line(line) -> bool:
    if not line.strip():
        return True
    if line.strip()[0:2] == "//":
        return True
    return False


def main():
    output = []
    INPUT_FILENAME = "test/vm/SimpleAdd/SimpleAdd.vm"
    OUTPUT_FILENAME = "output.asm"
    # Pass for user defined symbols
    for i, line in enumerate(open(INPUT_FILENAME).readlines()):
        # iterate through vm code lines
        if is_skipped_line(line):
            continue
        # modifying we have push and pop at the beginning
        # arithmatic functions: add, sub, neg, eq, gt, lt, and, or, not
        split_line = line.split()
        if split_line[0] == "push":
            if split_line[1] == "constant":
                constant_val = split_line[2]
                output += constant_push(constant_val)
        if split_line[0] == "add":
            output += add()

    output_with_newlines = [x + "\n" for x in output]
    with open(OUTPUT_FILENAME, "w") as outfile:
        outfile.writelines(output_with_newlines)


if __name__ == "__main__":
    main()
