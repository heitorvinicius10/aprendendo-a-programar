# Autor: Heitor Vinicius

# função: nomedafuncao()

#duais função: função(função("tal tal tal"))

#abaixo de 5 é insuficiente
#de 5 a 7 o conceito é regular
#de 7 a 9 o conceito é bom
#de 9 a 10 o conceito e excelente

print("Media de alunos")
prova1 = float(input("digite a primeira nota: "))
prova2 = float(input("digite a segunda nota: "))
prova3 = float(input("digite a terceira nota: "))
prova4 = float(input("digite a quarta nota: "))

somadasnotas = prova1+prova2+prova3+prova4
media = somadasnotas/4

if media>=5:
    if  media<7:
        print("seu conceito é regular")
    else:
        if media<9:
            print("seu conceito é bom")
        else:
            print("seu conceito é excelente")       
    print("voce foi aprovado,inteligente da professora")
else:
    print("seu conceito é insuficiente")
    print("voce foi reprovado")
    
print("a media é: ", media)