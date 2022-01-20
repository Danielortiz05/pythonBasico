menu = """
Bienvenido al conversor de monedas 🤑

1. Pesos colombianos a dolares
2. Pesos argentinos a dolares
3. Pesos mexicanos a dolares

Elige una opción: """
def conversor(mensaje, valor_dolar):
    pesos_colombianos = float(input("¿Cuántos pesos" +" "+ mensaje + " "+"tienes?:"))
    dolares = pesos_colombianos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Usted tiene $" + dolares + " dólares")

seleccion = int(input(menu))

if seleccion == 1:
    conversor("colombianos", 3877.50)
    
elif seleccion == 2:
    conversor("argentinos", 100.14)
    
elif seleccion == 3:
    conversor("mexicanos", 20.64)
else:
    print("Opción inválida")







