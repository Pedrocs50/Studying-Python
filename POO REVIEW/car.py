class Carro:
    def __init__(self, marca, modelo, ano):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        
    def __str__(self):
        return f"-Marca: {self._marca}\n-Modelo: {self._modelo}\nAno: {self._ano}"
    

def main():
    carros = []
    qtt_car = int(input("Quantos carros você quer adicionar? "))
    for i in range(qtt_car):
        car_marca = input(f"Qual a marca do seu {i+1}° carro: ")
        car_modelo = input(f"Qual o modelo do seu {i+1}° carro: ")
        car_ano = input(f"Qual o ano do seu {i+1}° carro: ")
        carro = Carro(car_marca, car_modelo, car_ano)
        carros.append(carro)

    for i, carro in enumerate(carros):  
        print(f"CARRO {i+1}")
        print(carro)

main()
