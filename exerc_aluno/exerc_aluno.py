class Aluno:
    def __init__(self,nome,n1,n2):
        self.n1=n1
        self.n2=n2
    def calculomedia (self):
        return (self.n1+self.n2)/2
    def passou (self):
        return "Aprovado" if self.calculomedia() >=7 else "Reprovado"
     
        
    