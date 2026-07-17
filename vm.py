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

from typing import Literal

## Initialization
RAM = [0 for _ in range(16384)]

SP_address = 0
LCL_address = 1
ARG_address = 2
THIS_address = 3
THAT_address = 4
TEMP_address = 5 # 5 - 12
STATIC_address = 16 # 16 - 255

SegmentType = Literal["local", "argument", "this", "that", "static", "temp", "pointer"]

# todo next time: we finished Fibonacci hehe back to chapter 8!

OPERATIONS_LUT = {
    "add": "binary",
    "sub": "binary",
    "eq": "binary",
    "gt": "binary",
    "lt": "binary",
}

def grab_range_value(segment: SegmentType, index: int):
    match segment:
        case "local":
            return [
                f"@{LCL_address}", # M is 200, A is 1
                # set the D register to the value
                "D=M", # D is 200
                f"@{index}", # grab_range_value(local, 0) -> # M is 256, A is 0
                # "A=D+A", # A is (200 + 0)
            ]
        case "argument":
            return [
                f"@{ARG_address}",
                # set the D register to the value
                "D=M",
                f"@{index}",
            ]
        case "that":
            return [
                f"@{THAT_address}",
                # set the D register to the value
                "D=M",
                f"@{index}",
            ]
        case "this":
            return [
                f"@{THIS_address}", # pop this 0 == save this number to THIS_ADDRESS + 0 (3000 + 0)
                # set the D register to the value
                "D=M",
                f"@{index}",
            ]
        case "static":
            return [
                f"@{STATIC_address}", # M is ??, A is 16
                "D=M", # Be sure to get the value "16" instead of de-reffing what's at addr 16
                f"@{index}",            ]
        case "temp":
            return [
                f"@{TEMP_address}", # M is ??, A is 5
                "D=M", # Be sure to get the value "5" instead of de-reffing what's at addr 5
                f"@{index}",
            ]
        case "pointer": # index will either be 0 (this) or 1 (that)
            if index == 0:
                return [
                f"@{THIS_address}",
                # set the D register to the value
                "D=0" # we have to do this for generic_pop
                ]
            else:
                return [
                f"@{THAT_address}",
                # set the D register to the value
                # "D=M",
                # f"@{index}",
                "D=0" # we have to do this for generic_pop, it kinda makes sense but we should refactor
                ]
    return 



def grab_value_off_stack():
    return [
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
    ]


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


def generic_push(segment: SegmentType, index: int):
    return grab_range_value(segment, index) + [
        "A=D+A",
        "D=M",
        f"@{SP_address}",
        "A=M",
        "M=D",
        f"@{SP_address}",
        "M=M+1",
    ]


def generic_pop(segment: SegmentType, index: int):
    """
    This current solution is shoddy as hell, we have to borrow some hopefully unused 
    memory @10000 to store a fourth value because we need to add index and address but 
    we also need to hold the value of interest (to be saved at the index+address address)
    So this current is a lil dumb

    Jared Snyder also came up w an alternate solution, maybe shoddier
    What if we create a for loop that does M=M+1 index times,
    If we can do this wo the D reg, then we wouldn't need a random memory spot to save this number

    Third option to consider:
    maybe one of these other memory segments we haven't really used/learned yet can be 
    the spiritual successor to @10000. Like temp and static, maybee that why it's called that
    temp?

    """
    return (
        grab_range_value(segment, index) + [
            "D=D+A",
            "@10000",
            "M=D",
        ]
        +
        grab_value_off_stack() + # D has our value
        [
            "@10000",
            "A=M",
            "M=D"
        ]

        # TODO: the 10000 is a placeholder random memory for extra space to store the 
        # 4 number we needed to do generic pop for now, maybe there's a better place
    )


"""
A is the memory address we are pointing to with the stack pointer, but we can use it as data, too
M is the value at memory address A
D is a spare register to use
"""

""" 03/27 notes
Right now we're decrementing the SP at the beginning of every operation, and incrementing the SP
at the end, this means between every command, we're incrementing and immediately decrementing again
It looks weird, maybe we should refactor. But the code works so maybe don't fix if not broken lol
We did neg, and, or, and not today, and got the code up to the point of simplelogic test

Next time, we'll create the =, <, > operations :)

We should also refactor the main function to not hardcode every command and function
"""


def binary_operator(instruction_list):
    grab_values_off_stack = grab_value_off_stack() + [
        # decrement stack pointer
        f"@{SP_address}",
        "M=M-1",
        # get value on top of stack
        "A=M",
    ]
    set_stack_and_increment = [
        "M=D",
        # go back to the SP address
        f"@{SP_address}",
        # increment so stack pointer is pointed at "blank" spot
        "M=M+1",
    ]
    return grab_values_off_stack + instruction_list + set_stack_and_increment


def unitary_operator(instruction_list):
    leave_value_go_to_stack_and_increment = [
        "M=D",
        # go back to the SP address
        f"@{SP_address}",
        # increment so stack pointer is pointed at "blank" spot
        "M=M+1",
    ]
    return (
        grab_value_off_stack()
        + instruction_list
        + leave_value_go_to_stack_and_increment
    )


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
    return sub() + not_operator()


