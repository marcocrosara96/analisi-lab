"""
Esercizio 3
Implementare in Python una procedura per il calcolo della Pasqua.
Implementare quindi dei test di unità adeguati a verificare la correttezza della procedura
implementata, in modo tale da ottenere una copertura dei sorgenti quanto più vicina al
100%. Motivare adeguatamente l’eventuale mancato raggiungimento del 100% di
copertura.

IDEA: [Pasqua cristiana]

Per il calcolo si usano teoricamente due fenomeni: l'equinozio di primavera e le fasi lunari
Tuttavia solitamente quando se ne deve implementare l'algoritmo si usa il metodo di Gauss <--
"""
from sys import argv

schema =   {15 : (22, 2), # anni 1583-1599
            16 : (22, 2), # anni 1600-1699 "
            17 : (23, 3), # anni 1700-1799
            18 : (23, 4), # anni 1800-1899
            19 : (24, 5), # anni 1900-1999
            20 : (24, 5), # anni 2000-2099 "
            21 : (24, 6), # anni 2100-2199
            22 : (25, 0), # anni 2200-2299
            23 : (26, 1), # anni 2300-2399
            24 : (25, 1), # anni 2400-2499
            25 : (26, 2)} # anni 2500-2599

month_word = ['Marzo', 'Aprile']

"""
    Procedura implementata per il calcolo della pasqua
"""
def main(argv):
    year = int(argv[1])

    if year < 1583 or year >= 2600: # funzione valida per le pasque gregoriane dal 1583 al 2599 (come da tabella sopra)
        print("Anno non valido: inserire un anno compreso tra il 1583 e il 2599")
        return None

    a = year % 19
    b = year % 4
    c = year % 7

    years_interval = int(year/100)
    m, n = schema[years_interval]
    d = (19*a + m) % 30
    e = (2*b + 4*c + 6*d + n) % 7

    day = d + e

    if (day < 10):
        day += 22
        month = 3 # mese di marzo
    else:
        day -= 9
        month = 4 # mese di aprile
        # eccezioni: Se la data è 26 aprile o Se la data risultante dalla formula è 
        # 25 aprile && d = 28 && e = 6 && a > 10, allora la Pasqua cadrà 7gg prima
        if (day == 26) or ((day == 25) and (d == 28) and (e == 6) and (a > 10)): 
            day -= 7

    easter = str(day) + " " + month_word[month-3] + " " + str(year)
    print("La Pasqua è il giorno " + easter)

    return easter

if __name__ == '__main__':  # pragma: no cover
    if len(argv) != 2:
        print("Parametri errati, uso: pasqua.py [anno]")
    else:
        main(argv)
