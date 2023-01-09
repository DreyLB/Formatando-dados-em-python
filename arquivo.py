import csv


def abrir_leitura(caminho):
    with open(caminho, 'r') as arquivo:
        abrir = csv.reader(arquivo)
        dados = list(abrir)
        arquivo.close()
        return dados


def escrever_bd(nome_banco, dados):
    tamanho = len(dados)
    with open(nome_banco, 'w+') as arquivo:
        for c in range(1, tamanho - 1):
            arquivo.write('\n')
            for i in range(4):
                arquivo.write(f'{dados[0][i]}: {dados[c][i]}\n')
        arquivo.close()


def adicionar_pessoa(nome_bd_para_editar, nome, posicao, departamento, salario):
    with open(nome_bd_para_editar, 'a+') as arquivo:
        arquivo.write(f'\nName: {nome}')
        arquivo.write(f'\nPosition Title: {posicao}')
        arquivo.write(f'\nDepartment: {departamento}')
        arquivo.write(f'\nEmployee Annual Salary: ${salario}\n')
        arquivo.close()


caminho = 'E:\VS Code Python\Manipulação de Arquivos\salarios.txt'
dados = abrir_leitura(caminho)
nome_banco = 'Dados.txt'

escrever_bd(nome_banco, dados)
adc = input('Deseja adicionar mais dados?[Sim]/[Não]').upper()
if adc == 'SIM':
    nome = input('Nome: ')
    posicao = input('Posição: ')
    departamento = input('Departamento')
    salario = input('Salário: ')
    adicionar_pessoa(nome_banco, nome, posicao, departamento, salario)
else:
    print('Fim da operação')
