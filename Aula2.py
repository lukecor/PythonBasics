a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))


soma = a + b
subtracao = a l- b
multiplicacao = a * b
divisao = a / b
resto = a % b

print('soma: ' + str(soma))
print('subtração: ' + str(subtracao))
print('multiplicação: ' + str(multiplicacao))
print('Divisão: ' + str(divisao))
print('divisão sem fração: ' + str(int(divisao)))
print('Resto: ' + str(resto))


print('soma: {}'.format(soma))

print('soma: {soma}. \nsubtração: {subtracao}.'
      f'\nmultiplicação: {multiplicacao} '
      f'\ndivisao: {divisao}'
      f'\nresto: {resto}'.format(soma=soma,
                                  subtracao=subtracao,
                                  multiplicacao=multiplicacao,
                                  divisao=divisao,
                                  resto=resto))
