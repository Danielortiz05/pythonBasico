def run():
    mi_diccionario = {
        'llave1' : 1,
        'llave2' : 2,
        'llave3' : 3,
    }
    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    poblacion_paises = {
        "argentina": 45_195_777,
        "brasil": 212_216_052,
        "colombia": 51_049_498
    }

    # print(poblacion_paises['colombia'])

    # for pais in poblacion_paises.keys():
    #     print(pais)


    # for poblacion in poblacion_paises.values():
    #     print(poblacion)


    for pais, poblacion in poblacion_paises.items():
        print("La poblacion de " + pais + " es: "+ str(poblacion) +".")

if __name__ == '__main__':
    run()