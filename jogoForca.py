import string
import random



palavras =  ["computador", "software", "hardware", "internet", "smartphone", "tablet", "aplicativo", "programação", "tecnologia", "inovação", "inteligência artificial", "big data", "realidade virtual", "realidade aumentada", "navegador", "segurança", "criptografia", "redes sociais", "blog", "e-commerce", "cibersegurança", "sistema operacional", "nuvem", "servidor", "tecnologia da informação", "banco de dados", "web design", "programação web", "IoT", "automação", "robotização", "indústria 4.0", "biotecnologia", "nanotecnologia", "integração", "API", "UX", "UI", "gamificação", "realidade mista", "ciberespaço", "ciberativismo", "algoritmo", "análise de dados", "backup", "cloud computing", "código-fonte", "dispositivos móveis", "driver", "ferramentas de produtividade", "geolocalização", "hacker", "hiperconectividade", "interface", "mídia digital", "mobilidade", "multimídia", "navegação", "pixel", "processador", "realidade simulada", "tecnologia assistiva", "tecnologia de ponta", "tecnologia emergente", "tecnologia móvel", "tecnologia vestível", "telecomunicações", "usabilidade", "VPN", "web analytics", "webinar", "wiki", "wi-fi", "zoom", "animação digital", "AR", "chatbot", "cloud storage", "computação em nuvem", "computação quântica", "cyberbullying", "data mining", "deep learning", "e-mail marketing", "engenharia de software", "gaming", "Google Maps", "machine learning", "open source", "realidade estendida", "realidade híbrida", "rede de computadores", "resolução", "SEO", "smart cities", "streaming", "tecnologia verde", "teste de software", "virtualização", "voz sobre IP"]


#palavra a ser descoberta
#secreta =  random.choice(palavras)
secreta =  'mamonas assassinas'
size = len(secreta)
secreta = list(secreta)
#criando palavra a ser preenchida pelo usuario    
palavra = '_' * size
palavra = list(palavra)
#adicionando um '-' caso a palavra possua um espaço
if ' ' in secreta:
   indexEspaco = secreta.index(' ')
   palavra[indexEspaco] = '-'
   secreta[indexEspaco] = '-'
vidas = 5
ganhou = False
perdeu = False



#loop jogo
while perdeu is False and ganhou is False:
    
    #imprimindo o atual estagio da descoberta, imprimindo as letras que ja foram acertadas em suas respectivas posições
    print(palavra)
    #Array para armazenar as letras que foram chutadas
    chutadas = []
    #input para coletar o chute
    character = input(f'Você possui {vidas} vidas\n Insira uma letra (Se quiser arriscar a palavra, digite: chutar): ')
    character = character.lower()
    #permitindo o usuário a chutar a palavra caso solicitado
    if character == 'chutar':
        chutar = input('Informe o seu chute: ')
        if chutar == secreta:
            ganhou = True
            continue
        else:
            perdeu = True
            continue

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
    
    


if perdeu is True:
    print(f'Você perdeu! \n A palavra era: {secreta}')
    
if ganhou is True:
    print(f'Você ganhou! {secreta}')



