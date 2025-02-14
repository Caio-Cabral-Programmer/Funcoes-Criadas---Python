def funcao_validacao_numero_int_positivo():
    numero = int(input('Digite um valor para calcular a fatorial: '))
    while numero < 0:
        numero = int(input('Digite um valor para calcular a fatorial: '))
    return numero

def funcao_fatorial(numero):
    resultado_fatorial = 1
    if numero == 0:
        return resultado_fatorial # O "return" já encerra a função e volta para o programa principal.
    else: # esta parte do código só será executada caso num > 0
        for i in range(1, numero + 1, 1):
            resultado_fatorial *= i
        return resultado_fatorial

#Programa principal
var_numero = funcao_validacao_numero_int_positivo()
print(f'A fatorial do número {var_numero} é = {funcao_fatorial(var_numero)}.')
print(f'{var_numero}! = {funcao_fatorial(var_numero)}.') # Outro modo de escrever.