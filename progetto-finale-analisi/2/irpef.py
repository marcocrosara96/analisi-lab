"""
Esercizio 2
Implementare in Python una procedura non ricorsiva per il calcolo dell'IRPEF.
Implementare quindi dei test di unità adeguati a verificare la correttezza della procedura
implementata, in modo tale da ottenere una copertura dei sorgenti quanto più vicina al
100%. Motivare adeguatamente l’eventuale mancato raggiungimento del 100% di
copertura.

Scaglione	                    Aliquota        Correttivo
1. fino € 15.000	            23%             € 0 
2. da € 15.001 a € 28.000	    27%             € 600
3. da € 28.001 a € 55.000	    38%             € 3.680
4. da € 55.001 a € 75.000	    41%             € 5.330
5. oltre € 75.000	            43%             € 6.830
"""
from sys import argv
from decimal import Decimal, ROUND_HALF_UP

table = {
    15000 : [0.23, 0],
    28000 : [0.27, 600],
    55000 : [0.38, 3680],
    75000 : [0.41, 5330],
    -1 : [0.43, 6830]
    }

"""
    Procedura implementata per il calcolo dell'irpef
"""
def main(argv):
    x = Decimal(argv[1])
    # Regolamento IRPEF: arrotondamento all'unità di euro per saldo irpef, arrotondamento al centesimo per acconti
    x = x.quantize(Decimal('0'), rounding=ROUND_HALF_UP)

    aliquota = None
    correttivo = None
    for t in table:
        if aliquota == None:
            if t == -1 or x <= t:
                aliquota = table[t][0]
                correttivo = table[t][1]

    irpef = x * Decimal(aliquota) - Decimal(correttivo)
    irpef = irpef.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    print("Sul tuo reddito di " + str(x) + " è stato  applicato il " +  str(aliquota) + "% e un correttivo di " + str(correttivo) + " euro")
    print("La quota irpef risulta quindi di " + str(irpef) + " euro")

    # Per comodità d'uso di eventuali programmi esterni, ritorno un float
    return float(irpef)

if __name__ == '__main__':  # pragma: no cover
    if len(argv) != 2:
        print("Parametri errati, uso: irpef.py [reddito]")
    else:
        main(argv)
