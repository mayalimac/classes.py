#Crie uma classe de sua preferência com, no mínimo, uma variável, um método e um incremento. 
#Depois, desenvolva três ou mais objetos para testar o código.

from typing_extensions import Self


class Professor:

    def __init__(self,nome, sexo, idade, materia):
        self.nome = nome
        self.sexo = sexo
        self.idade = idade
        self.materia = materia

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
    

if __name__ == "__main__":
    prof1 = Professor("Inácio", "32 anos", "M" "História",True)
    print(prof1.nome)

    def get_idade(self):
     return self.__idade
     
     def set_idade(self, idade):
        self.__idade = idade
if Self.idade > 22 +1: 
	print("Você é o professor mais novo da escola")

