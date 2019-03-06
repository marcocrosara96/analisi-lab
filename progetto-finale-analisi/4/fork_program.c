/**
 * Esercizio 4
 * Utilizzando gli strumenti di analisi dinamica introdotti nel corso del laboratorio, verificare la
 * possibilità di monitorare i fork di processo ed analizzare lo scambio di messaggi tra
 * processo padre e figlio.
 * Verificare la possibilità di furto di dati sensibili, quali credenziali di accesso, ad esempio
 * effettuando tale attività sul processo sshd.
 **/
#include<stdio.h> 
#include<stdlib.h> 
#include<unistd.h> 
#include<sys/types.h> 
#include<string.h> 
#include<sys/wait.h> 

// Pipe
int fd1[2];
int fd2[2];
// Id processo 
pid_t p; 

/*
    PROCESSO FIGLIO
    Gestisce l'inserimento della password da parte dell'utente e comunica password inserita e 
    password hardcoded (corretta) al padre
*/
void child() {
    char password_chk[10] = "mario1234";
    char password[100];
    char send[110] = "";

    printf("FIGLIO: Inserisci la password per avviare il servizio: ");
    scanf("%s", (char *)&password);
  
    close(fd1[0]);  // Chiudo l'altra parte della pipe
    sprintf(send,"%s%s%s", password, "|", password_chk); // Compongo la stringa
    write(fd1[1], send, strlen(send)+1); // Invio la password inserita e quella corretta al padre
    close(fd1[1]);
}

/*
    PROCESSO PADRE
    Verifica l'uguaglianza tra le due password che riceve dal figlio, se le password sono uguali
    avvia il servizio altrimenti termina il programma
*/
void parent() {
    char passwords[255];
    
    close(fd1[1]);  // Chiudo l'altra parte della pipe
    read(fd1[0], passwords, 111); // Aspetto la ricezione della stringa da parte del figlio e la leggo
    char* token1 = strtok(passwords, "|");
    char* token2 = strtok(0, "|");
    if(strcmp(token1, token2) == 0)
        printf("PADRE: Password corretta !!\n");
    else
        printf("PADRE: Password errata\n");

    exit(0); 
}

int main() {
    //Inizializzazione pipe
    if (pipe(fd1)==-1) { 
        printf("Pipe Failed"); 
        return 1; 
    } 
    if (pipe(fd2)==-1) { 
        printf("Pipe Failed"); 
        return 1; 
    } 
    
    //Fork processo
    p = fork(); 
    if (p < 0) { 
        printf("fork Failed"); 
        return 1; 
    }
    else if (p > 0) //Parent process
        parent();
    else //child process
        child();
}