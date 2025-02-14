def funcao_borda_traço_cruz (nome):
    tamanho_borda = len(nome)
    if tamanho_borda: # Se o "tamanho_borda" for verdadeiro, ou seja, se ele tem algum caracter dentro dele, faça o que tem abaixo.
        print('+', '-' * tamanho_borda, '+')
        print('|', nome, '|')
        print('+', '-' * tamanho_borda, '+')

funcao_borda_traço_cruz('Olá, mundo!')