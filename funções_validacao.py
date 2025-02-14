def funcao_validacao_numero_int_positivo():
    numero = int(input('Digite um valor inteiro e positivo: '))
    while numero < 0:
        print('Resposta inválida.')
        numero = int(input('Digite um valor inteiro e positivo: '))
    return numero