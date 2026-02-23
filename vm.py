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
    RAM[SP_address] += 1
    return 
    #["@the_constant",
    # "@SP",
    # "A=M",
    # "M=D",
    # ]
    # // SP++
    # @SP
    # M=M+1]




def pop():
    RAM[SP] -= 1


# Initialize pointers
RAM[SP] = STACK_RANGE[0]
RAM[LCL] = 2048
RAM[ARG] = 5000


# push constant 10
RAM[SP] += 1
RAM[RAM[SP]] = 10

print_stack()

# pop local 0
RAM[RAM[LCL] + 0] = RAM[RAM[SP]]
RAM[SP] -= 1


print_stack()
print(RAM[RAM[LCL]])
print(RAM[SP])

