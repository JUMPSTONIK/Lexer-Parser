TYPEVALUES = dict
TYPEVALUES = {
    "int" : 4,
    "char" : 2,
    "boolean" : 1
}
TYPEINITVALUE = {
    "int" : 0,
    "char" : "",
    "boolean" : False
}

class Metodos():
    def __init__(self):
        self.nombre = ""
        self.tipo = ""
        self.ambito = ""
        self.params = []
        self.offset = 0

    def showValues(self):
        print(self.nombre+ "\n" + self.tipo + "\n" + self.ambito + str(self.params) + "\n")


class Variables():
    def __init__(self):
        self.nombre = ""
        self.tipo = ""
        self.ambito = ""
        self.offset = 0
        self.size = 0
        self.value = None

    def showValues(self):
        if self.size == 0:
            print("nombre: " + self.nombre+ "\n" + "tipo:   " + self.tipo + "\n" + "ambito: "+str(self.ambito) + "\n" + "offset: " + str(self.offset) + "\n" + "value:  " + str(self.value) + "\n")
        else:
            print("nombre: " + self.nombre+ "\n" + "tipo:   " + self.tipo + "\n" + "ambito: "+str(self.ambito) + "\n" + "offset: " + str(self.offset) + "\n" + "value:  " +str(self.value) + "\n" + str(self.size) + "\n")
    
    def setOffset(self):
        if self.size != 0:
            self.offset = TYPEVALUES[self.tipo] * self.size
            self.value = TYPEINITVALUE[self.tipo]
        if self.size == 0 and "struct" not in self.tipo:
            self.offset = TYPEVALUES[self.tipo]
            self.value = TYPEINITVALUE[self.tipo]
            
class Structs():
    def __init__(self):
        self.nombre = ""
        self.ambito = "global"
        self.offset = 0
        self.variables = []

    def showVariables(self):
        print("-------------")
        print("Struct variables\n")
        for item in self.variables:
            item.showValues()

    def showValues(self):
        print("nombre: " + self.nombre+ "\n" + "ambito: "+str(self.ambito) + "\n" + "offset: " + str(self.offset) + "\n")
            