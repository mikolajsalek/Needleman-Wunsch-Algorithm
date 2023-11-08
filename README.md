# Needleman-Wunsch-Algorithm

Implementacja algorytmu Needlemana-Wunsch'a w Pythonie.

SPOSÓB UŻYCIA:
Program uruchamia się z poziomu konsoli, podając na wejściu pliki o rozszerzeniu .fasta z sekwencjami oraz 3 wartosci po spacji oznaczające punktowanie odpowiednia za: match, missmatch i gap.
(należy podać liczby nieujemne).

PRZYKŁAD UŻYCIA:
python main.py 1MBO.fasta 1HDB.fasta 1 1 1

OCZEKIWANY WYNIK:
VLSEGEWQLVLHVWAKVEADVAGHG-QDILIRLFKSHPETLEKFDRFKHL--KTEA-EMKASEDLKKHGVTVLTALGAILKKKGH-HEAELKPLAQS---H--ATKHKIP---IK--YLEFISEAIIHVL-HSRHP-GDFGA-DAQGAMNK-ALELFRKDIAAKYKELGYQG
VLSPADKTNVKAAWGKVGA-HAGEYGAEALERMFLSFP-T-TK-TYFPHFDLSHGSAQVK--GHGKK--V----A-DA-LTNAVAH--VDDMPNALSALSDLHA--HKLRVDPVNFK-L--LS-HCLLVTL-AAHLPAEFTPA--VHASLDKFLASVSTVLTSKY------R
