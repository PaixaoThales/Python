def arremesso(n: int, v: int) -> str:
    """
    -> verifica se um arremesso eh possivel realizar ou arremesso ou nao.
    :parâmetro n: distancia do buraco
    :parâmetro v: velocidade do arremesso
    :return: retorna possivel, caso o arremesso seja possivel, ou impossivel caso nao seja
    """  
    buraco = 0
    quique = 0
    while v != 0:
        buraco += v
        quique += 1
        if buraco == n:
            return 'possivel'
        if quique == v:
            v -= 1
            quique = 0
    return 'possivel' if buraco == n else 'impossivel'

    
def main():
    while True:
        entrada = list(map(int, input().strip().split()))
        if entrada[0] == 0 and entrada[1] == 0:
            break
        print(arremesso(entrada[0], entrada[1]))

        
main()
