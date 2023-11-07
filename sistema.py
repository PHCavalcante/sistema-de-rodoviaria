import os
from viagem import Terminal
from viagem import Viagem_Paulo_Afonso
from viagem import Viagem_Demiro
from viagem import Viagem_Gloria
from viagem import Aracaju
from viagem import Salvador
from viagem import Recife
from viagem import Petrolandia
from viagem import Senhor_do_Bonfim
from viagem import Garanhuns
from viagem import Serra_Talhada
from viagem import Floresta
from viagem import Delmiro_Golveia
from viagem import Arapiraca

def funcao_horario(hora):
    print("Sua saída está marcada para as" + hora, "horas! não se atrase!")

while(True):
    
    print("================================")
    print("ESCOLHA O TERMINAL QUE DESEJA: ")
    print("1 - Terminal De Paulo Afonso - Bahia")
    print("2 - Terminal de Glória - Bahia")
    print("3 - Terminal de Delmiro - Alagoas")
    print("=================================")

    terminal = int(input("Digite o terminal desejado: "))
    os.system('cls')
    break
    
while(True):
    print("=========================")
    print("ESCOLHA O SEU DESTINO:")
    print("1 - Aracaju - 80$$")
    print("2 - Salvador - 90$")
    print("3 - Recife - 115$")
    print("4 - Petrolândia - 50$")
    print("5 - Senhor do bomfim - 90$")
    print("6 - Garanhuns - 100$")
    print("7 - Serra Talhada - 80$")
    print("8 - Floresta - 85$")
    print("9 - Delmiro Golveia 40$")
    print(" 10 - Arapiraca - 70$")
    print("=========================")

    escolha = int(input("Digite o número do seu destino: "))
    os.system('cls')
    break

while(True):

    print("===========================")
    print("DIGITE O HORÁRIO DESEJADO: ")
    print("1 - 07:00h")
    print("2 - 10:00h")
    print("3 - 13:00h")
    print("4 - 15:00h")
    print("===========================")

    horario = int(input("Digite o horário de partida desejado: "))
    os.system('cls')
    break

while (True):
    if escolha == 1:
        Aracaju.valor_passagem()
        Aracaju.sua_viagem()
        if horario == 1:
            funcao_horario(7)
        elif horario == 2:
            print("S")
        break
    elif escolha == 2:
        Salvador.valor_passagem()
        Salvador.sua_viagem()
        break
    elif escolha == 3:
        Recife.valor_passagem()
        Recife.sua_viagem()
        break
    elif escolha == 4:
        Petrolandia.valor_passagem()
        Petrolandia.sua_viagem()
        break
    elif escolha == 5:
        Senhor_do_Bonfim.valor_passagem()
        Senhor_do_Bonfim.sua_viagem()
        break
    elif escolha == 6:
        Garanhuns.valor_passagem()
        Garanhuns.sua_viagem()
        break
    elif escolha == 7:
        Serra_Talhada.valor_passagem()
        Serra_Talhada.sua_viagem()
        break
    elif escolha == 8:
        Floresta.valor_passagem()
        Floresta.sua_viagem()
        break
    elif escolha == 9:
        Delmiro_Golveia.valor_passagem()
        Delmiro_Golveia.sua_viagem()
        break
    elif escolha == 10:
        Arapiraca.valor_passagem()
        Arapiraca.sua_viagem()
        break
    while escolha not in(1,10):
        print("Valor invalido! por favor digite apenas um dos números informados.")
        escolha = int(input("Digite novamente o numero de passagem desejado: "))
        if escolha == (1, 10):
            print("Número válido!")
        break