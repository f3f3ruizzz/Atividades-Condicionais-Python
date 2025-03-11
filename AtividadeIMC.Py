import os

os.system("cls") 

print('''
██╗███╗░░░███╗░█████╗░
██║████╗░████║██╔══██╗
██║██╔████╔██║██║░░╚═╝
██║██║╚██╔╝██║██║░░██╗
██║██║░╚═╝░██║╚█████╔╝
╚═╝╚═╝░░░░░╚═╝░╚════╝░''')

nome = input("Digite o seu nome: ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

imc = peso / altura 

if (imc <= 16): 
  print("Você está muito abaixo do peso")

elif (imc >= 17 and 18.4):
  print("Abaixo do peso")

elif (imc >= 18.5 and 24.9):
  print("Você tem um peso normal.")

elif (imc >= 24.9 and 29.9):
  print("Você está acima do peso.")

elif (imc >= 29.9 and 34.9):
  print("Você está com obesidade nível 1.")

elif (imc >= 34.9 and 40):
  print("Você está com obesidade nível 2.")

elif (imc > 40): 
  print("Você está com obesidade nível 3.")

  print("O seu IMC é de: " , imc)