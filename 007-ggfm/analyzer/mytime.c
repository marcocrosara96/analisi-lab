#include <time.h>
#include <stdio.h>
#include <stdlib.h>

time_t time (time_t *_timer){
	FILE *fs;
	int num;
	fs = fopen("num.txt", "r");
	fscanf(fs, "%d", &num);

	if(_timer) {
		*_timer = (time_t)num;	
	}
	return num;
}
