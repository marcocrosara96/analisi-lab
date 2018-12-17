/*
 * Restituisce numero randomico
 *
 * gcc -m32 -o random1.32 random1.c
 */
#include <time.h>
#include <stdlib.h>
#include <stdio.h>

void main(void){
    srand(time(NULL));
    int r = rand();

    printf("%d\n", r);
}
