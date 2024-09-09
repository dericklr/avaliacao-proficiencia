import Jogador
import Tabuleiro
import random

class Main:
    def main():
        while True:
         print("Escolha sua opção: ")
         print("1-Iniciar tabuleiro")
         print("2-Iniciar jogador")
         print("3-Numeros entre 5 e 15 ")
         print("4-Soma dos Valores")
         print("5-Operações com vetor")
         print("0-Sair")

         escolha=int(input())
         opcao={
            1:iniciaTabuleiro,
            2:iniciaJogador,
            3:NumerosInteiros,
            4:somaValores,
            5:operacoesVetor
            }
         if escolha==0:
             print("Programa encerrado")
             break
         elif escolha in opcao:
             opcao[escolha]
         else:
            print("Opção invalida")    




       
            #1-Tabuleiro
            def iniciaTabuleiro():
                n=int(input("Numero de linhas: "))
                m=int(input("Numero de colunas: "))
                letras=[input(f"Informe a letra{i+1}: " for i in range(5))]

                tabuleiro=Tabuleiro(n,m, letras)
                print("Tabuleiro gerado")
                tabuleiro.imprimir()

            #2-Classe jogador
            def iniciaJogador():
                jogador=Jogador(100,50)
                print("\Valores inicias do Jogador")
                print(f"Vida: {jogador._getVida()}")
                print(f"Energia: {jogador._getEnergia()}")

                jogador._setVida(80)
                jogador._setEnergia(20)
                print("\Valores Atualizados do Jogador")
                print(f"Vida: {jogador._getVida()}")
                print(f"Energia: {jogador._getEnergia()}")


            #3-Numeros inteiros entre 5 e 15
            def NumerosInteiros():
                print("Digite numero inteiros positivos")
                while True:
                    num=int(input())
                    if num==0:
                        break
                    if 5<=num<=15:
                        print("Numeros entre 5 e 15: {num}")


            #4-Vetor com a soma dos valores
            def somaValores():
                vetor1=[random.randint(20,50) for _ in range(10)]      
                soma=sum(vetor1)
                print(f"\soma dos valores do vetor: {soma}")

            #5-Vetor invertido, maior, menor e rotação a esquerda
            def operacoesVetor():
                vetor2=int(input(f"Digite o valor {i+1}") for i in range(10))
                print("\nVetor invertido: ")
                print(''.join(map(str,vetor2[::-1])))

                maior=max(vetor2)
                menor=min(vetor2)
                print(f"Maior valor: {maior}")
                print(f"Menor valor: {menor}")

                print("\nRotação a esquerda: ")
                for i in range(len(vetor2)):
                    primeiro=vetor2.pop(0)
                    vetor2.append(primeiro)
                    print(''.join(map(str,vetor2)))

    if __name__== "main":
        main()

