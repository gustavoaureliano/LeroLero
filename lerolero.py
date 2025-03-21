"""Gerador de Lero Lero.
Gera frases de efeito sem significado real."""
import ramdom

parte1 = []
parte2 = []
parte3 = []

lingua = int(input(
    """Escolha a lingua:
    [1] - português
    [2] - inglês
    :
    """))

if lingua == 2:
    parte1 = []
    parte2 = []
    parte3 = []


print(ramdom.choice(parte1), ramdom.choice(parte2), ramdom.choice(parte3))
