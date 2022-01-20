def run():
    # for contador in range(1000):
    #     if contador % 2 !=0:
    #         continue
    #     print(contador)
    # for i in range(10000):
    #     print(i)
    #     if i == 5678:
    #         break
    # texto = input("ingrese un texto: ")
    # for letra in texto:
    #     if letra == "o":
    #         break
    #     print(letra)
    
    # texto = input("ingrese un texto: ")
    # contador = 0
    # while contador < len(texto):
    #     if texto[contador] == "o":
    #         break
    #     if texto[contador] == "i":
    #         continue
    #     print(texto[contador])
    #     contador += 1
    
    contador = 0
    edad = 1
    while contador < edad:
        edad = int(input("Ingrese la edad de la computadora, pista: esta entre el 1 y el 50: "))
        if edad == 14:
            print("Felicidades, adivinaste la edad")
            break
        if edad > 50:
            print("No puedes ingresar una edad mayor a 50")
        else:
            print("Intenta de nuevo")
        contador += 1
        
        

if __name__ == '__main__':
    run()