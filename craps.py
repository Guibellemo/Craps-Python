import random
import sys

class Jogador:
    def __init__(self, nome):
        self.nome = nome

    def jogarDados(self):
        self.dado1 = random.randint(2,6)
        self.dado2 = random.randint(2,6)
        print(f'{self.nome} seus dados são: {self.dado1} e {self.dado2}')

    def faseUm(self):
        if self.dado1+self.dado2 == 7 or self.dado1+self.dado2 == 11:
            print('Você venceu!')
            sys.exit()
            
        elif self.dado1+self.dado2 == 2 or self.dado1+self.dado2 == 3 or self.dado1+self.dado2 == 12:
            print('Você perdeu')
            sys.exit()
            
        else:
            self.ponto = self.dado1+self.dado2
            print(self.ponto)
            


    def faseDois(self):
        while True and self.dado1 + self.dado2 != self.ponto or self.dado1 + self.dado2 != 7:

            self.dado1 = random.randint(2,12)
            self.dado2 = random.randint(2,12)
            print(f'Seus novos dados são: {self.dado1} e {self.dado2}')

            if self.dado1 + self.dado2 == self.ponto:
                print(f'Você tirou {self.dado1 + self.dado2} que é igual ao seu Ponto. Então você venceu!')
                break
            elif self.dado1 + self.dado2 == 7:
                print('Você tirou 7. Você perdeu!')
                break


nomeJogador = input('Digite seu nome: ')
j1 = Jogador(nomeJogador)
j1.jogarDados()
j1.faseUm()
j1.faseDois()