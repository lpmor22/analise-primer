# coding=utf-8
import os
import sys

enunciado = ('''-------------------------------------------------------------------------------------------------------------------------------------------

                                                            analise-primer v0.8                                                            

-------------------------------------------------------------------------------------------------------------------------------------------

                           3'-CTTCCTACAAGGGAAGGCCAGGGAATTTTCTTCAGAGCAGACCAGAGCCAACAGCCCCACCAGAAGAGAGCTTCAGGTC-5'                           
                           5'-GAAGGATGTTCCCTTCCGGTCCCTTAAAAGAAGTCTCGTCTGGTCTCGGTTGTCGGGGTGGTCTTCTCTCGAAGTCCAG-3'


                           3'-CTTCCTACAAGGGAAGGCCAGGGAATTTTCTTCAGAGCAGACCAGAGCCAACAGCCCCACCAGAAGAGAGCTTCAGGTC-5'
                                           |||||||||||||||||
                                        5'-TTCCGGTCCCTTAAAAG-3' --> primer 1

                                                                      primer 2 <-- 3'-CCACCAGAAGAGAGCTTC-5'
                                                                                      ||||||||||||||||||
                           5'-GAAGGATGTTCCCTTCCGGTCCCTTAAAAGAAGTCTCGTCTGGTCTCGGTTGTCGGGGTGGTCTTCTCTCGAAGTCCAG-3'


-------------------------------------------------------------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------------------------------------------------------------

PCR E PRIMERS

A PCR (Reação da Polimerase em Cadeia) é uma técnica capaz de gerar múltiplas cópias de uma sequência específica de nucleotídeos com alta sensibilidade e especificidade.
Para realizar PCR de uma região genômica específica, é necessário desenvolver um par de PRIMERS (iniciadores) para a região alvo em questão.
PRIMERS são oligonucleotídeos sintetizados quimicamente com base na sequência conhecida da região alvo.

O primer FORWARD (ou SENSO) é o primer que hibridiza com fita molde sentido 5'-3'. Ou seja, quando o primer é construído, o desenho do primer é criado em relação à fita molde.
O primer REVERSE (ou ANTI-SENSO) é aquele primer que hibridiza com a fita molde sentido 3'-5'. Ou seja, quando é construído, o desenho do primer é em relação ao COMPLEMENTO-REVERSO da fita molde.

-------------------------------------------------------------------------------------------------------------------------------------------

REGRAS GERAIS

O desenvolvimento de PRIMERS requer que alguns critérios sejam respeitados:

1- O COMPRIMENTO IDEAL DEVE SER ENTRE 17 A 28 PARES DE BASE (pb).
* Primers muito longos são ineficientes na hibridização, e quando os primers são muito curtos, perdem em especificidade.

2- A COMPOSIÇÃO DE BASES DEVE SER ENTRE 50 A 60% DE G+C.
* As ligações G+C são mais estáveis por conta da estrutura química da guanina e da citosina. Isto porque, para hibridizarem, necessitam de 3 ligações (ou pontes) de hidrogênio.
* As ligações T+A, entre a timina e a adenina, são consideradas fracas e menos estáveis, já que são necessárias 2 ligações (ou pontes) de hidrogênio.

3- PRIMERS DEVEM TERMINAR (3') EM G OU C, OU GC, OU CG.
* Devido às condições das 3 ligações (ou pontes) de hidrogênio, os primers são mais estáveis quando sua terminação é composta por G e/ou C.

4- A TEMPERATURA DE MELTING (Tm - temperature of melting) DEVE SER ENTRE 55 A 80°C.
* A Tm é a temperatura em que aproximadamente 50% dos primers estão hibridizados na fita molde.
* Para definir a Tm, utilizamos a fórmula: Tm = 4(G + C) + 2(A + T) °C.
* A compatibilidade entre os primers em um PCR é definida através da Tm. A diferença entre as temperaturas deve ser de até no máximo 2°C.
* A Tm também é importante para determinar a temperatura de hibridização (Ta - temperature of annealing).
* A Ta é a temperatura em que os primers começam a hibridizar na fita molde. O valor da Ta é até 5°C abaixo da Tm.

5- TERMINAÇÕES NÃO DEVEM SER COMPLEMENTARES (HAIRPIN).
* Os primers não devem conter regiões de complementariedade com as suas terminações 5' e/ou 3'. Caso isto ocorra, o primer forma um grampo (HAIRPIN), impedindo a hibridização com a fita molde.

6- PRIMERS NÃO DEVEM SER AUTO-COMPLEMENTARES (SELF DIMER).
* Os primers não devem conter regiões de complementariedade dentro de sua sequência. Caso isto ocorra, o primer hibridiza com ele mesmo (SELF-DIMER - outra molécula, porém igual), impedindo a hibridização com a fita molde.

7- PRIMERS NÃO DEVEM SER COMPLEMENTARES ENTRE SI (PRIMER DIMER).
* Os primers não devem conter regiões de complementariedade com o seu par. Caso isto ocorra, o primer hibridiza com o par (PRIMER-DIMER), impedindo a hibridização com a fita molde.

8- PRIMERS NÃO DEVEM TERMINAR COM MAIS DE TRÊS BASES REPETIDAS, ESPECIALMENTE EM CASO DE C OU G.
* Regiões com repetições muito longas aumentam o potencial de hibridização inespecífica (por exemplo, regiões ricas em guanina).

-------------------------------------------------------------------------------------------------------------------------------------------

SITUAÇÃO PROBLEMA

Abaixo há uma parte do genoma referência para o HIV-1, conhecido como HXB2 (Nature. 1985 Jan 24-30;313(6000):277-84).

A região em questão faz parte do gene pol do HIV-1.
O gene pol é responsável pela codificação das enzimas virais protease (PR), transcriptase reversa (RT) e integrase (IN) do HIV-1.

A atividade proposta é desenhar um par de primers para as regiões PR/RT do HIV-1:
* primer1 = FORWARD
* primer2 = REVERSE

ATENÇÃO! A área com nucleotídeos em MINÚSCULO é a região PR/RT do HIV-1 (região de interesse).
Em MAIÚSCULO, as regiões antecedem à região de interesse, são regiões os quais os primers devem ser hibridizados para não perder informação do alvo.

>Human immunodeficiency virus type 1 (HXB2), pol gene
TTTTTTAGGGAAGATCTGGCCTTCCTACAAGGGAAGGCCAGGGAATTTTCTTCAGAGCAGACCAGAGCCAACAGCCCCACCAGAAGAGAGCTTCAGGTC
TGGGGTAGAGACAACAActccccctcagaagcaggagccgatagacaaggaactgtatcctttaacttccctcaggtcactctttggcaacgacccctc
gtcacaataaagataggggggcaactaaaggaagctctattagatacaggagcagatgatacagtattagaagaaatgagtttgccaggaagatggaaa
ccaaaaatgatagggggaattggaggttttatcaaagtaagacagtatgatcagatactcatagaaatctgtggacataaagctataggtacagtatta
gtaggacctacacctgtcaacataattggaagaaatctgttgactcagattggttgcactttaaattttcccattagccctattgagactgtaccagta
aaattaaagccaggaatggatggcccaaaagttaaacaatggccattgacagaagaaaaaataaaagcattagtagaaatttgtacagagatggaaaag
gaagggaaaatttcaaaaattgggcctgaaaatccatacaatactccagtatttgccataaagaaaaaagacagtactaaatggagaaaattagtagat
ttcagagaacttaataagagaactcaagacttctgggaagttcaattaggaataccacatcccgcagggttaaaaaagaaaaaatcagtaacagtactg
gatgtgggtgatgcatatttttcagttcccttagatgaagacttcaggaagtatactgcatttaccatacctagtataaacaatgagacaccagggatt
agatatcagtacaatgtgcttccacagggatggaaaggatcaccagcaatattccaaagtagcatgacaaaaatcttagagccttttagaaaacaaaat
ccagacatagttatctatcaatacatggatgatttgtatgtaggatctgacttagaaatagggcagcatagaacaaaaatagaggagctgagacaacat
ctgttgaggtggggacttaccacaccagacaaaaaacatcagaaagaacctccattcctttggatgggttatgaactccatcctgataaatggacagta
cagcctatagtgctgccagaaaaagacagctggactgtcaatgacatacagaagttagtggggaaattgaattgggcaagtcagatttacccagggatt
aaagtaaggcaattatgtaaactccttagaggaaccaaagcactaacagaagtaataccactaacagaagaagcagagctagaactggcagaaaacaga
gagattctaaaagaaccagtacatggagtgtattatgacccatcaaaagacttaatagcagaaatacagaagcaggggcaaggccaatggacatatcaa
atttatcaagagccatttaaaaatctgaaaacaggaaaatatgcaagaatgaggggtgcccacactaatgatgtaaaacaattaacagaggcagtgcaa
aaaataaccacagaaagcatagtaatatggggaaagactcctaaatttaaactgcccatacaaaaggaaacatgggaaacatggtggacagagtattgg
caagccacctggattcctgagtgggagtttgttAATACCCCTCCCTTAGTGAAATTATGGTACCAGTTAGAGAAAGAACCCATAGTAGGAGCAGAAACC
TTCTATGTAGATGGGGCAGCTAACAGGGAGACTAAATTAGGAAAAGCAGGATATGTTACTAATAGAGGAAGACAAAAAGTTGTCACCCTAACTGACACA
ACAAATCAGAAGACTGAGTTACAAGCAATTTATCTAGCTTTGCAGGATTCGGGATTAGAAGTAAACATAGTAACAGACTCACAATATGCATTAGGAATC
ATTCAAGCACAACCAGATCAAAGTGAATCAGAGTTAGTCAATCAAATAATAGAGCAGTTAATAAAAAAGGAAAAGGTCTATCTGGCATGGGTACCAGCA
CACAAAGGAATTGGAGGAAATGAACAAGTAGATAAATTAGTCAGTGCTGGAATCAGGAAAGTACTATTTTTAGATGGAATAGATAAGGCCCAAGATGAA
CATGAGAAATATCACAGTAATTGGAGAGCAATGGCTAGTGATTTTAACCTGCCACCTGTAGTAGCAAAAGAAATAGTAGCCAGCTGTGATAAATGTCAG
CTAAAAGGAGAAGCCATGCATGGACAAGTAGACTGTAGTCCAGGAATATGGCAACTAGATTGTACACATTTAGAAGGAAAAGTTATCCTGGTAGCAGTT
CATGTAGCCAGTGGATATATAGAAGCAGAAGTTATTCCAGCAGAAACAGGGCAGGAAACAGCATATTTTCTTTTAAAATTAGCAGGAAGATGGCCAGTA
AAAACAATACATACTGACAATGGCAGCAATTTCACCGGTGCTACGGTTAGGGCCGCCTGTTGGTGGGCGGGAATCAAGCAGGAATTTGGAATTCCCTAC
AATCCCCAAAGTCAAGGAGTAGTAGAATCTATGAATAAAGAATTAAAGAAAATTATAGGACAGGTAAGAGATCAGGCTGAACATCTTAAGACAGCAGTA
CAAATGGCAGTATTCATCCACAATTTTAAAAGAAAAGGGGGGATTGGGGGGTACAGTGCAGGGGAAAGAATAGTAGACATAATAGCAACAGACATACAA
ACTAAAGAATTACAAAAACAAATTACAAAAATTCAAAATTTTCGGGTTTATTACAGGGACAGCAGAAATCCACTTTGGAAAGGACCAGCAAAGCTCCTC
TGGAAAGGTGAAGGGGCAGTAGTAATACAAGATAATAGTGACATAAAAGTAGTGCCAAGAAGAAAAGCAAAGATCATTAGGGATTATGGAAAACAGATG
GCAGGTGATGATTGTGTGGCAAGTAGACAGGATGAGGATTAG

-------------------------------------------------------------------------------------------------------------------------------------------''')

