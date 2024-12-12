class Colas():
    def __init__(self):
        self.Cola=[]

    def push(self, Valor):
        self.Cola.append(Valor)
    
    def pop(self):
        if len(self.Cola) !=0:
            self.Cola.pop(0)   
        else:
            print("Lista vacia.")
    def imprimir(self):
        if len(self.Cola) !=0:
            for i in self.Cola:
                print(self.Cola) 
        else:
            print("Lista vacia.")
if __name__== "__main__":
    Cola=Colas()

Cola.imprimir()
Cola.pop()
Cola.push(3)
Cola.push(4)
Cola.push(5)
Cola.imprimir()
Cola.pop()
Cola.imprimir()
