#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "exec.h"

char* exec(char* command){
    char buffer[128];
    char *response = malloc(4096);

    response[0] = '\0';

    FILE *pipe = popen(command, "r");
    if(pipe == NULL){
        free(response);
        return NULL;
    }

    while(fgets(buffer, sizeof(buffer), pipe) != NULL){
        strcat(response, buffer);            
    }

    return response;
}
