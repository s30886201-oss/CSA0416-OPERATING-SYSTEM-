#include <stdio.h>

int main() {
    int n, burst[20], process[20], wait[20], turnaround[20];

    printf("Enter number of processes: ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        process[i] = i + 1;
        printf("Enter burst time for P%d: ", i + 1);
        scanf("%d", &burst[i]);
    }

    /* Sort processes by burst time */
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (burst[i] > burst[j]) {
                int temp = burst[i];
                burst[i] = burst[j];
                burst[j] = temp;

                temp = process[i];
                process[i] = process[j];
                process[j] = temp;
            }
        }
    }

    wait[0] = 0;
    for (int i = 1; i < n; i++)
        wait[i] = wait[i - 1] + burst[i - 1];

    printf("\nProcess\tBurst\tWaiting\tTurnaround\n");
    for (int i = 0; i < n; i++) {
        turnaround[i] = wait[i] + burst[i];
        printf("P%d\t%d\t%d\t%d\n",
               process[i], burst[i], wait[i], turnaround[i]);
    }

    return 0;
}
