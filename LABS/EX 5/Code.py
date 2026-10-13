#include <stdio.h>

int main() {
    int n, burst[20], priority[20], process[20];
    int waiting[20], turnaround[20];

    printf("Enter number of processes: ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        process[i] = i + 1;
        printf("Enter burst time and priority for P%d: ", i + 1);
        scanf("%d %d", &burst[i], &priority[i]);
    }

    /* Sort by priority; smaller number means higher priority */
    for (int i = 0; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            if (priority[i] > priority[j]) {
                int temp = priority[i];
                priority[i] = priority[j];
                priority[j] = temp;

                temp = burst[i];
                burst[i] = burst[j];
                burst[j] = temp;

                temp = process[i];
                process[i] = process[j];
                process[j] = temp;
            }
        }
    }

    waiting[0] = 0;
    for (int i = 1; i < n; i++)
        waiting[i] = waiting[i - 1] + burst[i - 1];

    printf("\nProcess\tPriority\tBurst\tWaiting\tTurnaround\n");
    for (int i = 0; i < n; i++) {
        turnaround[i] = waiting[i] + burst[i];
        printf("P%d\t%d\t\t%d\t%d\t%d\n",
               process[i], priority[i], burst[i],
               waiting[i], turnaround[i]);
    }

    return 0;
}
