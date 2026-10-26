#include <stdio.h>
#include <pthread.h>

int counter = 0;
pthread_mutex_t lock;

void *process(void *arg)
{
    int i;

    pthread_mutex_lock(&lock);

    for (i = 0; i < 5; i++)
    {
        counter++;
        printf("Thread %ld: Counter = %d\n",
               (long)arg, counter);
    }

    pthread_mutex_unlock(&lock);

    return NULL;
}

int main()
{
    pthread_t t1, t2;

    pthread_mutex_init(&lock, NULL);

    pthread_create(&t1, NULL, process, (void *)1);
    pthread_create(&t2, NULL, process, (void *)2);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    pthread_mutex_destroy(&lock);

    printf("\nFinal Counter = %d\n", counter);

    return 0;
}
