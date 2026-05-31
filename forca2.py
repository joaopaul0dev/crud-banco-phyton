import random

palavrasLista = ["abacaxi", "banana", "laranja", "morango", "melancia", "uva", "kiwi", "manga"]

palavra = random.choice(palavrasLista).upper()

print(f'Bem vindo ao jogo da forca em Python!')
print(f'Sua palavra tem {len(palavra)} letras.')

def jogarForca(palavra):
    letrasDescobertas = ['_'] * len(palavra)
    tentativas = 6

    while '_' in letrasDescobertas and tentativas > 0:
        print(f'Palavra atual: ' + ' '.join(letrasDescobertas) )
        print(f'tentativas restantes: {tentativas}')

        chute = input('Digite seu chute: ').upper()
        if chute in palavra:
            print(f'Boa! a letra {chute} está na palavra')
            for indice, letra in enumerate(palavra):
                if letra == chute:
                    letrasDescobertas[indice] = chute
        else:
            print(f'Que pena {chute} não está na palavra')
            tentativas -= 1

    if '_'not in letrasDescobertas:
        print(f'Parabens você venceu a palavra era {palavra}')
    else:
        print(f"\nVocê perdeu! O boneco foi enforcado. A palavra era: {palavra}")

jogarForca(palavra)

