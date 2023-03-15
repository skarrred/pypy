#same no of 1s and 0s

def balmach(seq):
    ones = seq.count('1')
    zeros = seq.count('0')

    if ones == zeros:
        print('accepted')
    else:
        print('rejected')

balmach('11001')
balmach('1001010')
balmach('1111100001')
balmach('10')
balmach('11100011100010')














# def is_bal(instr):
#     ones = instr.count('1')
#     zeros = instr.count('0')
#     return ones == zeros

# def mach(instr):
#     if is_bal(instr):
#         print('accepted')
#     else:
#         print("rejected")

# mach(input("enter a string: "))


    