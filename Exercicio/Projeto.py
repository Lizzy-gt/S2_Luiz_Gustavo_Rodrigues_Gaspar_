# -*- coding: UTF-8 -*-
print ("Vamos ver a temperatura para Fahrenheit ou Celsius!")
cel = float(input("Fale a sua temperatura: "))
temp = input("Quer em Fahrenheit (F) ou Celsius (C)!")
def tempe ():
    global cel, fc
    if temp == "C" or temp == 'c':
        mult = 1.8 * cel + 32
        print(f"Sua calorias é %.2f"%mult)
    elif temp == "F" or temp == "f":
        mult = (cel - 32)/1.8
        print(f"Sua escola é %.2f"%mult)
tempe ()