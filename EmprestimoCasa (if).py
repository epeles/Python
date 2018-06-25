casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o seu salário? '))
anos = int(input('Em qts anos vc ira pagar? '))
prestacao = (casa / (anos*12))
porcent = salario * 0.3
#print('O valor da casa é de R$ {} que será quitado em {} meses. Valor de cada mês: R$ {:.2f}'.format(casa,anos*12,prestacao))
if prestacao > porcent:
    print('Seu empréstimo foi negado (Excedeu 30% do seu salário)!')
else:
    print('Seu empréstimo foi aprovado! Serão pagos R$ {:.2f} em {} meses'.format(prestacao,anos*12))