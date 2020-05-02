import Instructions
import re
import string
import sys

format_check = True
program_name = sys.argv[0]
file_path = sys.argv[1]

regs = {'A': '0000000000000001', 'B': '0000000000000010', 'C': '0000000000000011', 'D': '0000000000000100',
        'E': '0000000000000101', 'S': '0000000000000110', 'PC': '0000000000000000'}
asm = open(file_path, 'r')
#asm = open('test.asm', 'r')
asml = []

instructions_dic = Instructions.Instruction()
for line in asm:
    line = line.split('\n')
    asml.append(line[0].split(' '))
asm.close()
binaries_list = []
labels = {}
label_add = 10000

# reads all file and assigns arbitrary memory locations for labels
iline = 0
for i in asml:
    if ':' in i[0]:
        labels.update({i[0]: bin(iline*3)[2:].zfill(16)})
        label_add = label_add + 100
    iline = iline + 1


for elem in asml:
    if len(elem) == 2:
        # If the element is not a label or implicit instruction, check access mode and data type based on operand format
        # based on access mode add access modes binary representation to index 1 in inner list
        tmpl = [instructions_dic.getInstCode(elem[0]), '', '']
        if elem[1] in 'ABCDES' or elem[1] == 'PC':
            # check if the operand is a registry, if true get registry's 16bit binary code
            tmpl[1] = '01'
            tmpl[2] = regs[elem[1]]
        elif re.findall(r"'(\w+)'", elem[1]):
            # check if operand is a character, if true get character ascii code and convert it too 16bit binary
            if len(re.findall(r"'(\w+)'", elem[1])[0]) == 1:
                tmpl[1] = '00'
                tmpl[2] = bin(ord(re.findall(r"'(\w+)'", elem[1])[0]))[2:].zfill(16)
            elif len(re.findall(r"'(\w+)'", elem[1])[0]) == 2:
                tmpl[1] = '00'
                char1 = bin(ord(re.findall(r"'(\w+)'", elem[1])[0][0]))[2:].zfill(8)
                char2 = bin(ord(re.findall(r"'(\w+)'", elem[1])[0][1]))[2:].zfill(8)
                tmpl[2] = char1 + char2
            else:
                print('Character format error at line: ' + str(asml.index(elem) + 1))
                format_check = False
                break
        elif all(c in string.hexdigits for c in elem[1]) and len(elem[1]) == 4:
            tmpl[1] = '00'
            tmpl[2] = bin(int(elem[1], 16))[2:].zfill(16)
        elif '[' in elem[1] and len(elem[1]) == 3:
            tmpl[1] = '10'
            tmpl[2] = regs[elem[1][1]]
        elif '[' in elem[1] and len(elem[1]) == 6:
            tmpl[1] = '11'
            tmpl[2] = bin(int(elem[1][1:5], 16))[2:].zfill(16)
        else:
            tmpl[1] = '00'
            tmpl[2] = labels[elem[1] + ':']
    elif ':' in elem[0]:
        tmpl = [''] * 3
        tmpl[0] = '1' * 6
        tmpl[1] = '11'
        tmpl[2] = labels[elem[0]]
    elif len(elem) == 1 and elem[0] in instructions_dic.inst_list.keys():
        tmpl = [instructions_dic.getInstCode(elem[0]), '00', '0' * 16]

    binaries_list.append(tmpl)
if format_check:
    bin_out = open('prog.bin', 'a')
    for bincode in binaries_list:
        bin_out.write(bincode[0] + bincode[1] + bincode[2] + '\n')

    bin_out.close()
    for i in binaries_list:
        print(i)
else:
    print('File could not be assembled!')