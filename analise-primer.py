# coding=utf-8
import os

enunciado = ('''
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                                                             analise-primer v0.5                                                                                             
                                                                                             
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


                                                               5'-TAGCGCATCAGCGATAGAGAGAATCGATCAGCTAACGCTAGCACAGCTACAGACTCAGTAGCGCACAGCATCAGCATCA-3'                                                            
                                                                  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
                                                               3'-ATCGCGTAGTCGCTATCTCTCTTAGCTAGTCGATTGCGATCGTGTCGATGTCTGAGTCATCGCGTGTCGTAGTCGTAGT-5'


                                                               5'-TAGCGCATCAGCGATAGAGAGAATCGATCAGCTAACGCTAGCACAGCTACAGACTCAGTAGCGCACAGCATCAGCATCA-3'
                                                                     |||||||||||||||||||
                                                               5'-GCGTAGTCGCTATCTCTCT-3' --> primer 1

                                                                                                            primer 2 <-- 3-GTAGCGCACAGCATCAGCAT
                                                                                                                           ||||||||||||||||||||
                                                               3'-ATCGCGTAGTCGCTATCTCTCTTAGCTAGTCGATTGCGATCGTGTCGATGTCTGAGTCATCGCGTGTCGTAGTCGTAGT-5'


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

SITUAÇÃO PROBLEMA

A PCR (Reação da Polimerase em Cadeia) é  uma técnica capaz de gerar múltiplas cópias de uma sequência específica de nucleotídeos de um determinado organismo, com alta sensibilidade e especificidade.
Para realizar uma PCR para uma região genômica específica, é necessário desenvolver um par de PRIMERS para a região alvo em questão.
PRIMERS são oligonucleotídeos sintetizados quimicamente com base na sequência conhecida da região alvo.
O primer FORWARD (ou SENSO) é o primer que hibridiza com fita molde sentido 5'-3'. Ou seja, quando é construído, o desenho do primer é em relação à fita molde.
O primer REVERSE (ou ANTI-SENSO) é aquele primer que hibridiza com a fita molde sentido 3'-5'. Ou seja, quando é construído, o desenho do primer é em relação ao COMPLEMENTO-REVERSO da fita molde.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

O DESENVOLVIMENTO DE PRIMERS REQUER QUE ALGUNS CRITÉRIOS SEJAM RESPEITADOS:

1- O COMPRIMENTO IDEAL DEVE SER ENTRE 17 A 28 PARES DE BASE (pb).
Primers muito longos são ineficientes na hibridização e quando os primers são muito curtos, perdem especificidade.

2- A COMPOSIÇÃO DE BASES DEVE SER ENTRE 50 A 60% DE G+C.
As ligações G+C são mais estáveis por conta da estrutura de ambos nucleotídeos. Isto porque, para hibridizarem, necessitam de 3 ligações (ou pontes) de hidrogênio.
Enquanto as ligações T+A são consideradas fracas e menos estáveis, já que são necessárias 2 ligações (ou pontes) de hidrogênio.

3- PRIMERS DEVEM TERMINAR (3') EM G OU C, OU GC, OU CG.
Devido as mesmas condições das 3 ligações (ou pontes) de hidrogênio, os primers precisam de maior estabilidade quando sua terminação é composta por G e/ou C.

4- A TEMPERATURA DE MELTING (Tm - temperature of melting) DEVE SER ENTRE 55 A 80°C.
A Tm é a temperatura em que aproximadamente 50% dos primers estão já hibridizados na fita molde.
Para definir a Tm, utilizamos a fórmula: Tm = 4(G + C) + 2(A + T) °C.
E no caso de primers para PCR (um par), essas Tms devem ser compatíveis. A diferença entre as duas Tms só podem ser de até no máximo 2°C.
Essa Tm é importante para determinar a temperatura de hibridização (Ta - temperature of annealing), a qual é a temperatura em que os primers começam a hibridizar na fita molde.
O valor da Ta é até 5°C abaixo da Tm.

5- TERMINAÇÕES NÃO DEVEM SER COMPLEMENTARES (HAIRPIN).
Explicar.

6- PRIMERS NÃO DEVEM SER AUTO-COMPLEMENTARES (SELF DIMER).
Explicar.

7- PRIMERS NÃO DEVEM SER COMPLEMENTARES ENTRE SI (PRIMER DIMER).
Explicar.

8- PRIMERS NÃO DEVEM TERMINAR COM MAIS DE TRÊS BASES REPETIDAS, ESPECIALMENTE EM CASO DE C OU G.
Explicar.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Abaixo, há uma parte do genoma referência para o HIV-1, conhecido como HXB2 (Nature. 1985 Jan 24-30;313(6000):277-84).

A região em questão faz parte do gene pol do HIV-1. Este gene é o responsável pela codificação das enzimas virais protease (PR), transcriptase reversa (RT) e integrase (IN) do HIV-1.

A atividade proposta é desenhar um par de primers para as regiões PR/RT do HIV-1:
* primer1 = FORWARD
* primer2 = REVERSE
 
ATENÇÃO! A área com nucleotídeos em MINÚSCULO é a região de interesse.

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

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')

# regiões referente ao enunciado
lista_regiao1 = "TTTTTTAGGGAAGATCTGGCCTTCCTACAAGGGAAGGCCAGGGAATTTTCTTCAGAGCAGACCAGAGCCAACAGCCCCACCAGAAGAGAGCTTCAGGTCTGGGGTAGAGACAACAA"
lista_regiao1_complemento_reverso = "TTGTTGTCTCTACCCCAGACCTGAAGCTCTCTTCTGGTGGGGCTGTTGGCTCTGGTCTGCTCTGAAGAAAATTCCCTGGCCTTCCCTTGTAGGAAGGCCAGATCTTCCCTAAAAAA"
lista_regiao_interesse = "CTCCCCCTCAGAAGCAGGAGCCGATAGACAAGGAACTGTATCCTTTAACTTCCCTCAGGTCACTCTTTGGCAACGACCCCTCGTCACAATAAAGATAGGGGGGCAACTAAAGGAAGCTCTATTAGATACAGGAGCAGATGATACAGTATTAGAAGAAATGAGTTTGCCAGGAAGATGGAAACCAAAAATGATAGGGGGAATTGGAGGTTTTATCAAAGTAAGACAGTATGATCAGATACTCATAGAAATCTGTGGACATAAAGCTATAGGTACAGTATTAGTAGGACCTACACCTGTCAACATAATTGGAAGAAATCTGTTGACTCAGATTGGTTGCACTTTAAATTTTCCCATTAGCCCTATTGAGACTGTACCAGTAAAATTAAAGCCAGGAATGGATGGCCCAAAAGTTAAACAATGGCCATTGACAGAAGAAAAAATAAAAGCATTAGTAGAAATTTGTACAGAGATGGAAAAGGAAGGGAAAATTTCAAAAATTGGGCCTGAAAATCCATACAATACTCCAGTATTTGCCATAAAGAAAAAAGACAGTACTAAATGGAGAAAATTAGTAGATTTCAGAGAACTTAATAAGAGAACTCAAGACTTCTGGGAAGTTCAATTAGGAATACCACATCCCGCAGGGTTAAAAAAGAAAAAATCAGTAACAGTACTGGATGTGGGTGATGCATATTTTTCAGTTCCCTTAGATGAAGACTTCAGGAAGTATACTGCATTTACCATACCTAGTATAAACAATGAGACACCAGGGATTAGATATCAGTACAATGTGCTTCCACAGGGATGGAAAGGATCACCAGCAATATTCCAAAGTAGCATGACAAAAATCTTAGAGCCTTTTAGAAAACAAAATCCAGACATAGTTATCTATCAATACATGGATGATTTGTATGTAGGATCTGACTTAGAAATAGGGCAGCATAGAACAAAAATAGAGGAGCTGAGACAACATCTGTTGAGGTGGGGACTTACCACACCAGACAAAAAACATCAGAAAGAACCTCCATTCCTTTGGATGGGTTATGAACTCCATCCTGATAAATGGACAGTACAGCCTATAGTGCTGCCAGAAAAAGACAGCTGGACTGTCAATGACATACAGAAGTTAGTGGGGAAATTGAATTGGGCAAGTCAGATTTACCCAGGGATTAAAGTAAGGCAATTATGTAAACTCCTTAGAGGAACCAAAGCACTAACAGAAGTAATACCACTAACAGAAGAAGCAGAGCTAGAACTGGCAGAAAACAGAGAGATTCTAAAAGAACCAGTACATGGAGTGTATTATGACCCATCAAAAGACTTAATAGCAGAAATACAGAAGCAGGGGCAAGGCCAATGGACATATCAAATTTATCAAGAGCCATTTAAAAATCTGAAAACAGGAAAATATGCAAGAATGAGGGGTGCCCACACTAATGATGTAAAACAATTAACAGAGGCAGTGCAAAAAATAACCACAGAAAGCATAGTAATATGGGGAAAGACTCCTAAATTTAAACTGCCCATACAAAAGGAAACATGGGAAACATGGTGGACAGAGTATTGGCAAGCCACCTGGATTCCTGAGTGGGAGTTTGTT"
lista_regiao_interesse_complemento_reverso = "AACAAACTCCCACTCAGGAATCCAGGTGGCTTGCCAATACTCTGTCCACCATGTTTCCCATGTTTCCTTTTGTATGGGCAGTTTAAATTTAGGAGTCTTTCCCCATATTACTATGCTTTCTGTGGTTATTTTTTGCACTGCCTCTGTTAATTGTTTTACATCATTAGTGTGGGCACCCCTCATTCTTGCATATTTTCCTGTTTTCAGATTTTTAAATGGCTCTTGATAAATTTGATATGTCCATTGGCCTTGCCCCTGCTTCTGTATTTCTGCTATTAAGTCTTTTGATGGGTCATAATACACTCCATGTACTGGTTCTTTTAGAATCTCTCTGTTTTCTGCCAGTTCTAGCTCTGCTTCTTCTGTTAGTGGTATTACTTCTGTTAGTGCTTTGGTTCCTCTAAGGAGTTTACATAATTGCCTTACTTTAATCCCTGGGTAAATCTGACTTGCCCAATTCAATTTCCCCACTAACTTCTGTATGTCATTGACAGTCCAGCTGTCTTTTTCTGGCAGCACTATAGGCTGTACTGTCCATTTATCAGGATGGAGTTCATAACCCATCCAAAGGAATGGAGGTTCTTTCTGATGTTTTTTGTCTGGTGTGGTAAGTCCCCACCTCAACAGATGTTGTCTCAGCTCCTCTATTTTTGTTCTATGCTGCCCTATTTCTAAGTCAGATCCTACATACAAATCATCCATGTATTGATAGATAACTATGTCTGGATTTTGTTTTCTAAAAGGCTCTAAGATTTTTGTCATGCTACTTTGGAATATTGCTGGTGATCCTTTCCATCCCTGTGGAAGCACATTGTACTGATATCTAATCCCTGGTGTCTCATTGTTTATACTAGGTATGGTAAATGCAGTATACTTCCTGAAGTCTTCATCTAAGGGAACTGAAAAATATGCATCACCCACATCCAGTACTGTTACTGATTTTTTCTTTTTTAACCCTGCGGGATGTGGTATTCCTAATTGAACTTCCCAGAAGTCTTGAGTTCTCTTATTAAGTTCTCTGAAATCTACTAATTTTCTCCATTTAGTACTGTCTTTTTTCTTTATGGCAAATACTGGAGTATTGTATGGATTTTCAGGCCCAATTTTTGAAATTTTCCCTTCCTTTTCCATCTCTGTACAAATTTCTACTAATGCTTTTATTTTTTCTTCTGTCAATGGCCATTGTTTAACTTTTGGGCCATCCATTCCTGGCTTTAATTTTACTGGTACAGTCTCAATAGGGCTAATGGGAAAATTTAAAGTGCAACCAATCTGAGTCAACAGATTTCTTCCAATTATGTTGACAGGTGTAGGTCCTACTAATACTGTACCTATAGCTTTATGTCCACAGATTTCTATGAGTATCTGATCATACTGTCTTACTTTGATAAAACCTCCAATTCCCCCTATCATTTTTGGTTTCCATCTTCCTGGCAAACTCATTTCTTCTAATACTGTATCATCTGCTCCTGTATCTAATAGAGCTTCCTTTAGTTGCCCCCCTATCTTTATTGTGACGAGGGGTCGTTGCCAAAGAGTGACCTGAGGGAAGTTAAAGGATACAGTTCCTTGTCTATCGGCTCCTGCTTCTGAGGGGGAG"
lista_regiao2 = "AATACCCCTCCCTTAGTGAAATTATGGTACCAGTTAGAGAAAGAACCCATAGTAGGAGCAGAAACCTTCTATGTAGATGGGGCAGCTAACAGGGAGACTAAATTAGGAAAAGCAGGATATGTTACTAATAGAGGAAGACAAAAAGTTGTCACCCTAACTGACACAACAAATCAGAAGACTGAGTTACAAGCAATTTATCTAGCTTTGCAGGATTCGGGATTAGAAGTAAACATAGTAACAGACTCACAATATGCATTAGGAATCATTCAAGCACAACCAGATCAAAGTGAATCAGAGTTAGTCAATCAAATAATAGAGCAGTTAATAAAAAAGGAAAAGGTCTATCTGGCATGGGTACCAGCACACAAAGGAATTGGAGGAAATGAACAAGTAGATAAATTAGTCAGTGCTGGAATCAGGAAAGTACTATTTTTAGATGGAATAGATAAGGCCCAAGATGAACATGAGAAATATCACAGTAATTGGAGAGCAATGGCTAGTGATTTTAACCTGCCACCTGTAGTAGCAAAAGAAATAGTAGCCAGCTGTGATAAATGTCAGCTAAAAGGAGAAGCCATGCATGGACAAGTAGACTGTAGTCCAGGAATATGGCAACTAGATTGTACACATTTAGAAGGAAAAGTTATCCTGGTAGCAGTTCATGTAGCCAGTGGATATATAGAAGCAGAAGTTATTCCAGCAGAAACAGGGCAGGAAACAGCATATTTTCTTTTAAAATTAGCAGGAAGATGGCCAGTAAAAACAATACATACTGACAATGGCAGCAATTTCACCGGTGCTACGGTTAGGGCCGCCTGTTGGTGGGCGGGAATCAAGCAGGAATTTGGAATTCCCTACAATCCCCAAAGTCAAGGAGTAGTAGAATCTATGAATAAAGAATTAAAGAAAATTATAGGACAGGTAAGAGATCAGGCTGAACATCTTAAGACAGCAGTACAAATGGCAGTATTCATCCACAATTTTAAAAGAAAAGGGGGGATTGGGGGGTACAGTGCAGGGGAAAGAATAGTAGACATAATAGCAACAGACATACAAACTAAAGAATTACAAAAACAAATTACAAAAATTCAAAATTTTCGGGTTTATTACAGGGACAGCAGAAATCCACTTTGGAAAGGACCAGCAAAGCTCCTCTGGAAAGGTGAAGGGGCAGTAGTAATACAAGATAATAGTGACATAAAAGTAGTGCCAAGAAGAAAAGCAAAGATCATTAGGGATTATGGAAAACAGATGGCAGGTGATGATTGTGTGGCAAGTAGACAGGATGAGGATTAG"
lista_regiao2_complemento_reverso = "CTAATCCTCATCCTGTCTACTTGCCACACAATCATCACCTGCCATCTGTTTTCCATAATCCCTAATGATCTTTGCTTTTCTTCTTGGCACTACTTTTATGTCACTATTATCTTGTATTACTACTGCCCCTTCACCTTTCCAGAGGAGCTTTGCTGGTCCTTTCCAAAGTGGATTTCTGCTGTCCCTGTAATAAACCCGAAAATTTTGAATTTTTGTAATTTGTTTTTGTAATTCTTTAGTTTGTATGTCTGTTGCTATTATGTCTACTATTCTTTCCCCTGCACTGTACCCCCCAATCCCCCCTTTTCTTTTAAAATTGTGGATGAATACTGCCATTTGTACTGCTGTCTTAAGATGTTCAGCCTGATCTCTTACCTGTCCTATAATTTTCTTTAATTCTTTATTCATAGATTCTACTACTCCTTGACTTTGGGGATTGTAGGGAATTCCAAATTCCTGCTTGATTCCCGCCCACCAACAGGCGGCCCTAACCGTAGCACCGGTGAAATTGCTGCCATTGTCAGTATGTATTGTTTTTACTGGCCATCTTCCTGCTAATTTTAAAAGAAAATATGCTGTTTCCTGCCCTGTTTCTGCTGGAATAACTTCTGCTTCTATATATCCACTGGCTACATGAACTGCTACCAGGATAACTTTTCCTTCTAAATGTGTACAATCTAGTTGCCATATTCCTGGACTACAGTCTACTTGTCCATGCATGGCTTCTCCTTTTAGCTGACATTTATCACAGCTGGCTACTATTTCTTTTGCTACTACAGGTGGCAGGTTAAAATCACTAGCCATTGCTCTCCAATTACTGTGATATTTCTCATGTTCATCTTGGGCCTTATCTATTCCATCTAAAAATAGTACTTTCCTGATTCCAGCACTGACTAATTTATCTACTTGTTCATTTCCTCCAATTCCTTTGTGTGCTGGTACCCATGCCAGATAGACCTTTTCCTTTTTTATTAACTGCTCTATTATTTGATTGACTAACTCTGATTCACTTTGATCTGGTTGTGCTTGAATGATTCCTAATGCATATTGTGAGTCTGTTACTATGTTTACTTCTAATCCCGAATCCTGCAAAGCTAGATAAATTGCTTGTAACTCAGTCTTCTGATTTGTTGTGTCAGTTAGGGTGACAACTTTTTGTCTTCCTCTATTAGTAACATATCCTGCTTTTCCTAATTTAGTCTCCCTGTTAGCTGCCCCATCTACATAGAAGGTTTCTGCTCCTACTATGGGTTCTTTCTCTAACTGGTACCATAATTTCACTAAGGGAGGGGTATT"

print(enunciado) # mostrar o enunciado com a situação problema e informações para a construção de primers

while True:
    primer1 = input('''
A partir destes conhecimentos, crie o desenho para o primer FORWARD.
ATENÇÃO! Sempre escrever o primer no sentido 5'-3'.

Desenho do primer FORWARD: ''').upper() # pedir o desenho do primer1
    encontrar_primer1 = lista_regiao1.find(primer1) # encontrar o desenho do primer1 dentro da lista_regiao1
    tamanho_primer1 = len(primer1) # determinar o tamanho do primer1
    ultimo_primer1 = primer1[-1] # determinar se o primer1 termina com G ou C, ou GC, ou CG
    composicao_c_primer1 = primer1.count("C") # determinar a composição de citosina do primer1
    composicao_g_primer1 = primer1.count("G") # determinar a composição de guanina do primer1
    composicao_t_primer1 = primer1.count("T") # determinar a composição de timina do primer1
    composicao_a_primer1 = primer1.count("A") # determinar a composição de adenina do primer1
    porcentagem_gc_primer1 = (composicao_c_primer1 + composicao_g_primer1)/tamanho_primer1 * 100 # determinar a composição de G+C do primer1
    temperatura_melting_primer1 = (4*(composicao_c_primer1 + composicao_g_primer1)) + (2*(composicao_a_primer1 + composicao_t_primer1)) # determinar a temperatura de melting (Tm) do primer1
    temperatura_min_hibridizacao_primer1 = temperatura_melting_primer1 - 5 # determinar a temperatura de hibridização (Ta) do primer1
    if encontrar_primer1 >= 0:
        print('''
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
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

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
                        primer2 = input('''
Agora crie o desenho para o primer REVERSE.
ATENÇÃO! Sempre escrever o primer no sentido 5'-3'.

O site https://www.bioinformatics.org/sms/rev_comp.html pode ajudar para determinar o COMPLEMENTO-REVERSO da região de interesse.

Desenho do primer REVERSE: ''').upper() # pedir o desenho do primer2
                        encontrar_primer2 = lista_regiao2_complemento_reverso.find(primer2)  # encontrar o desenho do primer2 dentro da lista_regiao2
                        tamanho_primer2 = len(primer2) # determinar o tamanho do primer2
                        ultimo_primer2 = primer2[-1]  # determinar se o primer2 termina com G ou C, ou GC, ou CG
                        composicao_c_primer2 = primer2.count("C") # determinar a composição de citosina do primer2
                        composicao_g_primer2 = primer2.count("G") # determinar a composição de guanina do primer2
                        composicao_t_primer2 = primer2.count("T") # determinar a composição de timina do primer2
                        composicao_a_primer2 = primer2.count("A") # determinar a composição de adenina do primer2
                        porcentagem_gc_primer2 = (composicao_c_primer2 + composicao_g_primer2)/tamanho_primer2 * 100 # determinar a composição de G+C do primer2
                        temperatura_melting_primer2 = (4*(composicao_c_primer2 + composicao_g_primer2)) + (2*(composicao_a_primer2 + composicao_t_primer2)) # determinar a temperatura de melting (Tm) do primer2
                        temperatura_min_hibridizacao_primer2 = temperatura_melting_primer2 - 5 # determinar a temperatura de hibridização (Ta) do primer2
                        if encontrar_primer2 >= 0:
                            print('''
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

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

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Agora o último teste: compatibilidade entre as temperaturas de melting dos primers FORWARD e REVERSE...

Testando...

...
''')
                                            compatibilidade_temperatura_melting_primers = temperatura_melting_primer1 - temperatura_melting_primer2 # determinar compatibilidade entre as Ta do primer1 e primer2
                                            compatibilidade_temperatura_melting_primers_abs = abs(compatibilidade_temperatura_melting_primers) # valor positivo da compatibilidade entre as Ta do primer1 e primer2
                                            if compatibilidade_temperatura_melting_primers_abs <= 2:
                                                print("Está Ótimo! Os primers FORWARD e REVERSE apresentam temperaturas de melting %.1f°C e %.1f°C respectivamente." % (temperatura_melting_primer1, temperatura_melting_primer2))
                                                print('''
Infelizmente este programinha (ainda) não consegue testar HAIRPIN, SELF-DIMER e PRIMER-DIMER :(

Essa aplicação apenas tem a finalidade didática sobre desenho de primer.

Espero que tenha ajudado!


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

                                                                                             analise-primer v0.5                                                                                             
                                                                                             
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Esta aplicação foi desenvolvida para fins didáticos
Minicurso BIOLOGIA MOLECULAR: DESENHO DE PRIMERS PARA PCR
VIII Simpósio de Biomedicina da Bahiana
Escola Bahiana de Medicina e Saúde Pública

Desenvolvido por Laise de Moraes
http://lattes.cnpq.br/7097758558494370 % lattes
https://github.com/lpmor22 % github
https://slides.com/lpmor22_ % decks
laisepaixao@live.com % email
@lpmor22 % (twitter, instagram)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------''')
                                            else:
                                                print('''Os primers FORWARD e REVERSE não apresentam temperaturas compatíveis entre si (%.1f°C e %.1f°C respectivamente).
Por favor, reveja os critérios para a construção de primers e tente novamente!
''' % (temperatura_melting_primer1, temperatura_melting_primer2))
                                        else:
                                            print('''
Talvez você tenha digitado errado ou o primer REVERSE não esteja bom!
Os 4 primeiros critérios para o desenho do primer precisam ser cumpridos!
Por favor, reveja-os e tente novamente!''')
                                    else:
                                        print('''
Talvez você tenha digitado errado ou o primer REVERSE não esteja bom!
Os 4 primeiros critérios para o desenho do primer precisam ser cumpridos!
Por favor, reveja-os e tente novamente!''')
                                else:
                                    print('''
Talvez você tenha digitado errado ou o primer REVERSE não esteja bom!
Os 4 primeiros critérios para o desenho do primer precisam ser cumpridos!
Por favor, reveja-os e tente novamente!''')
                            else:
                                print('''
Talvez você tenha digitado errado ou o primer REVERSE não esteja bom!
Os 4 primeiros critérios para o desenho do primer precisam ser cumpridos!
Por favor, reveja-os e tente novamente!''')
                        else:
                            print("Talvez você tenha digitado errado ou o primer REVERSE não tá bom! Por favor, reveja os critérios para a construção de primers e tente novamente!")
                    else:
                        print('''
Talvez você tenha digitado errado ou o primer FORWARD não esteja bom!
Os 4 primeiros critérios para o desenho do primer precisam ser cumpridos!
Por favor, reveja-os e tente novamente!''')
                else:
                    print('''
Talvez você tenha digitado errado ou o primer FORWARD não esteja bom!
Os 4 primeiros critérios para o desenho do primer precisam ser cumpridos!
Por favor, reveja-os e tente novamente!''')
            else:
                print('''
Talvez você tenha digitado errado ou o primer FORWARD não esteja bom!
Os 4 primeiros critérios para o desenho do primer precisam ser cumpridos!
Por favor, reveja-os e tente novamente!''')
        else:
            print('''
Talvez você tenha digitado errado ou o primer FORWARD não esteja bom!
Os 4 primeiros critérios para o desenho do primer precisam ser cumpridos!
Por favor, reveja-os e tente novamente!''')
    else:
        print('''
Talvez você tenha digitado errado ou o primer FORWARD não esteja bom! Por favor, reveja os critérios para a construção de primers e tente novamente!''')