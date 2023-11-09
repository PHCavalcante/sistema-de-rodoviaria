class Viagem_Demiro:

    def __init__(self, preco, tempo, distancia, destino):
        self.preco = preco
        self.tempo = tempo
        self.distancia = distancia
        self.destino = destino

    def sua_viagem(self):
        print(f"Você está viajando para", self.destino + "!", "Distância da viagem",
              self.distancia + "Km"", " "tempo da viagem", self.tempo, "horas"",", "Boa viagem!")

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
