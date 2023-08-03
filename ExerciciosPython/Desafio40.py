nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f} a média do aluno é {:.1f}'.format(nota1, nota2, media))
if media < 5:
    print('O aluno foi REPROVADO!')
elif media > 5 and media <= 7:
    print('O Aluno está de RECUPERAÇÃO!')
elif media >= 7:
    print('O Aluno foi APROVADO!') 
    

