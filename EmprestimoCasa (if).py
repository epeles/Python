casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual é o seu salário? '))
anos = int(input('Em qts anos vc ira pagar? '))
prestacao = (casa / (anos*12))
porcent = salario * 0.3
if prestacao > porcent:
    print('Seu empréstimo foi negado (Excedeu 30% do seu salário)!')
else:
    print(f'Seu empréstimo foi aprovado! Serão pagos R$ {prestacao:.2f} em {anos*12} meses)
