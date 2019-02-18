#Função de criptografia seguindo a Cifra de César, com chave de troca de valor 4
#Autor: Carla Lutz Dias - data: 17/02/2019

def criptografa (frase,codigo):
    resultado = ''
    tamanho = len(frase)
    i = 0
    for i in range (tamanho):
        letra = frase[i]
        resultado += codigo[letra]
        i += 1
    print (resultado)
    return resultado

def descriptografa(frase,codigo):
    resultado = ''
    tamanho = len(frase)
    i = 0
    for i in range (tamanho):
        letra = frase[i]
        for k,v in codigo.items():
            if letra == v:
                resultado += k
    print (resultado)
    return resultado

#dicionário a ser utilizado como base para efetuar as trocas     
codigo = {'A':'E' , 'B':'F', 'C':'G', 'D':'H', 'E':'I', 'F':'J', 'G':'K',
'H':'L', 'I':'M', 'J':'N', 'K':'O', 'L':'P', 'M':'Q', 'N':'R', 'O':'S',
'P':'T', 'Q':'U', 'R':'V', 'S':'W', 'T':'X', 'U':'Y', 'V':'Z',
'W':'A', 'X':'B', 'Y':'C', 'Z':'D', ' ':' '}

#Capta a entrada do usuário, dando a opção de criptografar ou descriptografar
opcao = ''
while opcao != '1' or opcao != '2':
    opcao = input("Digite 1 para criptografar ou 2 para descriptografar: ")
    if opcao == '1' or opcao == '2':
        break
entrada = input("Digite a frase desejada: ")

#converte a frase digitada pelo usuário para letras maiúsculas, para que
#sejam encontradas as devidas correspondências de chaves no dicionário
conversao = entrada.upper()
frase = list(conversao)

#Se a opção for 1, criptografa:
if opcao == '1':
    resultado = criptografa(frase,codigo)
    resposta = input("Digite 1 para descriptografar novamente ou qualquer tecla para sair: ")
    if resposta == '1':
        novoResultado = descriptografa(resultado,codigo)
    else:
        quit()
        
#Se a opção for 2, descriptografa:
elif opcao == '2':
    resultado = descriptografa(frase,codigo)
    resposta = input("Digite 1 para criptografar novamente ou qualquer tecla para sair: ")
    if resposta == '1':
        novoResultado = criptografa(resultado,codigo)
    else:
        quit()
