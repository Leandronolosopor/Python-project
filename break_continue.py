from socket import NI_NUMERICHOST


def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range (10000):
    #     print(i)
    #     if i == 5578:
    #         break

    # texto = input('Escribe un texto: ')
    # for letra in texto:
    #     if letra == 'o':
    #         break
    #     print(letra)

    numeros = 1
    while numeros < 101:
        numeros += 1
        print (numeros)
        if numeros == 98:
            break

    # Esto no anda
    # numeros = range (1, 100)
    # while numeros:
    #     print (numeros)
    #     if numeros == range(98):
    #         break


if __name__ == '__main__':
    run()