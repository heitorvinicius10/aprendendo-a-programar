# Autor: Heitor Vinicius

print("Novo Exercicio")

print("Maior ou menor")

numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))

if (numero1 < numero2): #falso
    print("o maior numero é: ", numero2)
    
else:
    if (numero1 == numero2): #falso
        print("os numeros sao iguais")
        
    else:
        print("o maior numero é: ", numero1)