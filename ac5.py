"""15/03/2024
Pesquise sobre o módulo random, em particular sobre a função randint()
Entendendo como essa função é utilizada, elabore um jogo por CLI e que você controla um aventureiro e está
lutando contra um monstro. Considere os seguintes requisitos:
O aventureiro possui uma vida inicial igual a 100, seu ataque é um valor aleatório entre 10 e 20, e sua defesa é um valor aleatório entre 1 e 5;
O monstro possui uma vida aleatória entre 60 e 80, seu ataque é um valor aleatório entre 20 e 30, e não possui defesa;
Após a definição dos atributos do aventureiro e do monstro, o programa deve exibir os atributos iniciais e em
seguida rodar um loop até que a vida de um dos dois fique igual ou abaixo de zero;

No loop, considere as seguintes ações:
O programa escreve o número da rodada do combate;
O aventureiro ataca o monstro, reduzindo da vida do monstro um valor aleatório entre 1 e o ataque do aventureiro;
Se a vida do monstro ficar igual ou abaixo de zero, o programa deve escrever na tela que o monstro morreu e encerrar o loop;
Em seguida, o monstro ataca o aventureiro, reduzindo da vida deste um valor aleatório entre 1 e o ataque do monstro, menos a defesa do aventureiro;
Se a vida do aventureiro ficar igual ou abaixo de zero, o programa deve escrever na tela que o aventureiro morreu e encerrar o loop;
Por fim, o programa deve escrever os atributos do aventureiro e do monstro.
O programa não deve possuir inputs do usuário, ele apenas deve exibir as informações. Faça o exercício em uma única função, main().
"""

import random

def main():
    # Aventureiro
    aven_vida = 100
    aven_ataque = random.randint(10, 20)
    aven_defesa = random.randint(1, 5)

    # Monstro
    mon_vida = random.randint(60, 80)
    mon_ataque = random.randint(20, 30)

    print("Atributos iniciais:")
    print("Aventureiro - Vida: ", aven_vida, ", Ataque: ", aven_ataque, ", Defesa: ", aven_defesa)
    print("Monstro - Vida: ", mon_vida, ", Ataque: ", mon_ataque)

    num_rodada = 1

    while aven_vida > 0 and mon_vida > 0:
        print("\nRodada ", num_rodada, ":")


        # Aventureiro ataca o monstro
        aven_dano = random.randint(1, aven_ataque)
        mon_vida -= aven_dano

        # Verifica se o monstro morreu
        if mon_vida <= 0:
            print("O monstro morreu!")
            break

        # Monstro ataca o aventureiro
        mon_dano = random.randint(1, mon_ataque) - aven_defesa
        if mon_dano < 0:
            mon_dano = 0
        aven_vida -= mon_dano

        # Verifica se o aventureiro morreu
        if aven_vida <= 0:
            print("O aventureiro morreu!")
            break

        num_rodada += 1
        print("Aventureiro - Vida: ", aven_vida, ", Ataque: ", aven_ataque, ", Defesa: ", aven_defesa)
        print("Monstro - Vida: ", mon_vida, ", Ataque: ", mon_ataque)

main()