def funcao_ordem_crescente_para_3(var_valor_1=0, var_valor_2=0, var_valor_3=0):
    if (var_valor_1 < var_valor_2 and var_valor_1 < var_valor_3) and (var_valor_2 < var_valor_3):
        print(f'Ordem crescente: {var_valor_1}, {var_valor_2}, {var_valor_3}')

    elif (var_valor_1 < var_valor_2 and var_valor_1 < var_valor_3) and (var_valor_3 < var_valor_2):
        print(f'Ordem crescente: {var_valor_1}, {var_valor_3}, {var_valor_2}')

    elif (var_valor_2 < var_valor_1 and var_valor_2 < var_valor_3) and (var_valor_1 < var_valor_3):
        print(f'Ordem crescente: {var_valor_2}, {var_valor_1}, {var_valor_3}')

    elif (var_valor_2 < var_valor_1 and var_valor_2 < var_valor_3) and (var_valor_3 < var_valor_1):
        print(f'Ordem crescente: {var_valor_2}, {var_valor_3}, {var_valor_1}')

    elif (var_valor_3 < var_valor_1 and var_valor_3 < var_valor_2) and (var_valor_1 < var_valor_2):
        print(f'Ordem crescente: {var_valor_3}, {var_valor_1}, {var_valor_2}')

    elif (var_valor_3 < var_valor_1 and var_valor_3 < var_valor_2) and (var_valor_2 < var_valor_1):
        print(f'Ordem crescente: {var_valor_3}, {var_valor_2}, {var_valor_1}')

    elif var_valor_1 == var_valor_2 == var_valor_3:
        print(f'Ordem crescente: {var_valor_3}, {var_valor_2}, {var_valor_1}')

    elif var_valor_1 == var_valor_2:
        if var_valor_1 > var_valor_3:
            print(f'Ordem crescente: {var_valor_3}, {var_valor_2}, {var_valor_1}')
        else:
            print(f'Ordem crescente: {var_valor_1}, {var_valor_2}, {var_valor_3}')

    elif var_valor_3 == var_valor_2:
        if var_valor_2 > var_valor_1:
            print(f'Ordem crescente: {var_valor_1}, {var_valor_2}, {var_valor_3}')
        else:
            print(f'Ordem crescente: {var_valor_3}, {var_valor_2}, {var_valor_1}')

    elif var_valor_3 == var_valor_1:
        if var_valor_1 > var_valor_2:
            print(f'Ordem crescente: {var_valor_2}, {var_valor_3}, {var_valor_1}')
        else:
            print(f'Ordem crescente: {var_valor_1}, {var_valor_3}, {var_valor_2}')


var_valor_1 = int(input('Digite o valor 1: '))
var_valor_2 = int(input('Digite o valor 2: '))
var_valor_3 = int(input('Digite o valor 3: '))
funcao_ordem_crescente_para_3(var_valor_1, var_valor_2, var_valor_3)