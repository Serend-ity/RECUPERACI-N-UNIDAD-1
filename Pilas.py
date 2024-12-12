class Pilas():
    def __init__(self):
        self.Pila=[]

    def push(self, Valor):
        self.Pila.append(Valor)
    
    def pop(self):
        if len(self.Pila ) !=0:
            self.Pila.pop()
        else:
            print ("Lista vacia.")

    def imprimir(self):
        if len(self.Pila ) !=0:
            for i in self.Pila:
                print(self.Pila) 
        else:
            print ("Lista vacia.")
if __name__== "__main__":
    Pila=Pilas()

Pila.imprimir()
Pila.pop()
Pila.push(3)
Pila.push(4)
Pila.push(5)
Pila.imprimir()
Pila.pop()
Pila.imprimir()
