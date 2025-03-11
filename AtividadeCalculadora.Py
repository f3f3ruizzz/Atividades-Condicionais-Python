import os 

os.system("cls")

print('''
█▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ █▀▄ █▀█ █▀█ ▄▀█
█▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ █▄▀ █▄█ █▀▄ █▀█''')

valor01 = int (input ("Digite o primeiro número: "))
valor02 = int (input("Digite o segundo número: "))
operação = input("Digite a operação: ")

if (operação == "+"):
    resultado = valor01 + valor02
    print("Será realizada a soma de dois valores")

elif (operação =="-"):
    resultado = valor01 - valor02
    print("Será realizada a subtração de dois valores")

elif (operação == "*"):
    resultado = valor01 * valor02
    print("Será realizado a multiplicação dos valores")

elif (operação == "/"): 
    resultado = valor01 / valor02
    print("Será realizado a divisão de dois números")

print("O resultado foi: " , resultado) 