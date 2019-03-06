/*
* Esercizio 5.B (complesso)
* Implementare in C una procedura che accede ad aree di memoria scelte in modo casuale.
* Utilizzando gli strumenti di analisi dinamica introdotti nel corso del laboratorio, verificare la
* possibilità di monitorare i tentativi di accesso ad aree di memoria non allocate al processo
* e gestirli generando un log.
*/
#include <stdio.h>
#include <stdlib.h>
#include <malloc.h>
#include <time.h>

int main(int argc, char** argv)
{
    /*srand(time(NULL));
    void *p = &argc;
    printf("&argc = %p\n", p);
    int r = rand() % 100;
    p += r;
    printf("p = %p\n", p);
    printf("r = %i\n", r);
    printf("*p = %i\n", *((int *)p));*/

    //Tento di visualizzare sulla console il contenuto di una zona di memori scelta a caso

    srand(time(NULL));

    int *m = (int*)malloc(1);
    *m = 5;
    int *x = (int*)rand();

    printf("PROGRAM ADDRESS: %p\n", m );
    printf("              >>: %i\n", *m );
    printf("RANDOM ADDRESS: %p\n", x );
    printf("            >>: %i\n", *x );

    return 0;
}
