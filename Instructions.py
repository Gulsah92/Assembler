class Instraction:
    def __init__(self):
        self.inst_list = {'HALT':'0001', 'LOAD': '0002', 'STORE': '0003', 'ADD': '0004', 'SUB': '0005', 'INC': '0006',
                          'DEC': '0007', 'MUL': '0008', 'DIV': '0009', 'XOR': '000A'}

    def getInstCode(self,instcode):
        return self.inst_list[instcode]

myinst = Instraction()
print(myinst.getInstCode('STORE'))