# Reads a plain text file. translates every line to its binary representation according to given code syntax
# Creates a file in binary with translated lines


import Instructions
import re
import string
import sys

# Keeps a flag for format errors, we set it to False when we find a formatting error
# in given .asm file and break without creating .bin file
format_check = True

# Gets program name and file path as arguments (Only the file name can be entered if the file is at the same directory)
# program_name = sys.argv[0]
# file_path = sys.argv[1]

# Removes extension and extracts file name from path
# file_name = file_path.split('.')[0].split('\\')[-1]

# Dictionary to look up registries' binary representations
regs = {'A': '0000000000000001', 'B': '0000000000000010', 'C': '0000000000000011', 'D': '0000000000000100',
        'E': '0000000000000101', 'S': '0000000000000110', 'PC': '0000000000000000'}

# Reads the file if file cannot be opened throws 'File could not be found' exception
# try:
#     asm = open(file_path, 'r')
# except:
#     print('File "' + file_name + '" could not be found!')
#     format_check = False
asm = open('test.asm', 'r')

# An empty list for keeping code lines in given .asm file
asml = []

# Initialize instruction object
instructions_dic = Instructions.Instruction()

# For every line in code file, remove new line characters split lines as single words
# append every line as a list of words to asml list
for line in asm:
    line = line.split('\n')
    asml.append(line[0].split(' '))
asm.close()

# Create an empty list for keeping binary representations of each code line
binaries_list = []

# Create an empty dictionary for keeping label names and values
labels = {}

# Check code file for labels, assign a binary value to label according to its line number
# in the code file, add label name and labels binary value to labels dictionary
for i in asml:
    if ':' == i[0][-1] and len(i) == 1:
        labels.update({i[0]: bin(asml.index(i) * 3)[2:].zfill(16)})

# Check syntax each code lines and convert it to binary accordingly
for elem in asml:
    if len(elem) == 2:
        # If the element is not a label or implicit instruction, check access mode and data type based on operand format
        # based on access mode add access modes binary representation to index 1 in inner list
        tmpl = [instructions_dic.getInstCode(elem[0]), '', '']
        if elem[1] in 'A B C D E S'.split(' ') or elem[1] == 'PC':
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
        elif all(c in string.hexdigits for c in elem[1]):
            if len(elem[1]) == 4:
                tmpl[1] = '00'
                tmpl[2] = bin(int(elem[1], 16))[2:].zfill(16)
            else:
                print('Hexadecimal format error at line :' + str(asml.index(elem) + 1))
                format_check = False
                break
        elif '[' == elem[1][0] and ']' == elem[1][-1]:
            if '[' == elem[1][0] and ']' == elem[1][2] and len(elem[1]) == 3:
                tmpl[1] = '10'
                try:
                    tmpl[2] = regs[elem[1][1]]
                except:
                    print('Unknown registry name at line :' + str(asml.index(elem) + 1))
                    format_check = False
                    break
            elif '[' == elem[1][0] and ']' == elem[1][-1] and len(elem[1]) == 6 and all(c in string.hexdigits for c in elem[1][1:5]):
                tmpl[1] = '11'
                tmpl[2] = bin(int(elem[1][1:5], 16))[2:].zfill(16)
            elif '[' == elem[1][0] and ']' == elem[1][3] and len(elem[1]) == 4:
                tmpl[1] = '10'
                try:
                    tmpl[2] = regs[elem[1][1:3]]
                except:
                    print('Unknown registry name at line :' + str(asml.index(elem) + 1))
                    format_check = False
                    break
            else:
                print('Memory addressing error at line: ' + str(asml.index(elem) + 1))
                format_check = False
                break
        else:
            tmpl[1] = '00'
            try:
                tmpl[2] = labels[elem[1] + ':']
            except:
                print('Label "' + elem[1] + '" is not defined. Line :' + str(asml.index(elem) + 1))
                format_check = False
                break
    elif ':' == elem[0][-1] and len(elem) == 1:
        tmpl = [''] * 3
        tmpl[0] = '1' * 6
        tmpl[1] = '11'
        tmpl[2] = labels[elem[0]]
    elif len(elem) == 1 and elem[0] in instructions_dic.inst_list.keys():
        tmpl = [instructions_dic.getInstCode(elem[0]), '00', '0' * 16]
    else:
        print('Syntax error at line :' + str(asml.index(elem) + 1))
        format_check = False
        break
    binaries_list.append(tmpl)

#     If there is not any format error create a file and write binaries to file.
if format_check:
    bin_out = open(('file_name' + '.bin'), 'w')
    for bincode in binaries_list:
        bin_out.write(bincode[0] + bincode[1] + bincode[2] + '\n')

    bin_out.close()
    for i in binaries_list:
        print(i)
else:
    print('File could not be assembled!')
