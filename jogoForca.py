import string

#palavra a ser descoberta
secreta = "banana"
size = len(secreta)
secreta = list(secreta)
#criando palavra a ser preenchida pelo usuario
palavra = '_' * size
palavra = list(palavra)
vidas = 5
ganhou = False
perdeu = False

#loop jogo
while perdeu is False and ganhou is False:
    #Array para armazenar as letras que foram chutadas
    chutadas = []
    #input para coletar o chute
    character = input(f'Você possui {vidas} vidas\n Insira uma letra: ')
    character = character.lower()
    
    #validando se o chute possui apenas uma letra
    if len(character) != 1 :
        print('Informe uma letra válida')
        continue
    
    #validando se o chute não é um caractere especial
    if not character in string.ascii_letters:
        print('Informe uma letra')
        continue
    
    #validando se a letra chutada está presente na palavra secreta e se essa letra ja não foi chutada anteriormente
    if character in secreta and character not in chutadas:
        for i in range(size):
            if character == secreta[i]:
                palavra[i] = character
    
    #validando e informando que a letra ja foi chutada anteriormente
    elif character in chutadas:
        print('Essa letra já foi chutada')
        continue
    
    #retirando vida caso a letra esteja validada e não esteja na palavra secreta e finalizando o jogo caso o usuário esteja sem vida
    else:
        vidas -= 1
        if vidas == 0:
            perdeu = True
            continue
    
    #adicionando a letra a lista de letras chutadas
    chutadas.append(character)
    
    #validando se o usuario encontrou a palavra 
    if palavra == secreta:
        ganhou = True
    
    #imprimindo o atual estagio da descoberta, imprimindo as letras que ja foram acertadas em suas respectivas posições
    print(palavra)


if perdeu is True:
    print('Você perdeu! ')
    
if ganhou is True:
    print('Você ganhou! ')



