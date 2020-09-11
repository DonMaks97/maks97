# adivinador   
import random

print("hola como te llamas")
nombrePlayer = input()

intentos = 0

numero = random.randint(1,50)
print("Hola, " + nombrePlayer + " estoy penando un numero entre 1 y 50, tienes 6 intentos")

while intentos < 7:
    print("Intenta adivinar:")
    adivinacion = input()
    adivinacion = int(adivinacion)

    intentos = intentos + 1

    if adivinacion < numero:
        print("Tu estimacion es muy baja")

    if adivinacion > numero:
        print("Tu estimacion es muy alta")

    if adivinacion == numero:
        break

if adivinacion == numero:
    intentos = str(intentos)
    print("Felicidades, " + nombrePlayer + "adivinaste en " + intentos + "intentos")

if adivinacion != numero:
    numero = str(numero)
    print("Que mal, el numero era, " + numero)

