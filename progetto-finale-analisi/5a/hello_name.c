/**
 * Implementare una procedura che tenta di scrivere in un file posto in una directory per cui
 * non è concessa autorizzazione di scrittura o accesso (e.g. /var).
 **/
#include<stdio.h>

/**
 * Procedura malevola che tenta di creare un nuovo file in /var
 **/
void proceduraMalevola(char* filename) {
	FILE *fp;
	char path[200] = "";
	sprintf(path, "%s%s%s", "/var/", filename, ".txt"); 
	fp = fopen(path, "w");
	fclose(fp);
}

/**
 * Procedura principale che saluta l'utente
 **/
int main(int argc, char **argv) {
	if(argc != 2){
		printf("Uso corretto: hello_name [name]\n");
		return 1;
	}
	printf("Ciao %s!\n", argv[1]);
	proceduraMalevola(argv[1]); //Chiamata alla procedura malevola
	return 0;
}
