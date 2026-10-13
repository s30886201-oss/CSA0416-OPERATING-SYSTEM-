#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <sys/wait.h>

struct Message {
    long type;
    char text[100];
};

int main() {
    int queue_id = msgget(IPC_PRIVATE, 0600 | IPC_CREAT);
    if (queue_id == -1) {
        perror("msgget");
        return 1;
    }

    pid_t pid = fork();

    if (pid == -1) {
        perror("fork");
        msgctl(queue_id, IPC_RMID, NULL);
        return 1;
    }

    if (pid == 0) {
        struct Message message;

        if (msgrcv(queue_id, &message, sizeof(message.text), 1, 0) == -1) {
            perror("msgrcv");
            exit(1);
        }

        printf("Child received: %s\n", message.text);
        exit(0);
    }

    struct Message message;
    message.type = 1;
    strcpy(message.text, "Hello from the parent process!");

    if (msgsnd(queue_id, &message, sizeof(message.text), 0) == -1)
        perror("msgsnd");

    wait(NULL);
    msgctl(queue_id, IPC_RMID, NULL);

    return 0;
}
