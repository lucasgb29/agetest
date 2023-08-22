import keyboard
import os
import time


def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def entrada_idade():
    sua_idade = input("Sua idade: ")
    idade_pessoa = input("Idade da outra pessoa: ")
    return sua_idade, idade_pessoa


def converter_idade(sua_idade, idade_pessoa):
    int_sua_idade = int(sua_idade)
    int_idade_pessoa = int(idade_pessoa)
    return int_sua_idade, int_idade_pessoa


def verificar_idade_minima(sua_idade, idade_pessoa):
    int_sua_idade = int(sua_idade)
    int_idade_pessoa = int(idade_pessoa)
    if int_sua_idade < 14:
        print("Você é muito jovem para namorar, vá ser uma criança!!!")
        return False
    elif int_idade_pessoa < 14:
        print("Ele/a é muito jovem para namorar, encontre alguém da sua idade")
        return False
    else:
        return True


def verificar_faixa_etaria(int_sua_idade, int_idade_pessoa):
    idade_minima = (int_sua_idade / 2) + 7
    idade_maxima = (int_sua_idade - 7) * 2
    muito_jovem = int_idade_pessoa < idade_minima
    muito_velho = int_idade_pessoa > idade_maxima
    return muito_jovem, muito_velho


def calcular_reajuste(muito_jovem, muito_velho, int_sua_idade, int_idade_pessoa):
    reajuste = 0
    while muito_jovem or muito_velho:
        int_sua_idade += 1
        int_idade_pessoa += 1
        reajuste += 1
        muito_jovem, muito_velho = verificar_faixa_etaria(int_sua_idade, int_idade_pessoa)
    return reajuste


def exibir_resultado(muito_jovem, muito_velho, reajuste):
    if muito_jovem:
        print("Ele/a é considerado/a muito jovem para você.")
        print("Vocês terão a idade certa em {} anos".format(reajuste))
    elif muito_velho:
        print("Ele/a é considerado/a muito velho/a para você.")
        print("Vocês terão a idade certa em {} anos".format(reajuste))
    else:
        print("Ele/a é considerado/a na faixa etária certa para você.")


def opcoes():
    print("\nPressione R para reiniciar")
    print("Pressione Q para sair")
    
    while True:
        tecla = keyboard.read_key().upper()
        if tecla == "Q":
            print("\nTchau tchau!!")
            return "Q"
        elif tecla == "R":
            return "R"


def idade_invalida():
    limpar_tela()
    print("############")
    print("Idade inválida.")
    print("############")
    time.sleep(1)  # Aguarda por 1 segundo antes de reiniciar
    return entrada_idade()


def teste_idade():
    while True:
        limpar_tela()

        sua_idade, idade_pessoa = entrada_idade()

        if sua_idade.isdigit() and idade_pessoa.isdigit():
            if verificar_idade_minima(sua_idade, idade_pessoa):
                int_sua_idade, int_idade_pessoa = converter_idade(sua_idade, idade_pessoa)

                muito_jovem, muito_velho = verificar_faixa_etaria(int_sua_idade, int_idade_pessoa)

                reajuste = calcular_reajuste(muito_jovem, muito_velho, int_sua_idade, int_idade_pessoa)

                exibir_resultado(muito_jovem, muito_velho, reajuste)

        else:
            sua_idade, idade_pessoa = idade_invalida()

        tecla = opcoes()
        if tecla == "Q":
            break


if __name__ == "__main__":
    teste_idade()
