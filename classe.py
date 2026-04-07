#criação da clase aluno
class Aluno:
# definindo os atributos da classe aluno    
    def __init__(self, nome, idade, curso, notas):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.ra = ""
        self.notas = notas

#apresentando os atributos da classe aluno        
    def apresentar(self):
        print(f"olá, meu nome é {self.nome}, tenho {self.idade} anos, e faço o curso {self.curso} ") 
        if(self.ra == ""):
            print("esse aluno não tem r.a")
            self.ra = input("informe seu r.a : ")
        else:
            print(F"O R.A É : {self.ra}")
#metodo que calcula média do aluno
    def calcular_media(self):
        soma = 0.0
        for i in range(0, len(self.notas)):
            soma += self.notas[i]
        media = soma/len(self.notas)
        return media
#pedindo valores dos atributos da classe aluno
nome = input("qual é seu nome : ")
idade = input("qual é sua idade : ")
curso = input (" qual curso você está cursando : ")

#apresentando o aluno da classe Aluno
aluno1 = Aluno(nome, idade, curso, [7, 10, 8])
aluno1.apresentar()

aluno1.apresentar()
print(f"o nome do aluno é : {aluno1.nome}")
print(f" a média das notas é {aluno1.calcular_media()}")
