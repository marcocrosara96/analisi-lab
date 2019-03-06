"""
    Errori riscontrati a lezione:
     - se il nome è troppo lungo --> non funziona
     - se il cognome è troppo corto --> non funziona
     - se il nome contiene uno spazio --> non funziona

    Specifiche:
    Implementare dei test di unità adeguati a verificare la correttezza delle procedure viste a
    lezione per il calcolo del codice fiscale, in modo tale da ottenere una copertura dei sorgenti
    quanto più vicina al 100%. Motivare adeguatamente l’eventuale mancato raggiungimento
    del 100% di copertura.
"""

import unittest
import codicefiscale as c

class CodiceFiscaleTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('>> Avvio i test delle procedure... ')

    @classmethod
    def tearDownClass(cls):
        print('... Test delle procedure conclusi <<')

    # ------- main

    def test_CrosaraMarco(self): # test passato
        argv = ['0', 'crosara', 'marco', '02/08/1996', 'thiene', 'm']
        self.assertEqual(c.main(argv), 'crsmrc96m02l157j')

    def test_ControFilippo(self): # test fallito
        argv = ['0', 'contro', 'filippo', '12/10/1996', 'verona', 'm']
        self.assertEqual(c.main(argv), 'cntfpp96r12l781c')
    
    def test_RossiLuisa(self): # test fallito
        argv = ['0', 'rossi', 'luisa', '08/10/1993', 'verona', 'f']
        self.assertEqual(c.main(argv), 'rsslsu93r08l781m')

    #def test_SunyiXu(self):  # test fallito --> prococa un errore <-----
    #    argv = ['0', 'xu', 'sunyi', '20/09/1996', 'cina', 'f']
    #    self.assertEquals(c.main(argv), 'snyxux96p60z210y')

    # ------- estrai_nome_cognome

    def test_estrai_nome_cognome_COGNOME(self): # test passato
        cognome = 'crosara'
        self.assertEqual(c.estrai_nome_cognome(cognome), 'crs')

    def test_estrai_nome_cognome_NOME(self): #test passato
        nome = 'marco'
        self.assertEqual(c.estrai_nome_cognome(nome), 'mrc')

    def test_estrai_nome_cognome_NOME2(self): #test fallito
        nome = 'filippo'
        self.assertEqual(c.estrai_nome_cognome(nome), 'fpp')

    def test_estrai_nome_cognome_NOME3(self): #test fallito --> nome con spazio
        nome = 'luisa maria'
        self.assertEqual(c.estrai_nome_cognome(nome), 'lmr')

    # ------- genera_mese

    def test_genera_mese_GENNAIO(self): #test passato
        mese = '01'
        self.assertEqual(c.genera_mese(mese), 'a')
    
    def test_genera_mese_DICEMBRE(self): #test passato
        mese = '12'
        self.assertEqual(c.genera_mese(mese), 't')

    # ------- codice_comune

    def test_codice_comune_VERONA(self): #test passato
        comune = 'verona'
        self.assertEqual(c.codice_comune(comune), 'l781')

    def test_codice_comune_CINA(self): #test passato
        comune = 'cina'
        self.assertEqual(c.codice_comune(comune), 'z210')

    # ------- genera_giorno

    def test_genera_giorno_UOMO(self):  #test passato
        giorno = '12'
        sesso = 'm'
        self.assertEqual(c.genera_giorno(giorno, sesso), '12')

    def test_genera_giorno_DONNA(self):   #test fallito -->  sul codice è stato usato range(1,31) che ritorna [1 ... 30] dunque manca il giorno 31
        giorno = '31'
        sesso = 'f'
        self.assertEqual(c.genera_giorno(giorno, sesso), '71')

    # ------- genera_codice_controllo

    def test_genera_codice_controllo_Crosara_Marco(self):
        codfisc_parziale = 'crsmrc96m02l157'
        self.assertEqual(c.genera_codice_controllo(codfisc_parziale), 'j')

    def test_genera_codice_controllo_Contro_Filippo(self):
        codfisc_parziale = 'cntfpp96r12l781'
        self.assertEqual(c.genera_codice_controllo(codfisc_parziale), 'c')

    def test_genera_codice_controllo_Xu_Sunyi(self):
        codfisc_parziale = 'snyxux96p60z210'
        self.assertEqual(c.genera_codice_controllo(codfisc_parziale), 'y')


if __name__ == '__main__':
   unittest.main()
