class Pilas():
    def __init__(self):
        self.Pila=[]

    def push(self, Valor):
        self.Pila.append(Valor)
    
    def pop(self):
        self.Pila.pop()

    def imprimir(self):
        for i in self.Pila:
            print(self.Pila) 

if __name__== "__main__":
    Pila=Pilas()

Pila.push(3)
Pila.push(4)
Pila.push(5)
Pila.imprimir()
Pila.pop()
Pila.imprimir()