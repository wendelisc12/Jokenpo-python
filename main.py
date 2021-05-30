import random

class Player:
    def __init__ (self, escolhaPlayer):
        self.escolhaPlayer = escolhaPlayer
    
    def pedra(self, iaEscolha):
        if iaEscolha == "papel":
            print("Você perdeu")
        elif iaEscolha == "pedra":
            print("Deu empate")
        elif iaEscolha == "tesoura":
            print("Você ganhou")

    def papel(self, iaEscolha):
        if iaEscolha == "papel":
            print("Deu empate")
        elif iaEscolha == "pedra":
            print("Você ganhou")
        elif iaEscolha == "tesoura":
            print("Você perdeu")

    def tesoura(self, iaEscolha):
        if iaEscolha == "papel":
            print("Você ganhou")
        elif iaEscolha == "pedra":
            print("Você perdeu")
        elif iaEscolha == "tesoura":
            print("Deu empate")
    
    def outraOpcao(self):
        print("Escolha uma opção válida")

ia= ["pedra", "papel", "tesoura"]

while(True):
    print(' ')
    print("---------------[ JOKENPO ]---------------")
    escolhaPlayer = input("Escolha entre pedra, papel ou tesoura (escreva sair para sair): ")
    player = Player(escolhaPlayer)
    print('-'*40)
    print(' ')
    
    if escolhaPlayer != 'pedra' and escolhaPlayer != 'papel' and escolhaPlayer != 'tesoura' and escolhaPlayer != 'sair':
        player.outraOpcao()
    else:
        if escolhaPlayer == 'sair':
            break
        else:
            iaEscolhe = random.choice(ia)
            print("O robô escolheu {} e você escolheu {}".format(iaEscolhe, escolhaPlayer))

            if escolhaPlayer == 'pedra':
                player.pedra(iaEscolhe)
            elif escolhaPlayer == 'papel':
                player.papel(iaEscolhe)
            elif escolhaPlayer == 'tesoura':
                player.tesoura(iaEscolhe)

