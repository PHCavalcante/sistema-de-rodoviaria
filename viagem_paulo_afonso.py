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
