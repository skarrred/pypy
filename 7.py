def machine(seq):
    if seq[-3:] == '101':
        return True
    else:
        return False
    
print(machine('100101001011'))
print(machine('1010100000101'))
print(machine('1010100010'))
print(machine('101'))