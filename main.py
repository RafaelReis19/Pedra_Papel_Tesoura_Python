import random


def play():
    user = input("Qual você escolhe? 'p' para PEDRA, 'a' para PAPEL, 't' para TESOURA\n")
    computer = random.choice(['p', 'a', 't'])

    if user == computer:
        return 'É um empate!'

    if is_win(user, computer):
        return 'Você venceu!'

    return 'Você perdeu!'


def is_win(player, opponent):
    #
    #
    if (player == 'p' and opponent == 't') or (player == 't' and opponent == 'a') \
            or (player == 'a' and opponent == 'p'):
        return True


print(play())