# regiões referente ao enunciado
lista_regiao1 = "TTTTTTAGGGAAGATCTGGCCTTCCTACAAGGGAAGGCCAGGGAATTTTCTTCAGAGCAGACCAGAGCCAACAGCCCCACCAGAAGAGAGCTTCAGGTCTGGGGTAGAGACAACAA"
lista_regiao1_complemento = "AAAAAATCCCTTCTAGACCGGAAGGATGTTCCCTTCCGGTCCCTTAAAAGAAGTCTCGTCTGGTCTCGGTTGTCGGGGTGGTCTTCTCTCGAAGTCCAGACCCCATCTCTGTTGTT"
lista_regiao1_complemento_reverso = "TTGTTGTCTCTACCCCAGACCTGAAGCTCTCTTCTGGTGGGGCTGTTGGCTCTGGTCTGCTCTGAAGAAAATTCCCTGGCCTTCCCTTGTAGGAAGGCCAGATCTTCCCTAAAAAA"
lista_regiao_interesse = "CTCCCCCTCAGAAGCAGGAGCCGATAGACAAGGAACTGTATCCTTTAACTTCCCTCAGGTCACTCTTTGGCAACGACCCCTCGTCACAATAAAGATAGGGGGGCAACTAAAGGAAGCTCTATTAGATACAGGAGCAGATGATACAGTATTAGAAGAAATGAGTTTGCCAGGAAGATGGAAACCAAAAATGATAGGGGGAATTGGAGGTTTTATCAAAGTAAGACAGTATGATCAGATACTCATAGAAATCTGTGGACATAAAGCTATAGGTACAGTATTAGTAGGACCTACACCTGTCAACATAATTGGAAGAAATCTGTTGACTCAGATTGGTTGCACTTTAAATTTTCCCATTAGCCCTATTGAGACTGTACCAGTAAAATTAAAGCCAGGAATGGATGGCCCAAAAGTTAAACAATGGCCATTGACAGAAGAAAAAATAAAAGCATTAGTAGAAATTTGTACAGAGATGGAAAAGGAAGGGAAAATTTCAAAAATTGGGCCTGAAAATCCATACAATACTCCAGTATTTGCCATAAAGAAAAAAGACAGTACTAAATGGAGAAAATTAGTAGATTTCAGAGAACTTAATAAGAGAACTCAAGACTTCTGGGAAGTTCAATTAGGAATACCACATCCCGCAGGGTTAAAAAAGAAAAAATCAGTAACAGTACTGGATGTGGGTGATGCATATTTTTCAGTTCCCTTAGATGAAGACTTCAGGAAGTATACTGCATTTACCATACCTAGTATAAACAATGAGACACCAGGGATTAGATATCAGTACAATGTGCTTCCACAGGGATGGAAAGGATCACCAGCAATATTCCAAAGTAGCATGACAAAAATCTTAGAGCCTTTTAGAAAACAAAATCCAGACATAGTTATCTATCAATACATGGATGATTTGTATGTAGGATCTGACTTAGAAATAGGGCAGCATAGAACAAAAATAGAGGAGCTGAGACAACATCTGTTGAGGTGGGGACTTACCACACCAGACAAAAAACATCAGAAAGAACCTCCATTCCTTTGGATGGGTTATGAACTCCATCCTGATAAATGGACAGTACAGCCTATAGTGCTGCCAGAAAAAGACAGCTGGACTGTCAATGACATACAGAAGTTAGTGGGGAAATTGAATTGGGCAAGTCAGATTTACCCAGGGATTAAAGTAAGGCAATTATGTAAACTCCTTAGAGGAACCAAAGCACTAACAGAAGTAATACCACTAACAGAAGAAGCAGAGCTAGAACTGGCAGAAAACAGAGAGATTCTAAAAGAACCAGTACATGGAGTGTATTATGACCCATCAAAAGACTTAATAGCAGAAATACAGAAGCAGGGGCAAGGCCAATGGACATATCAAATTTATCAAGAGCCATTTAAAAATCTGAAAACAGGAAAATATGCAAGAATGAGGGGTGCCCACACTAATGATGTAAAACAATTAACAGAGGCAGTGCAAAAAATAACCACAGAAAGCATAGTAATATGGGGAAAGACTCCTAAATTTAAACTGCCCATACAAAAGGAAACATGGGAAACATGGTGGACAGAGTATTGGCAAGCCACCTGGATTCCTGAGTGGGAGTTTGTT"
lista_regiao_interesse_complemento_reverso = "AACAAACTCCCACTCAGGAATCCAGGTGGCTTGCCAATACTCTGTCCACCATGTTTCCCATGTTTCCTTTTGTATGGGCAGTTTAAATTTAGGAGTCTTTCCCCATATTACTATGCTTTCTGTGGTTATTTTTTGCACTGCCTCTGTTAATTGTTTTACATCATTAGTGTGGGCACCCCTCATTCTTGCATATTTTCCTGTTTTCAGATTTTTAAATGGCTCTTGATAAATTTGATATGTCCATTGGCCTTGCCCCTGCTTCTGTATTTCTGCTATTAAGTCTTTTGATGGGTCATAATACACTCCATGTACTGGTTCTTTTAGAATCTCTCTGTTTTCTGCCAGTTCTAGCTCTGCTTCTTCTGTTAGTGGTATTACTTCTGTTAGTGCTTTGGTTCCTCTAAGGAGTTTACATAATTGCCTTACTTTAATCCCTGGGTAAATCTGACTTGCCCAATTCAATTTCCCCACTAACTTCTGTATGTCATTGACAGTCCAGCTGTCTTTTTCTGGCAGCACTATAGGCTGTACTGTCCATTTATCAGGATGGAGTTCATAACCCATCCAAAGGAATGGAGGTTCTTTCTGATGTTTTTTGTCTGGTGTGGTAAGTCCCCACCTCAACAGATGTTGTCTCAGCTCCTCTATTTTTGTTCTATGCTGCCCTATTTCTAAGTCAGATCCTACATACAAATCATCCATGTATTGATAGATAACTATGTCTGGATTTTGTTTTCTAAAAGGCTCTAAGATTTTTGTCATGCTACTTTGGAATATTGCTGGTGATCCTTTCCATCCCTGTGGAAGCACATTGTACTGATATCTAATCCCTGGTGTCTCATTGTTTATACTAGGTATGGTAAATGCAGTATACTTCCTGAAGTCTTCATCTAAGGGAACTGAAAAATATGCATCACCCACATCCAGTACTGTTACTGATTTTTTCTTTTTTAACCCTGCGGGATGTGGTATTCCTAATTGAACTTCCCAGAAGTCTTGAGTTCTCTTATTAAGTTCTCTGAAATCTACTAATTTTCTCCATTTAGTACTGTCTTTTTTCTTTATGGCAAATACTGGAGTATTGTATGGATTTTCAGGCCCAATTTTTGAAATTTTCCCTTCCTTTTCCATCTCTGTACAAATTTCTACTAATGCTTTTATTTTTTCTTCTGTCAATGGCCATTGTTTAACTTTTGGGCCATCCATTCCTGGCTTTAATTTTACTGGTACAGTCTCAATAGGGCTAATGGGAAAATTTAAAGTGCAACCAATCTGAGTCAACAGATTTCTTCCAATTATGTTGACAGGTGTAGGTCCTACTAATACTGTACCTATAGCTTTATGTCCACAGATTTCTATGAGTATCTGATCATACTGTCTTACTTTGATAAAACCTCCAATTCCCCCTATCATTTTTGGTTTCCATCTTCCTGGCAAACTCATTTCTTCTAATACTGTATCATCTGCTCCTGTATCTAATAGAGCTTCCTTTAGTTGCCCCCCTATCTTTATTGTGACGAGGGGTCGTTGCCAAAGAGTGACCTGAGGGAAGTTAAAGGATACAGTTCCTTGTCTATCGGCTCCTGCTTCTGAGGGGGAG"
lista_regiao2 = "AATACCCCTCCCTTAGTGAAATTATGGTACCAGTTAGAGAAAGAACCCATAGTAGGAGCAGAAACCTTCTATGTAGATGGGGCAGCTAACAGGGAGACTAAATTAGGAAAAGCAGGATATGTTACTAATAGAGGAAGACAAAAAGTTGTCACCCTAACTGACACAACAAATCAGAAGACTGAGTTACAAGCAATTTATCTAGCTTTGCAGGATTCGGGATTAGAAGTAAACATAGTAACAGACTCACAATATGCATTAGGAATCATTCAAGCACAACCAGATCAAAGTGAATCAGAGTTAGTCAATCAAATAATAGAGCAGTTAATAAAAAAGGAAAAGGTCTATCTGGCATGGGTACCAGCACACAAAGGAATTGGAGGAAATGAACAAGTAGATAAATTAGTCAGTGCTGGAATCAGGAAAGTACTATTTTTAGATGGAATAGATAAGGCCCAAGATGAACATGAGAAATATCACAGTAATTGGAGAGCAATGGCTAGTGATTTTAACCTGCCACCTGTAGTAGCAAAAGAAATAGTAGCCAGCTGTGATAAATGTCAGCTAAAAGGAGAAGCCATGCATGGACAAGTAGACTGTAGTCCAGGAATATGGCAACTAGATTGTACACATTTAGAAGGAAAAGTTATCCTGGTAGCAGTTCATGTAGCCAGTGGATATATAGAAGCAGAAGTTATTCCAGCAGAAACAGGGCAGGAAACAGCATATTTTCTTTTAAAATTAGCAGGAAGATGGCCAGTAAAAACAATACATACTGACAATGGCAGCAATTTCACCGGTGCTACGGTTAGGGCCGCCTGTTGGTGGGCGGGAATCAAGCAGGAATTTGGAATTCCCTACAATCCCCAAAGTCAAGGAGTAGTAGAATCTATGAATAAAGAATTAAAGAAAATTATAGGACAGGTAAGAGATCAGGCTGAACATCTTAAGACAGCAGTACAAATGGCAGTATTCATCCACAATTTTAAAAGAAAAGGGGGGATTGGGGGGTACAGTGCAGGGGAAAGAATAGTAGACATAATAGCAACAGACATACAAACTAAAGAATTACAAAAACAAATTACAAAAATTCAAAATTTTCGGGTTTATTACAGGGACAGCAGAAATCCACTTTGGAAAGGACCAGCAAAGCTCCTCTGGAAAGGTGAAGGGGCAGTAGTAATACAAGATAATAGTGACATAAAAGTAGTGCCAAGAAGAAAAGCAAAGATCATTAGGGATTATGGAAAACAGATGGCAGGTGATGATTGTGTGGCAAGTAGACAGGATGAGGATTAG"
lista_regiao2_complemento_reverso = "CTAATCCTCATCCTGTCTACTTGCCACACAATCATCACCTGCCATCTGTTTTCCATAATCCCTAATGATCTTTGCTTTTCTTCTTGGCACTACTTTTATGTCACTATTATCTTGTATTACTACTGCCCCTTCACCTTTCCAGAGGAGCTTTGCTGGTCCTTTCCAAAGTGGATTTCTGCTGTCCCTGTAATAAACCCGAAAATTTTGAATTTTTGTAATTTGTTTTTGTAATTCTTTAGTTTGTATGTCTGTTGCTATTATGTCTACTATTCTTTCCCCTGCACTGTACCCCCCAATCCCCCCTTTTCTTTTAAAATTGTGGATGAATACTGCCATTTGTACTGCTGTCTTAAGATGTTCAGCCTGATCTCTTACCTGTCCTATAATTTTCTTTAATTCTTTATTCATAGATTCTACTACTCCTTGACTTTGGGGATTGTAGGGAATTCCAAATTCCTGCTTGATTCCCGCCCACCAACAGGCGGCCCTAACCGTAGCACCGGTGAAATTGCTGCCATTGTCAGTATGTATTGTTTTTACTGGCCATCTTCCTGCTAATTTTAAAAGAAAATATGCTGTTTCCTGCCCTGTTTCTGCTGGAATAACTTCTGCTTCTATATATCCACTGGCTACATGAACTGCTACCAGGATAACTTTTCCTTCTAAATGTGTACAATCTAGTTGCCATATTCCTGGACTACAGTCTACTTGTCCATGCATGGCTTCTCCTTTTAGCTGACATTTATCACAGCTGGCTACTATTTCTTTTGCTACTACAGGTGGCAGGTTAAAATCACTAGCCATTGCTCTCCAATTACTGTGATATTTCTCATGTTCATCTTGGGCCTTATCTATTCCATCTAAAAATAGTACTTTCCTGATTCCAGCACTGACTAATTTATCTACTTGTTCATTTCCTCCAATTCCTTTGTGTGCTGGTACCCATGCCAGATAGACCTTTTCCTTTTTTATTAACTGCTCTATTATTTGATTGACTAACTCTGATTCACTTTGATCTGGTTGTGCTTGAATGATTCCTAATGCATATTGTGAGTCTGTTACTATGTTTACTTCTAATCCCGAATCCTGCAAAGCTAGATAAATTGCTTGTAACTCAGTCTTCTGATTTGTTGTGTCAGTTAGGGTGACAACTTTTTGTCTTCCTCTATTAGTAACATATCCTGCTTTTCCTAATTTAGTCTCCCTGTTAGCTGCCCCATCTACATAGAAGGTTTCTGCTCCTACTATGGGTTCTTTCTCTAACTGGTACCATAATTTCACTAAGGGAGGGGTATT"

