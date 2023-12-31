import os

# função que mostra o horário de partida que o cliente escolhe
def funcao_horario(hora):
    print("Sua saída está marcada para as " + hora, "horas! não se atrase!")

while (True):
    print("================================")
    print("ESCOLHA O TERMINAL QUE DESEJA: ")
    print("1 - Terminal De Paulo Afonso - Bahia")
    print("2 - Terminal de Glória - Bahia")
    print("3 - Terminal de Delmiro - Alagoas")
    print("=================================")

    terminal = int(input("Digite o terminal desejado: "))
    os.system('cls')
    break

while (True):
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

while (True):
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

# checagem de horário
while horario < 1 or horario > 4:
    os.system('cls')
    print("Horário inválido!, por favor, selecione apenas os horários disponiveis:")
    print("===========================")
    print("1 - 07:00h")
    print("2 - 10:00h")
    print("3 - 13:00h")
    print("4 - 15:00h")
    print("===========================")
    horario = int(input("DIGITE O HORÁRIO DESEJADO: "))

# Muda o toda a tragetória, valores, preços, e distância dependendo de qual terminal o cliente escolhe
# (não ficou muito bonito mas foi o único que funcionou)
if terminal == 1:
    from viagem_paulo_afonso import Viagem_Paulo_Afonso
    from viagem_paulo_afonso import Aracaju
    from viagem_paulo_afonso import Salvador
    from viagem_paulo_afonso import Recife
    from viagem_paulo_afonso import Petrolandia
    from viagem_paulo_afonso import Senhor_do_Bonfim
    from viagem_paulo_afonso import Garanhuns
    from viagem_paulo_afonso import Serra_Talhada
    from viagem_paulo_afonso import Floresta
    from viagem_paulo_afonso import Delmiro_Golveia
    from viagem_paulo_afonso import Arapiraca
elif terminal == 2:
    from viagem_glória import Viagem_Nossa_Senhora_Da_Gloria
    from viagem_glória import Aracaju
    from viagem_glória import Salvador
    from viagem_glória import Recife
    from viagem_glória import Petrolandia
    from viagem_glória import Senhor_do_Bonfim
    from viagem_glória import Garanhuns
    from viagem_glória import Serra_Talhada
    from viagem_glória import Floresta
    from viagem_glória import Delmiro_Golveia
    from viagem_glória import Arapiraca
elif terminal == 3:
    from viagem_delmiro import Viagem_Demiro
    from viagem_delmiro import Aracaju
    from viagem_delmiro import Salvador
    from viagem_delmiro import Recife
    from viagem_delmiro import Petrolandia
    from viagem_delmiro import Senhor_do_Bonfim
    from viagem_delmiro import Garanhuns
    from viagem_delmiro import Serra_Talhada
    from viagem_delmiro import Floresta
    from viagem_delmiro import Delmiro_Golveia
    from viagem_delmiro import Arapiraca
else:
    while terminal > 3 or terminal < 1:
        print("Número de terminal inválido! escolha somente os números disponíveis")
        print("================================")
        print("1 - Terminal De Paulo Afonso - Bahia")
        print("2 - Terminal de Glória - Bahia")
        print("3 - Terminal de Delmiro - Alagoas")
        print("=================================")
        terminal = int(input("Por favor, digite novamente o número desejado: "))

# O sistema em sí. (ta meio bagunçado mas n consegui pensar em nada melhor pra fzr tudo isso)
while (True):
    if escolha == 1:
        Aracaju.valor_passagem()
        Aracaju.sua_viagem()
        if horario == 1:
            funcao_horario("7:00")
        elif horario == 2:
            funcao_horario("10:00")
        elif horario == 3:
            funcao_horario("13:00")
        else:
            funcao_horario("15:00")
        break
    elif escolha == 2:
        Salvador.valor_passagem()
        Salvador.sua_viagem()
        if horario == 1:
            funcao_horario("7:00")
        elif horario == 2:
            funcao_horario("10:00")
        elif horario == 3:
            funcao_horario("13:00")
        else:
            funcao_horario("15:00")
        break
    elif escolha == 3:
        Recife.valor_passagem()
        Recife.sua_viagem()
        if horario == 1:
            funcao_horario("7:00")
        elif horario == 2:
            funcao_horario("10:00")
        elif horario == 3:
            funcao_horario("13:00")
        else:
            funcao_horario("15:00")
        break
    elif escolha == 4:
        Petrolandia.valor_passagem()
        Petrolandia.sua_viagem()
        if horario == 1:
            funcao_horario("7:00")
        elif horario == 2:
            funcao_horario("10:00")
        elif horario == 3:
            funcao_horario("13:00")
        else:
            funcao_horario("15:00")
        break
    elif escolha == 5:
        Senhor_do_Bonfim.valor_passagem()
        Senhor_do_Bonfim.sua_viagem()
        if horario == 1:
            funcao_horario("7:00")
        elif horario == 2:
            funcao_horario("10:00")
        elif horario == 3:
            funcao_horario("13:00")
        else:
            funcao_horario("15:00")
        break
    elif escolha == 6:
        Garanhuns.valor_passagem()
        Garanhuns.sua_viagem()
        if horario == 1:
            funcao_horario("7:00")
        elif horario == 2:
            funcao_horario("10:00")
        elif horario == 3:
            funcao_horario("13:00")
        else:
            funcao_horario("15:00")
        break
    elif escolha == 7:
        Serra_Talhada.valor_passagem()
        Serra_Talhada.sua_viagem()
        if horario == 1:
            funcao_horario("7:00")
        elif horario == 2:
            funcao_horario("10:00")
        elif horario == 3:
            funcao_horario("13:00")
        else:
            funcao_horario("15:00")
        break
    elif escolha == 8:
        Floresta.valor_passagem()
        Floresta.sua_viagem()
        if horario == 1:
            funcao_horario("7:00")
        elif horario == 2:
            funcao_horario("10:00")
        elif horario == 3:
            funcao_horario("13:00")
        else:
            funcao_horario("15:00")
        break
    elif escolha == 9:
        Delmiro_Golveia.valor_passagem()
        Delmiro_Golveia.sua_viagem()
        if horario == 1:
            funcao_horario("7:00")
        elif horario == 2:
            funcao_horario("10:00")
        elif horario == 3:
            funcao_horario("13:00")
        else:
            funcao_horario("15:00")
        break
    elif escolha == 10:
        Arapiraca.valor_passagem()
        Arapiraca.sua_viagem()
        if horario == 1:
            funcao_horario("7:00")
        elif horario == 2:
            funcao_horario("10:00")
        elif horario == 3:
            funcao_horario("13:00")
        else:
            funcao_horario("15:00")
        break
    #essa parte não era pra funcinar direito mas funciona e não sei nem como. (time que ta ganhando não mexe)
    while escolha not in (1, 10):
        print("Valor invalido! por favor digite apenas um dos números informados.")
        escolha = int(input("Digite novamente o numero de passagem desejado: "))
        if escolha == (1, 10):
            print("Número válido!")
        break
