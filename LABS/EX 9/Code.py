#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/wait.h>
#include <semaphore.h>

struct SharedData {
    sem_t ready;
    char message[100];
};

int main() {
    struct SharedData *shared = mmap(
        NULL, sizeof(struct SharedData),
        PROT_READ | PROT_WRITE,
        MAP_SHARED | MAP_ANONYMOUS, -1, 0
    );

    if (shared == MAP_FAILED) {
        perror("mmap");
        return 1;
    }

    sem_init(&shared->ready, 1, 0);

    if (fork() == 0) {
        sem_wait(&shared->ready);
        printf("Child received: %s\n", shared->message);
        return 0;
    }

    strcpy(shared->message, "Hello from the parent process!");
    sem_post(&shared->ready);

    wait(NULL);
    sem_destroy(&shared->ready);
    munmap(shared, sizeof(struct SharedData));

    return 0;
}
