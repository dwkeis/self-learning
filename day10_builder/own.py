"""some codes inspired by online sample, yet i think there's a more simple way to access"""

class Director:
    __builder = None
    def setBuilder(self,builder):
        self.__builder = builder
    def getMac(self):
        mac = Mac()
        cpu = self.__builder.getCPU()
        mac.setCPU(cpu)
        ram = self.__builder.getRAM()
        mac.setRAM(ram)
        gpu = self.__builder.getGPU()
        mac.setGPU(gpu)
        return mac

class Mac:
    def __init__(self):
        self.__cpu = None
        self.__ram = None
        self.__gpu = None
    def setCPU(self,cpu):
        self.__cpu = cpu
    def setRAM(self,ram):
        self.__ram = ram
    def setGPU(self,gpu):
        self.__gpu = gpu
    def spec(self):
        print("CPU : %s"%self.__cpu.name)
        print("RAM : %s"%self.__ram.name)
        print("GPU : %s"%self.__gpu.name)

class Builder:
    def getCPU(self): pass
    def getRAM(self): pass
    def getGPU(self): pass

class Mac2018(Builder):
    def getCPU(self):
        cpu = CPU()
        cpu.name = "i7 8700"
        return cpu
    def getRAM(self):
        ram = RAM()
        ram.name = "16GB"
        return ram
    def getGPU(self):
        gpu = GPU()
        gpu.name = "2080"
        return gpu

class CPU:
    cpu = None
class RAM:
    ram = None
class GPU:
    gpu = None

if __name__ == "__main__":
    mac2018 = Mac2018()
    director = Director()
    print("Mac2018 spec :")
    director.setBuilder(mac2018)
    mac = director.getMac()
    mac.spec()
    print("")
