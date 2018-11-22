#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>

void handler(int code) {
    fprintf(stderr, "Signal %d caught\n", code);
}

int main() {
    int i = 0;
    
    struct sigaction newact;
    newact.sa_handler = handler;
    newact.sa_flags = 0;
    sigemptyset(&newact.sa_mask);
    sigaction(SIGINT, &newact, NULL);
    
    for(;;) {
        if ((i++ % 50000000) == 0) {
            fprintf(stderr, ".");
        }
    }
    return 0;
}