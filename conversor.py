def conversor(tipo_pesos, valor_dolar):
    pesos = input('¿Cuantos pesos ' + tipo_pesos + ' colombianos tienes?: ')
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' dolares')

menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opcion: """

opcion = int(input(menu)) #Estoy haciendo que al usuario le muestre el mensaje de menu y lo que escriba como respuesta sera un input que se guardara en opcion

if opcion == 1:
    conversor('colombianos', 3875)
elif opcion == 2:
    conversor('argentinos', 65)
elif opcion == 3:
    conversor('mexicanos', 24)
else:
    print('Elige una opcion correcta, por favor')

