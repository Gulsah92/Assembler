class Instruction:
    # Initialize a dictionary of instructions and their binary representation
    # Provides a get method to get binary representation of given instruction
    def __init__(self):
        self.inst_list = {'HALT':'000001', 'LOAD': '000010', 'STORE': '000011', 'ADD': '000100', 'SUB': '000101', 'INC': '000110',
                          'DEC': '000110', 'MUL': '001000', 'DIV': '001001', 'XOR': '001010','AND': '001011', 'OR':'001100',
                          'NOT': '001101', 'SHL': '001110', 'SHR':'001111', 'NOP': '010000','PUSH': '010001', 'POP': '010010',
                          'CMP': '010011', 'JMP': '010100', 'JZ':'010101', 'JE': '010101','JNZ': '010110', 'JNE': '010110',
                          'JC': '010111', 'JNC': '011000', 'JA': '011001', 'JAE': '100000','JB': '100001', 'JBE': '100010',
                          'READ': '100011', 'PRINT': '100100'}

    def getInstCode(self, instcode):
        return self.inst_list[instcode]


myinst = Instruction()

print(myinst.getInstCode('STORE'))
