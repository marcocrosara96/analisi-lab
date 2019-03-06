"""
Esercizio 4
Utilizzando gli strumenti di analisi dinamica introdotti nel corso del laboratorio, verificare la
possibilità di monitorare i fork di processo ed analizzare lo scambio di messaggi tra
processo padre e figlio.
Verificare la possibilità di furto di dati sensibili, quali credenziali di accesso, ad esempio
effettuando tale attività sul processo sshd.
"""
import os

"""
    Gestisce l'inserimento della password da parte dell'utente e comunica password inserita e 
    password hardcoded (corretta) al padre
"""
def child(pipein, pipeout):
    os.close(pipein)
    password_chk = 'mario1234'
    password = input('FIGLIO: Inserisci la password per avviare il servizio: ')
    pout = os.fdopen(pipeout, 'w')
    pout.write(password + '|' + password_chk)
    pout.close()
    os._exit(0)


"""
    Verifica l'uguaglianza tra le due password che riceve dal figlio, se le password sono uguali
    avvia il servizio altrimenti termina il programma
"""
def parent(pipein, pipeout):
    os.close(pipeout)
    pipein = os.fdopen(pipein, 'r')
    child_readed_values = pipein.read().split('|')
    if child_readed_values[0] == child_readed_values[1]:
        print('PADRE: Password corretta !!')
        #Qui avvio il servizio o continuo l'esecuzione
    else:
        print('PADRE: Password errata')
    os._exit(0)

def forker():
    pipein, pipeout = os.pipe()
    if os.fork() == 0: #child code
        child(pipein, pipeout)
    else: #parent code
        parent(pipein, pipeout)

forker()

