import os

os.system("cls")

print('''ℙ𝕣𝕠𝕗𝕖𝕤𝕤𝕠𝕣''')

professor = (input("Digite o seu nome: "))
quantidade = int(input("Digite a quantidade de aulas: "))
nivel = input("Digite o nível em que você está: ")

salario = quantidade * nivel 

if    nivel == 1:
  salario = quantidade * 12
  
elif  nivel == 2:
  salario = quantidade * 17
 
else: 
  salario = quantidade * 25

print("O seu salário foi de: ", salario)
