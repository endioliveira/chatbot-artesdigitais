import os

def processarResposta(resposta, nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}, Eu trabalho fazendo as seguintes artes: Convite digital (vários tamanhos), Convite digital interativo, Cardápio digital interativo, cartão de visita/fidelidade, logomarca, marca d água, arte para bolsinhas de festas, artes para lembrancinhas de festas, posts para redes sociais{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}, Convite digital (vários tamanhos): 15,00 | Convite digital interativo 25,00 | Cardápio digital interativo 35,00 | cartão de visita/fidelidade 20,00 | logomarca 20,00 | marca d água 20,00 | arte para bolsinhas de festas 15,00 | artes para lembrancinhas de festas 15,00 | posts para redes sociais 20,00{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, Faço nos temas de princesas, heróis, circo, mickey, disney, fazendinha, patrulha canina, piquenique, aquarela, safari, galinha pintadinha, pequeno principe, minecraft, carros, bailarina, girassol, fundo do mar, moranguinho, peppa pig, carrossel, 15 anos, tropical, pool party, flamengo...{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome}, O Horário de atendimento é das 9h até 17h{os.linesep}')
    else: 
        print('Você precisa digitar a opção 1, 2, 3 ou 4.')

def start():
    #Apresentar o chatbot
    print('Olá!! Bem vindo ao meu chatbot')

    #Pedindo nome
    nome = input('Digite seu nome: ')

    #Pedindo número de WhatsApp
    email = input('Número do WhatsApp: ')
    while True:
        #Oferecer o menu de opções
        resposta = input(f'O que gostaria de saber sobre o meu trabalho?{os.linesep}[1] - Artes digitais que eu monto aqui na lojinha{os.linesep}[2] - Veja os valores de cada arte digital{os.linesep}[3] - Veja os temas que eu faço por aqui{os.linesep}[4] - Veja o Horário de Atendimento da lojinha{os.linesep}')

        #Processar a resposta enviada
        processarResposta(resposta, nome)


if __name__ == '__main__': #Estou dizendo aqui que assim que inicializar esse programa, eu vou rodar uma função
    start()


# {os.linesep}: serve para quebrar a linha