def lt():
    """
    idea 1:
    subract the top of the stack (last in) from the number below
    if difference is not negative, return false
    if difference is negative, return true
    !!! handle eq case too?
    X1 - X2
    push 16384 -> 100 0000 0000 0000
    AND
    EQ -> true means result is negative

    idea 2:
    subract the top of the stack (last in) from the number below
    use the JLT instructions to figure out if the number is less, eq, or greater
    if its less than, we'll jump, and the place we jump to will set the result to true
    otherwise, set the result to false on the result part of the top of the stack
    set stack pointer to that place
    """
    return sub() + [
        "@IS_LESS_THAN",
        "D;JLT",
        f"@{SP_address}",
        "M=M-1",
        "A=M",
        "M=0",
        "@END",
        "0;JMP",
        "(IS_LESS_THAN)",
        f"@{SP_address}",
        "M=M-1",
        "A=M",
        "M=-1",
        "(END)",
    ]


def gt():
    """
    X1 > X2
    idea:
    subract the top of the stack (last in) from the number below
    if difference is negative OR zero, return false
    if difference is positive, return true
    !!! handle eq case too?
    """
    return sub() + [
        "@IS_GREATER_THAN",
        "D;JGT",
        f"@{SP_address}",
        "M=M-1",
        "A=M",
        "M=0",
        "@END",
        "0;JMP",
        "(IS_GREATER_THAN)",
        f"@{SP_address}",
        "M=M-1",
        "A=M",
        "M=-1",
        "(END)",
    ]


def neg():
    """
    takes the item from the top of the stack
    and sets to its negative
    """

    # CPU Emulator's  RAM visualizer tip:
    # left hand side is A
    # right hand side is D
    return unitary_operator(["@0", "D=A-D", "A=M"])


def and_operator():
    """
    takes the top two items off the stack
    and compares for logical AND, returns result
    """

    # CPU Emulator's  RAM visualizer tip:
    # left hand side is A
    # right hand side is D
    return binary_operator(["D=D&M"])


def or_operator():
    """
    takes the top two items off the stack
    and compares for logical OR, returns result
    """

    # CPU Emulator's  RAM visualizer tip:
    # left hand side is A
    # right hand side is D
    return binary_operator(["D=D|M"])


def not_operator():
    """
    takes the top item off the stack
    sets to its logical NOT, returns result
    """

    # CPU Emulator's  RAM visualizer tip:
    # left hand side is A
    # right hand side is D
    return unitary_operator(["D=!D"])


def is_skipped_line(line) -> bool:
    if not line.strip():
        return True
    if line.strip()[0:2] == "//":
        return True
    return False


## Start of Chapter 8 methods
def write_label(label_name):
    """Writes assembly code to handle the label command"""
    return [f"({label_name})"]


def write_goto(label_name):
    return [f"@{label_name}", "0;JMP"]


def write_if(label_name):
    """Writes assembly code to handle the if-goto command"""
    x = grab_value_off_stack()
    return x + [f"@{label_name}", "D;JNE"]

def write_function(function_name, num_vars):
    """Writes assembly code to handle the function command"""
    instructions = write_label(function_name)
    for _ in range(int(num_vars)):
        instructions += constant_push(0)
    return instructions

#def write_return(...):
#    """Writes assembly code to handle the return command
#       IMPLEMENT ME NEXT!!!!!!!!!!!! TODO TODO
#     """
#    pass

def main():
    output = []
    INPUT_FILENAME = "test/vm/SimpleFunction/SimpleFunction.vm"
    OUTPUT_FILENAME = "simple_function.asm"

    # Pass for user defined symbols
    for i, line in enumerate(open(INPUT_FILENAME).readlines()):
        # iterate through vm code lines
        if is_skipped_line(line):
            continue
        # modifying we have push and pop at the beginning
        # arithmatic functions: add, sub, neg, eq, gt, lt, and, or, not
        split_line = line.split()
        output += [f"//{line}"]
        if split_line[0] == "push":
            if split_line[1] == "constant":
                constant_val = split_line[2]
                output += constant_push(constant_val)
            elif (
                split_line[1] == "argument"
                or split_line[1] == "local"
                or split_line[1] == "that"
                or split_line[1] == "this"
                or split_line[1] == "static"
                or split_line[1] == "temp"
                or split_line[1] == "pointer"
            ):
                index = int(split_line[2])
                output += generic_push(split_line[1], index)
        if split_line[0] == "pop":
            if (
                split_line[1] == "argument"
                or split_line[1] == "local"
                or split_line[1] == "that"
                or split_line[1] == "this"
                or split_line[1] == "static"
                or split_line[1] == "temp"
                or split_line[1] == "pointer"
            ):
                index = int(split_line[2])
                output += generic_pop(split_line[1], index)
        if split_line[0] == "add":
            output += add()
        if split_line[0] == "sub":
            output += sub()
        if split_line[0] == "neg":
            output += neg()
        if split_line[0] == "eq":
            output += eq()
        if split_line[0] == "lt":
            output += lt()
        if split_line[0] == "gt":
            output += gt()
        if split_line[0] == "and":
            output += and_operator()
        if split_line[0] == "or":
            output += or_operator()
        if split_line[0] == "not":
            output += not_operator()
        if split_line[0] == "label":
            output += write_label(split_line[1])
        if split_line[0] == "goto":
            output += write_goto(split_line[1])
        if split_line[0] == "if-goto":
            output += write_if(split_line[1])
        if split_line[0] == "function":
            output += write_function(split_line[1], split_line[2])
        #if split_line[0] == "return":
        #    output += write_return(...) TODO TODO

    output_with_newlines = [x + "\n" for x in output]
    with open(OUTPUT_FILENAME, "w") as outfile:
        outfile.writelines(output_with_newlines)


if __name__ == "__main__":
    main()
