#Algoritmo criado para calcular as operações lógicas binárias (AND, OR, XOR, NAD, NOR) entre duas sequências de bits de um mesmo tamanho N.  

#funções de cada uma das operações:
def l_or(n, x1, x2):    
    result = []
    for c in range(n):
        if x1[c] == '1' or x2[c] == '1':
            result.append('1')
        else:
            result.append('0')
    result = ''.join(result)
    return result

def l_and(n, x1, x2):
    result = []
    for c in range(n):
        if x1[c] == '1' and x2[c] == '1':
            result.append('1')
        else:
            result.append('0')
    result = ''.join(result)
    return result

def l_xor (n, x1, x2):
    result = []
    for c in range(n):
        if x1[c] == x2[c]:
            result.append('0')
        else:
            result.append('1')
    result = ''.join(result)
    return result

def l_nand(n, x1, x2):
    result = []
    for c in range(n):
        if x1[c] == '1' and x2[c] == '1':
            result.append('0')
        else:
            result.append('1')
    result = ''.join(result)
    return result

def l_nor(n, x1, x2):
    result = []
    for c in range(n):
        if x1[c] == '0' and x2[c] == '0':
            result.append('1')
        else:
            result.append('0')
    result = ''.join(result)
    return result

def l_mor(n, x1, x2):
    result1 = []
    result=[]
    for c in range(n):
        if x1[c] == '1':
            result1.append('0')
        else:
            result1.append('1')
    for i in range(n):
        if result1[i] == '1' or x2[i] == '1':
            result.append('1')
        else:
            result.append('0')
    result = ''.join(result)
    return result

tamanho_vetor = int(input())    #Entrada de um número inteiro que representa a quantidade de elementos que serão 
                                #inseridos em S1 e S2
