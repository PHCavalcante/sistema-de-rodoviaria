class Viagem_Paulo_Afonso:
    def __init__(self, preco, tempo, distancia, destino):
        self.preco = preco
        self.tempo = tempo
        self.distancia = distancia
        self.destino = destino
    
    def sua_viagem(self):
        print(f"Você está viajando para", self.destino + "!", "Distância da viagem", self.distancia + "Km"", " "tempo da viagem", self.tempo, "horas"",", "Boa viagem!")
    def valor_passagem(self):
        print(f"Sua passagem para", self.destino, "custa", self.preco + "$")

Aracaju = Viagem_Paulo_Afonso("80", "6", "281.1", "Aracaju")
Salvador = Viagem_Paulo_Afonso("90", "8", "470.3", "Salvador")
Recife = Viagem_Paulo_Afonso("115", "9", "447.4", "Recife")
Petrolandia = Viagem_Paulo_Afonso("50", "2", "63.4", "Petrolândia")
Senhor_do_Bonfim = Viagem_Paulo_Afonso("90", "5", "397.5", "Senhor do bomfim")
Garanhuns = Viagem_Paulo_Afonso("100", "6", "219.9", "Garanhuns")
Serra_Talhada = Viagem_Paulo_Afonso("80", "5", "214.1", "Serra Talhada")
Floresta = Viagem_Paulo_Afonso("85", "4", "98.2", "Floresta")
Delmiro_Golveia = Viagem_Paulo_Afonso("40", "1.30", "37.7", "Delmiro Golveia")
Arapiraca = Viagem_Paulo_Afonso("70", "6", "203.6", "Arapiraca")

""""
class Viagem_Nossa_Senhora_Da_Gloria:
    def __init__(self, preco, tempo, distancia, destino):
        self.preco = preco
        self.tempo = tempo
        self.distancia = distancia
        self.destino = destino
    
    def sua_viagem(self):
        print(f"Você está viajando para", self.destino + "!", "Distância da viagem", self.distancia + "Km"", " "tempo da viagem", self.tempo, "horas"",", "Boa viagem!")
    def valor_passagem(self):
        print(f"Sua passagem para", self.destino, "custa", self.preco + "$")

Aracaju = Viagem_Nossa_Senhora_Da_Gloria("80", "6", "117", "Aracaju")
Salvador = Viagem_Nossa_Senhora_Da_Gloria("90", "8", "424", "Salvador")
Recife = Viagem_Nossa_Senhora_Da_Gloria("115", "9", "493", "Recife")
Petrolandia = Viagem_Nossa_Senhora_Da_Gloria("50", "2", "202", "Petrolândia")
Senhor_do_Bonfim = Viagem_Nossa_Senhora_Da_Gloria("90", "5", "437", "Senhor do bomfim")
Garanhuns = Viagem_Nossa_Senhora_Da_Gloria("100", "6", "256", "Garanhuns")
Serra_Talhada = Viagem_Nossa_Senhora_Da_Gloria("80", "5", "359", "Serra Talhada")
Floresta = Viagem_Nossa_Senhora_Da_Gloria("85", "4", "268", "Floresta")
Delmiro_Golveia = Viagem_Nossa_Senhora_Da_Gloria("40", "1.30", "128", "Delmiro Golveia")
Arapiraca = Viagem_Nossa_Senhora_Da_Gloria("70", "6", "163", "Arapiraca")

class Viagem_Demiro:

    def __init__(self, preco, tempo, distancia, destino):
        self.preco = preco
        self.tempo = tempo
        self.distancia = distancia
        self.destino = destino
    
    def sua_viagem(self):
        print(f"Você está viajando para", self.destino + "!", "Distância da viagem", self.distancia + "Km"", " "tempo da viagem", self.tempo, "horas"",", "Boa viagem!")
    def valor_passagem(self):
        print(f"Sua passagem para", self.destino, "custa", self.preco + "$")

Aracaju = Viagem_Demiro("80", "6", "245", "Aracaju")
Salvador = Viagem_Demiro("90", "8", "486", "Salvador")
Recife = Viagem_Demiro("115", "9", "415", "Recife")
Petrolandia = Viagem_Demiro("50", "2", "75.9", "Petrolândia")
Senhor_do_Bonfim = Viagem_Demiro("90", "5", "414", "Senhor do bomfim")
Garanhuns = Viagem_Demiro("100", "6", "188", "Garanhuns")
Serra_Talhada = Viagem_Demiro("80", "5", "233", "Serra Talhada")
Floresta = Viagem_Demiro("85", "4", "141", "Floresta")
Delmiro_Golveia = Viagem_Demiro("40", "1.30", "0", "Delmiro Golveia")
Arapiraca = Viagem_Demiro("70", "6", "165", "Arapiraca")

class Terminal:
    def __init__(self, terminal):
        self.terminal = terminal 

    def Seu_terminal(self):
        print(f"Você escolheu o terminal de", self.terminal)
"""
