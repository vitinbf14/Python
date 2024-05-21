n1 = float(input('Digite um número:'))
n2 = float(input('Digite outro número:'))
m = (n1+n2)/2
print('Sua média foi {:.1f}'.format(m))
if m >= 7.0:
    print('Parabens!! Você foi acima da média!')
else:
    print('Você foi abaixo da média, precisa estudar mais!')