if tamanho_vetor <= 1000:
    primeiro = list(map(str, input().strip()))  #Entrada da S1(sequência 1)
    segundo = list(map(str, input().strip()))   #Entrada da S2(sequência 2)
    funcao = list(input().split())
    cont1 = 0
    cont2 = 0
    for c in range(len(primeiro)):                          #Conferindo se o número de bits é igual ao da variavel
                                                            #tamanho_vetor
        if (primeiro[c] != '0' and primeiro[c] != '1'):
            cont1+=1
    for c in range(len(segundo)):
        if(segundo[c] != '0' and segundo[c] != '1'):
            cont2+=1
    if cont1 != 0:
        print("ERRO")
    elif cont2 != 0:
        print('ERRO')
    elif (len(primeiro) != tamanho_vetor):
        print("ERRO")
    elif (len(segundo) != tamanho_vetor):
        print("ERRO")
    elif (len(funcao) == 3) and (len(primeiro) == tamanho_vetor) and (len(segundo) == tamanho_vetor) and (cont1 == 0) and (cont2 == 0):
        if funcao[0] == 'S1' and funcao[2] == 'S2':
            if funcao[1] == 'OR':
                print(l_or(tamanho_vetor, primeiro, segundo))
            elif funcao[1] == 'AND':
                print(l_and(tamanho_vetor, primeiro, segundo))
            elif funcao[1] == 'XOR':
                print(l_xor(tamanho_vetor, primeiro, segundo))
            elif funcao[1] == 'NAND':
                print(l_nand(tamanho_vetor, primeiro, segundo))
            elif funcao[1] == 'NOR':
                print(l_nor(tamanho_vetor, primeiro, segundo))
            elif funcao[1] == 'MOR':
                print(l_mor(tamanho_vetor, primeiro, segundo))
            else:
                print('ERRO')
        elif funcao[0] == 'S1' and funcao[2] == 'S1':
            if funcao[1] == 'OR':
                print(l_or(tamanho_vetor, primeiro, primeiro))
            elif funcao[1] == 'AND':
                print(l_and(tamanho_vetor, primeiro, primeiro))
            elif funcao[1] == 'XOR':
                print(l_xor(tamanho_vetor, primeiro, primeiro))
            elif funcao[1] == 'NAND':
                print(l_nand(tamanho_vetor, primeiro, primeiro))
            elif funcao[1] == 'NOR':
                print(l_nor(tamanho_vetor, primeiro, primeiro))
            elif funcao[1] == 'MOR':
                print(l_mor(tamanho_vetor, primeiro, primeiro))
            else:
                print('ERRO')
        elif funcao[0] == 'S2' and funcao[2] == 'S1':
            if funcao[1] == 'OR':
                print(l_or(tamanho_vetor, segundo, primeiro))
            elif funcao[1] == 'AND':
                print(l_and(tamanho_vetor, segundo, primeiro))
            elif funcao[1] == 'XOR':
                print(l_xor(tamanho_vetor, segundo, primeiro))
            elif funcao[1] == 'NAND':
                print(l_nand(tamanho_vetor, segundo, primeiro))
            elif funcao[1] == 'NOR':
                print(l_nor(tamanho_vetor, segundo, primeiro))
            elif funcao[1] == 'MOR':
                print(l_mor(tamanho_vetor, segundo, primeiro))
            else:
                print('ERRO')
        elif funcao[0] == 'S2' and funcao[2] == 'S2':
            if funcao[1] == 'OR':
                print(l_or(tamanho_vetor, segundo, segundo))
            elif funcao[1] == 'AND':
                print(l_and(tamanho_vetor, segundo, segundo))
            elif funcao[1] == 'XOR':
                print(l_xor(tamanho_vetor, segundo, segundo))
            elif funcao[1] == 'NAND':
                print(l_nand(tamanho_vetor, segundo, segundo))
            elif funcao[1] == 'NOR':
                print(l_nor(tamanho_vetor, segundo, segundo))
            elif funcao[1] == 'MOR':
                print(l_mor(tamanho_vetor, segundo, segundo))
            else:
                print('ERRO')
    elif (len(funcao) == 5) and (len(primeiro) == tamanho_vetor) and (len(segundo) == tamanho_vetor) and (cont1 == 0) and (cont2 == 0):
        if funcao[0] == 'S1' and funcao[2] == 'S2':
            if funcao[1] == 'OR':
                x = l_or(tamanho_vetor, primeiro, segundo)
                if funcao[4] == "S1":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "AND":
                        print(l_and(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, primeiro))
                    else:
                        print('ERRO')
                elif funcao[4] == 'S2':
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, segundo))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, segundo))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, segundo))
                    else:
                        print('ERRO')
                else:
                    print('ERRO')
            elif funcao[1] == 'AND':
                x = l_and(tamanho_vetor, primeiro, segundo)
                if funcao[4] == "S1":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, primeiro))
                    else:
                        print('ERRO')
                elif funcao[4] == 'S2':
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, segundo))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, segundo))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, segundo))
                    else:
                        print('ERRO')
                else:
                    print('ERRO')
            elif funcao[1] == 'XOR':
                x = l_xor(tamanho_vetor, primeiro, segundo)
                if funcao[4] == "S1":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, primeiro))
                    else:
                        print("ERRO")
                elif funcao[4] == 'S2':
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, segundo))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, segundo))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, segundo))
                    else:
                        print('ERRO')
                else:
                    print('ERRO')
            elif funcao[1] == 'NAND':
                x = l_nand(tamanho_vetor, primeiro, segundo)
                if funcao[4] == "S1":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, primeiro))
                    else:
                        print("ERRO")
                elif funcao[4] == 'S2':
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, segundo))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, segundo))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, segundo))
                    else:
                        print("ERRO")
                else:
                    print('ERRO')
            elif funcao[1] == 'NOR':
                x = l_nor(tamanho_vetor, primeiro, segundo)
                if funcao[4] == "S1":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, primeiro))
                    else:
                        print("ERRO")
                elif funcao[4] == "S2":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, segundo))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, segundo))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, segundo))
                    else:
                        print("ERRO")
                else:
                    print('ERRO')
            elif funcao[1] == 'MOR':
                x = l_mor(tamanho_vetor, primeiro, segundo)
                if funcao[4] == "S1":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, primeiro))
                    else:
                        print("ERRO")
                elif funcao[4] == "S2":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, segundo))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, segundo))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, segundo))
                    else:
                        print("ERRO")
                else:
                    print("ERRO")
        elif funcao[0] == "S1" and funcao[2] == "S1":
            if funcao[1] == 'OR':
                x = l_or(tamanho_vetor, primeiro, primeiro)
                if funcao[4] == "S1":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, primeiro))
                    else:
                        print("ERRO")
                elif funcao[4] == "S2":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, segundo))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, segundo))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, segundo))
                    else:
                        print("ERRO")
                else:
                    print("ERRO")
            elif funcao[1] == 'AND':
                x = l_and(tamanho_vetor, primeiro, primeiro)
                if funcao[4] == "S1":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, primeiro))
                    else:
                        print("ERRO")
                elif funcao[4] == "S2":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, segundo))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, segundo))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, segundo))
                    else:
                        print("ERRO")
                else:
                    print("ERRO")
            elif funcao[1] == 'XOR':
                x = l_xor(tamanho_vetor, primeiro, primeiro)
                if funcao[4] == "S1":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, primeiro))
                    else:
                        print("ERRO")
                elif funcao[4] == "S2":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, segundo))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, segundo))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, segundo))
                    else:
                        print("ERRO")
                else:
                    print("ERRO")

            elif funcao[1] == 'NAND':
                x = l_nand(tamanho_vetor, primeiro, primeiro)
                if funcao[4] == "S1":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, primeiro))
                    else:
                        print("ERRO")
                elif funcao[4] == "S2":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, segundo))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, segundo))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, segundo))
                    else:
                        print("ERRO")
                else:
                    print("ERRO")
            elif funcao[1] == 'NOR':
                x = l_nor(tamanho_vetor, primeiro, primeiro)
                if funcao[4] == "S1":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, primeiro))
                    else:
                        print("ERRO")
                elif funcao[4] == "S2":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, segundo))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, segundo))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, segundo))
                    else:
                        print("ERRO")
                else:
                    print("ERRO")
            elif funcao[1] == 'MOR':
                x = l_mor(tamanho_vetor, primeiro, primeiro)
                if funcao[4] == "S1":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, primeiro))
                    else:
                        print("ERRO")
                elif funcao[4] == "S2":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, segundo))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, segundo))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, segundo))
                    else:
                        print("ERRO")
                else:
                    print("ERRO")
        elif funcao[0] == 'S2' and funcao[2] == 'S1':
            if funcao[1] == 'OR':
                x = l_or(tamanho_vetor, segundo, primeiro)
                if funcao[4] == "S1":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, primeiro))
                    else:
                        print("ERRO")
                elif funcao[4] == "S2":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, segundo))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, segundo))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, segundo))
                    else:
                        print("ERRO")
                else:
                    print("ERRO")
            elif funcao[1] == 'AND':
                x = l_and(tamanho_vetor, segundo, primeiro)
                if funcao[4] == "S1":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, primeiro))
                    else:
                        print("ERRO")
                elif funcao[4] == "S2":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, segundo))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, segundo))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, segundo))
                    else:
                        print("ERRO")
                else:
                    print("ERRO")
            elif funcao[1] == 'XOR':
                x = l_xor(tamanho_vetor, segundo, primeiro)
                if funcao[4] == "S1":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, primeiro))
                    else:
                        print("ERRO")
                elif funcao[4] == "S2":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, segundo))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, segundo))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, segundo))
                    else:
                        print("ERRO")
                else:
                    print("ERRO")

            elif funcao[1] == 'NAND':
                x = l_nand(tamanho_vetor, segundo, primeiro)
                if funcao[4] == "S1":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, primeiro))
                    else:
                        print("ERRO")
                elif funcao[4] == "S2":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, segundo))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, segundo))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, segundo))
                    else:
                        print("ERRO")
                else:
                    print("ERRO")
            elif funcao[1] == 'NOR':
                x = l_nor(tamanho_vetor, segundo, primeiro)
                if funcao[4] == "S1":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, primeiro))
                    else:
                        print("ERRO")
                elif funcao[4] == "S2":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, segundo))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, segundo))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, segundo))
                    else:
                        print("ERRO")
                else:
                    print("ERRO")
            elif funcao[1] == 'MOR':
                x = l_mor(tamanho_vetor, segundo, primeiro)
                if funcao[4] == "S1":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, primeiro))
                    else:
                        print("ERRO")
                elif funcao[4] == "S2":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, segundo))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, segundo))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, segundo))
                    else:
                        print("ERRO")
                else:
                    print("ERRO")
        elif funcao[0] == 'S2' and funcao[2] == 'S2':
            if funcao[1] == 'OR':
                x = l_or(tamanho_vetor, segundo, segundo)
                if funcao[4] == "S1":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, primeiro))
                    else:
                        print("ERRO")
                elif funcao[4] == "S2":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, segundo))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, segundo))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, segundo))
                    else:
                        print("ERRO")
            elif funcao[1] == 'AND':
                x = l_and(tamanho_vetor, segundo, segundo)
                if funcao[4] == "S1":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, primeiro))
                    else:
                        print("ERRO")
                elif funcao[4] == "S2":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, segundo))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, segundo))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, segundo))
                    else:
                        print("ERRO")
                else:
                    print("ERRO")
            elif funcao[1] == 'XOR':
                x = l_xor(tamanho_vetor, segundo, segundo)
                if funcao[4] == "S1":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, primeiro))
                    else:
                        print("ERRO")
                elif funcao[4] == "S2":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, segundo))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, segundo))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, segundo))
                    else:
                        print("ERRO")
                else:
                    print("ERRO")

            elif funcao[1] == 'NAND':
                x = l_nand(tamanho_vetor, segundo, segundo)
                if funcao[4] == "S1":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, primeiro))
                    else:
                        print("ERRO")
                elif funcao[4] == "S2":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, segundo))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, segundo))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, segundo))
                    else:
                        print("ERRO")
                else:
                    print("ERRO")
            elif funcao[1] == 'NOR':
                x = l_nor(tamanho_vetor, segundo, segundo)
                if funcao[4] == "S1":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, primeiro))
                    else:
                        print("ERRO")
                elif funcao[4] == "S2":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, segundo))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, segundo))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, segundo))
                    else:
                        print("ERRO")
                else:
                    print("ERRO")
            elif funcao[1] == 'MOR':
                x = l_mor(tamanho_vetor, segundo, segundo)
                if funcao[4] == "S1":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, primeiro))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, primeiro))
                    else:
                        print("ERRO")
                elif funcao[4] == "S2":
                    if funcao[3] == "OR":
                        print(l_or(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'AND':
                        print(l_and(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'XOR':
                        print(l_xor(tamanho_vetor, x, segundo))
                    elif funcao[3] == 'NAND':
                        print(l_nand(tamanho_vetor, x, segundo))
                    elif funcao[3] == "NOR":
                        print(l_nor(tamanho_vetor, x, segundo))
                    elif funcao[3] == "MOR":
                        print(l_mor(tamanho_vetor, x, segundo))
                    else:
                        print("ERRO")
                else:
                    print("ERRO")
            else:
                print("ERRO")
    else:
        print("ERRO")
else:
    print("ERRO")