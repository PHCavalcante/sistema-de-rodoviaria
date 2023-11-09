class Viagem_Nossa_Senhora_Da_Gloria:
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