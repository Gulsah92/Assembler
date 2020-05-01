class Instruction:
    def __init__(self):
        self.inst_list = {'HALT':'00000001', 'LOAD': '00000010', 'STORE': '00000011', 'ADD': '00000100', 'SUB': '00000101', 'INC': '0006',
                          'DEC': '00000110', 'MUL': '00001000', 'DIV': '00001001', 'XOR': '00001010','AND': '00001011', 'OR':'00001100' ,
                          'NOT': '00001101', 'SHL': '00001110', 'SHR':'00001111', 'NOP': '00010000','PUSH': '00010001', 'POP': '00010010',
                          'CMP': '00010011', 'JMP': '00010100', 'JZ':'00010101', 'JE': '00010101','JNZ': '00010110', 'JNE': '00010110',
                          'JC': '00010111', 'JNC': '00011000', 'JA': '00011001', 'JAE': '00100000','JB': '00100001', 'JBE': '00100010',
                          'READ': '00100011', 'PRINT': '00100100'}

    def getInstCode(self, instcode):
        return self.inst_list[instcode]


myinst = Instruction()

print(myinst.getInstCode('STORE'))
