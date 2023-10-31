class Viagem:
    def __init__(self, preco, tempo, distancia, destino):
        self.preco = preco
        self.tempo = tempo
        self.distancia = distancia
        self.destino = destino
    
    def sua_viagem(self):
        print("Você está viajando para", destino, "Distância da viagem". distancia, "Boa viagem!")
    def valor_passagem(self):
        print("Sua viagem para", destino, "custa", preco)
        
Aracaju = Viagem(preco= 80, tempo= 5, distancia= 281.1, destino="Aracaju")
Salvador = Viagem(preco= 90, tempo=8, distancia= 470.3, destino="Salvador")
Recife = Viagem(preco= 115, tempo=9, distancia= 447.4, destino="Recife")
Petrolandia = Viagem(preco= 50, tempo=2, distancia= 63.4, destino="Petrollândia")
Senhor_do_Bonfim = Viagem(preco=90, tempo= 5, distancia= 397.5, destino="Senhor do bomfim")
Garanhuns = Viagem(preco=100, tempo=6, distancia= 219.9, destino="Garanhuns")
Serra_Talhada = Viagem(preco=80, tempo=5, distancia= 214.1, destino="Serra Talhada")
Floresta = Viagem(preco=85, tempo=4, distancia= 98.2, destino="Floresta")
Delmiro_Golveia = Viagem(preco=40, tempo=1.30, distancia= 37.7, destino="Delmiro Golveia")
Arapiraca = Viagem(preco=70 , tempo=6, distancia= 203.6, destino="Arapiraca")
