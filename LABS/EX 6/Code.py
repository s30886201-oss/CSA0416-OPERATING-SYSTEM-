#include <stdio.h>

int main() {
    int n, burst[20], remaining[20], priority[20];
    int waiting[20] = {0}, turnaround[20];
    int time = 0, completed = 0;

    printf("Enter number of processes: ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        printf("Enter burst time and priority for P%d: ", i + 1);
        scanf("%d %d", &burst[i], &priority[i]);
        remaining[i] = burst[i];
    }

    while (completed < n) {
        int selected = -1;

        /* All processes arrive at time 0.
           Pick the unfinished process with the highest priority. */
        for (int i = 0; i < n; i++) {
            if (remaining[i] > 0 &&
                (selected == -1 || priority[i] < priority[selected])) {
                selected = i;
            }
        }

        remaining[selected]--;
        time++;

        if (remaining[selected] == 0) {
            completed++;
            turnaround[selected] = time;
            waiting[selected] = turnaround[selected] - burst[selected];
        }
    }

    printf("\nProcess\tPriority\tBurst\tWaiting\tTurnaround\n");
    for (int i = 0; i < n; i++) {
        printf("P%d\t%d\t\t%d\t%d\t%d\n",
               i + 1, priority[i], burst[i],
               waiting[i], turnaround[i]);
    }

    return 0;
}
