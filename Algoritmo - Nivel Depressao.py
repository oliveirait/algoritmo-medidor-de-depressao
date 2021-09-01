import sys
from time import sleep


print('-='*30)
print('Olá! Este algoritmo te ajuda a medir seu nivel de depressão, baseado no questionário DASS 21.\n')
print('\033[1;31mATENCAO! O resultado da avaliação não indica um diagnóstico conclusivo\nPara determinar '
'qualquer diagnóstico potencial discuta seu resultado com um psicólogo ou um médico psiquiatra.\033[0;0m')
print('-='*30)
sleep(5)

print('\033[1;92m\nSao 4 opcoes de resposta disponiveis abaixo: \033[0;0m')
print('''
\033[1;36m0 --> NUNCA - Não se aplica a mim de forma alguma\033[0;0m
\033[1;34m1 --> ÀS VEZES - Aplica-se a mim em algum grau, ou parte do tempo\033[0;0m
\033[1;95m2 --> FREQUENTEMENTE - Aplica-se a mim em um grau considerável, ou boa parte do tempo\033[0;0m
\033[1;33m3 --> QUASE SEMPRE- Aplica-se muito a mim, ou na maioria das vezes \033[0;0m \n ''')
print('-='*30)
sleep(6)

print('\033[1;31mApós digitar o número que corresponde à resposta, '
      'pressione\033[0;0m \033[1;96mENTER\033[0;0m. \033[1;31mVamos começar ?\n')
sleep(3)

def p1_depressao():
    p1 = input(str('\033[1;92mPergunta 1:\033[0;0m Eu não consigo sentir nenhum sentimento positivo: '))
    if p1 in opcoes:
        return int(p1)
    else:
        print('\033[1;31mOPS! Digite apenas número correspondente! \033[1;31m ')
        return p1_depressao()
        
def p2_depressao():
    p2 = input(str('\033[1;92mPergunta 2:\033[0;0m Acho difícil desenvolver a iniciativa de fazer as coisas: \033[0;0m'))
    if p2 in opcoes:
        return int(p2)
    else:
        print('\033[1;31mOPS! Digite apenas número correspondente! \033[1;31m ')
        return p2_depressao()
       
def p3_depressao():
    p3 = input(str('\033[1;92mPergunta 3: \033[0;0mSinto que não tenho nada pelo que ansiar: \033[0;0m'))
    if p3 in opcoes:
        return int(p3)
    else:
        print('\033[1;31mOPS! Digite apenas número correspondente! \033[1;31m ')
        return p3_depressao()
        
def p4_depressao():
    p4 = input(str('\033[1;92mPergunta 4: \033[0;0mSinto o coração desanimado e triste: \033[0;0m'))
    if p4 in opcoes:
        return int(p4)
    else:
        print('\033[1;31mOPS! Digite apenas número correspondente! \033[1;31m ')
        return p4_depressao()

def p5_depressao():
    p5 = input(str('\033[1;92mPergunta 5: \033[0;0mNão consigo ficar entusiasmado com nada: \033[0;0m'))
    if p5 in opcoes:
        return int(p5)
    else:
        print('\033[1;31mOPS! Digite apenas número correspondente! \033[1;31m ')
        return p5_depressao()

def p6_depressao():
    p6 = input(str('\033[1;92mPergunta 6: \033[0;0mSinto que não tenho valor como pessoa: \033[0;0m'))
    if p6 in opcoes:
        return int(p6)
    else:
        print('\033[1;31mOPS! Digite apenas número correspondente! \033[1;31m ')
        return p6_depressao()

def p7_depressao():
    p7 = input(str('\033[1;92mPergunta 7: \033[0;0mSinto que a vida não tem ou faz sentido: \033[0;0m'))
    if p7 in opcoes:
        return int(p7)
    else:
        print('\033[1;31mOPS! Digite apenas número correspondente! \033[1;31m ')
        return p7_depressao()
    
def exibir_resultado_depressao(resultado, nivel):
    if resultado <= 4:
        print(nivel[1])
    elif resultado  <= 6:
        print(nivel[2])
    elif resultado  <= 10:
        print(nivel[3])
    elif resultado  <= 13:
        print(nivel[4])
    else:
        if resultado  >= 14:
            print(nivel[5])
            
#-----------------------------------------------------------------------------

#lista de opcoes para o usuario
opcoes = ['0','1','2','3']

#dicionario com todas as funcoes que executam as perguntas
dic = {'p1' : p1_depressao(),
       'p2' : p2_depressao(),
       'p3' : p3_depressao(),
       'p4' : p4_depressao(),
       'p5' : p5_depressao(),
       'p6' : p6_depressao(),
       'p7' : p7_depressao()
       }

#dicionario com as respostas pré-definidas
nivel = {
        1 : '\nNORMAL - Está tudo bem! Só fique atento a qualquer alteração de humor. ',
        
        2 : '\n\033[1;34mSUAVE - Nada sério por enquanto! Por hora você pode ler um pouco mais sobre a depressão. '
        '\033[1;96mAcesse o site vittude.com e baixe grátis o e-book "Depressão, como ela é?".\033[0;0m',
        
        3 : '\n\033[1;33mMODERADO - Sinal amarelo!\033[0;0m É bom entender melhor se é fruto da situação ou algo mais grave. '
        'Fale online com um psicólogo. \033[0;0m \033[1;96mAcesse vittude.com e encontre um psicólogo para atendimento online.\033[0;0m',
        
        4 : '\n\033[1;33mSEVERO - Fique atento! Este grau de severidade requer apoio de um profissional. '
        'Recomendamos que você busque um psicólogo ou psiquiatra para diagnóstico adequado. '
        '\033[1;96mA vittude.com oferece mais de 1000 psicólogos espalhados pelo Brasil, encontre o seu.\033[0;0m',
        
        5 : '\n\033[1;33mEXTREMAMENTE SEVERO - Atenção! Essa é uma situação crítica. '
        'Recomendamos que você busque um psicólogo ou psiquiatra para diagnóstico adequado.\033[0;0m '
        '\033[1;96mO site vittude.com oferece mais de 1000 psicólogos espalhados pelo Brasil\033[0;0m.'
            }

#esta variavel armazena a soma de todas as respostas do usuario
resultado = sum(dic.values())

#esta funcao verifica o resultado e exibe o nivel de depressao para o usuario
exibir_resultado_depressao(resultado, nivel)

#encerra o algoritmo
sys.exit(0)

if __name__ == '__main__':
    main()