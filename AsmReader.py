import  Instructions

regs = {'A':'0000000000000001', 'B':'0000000000000010', 'C':'0000000000000011', 'D':'0000000000000100', 'E':'0000000000000101', 'S':'0000000000000110', 'PC':'0000000000000000'}

myinst = Instructions.Instruction()
asm = open('C:\\Users\\semih\\OneDrive\\Desktop\\test.asm', 'r')
asml = []
for line in asm:
    line = line.split('\n')
    asml.append(line[0].split(' '))
binl = []
for elem in asml:
    tmpl = [myinst.getInstCode(elem[0]),'']
    if len(elem) == 2:
        if elem[1] in 'ABCDES' or elem[1] == 'PC':
            tmpl[1] = regs[elem[1]]
    # tmpl.append(elem[1])
    binl.append(tmpl)



print(binl)
