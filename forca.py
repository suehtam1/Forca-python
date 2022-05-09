from random import choice
from time import sleep
from jogo_forca.desenho import desenho

palavras = ['PASTO', 'MELHOR', 'FUGIR', 'QUERIA', 'MISTA', 'FELIZ', 'CAMPO', 'ESCOLA', 'IGREJA']
escolha = palpite_Letra = comparacao = jogar = ' '
usadas = []
lista_Escolha = []
palavra_Escondida = []
errada = []
tentativa_Valida = 1
count_erro = 0
derrota = False
vitoria = False


def linha(car, qtd):
    print(car * qtd)


def escolhe_Palavra(esc_palavras):
    global escolha
    escolha = choice(esc_palavras)
    for letra_Escolha in escolha:
        lista_Escolha.append(letra_Escolha)
        palavra_Escondida.append(' _ ')
    return escolha


def mostra_Palavra(letra_atual):
    global lista_Escolha, palavra_Escondida, errada, count_erro
    for add in range(1, len(lista_Escolha) + 1):
        if letra_atual == lista_Escolha[add - 1]:
            palavra_Escondida[add - 1] = letra_atual
        erro = letra_atual in escolha
        errada.append(erro)
    if errada.count(False) == len(lista_Escolha):
        count_erro += 1
        errada.clear()
    return str(palavra_Escondida).replace(',', '').replace("' '", "").replace('[', '').replace(']', '').replace("'", "")


def palpite():
    global usadas, tentativa_Valida, palpite_Letra, comparacao
    while True:
        palpite_Letra = str(input('Digite uma letra: ')).upper().strip()
        if len(palpite_Letra) == 1 and palpite_Letra not in usadas and palpite_Letra.isalpha() is True:
            print(f'Verificando letra {palpite_Letra} na palavra')
            sleep(0.5)
            usadas.append(palpite_Letra)
            tentativa_Valida += 1
            comparacao = palpite_Letra
            print(f'Letras usadas: {usadas}')
            return palpite_Letra
        else:
            print('ERRO. ATENÇÃO:\nDigite APENAS letra, sem caracteres especiais ou números\nDigite APENAS 1 letra'
                  '\nVerifique se a letra já foi digitada')


def jogar_Novamente():
    while True:
        global jogar
        jogar = str(input('Continuar jogando? [S/N]: ')).upper().strip()
        if jogar in 'S' or jogar in 'N':
            return jogar
        else:
            print('ERRO. Digite APENAS S ou N')


def perdeu():
    global jogar, tentativa_Valida, escolha, derrota
    if jogar == 'N':
        linha('-=', 20)
        print('desistiu')
        print(f'A resposta era: {escolha}')
        derrota = True
    elif tentativa_Valida >= 10:
        linha('-=', 20)
        print('numero de tentativas excedido')
        print(f'A resposta era: {escolha} ')
        derrota = True
    return derrota


def ganhou():
    global lista_Escolha, palavra_Escondida, vitoria
    if lista_Escolha == palavra_Escondida:
        linha('-=', 20)
        print('Parabens voce GANHOU')
        vitoria = True
    return vitoria


def main():
    global derrota, vitoria
    linha('<>', 20)
    print('JOGO da forca'.center(40).upper())
    linha('<>', 20)
    escolhe_Palavra(palavras)
    print(' _ ' * len(escolha))
    linha('-=', 15)
    while True:
        if derrota is True:
            sleep(2)
            print(desenho(10))
            break
        if vitoria is True:
            break
        print(f'Tentativa {tentativa_Valida}/10')
        sleep(2)
        print(desenho(count_erro))
        palpite()
        print(mostra_Palavra(comparacao))
        ganhou()
        perdeu()
        if derrota is True:
            break
        if vitoria is True:
            break
        linha('-=', 15)
        jogar_Novamente()
        perdeu()
        ganhou()


main()
