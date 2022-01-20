import random 


def run():
    vidas = 10
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("Adivina un número de 1 hasta 100: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Busca un número mayor")
            vidas += -1   
        else: 
            print("Busca un número menor")
            vidas += -1
        print("Tus vidas " + str(vidas)+ " sige intentando")
        numero_elegido = int(input("Elige otro número: "))


        if  numero_elegido == numero_aleatorio:
            print("Adivinaste el número")
            break
        
        
        if vidas == 1:
            print("Perdiste")
            break
        
    


if __name__ == "__main__":
    run()   