print(enunciado)  # mostrar o enunciado com a situação problema e informações para a construção de primers

primer_tests = True
while primer_tests:
    primer1 = input('''
A partir destes conhecimentos, crie o desenho para o primer FORWARD.
ATENÇÃO! Sempre escrever o primer no sentido 5'-3'.

O site https://www.bioinformatics.org/sms/rev_comp.html pode ajudar para determinar o COMPLEMENTO da região de interesse.

Desenho do primer FORWARD: ''').upper()  # pedir o desenho do primer1
    encontrar_primer1 = lista_regiao1_complemento.find(primer1)  # encontrar o desenho do primer1 dentro da lista_regiao1
    tamanho_primer1 = len(primer1)  # determinar o tamanho do primer1
    ultimo_primer1 = primer1[-1]  # determinar se o primer1 termina com G ou C, ou GC, ou CG
    composicao_c_primer1 = primer1.count("C")  # determinar a composição de citosina do primer1
    composicao_g_primer1 = primer1.count("G")  # determinar a composição de guanina do primer1
    composicao_t_primer1 = primer1.count("T")  # determinar a composição de timina do primer1
    composicao_a_primer1 = primer1.count("A")  # determinar a composição de adenina do primer1
    porcentagem_gc_primer1 = (composicao_c_primer1 + composicao_g_primer1) / tamanho_primer1 * 100  # determinar a composição de G+C do primer1
    temperatura_melting_primer1 = (4 * (composicao_c_primer1 + composicao_g_primer1)) + (2 * (composicao_a_primer1 + composicao_t_primer1))  # determinar a temperatura de melting (Tm) do primer1
    temperatura_min_hibridizacao_primer1 = temperatura_melting_primer1 - 5  # determinar a temperatura de hibridização (Ta) do primer1
    if encontrar_primer1 >= 0:
        print('''
-------------------------------------------------------------------------------------------------------------------------------------------

O seu primer FORWARD:
''')
        print("1- Hibridiza perfeitamente com a sequência-alvo.")
        if tamanho_primer1 != -1 and tamanho_primer1 >= 17 and tamanho_primer1 <= 28 and encontrar_primer1 >= 0:
            print("2- Possui %dpb." % tamanho_primer1)
            if ultimo_primer1 is "C" or ultimo_primer1 is "G":
                print("3- Possui terminação 3' composta por %s." % primer1[-1])
                if porcentagem_gc_primer1 >= 50 and porcentagem_gc_primer1 <= 60:
                    print("4- Contém %.1d%% de G+C." % porcentagem_gc_primer1)
                    if temperatura_melting_primer1 >= 55 and temperatura_melting_primer1 <= 80:
                        print("5- A temperatura de melting é %.1f°C." % temperatura_melting_primer1)
                        print('''
O primer FORWARD está OK!

-------------------------------------------------------------------------------------------------------------------------------------------''')
                        primer2 = input('''
Agora crie o desenho para o primer REVERSE.
ATENÇÃO! Sempre escrever o primer no sentido 5'-3'.

O site https://www.bioinformatics.org/sms/rev_comp.html pode ajudar para determinar o COMPLEMENTO-REVERSO da região de interesse.

Desenho do primer REVERSE: ''').upper()  # pedir o desenho do primer2
                        encontrar_primer2 = lista_regiao2_complemento_reverso.find(primer2)  # encontrar o desenho do primer2 dentro da lista_regiao2
                        tamanho_primer2 = len(primer2)  # determinar o tamanho do primer2
                        ultimo_primer2 = primer2[-1]  # determinar se o primer2 termina com G ou C, ou GC, ou CG
                        composicao_c_primer2 = primer2.count("C")  # determinar a composição de citosina do primer2
                        composicao_g_primer2 = primer2.count("G")  # determinar a composição de guanina do primer2
                        composicao_t_primer2 = primer2.count("T")  # determinar a composição de timina do primer2
                        composicao_a_primer2 = primer2.count("A")  # determinar a composição de adenina do primer2
                        porcentagem_gc_primer2 = (composicao_c_primer2 + composicao_g_primer2) / tamanho_primer2 * 100  # determinar a composição de G+C do primer2
                        temperatura_melting_primer2 = (4 * (composicao_c_primer2 + composicao_g_primer2)) + (2 * (composicao_a_primer2 + composicao_t_primer2))  # determinar a temperatura de melting (Tm) do primer2
                        temperatura_min_hibridizacao_primer2 = temperatura_melting_primer2 - 5  # determinar a temperatura de hibridização (Ta) do primer2
                        if encontrar_primer2 >= 0:
                            print('''
-------------------------------------------------------------------------------------------------------------------------------------------

O seu primer REVERSE:
''')
                            print("1- Hibridiza perfeitamente com a sequência-alvo.")
                            if tamanho_primer2 != -1 and tamanho_primer2 >= 17 and tamanho_primer2 <= 28 and encontrar_primer2 >= 0:
                                print("2- Possui %dpb." % tamanho_primer2)
                                if ultimo_primer2 is "C" or ultimo_primer2 is "G":
                                    print("3- Possui terminação 3' composta por %s." % primer2[-1])
                                    if porcentagem_gc_primer2 >= 50 and porcentagem_gc_primer2 <= 60:
                                        print("4- Contém %.1d%% de G+C." % porcentagem_gc_primer2)
                                        if temperatura_melting_primer2 >= 55 and temperatura_melting_primer2 <= 80:
                                            print("5- A temperatura de melting é %.1f°C." % temperatura_melting_primer2)
                                            print('''
O primer REVERSE também está OK!

-------------------------------------------------------------------------------------------------------------------------------------------

ÚLTIMO TESTE

Compatibilidade entre as temperaturas de melting dos primers FORWARD e REVERSE...

Testando...''')
                                            compatibilidade_temperatura_melting_primers = temperatura_melting_primer1 - temperatura_melting_primer2  # determinar compatibilidade entre as Ta do primer1 e primer2
                                            compatibilidade_temperatura_melting_primers_abs = abs(compatibilidade_temperatura_melting_primers)  # valor positivo da compatibilidade entre as Ta do primer1 e primer2
                                            if compatibilidade_temperatura_melting_primers_abs <= 2:
                                                print('''
Está Ótimo!
Os primers FORWARD e REVERSE apresentam temperaturas de melting %.1f°C e %.1f°C respectivamente.

Infelizmente este programinha (ainda) não consegue testar HAIRPIN, SELF-DIMER e PRIMER-DIMER :(
Essa aplicação tem como finalidade exemplificar de forma didática sobre as regras gerais para o desenho de primer.

Espero que tenha ajudado!


-------------------------------------------------------------------------------------------------------------------------------------------

                                                            analise-primer v0.8                                                            

-------------------------------------------------------------------------------------------------------------------------------------------

2019
Desenvolvido com fins didáticos para o Minicurso BIOLOGIA MOLECULAR: DESENHO DE PRIMERS PARA PCR (VIII Simpósio de Biomedicina da Bahiana)

Laise de Moraes
http://lattes.cnpq.br/7097758558494370 # lattes
https://slides.com/lpmor22 # decks
https://github.com/lpmor22 # github
laisepaixao@live.com # email
@lpmor22 # instagram
@lpmor22_ # twitter

-------------------------------------------------------------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------------------------------------------------------------''' % (temperatura_melting_primer1, temperatura_melting_primer2))
                                                primer_tests = False
                                            else:
                                                print('''Os primers FORWARD e REVERSE não apresentam temperaturas compatíveis entre si (%.1f°C e %.1f°C respectivamente).
Por favor, reveja os critérios para a construção de primers e tente novamente!''' % (temperatura_melting_primer1, temperatura_melting_primer2))
                                        else:
                                            print('''
Talvez você tenha digitado errado ou o primer REVERSE não esteja bom.
Neste caso, a temperatura de melting do seu primer REVERSE é %.1f°C.
Por favor, reveja os critérios de desenho de primer e tente novamente!''' % temperatura_melting_primer2)
                                    else:
                                        print('''
Talvez você tenha digitado errado ou o primer REVERSE não esteja bom.
Neste caso, seu primer REVERSE contém %.1d%% de G+C.
Por favor, reveja os critérios de desenho de primer e tente novamente!''' % porcentagem_gc_primer2)
                                else:
                                    print('''
Talvez você tenha digitado errado ou o primer REVERSE não esteja bom.
Neste caso, seu primer REVERSE possui terminação 3' composta por %s.
Por favor, reveja os critérios de desenho de primer e tente novamente!''' % primer2[-1])
                            else:
                                print('''
Talvez você tenha digitado errado ou o primer REVERSE não esteja bom.
Neste caso, seu primer REVERSE possui %dpb.
Por favor, reveja os critérios de desenho de primer e tente novamente!''' % tamanho_primer2)
                        else:
                            print('''
Talvez você tenha digitado errado ou o primer REVERSE não esteja bom.
Neste caso, seu primer REVERSE não hibridiza com a região de interesse.
Por favor, reveja os critérios de desenho de primer e tente novamente!''')
                    else:
                        print('''
Talvez você tenha digitado errado ou o primer FORWARD não esteja bom.
Neste caso, a temperatura de melting do seu primer FORWARD é %.1f°C.
Por favor, reveja os critérios de desenho de primer e tente novamente!''' % temperatura_melting_primer1)
                else:
                    print('''
Talvez você tenha digitado errado ou o primer FORWARD não esteja bom.
Neste caso, seu primer FORWARD contém %.1d%% de G+C.
Por favor, reveja os critérios de desenho de primer e tente novamente!''' % porcentagem_gc_primer1)
            else:
                print('''
Talvez você tenha digitado errado ou o primer FORWARD não esteja bom.
Neste caso, seu primer FORWARD possui terminação 3' composta por %s.
Por favor, reveja os critérios de desenho de primer e tente novamente!''' % primer1[-1])
        else:
            print('''
Talvez você tenha digitado errado ou o primer FORWARD não esteja bom.
Neste caso, seu primer FORWARD possui %dpb.
Por favor, reveja os critérios de desenho de primer e tente novamente!''' % tamanho_primer1)
    else:
        print('''
Talvez você tenha digitado errado ou o primer FORWARD não esteja bom.
Neste caso, seu primer FORWARD não hibridiza com a região de interesse.
Por favor, reveja os critérios de desenho de primer e tente novamente!''')

input('''
Pressione QUALQUER TECLA para sair ;) ''')
sys.exit()