# accept 3 consecutive ones
def machine(seq):
    onecount = 0
    for i in seq:
        if i == '1':
            onecount +=1
            if onecount == 3:
                return True
        else:
            onecount = 0
    return False
            
        
print(machine("11010101100"))
print(machine("11000101001"))
print(machine("110001111"))
print(machine("11101100101"))