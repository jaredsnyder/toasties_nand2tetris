# Chapter 7
# VM Language -> Assembly
# https://drive.google.com/file/d/1BPmhMLu_4QTcte0I5bK4QBHI8SACnQSt/view
#
# Key Slides
# -------------------------------------------
# Slide 47 - push
# Slide 70 - arithmetic operations
# Slide 83 - segments and stack in the ram

# Our VM is stack-based.
# Every high-level arithmetic or logical expression in the object oriented Jack language can be translated into
# a sequence of VM commands, operating in a stack (stack arithmetic, stack logical ops).
#
# The first goal is to the support the push / pop commands of the VM language:
# push/pop {segment} {i}
# {segment} is one of the 8 areas of virtual memory that we only ever access LIFO. Segments are stacks as well.
# {i} is the value we want to put into the virtual memory
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
