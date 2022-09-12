frase = str(input('Digite uma frase qualquer: ')).upper()
print('A letra -A- aparece {} vezes na sua frase'.format(frase.count('A')))
print('Primeira ocorrencia da letra -A- na posicao {}'.format(frase.find('A')))
print('Ultima ocorrencia da letra -A- na posicao {}\n'.format(frase.rfind('A')))
