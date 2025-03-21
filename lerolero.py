"""Gerador de Lero Lero.
Gera frases de efeito sem significado real."""
import ramdom


parte1 = ["O sistema em desenvolvimento", 
          "O novo protocolo de comunicação", 
          "O algoritmo foi otimizado e"]
parte2 = ["possui exelente desempenho", 
          "oferece garantias de precisão acima da média", 
          "preenche uma lacuna significativa"]
parte3 = ["nas aplicações a que se destina", 
          "em relação às opções disponíveis no mercado", 
          ", provendo ampla vantagem competitiva a seus usuários"]

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
