dias = int(input('Quantos dias alugados ?')) #aluguel de carro
km = float(input('Quantos km rodados ?'))
total = (dias * 60) + (km * 0.15)
print('o total a pagar R$ {:.2f}'.format(total)) #pagar por km rodado e diaria
