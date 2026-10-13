#include <stdio.h>

int main() {
    int n, quantum;
    int burst[20], remaining[20], waiting[20] = {0}, turnaround[20];
    int time = 0, completed = 0;

    printf("Enter number of processes: ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        printf("Enter burst time for P%d: ", i + 1);
        scanf("%d", &burst[i]);
        remaining[i] = burst[i];
    }

    printf("Enter time quantum: ");
    scanf("%d", &quantum);

    while (completed < n) {
        for (int i = 0; i < n; i++) {
            if (remaining[i] > 0) {
                if (remaining[i] > quantum) {
                    time += quantum;
                    remaining[i] -= quantum;
                } else {
                    time += remaining[i];
                    remaining[i] = 0;
                    turnaround[i] = time;
                    waiting[i] = turnaround[i] - burst[i];
                    completed++;
                }
            }
        }
    }

    printf("\nProcess\tBurst\tWaiting\tTurnaround\n");
    for (int i = 0; i < n; i++)
        printf("P%d\t%d\t%d\t%d\n",
               i + 1, burst[i], waiting[i], turnaround[i]);

    return 0;
}
