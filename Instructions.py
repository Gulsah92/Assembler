class Instraction:
    def __init__(self):
        self.inst_list = {'HALT':'0001', 'LOAD': '0002', 'STORE': '0003'}

    def getInstCode(self,instcode):
        return self.inst_list[instcode]

myinst = Instraction()
print(myinst.getInstCode('STORE'))