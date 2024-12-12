class Colas():
    def __init__(self):
        self.Cola=[]

    def push(self, Valor):
        self.Cola.append(Valor)
    
    def pop(self):
        self.Cola.pop(0)   

    def imprimir(self):
        for i in self.Cola:
            print(self.Cola) 

if __name__== "__main__":
    Cola=Colas()

Cola.push(3)
Cola.push(4)
Cola.push(5)
Cola.imprimir()
Cola.pop()
Cola.imprimir()